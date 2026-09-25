"""Runtime control plane (AI_CONTROL enforcement), governed by AI_CONTROL/CONTROL_PLANE_POLICY.yaml.

This module is the single authorization implementation and the single tool executor of the project:

    request -> _decide() [policy, action, state, phase, study, environment, provenance, approval, scope]
            -> ALLOW / DENY -> decision log -> _execute() (ALLOW only) -> tool

Public entry points:
  authorize()        decide and log; never executes anything.
  run_authorized()   decide, then execute argv only on ALLOW; DENY never reaches subprocess.
  transition()       the canonical phase-state transition (PHASE_CONTROL.yaml transition table).
  repository_control_errors()   state/approval/provenance checks shared with scripts/validate_project.py.
  tool_gate_main()   entry point of the launcher's PATH gate (environments/xilinx_2025_2_1/bin/*).

Everything fails closed: a missing or malformed policy, state, approval or log, an unknown value, or any
unexpected error yields DENY. State and approvals are always read from the canonical files, never taken from
the caller, so a caller cannot hand in a forged state or approval.
"""
from __future__ import annotations

import hashlib
import hmac
import inspect
import json
import os
import re
import secrets
import subprocess
import sys
import uuid
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
from pathlib import Path

import yaml

# The repository root. HLSDSE_ROOT overrides the source-tree default (needed when the package is installed).
ROOT = Path(os.environ.get('HLSDSE_ROOT') or Path(__file__).resolve().parents[2]).resolve()
POLICY_PATH = 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml'
DEFAULT_LOG = 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl'   # used only when the policy itself is unreadable
EXECUTABLE_STUDY_STATUSES = ('PLANNED', 'ACTIVE')
ACTIVE_GATE_STATES = ('IMPLEMENTING', 'VALIDATING', 'GATE_REVIEW')
_STATE_BOOL_FIELDS = ('p1_authorized', 'p1_gate_required', 'human_gate_required', 'automatic_advance',
                      'next_phase_implementation_allowed', 'future_phase_implementation_allowed')
_APPROVAL_KEYS = ('approval_id', 'project_version', 'phase', 'study', 'environment', 'approver', 'approved_at',
                  'approved_commit', 'expires_at', 'status')
_PLACEHOLDER = re.compile(r'<[^>]*>')

_PROCESS_KEY = secrets.token_bytes(32)
_ISSUED = {}                     # request_id -> seal; decisions issued for execution by run_authorized, single use


class ControlError(Exception):
    def __init__(self, code, detail=''):
        super().__init__(f'{code}: {detail}')
        self.code, self.detail = code, detail


class ExecutionDenied(Exception):
    """Raised when the executor is reached without a valid, unused ALLOW decision for exactly this argv."""


@dataclass(frozen=True)
class Decision:
    decision: str
    reason_code: str
    reason: str
    request_id: str
    timestamp_utc: str
    actor: str
    caller: str
    action: str | None
    category: str | None
    phase: str | None
    study: str | None
    environment: str | None
    approval_id: str | None
    project_version: str | None
    policy_version: str | None
    state_schema_version: str | None
    approval_schema_version: str | None
    contract_version: str | None
    repository_commit: str | None
    state_hash: str | None
    argv_sha256: str | None

    @property
    def allowed(self):
        return self.decision == 'ALLOW'


# ---------------------------------------------------------------------------------------------------- loading

def _now():
    return datetime.now(timezone.utc)


def _sha256(data: bytes):
    return hashlib.sha256(data).hexdigest()


def _git(root, *args):
    try:
        cp = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True)
    except OSError:
        return 127, ''
    return cp.returncode, cp.stdout.strip()


def _load_yaml(path: Path, code: str):
    if not path.is_file():
        raise ControlError(code, f'{path.name} missing')
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except Exception as exc:
        raise ControlError(code, f'{path.name} unparseable ({type(exc).__name__})')
    if not isinstance(data, dict):
        raise ControlError(code, f'{path.name} is not a mapping')
    return data


def load_policy(root=None):
    root = Path(root or ROOT)
    pol = _load_yaml(root / POLICY_PATH, 'POLICY_INVALID')
    required = ('policy_version', 'project_version', 'state_schema_version', 'approval_schema_version', 'paths',
                'known_phases', 'phase_states', 'gate_fields', 'categories', 'actions', 'tools', 'discovery_flags',
                'transition_requirements', 'canonical_contract')
    missing = [k for k in required if k not in pol]
    if missing:
        raise ControlError('POLICY_INVALID', f'missing keys: {", ".join(missing)}')
    for action, cat in pol['actions'].items():
        if cat not in pol['categories']:
            raise ControlError('POLICY_INVALID', f'action {action} maps to unknown category {cat}')
    for name, cat in pol['categories'].items():
        if not isinstance(cat, dict) or not isinstance(cat.get('gated'), bool):
            raise ControlError('POLICY_INVALID', f'category {name} lacks a boolean gated flag')
        if cat['gated'] and not cat.get('allowed_phase_states'):
            raise ControlError('POLICY_INVALID', f'gated category {name} lacks allowed_phase_states')
    return pol


def _registry(root, pol):
    reg = _load_yaml(root / pol['paths']['study_registry'], 'REGISTRY_INVALID')
    if not isinstance(reg.get('reserved'), dict):
        raise ControlError('REGISTRY_INVALID', 'study registry has no reserved mapping')
    return reg


def _environments(root, pol):
    reg = _load_yaml(root / pol['paths']['environment_registry'], 'ENVIRONMENT_REGISTRY_INVALID')
    envs = reg.get('environments')
    if not isinstance(envs, list):
        raise ControlError('ENVIRONMENT_REGISTRY_INVALID', 'environments is not a list')
    return {e['id']: e for e in envs if isinstance(e, dict) and e.get('id')}


def _registered_environment(envs, env_id):
    e = envs.get(env_id) if isinstance(env_id, str) else None
    return e if e and e.get('status') == 'registered' else None


def gate_hash(pol, state, pc):
    fields = pol['gate_fields']
    snap = {'state': {k: state.get(k) for k in fields[pol['paths']['state']]},
            'phase_control': {k: pc.get(k) for k in fields[pol['paths']['phase_control']]}}
    return _sha256(json.dumps(snap, sort_keys=True, default=str).encode())


def load_state(root, pol):
    """Load and validate RESEARCH_STATE.yaml + PHASE_CONTROL.yaml. Returns (state, phase_control, state_sha256)."""
    sp = root / pol['paths']['state']
    raw = sp.read_bytes() if sp.is_file() else None
    state = _load_yaml(sp, 'STATE_INVALID')
    pc = _load_yaml(root / pol['paths']['phase_control'], 'STATE_INVALID')
    validate_state(root, pol, state, pc)
    return state, pc, _sha256(raw)


def validate_state(root, pol, state, pc):
    def bad(detail):
        raise ControlError('STATE_INVALID', detail)
    if state.get('project_version') != pol['project_version']:
        bad(f'project_version {state.get("project_version")!r} != policy {pol["project_version"]!r}')
    if str(state.get('state_schema_version')) != str(pol['state_schema_version']) or 'state_schema_version' not in state:
        bad(f'state_schema_version {state.get("state_schema_version")!r} != policy {pol["state_schema_version"]!r}')
    phase = state.get('current_phase')
    if phase not in pol['known_phases']:
        bad(f'unknown current_phase {phase!r}')
    if state.get('active_phase') != phase:
        bad(f'active_phase {state.get("active_phase")!r} != current_phase {phase!r}')
    st = state.get('active_phase_state')
    if st not in pol['phase_states']:
        bad(f'unknown active_phase_state {st!r}')
    if state.get('status') != st:
        bad(f'status {state.get("status")!r} != active_phase_state {st!r}')
    for f in _STATE_BOOL_FIELDS:
        if not isinstance(state.get(f), bool):
            bad(f'{f} missing or not boolean ({state.get(f)!r})')
    if state['human_gate_required'] is not True:
        bad('human_gate_required must be true')
    if state['automatic_advance'] is not False:
        bad('automatic_advance must be false')
    if state['next_phase_implementation_allowed'] or state['future_phase_implementation_allowed']:
        bad('next/future phase implementation must not be allowed')
    if phase == 'P0' and (state['p1_authorized'] is not False or state['p1_gate_required'] is not True):
        bad('in P0, p1_authorized must be false and p1_gate_required true (P1 needs the G0 gate)')
    study = state.get('current_study')
    reg = _registry(root, pol)
    if not isinstance(study, str) or study not in reg['reserved']:
        bad(f'unknown current_study {study!r}')
    contract = root / 'studies' / study / 'CONTRACT.yaml'
    if contract.is_file():
        cphase = (yaml.safe_load(contract.read_text(encoding='utf-8')) or {}).get('phase_id')
        if cphase is not None and cphase != phase:
            bad(f'{study} contract phase_id {cphase} != current_phase {phase}')
    if 'active_environment' not in state:
        bad('active_environment missing')
    env = state['active_environment']
    if env is not None and not _registered_environment(_environments(root, pol), env):
        bad(f'active_environment {env!r} is not a registered environment')
    if pc.get('active_phase') != phase or pc.get('state') != st:
        bad(f'PHASE_CONTROL {pc.get("active_phase")}/{pc.get("state")} != RESEARCH_STATE {phase}/{st}')
    if pc.get('human_approval_required') is not True or pc.get('automatic_advance') is not False:
        bad('PHASE_CONTROL must require human approval and forbid automatic advance')
    if not isinstance(pc.get('transition_rules'), list) or not pc['transition_rules']:
        bad('PHASE_CONTROL transition_rules missing')


# -------------------------------------------------------------------------------------------------- approvals

def _ts(value, field):
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError:
            raise ControlError('APPROVAL_INVALID', f'{field} is not ISO-8601: {value!r}')
    else:
        raise ControlError('APPROVAL_INVALID', f'{field} is not a timestamp: {value!r}')
    if dt.tzinfo is None:
        raise ControlError('APPROVAL_INVALID', f'{field} has no timezone')
    return dt


def approval_scope(appr):
    """Return (allowed, forbidden, layout). Accepts `scope: {allowed, forbidden}` (nested) or, when `scope` is
    present but empty, top-level `allowed`/`forbidden` (the indentation-collapsed form of the same YAML).
    Both forms at once, or anything else, is malformed."""
    scope = appr.get('scope', '<absent>')
    if isinstance(scope, dict) and 'allowed' not in appr and 'forbidden' not in appr:
        allowed, forbidden, layout = scope.get('allowed'), scope.get('forbidden'), 'nested'
    elif scope is None and 'allowed' in appr and 'forbidden' in appr:
        allowed, forbidden, layout = appr['allowed'], appr['forbidden'], 'flat'
    else:
        raise ControlError('APPROVAL_INVALID', 'scope must be scope.{allowed,forbidden} or scope: + top-level allowed/forbidden')
    for name, lst in (('allowed', allowed), ('forbidden', forbidden)):
        if not isinstance(lst, list) or not all(isinstance(x, str) for x in lst):
            raise ControlError('APPROVAL_INVALID', f'scope {name} must be a list of action names')
    return list(allowed), list(forbidden), layout


def load_approvals(root, pol):
    """Parse every approval file. Any unparseable file is corrupt permission data: raises APPROVAL_CORRUPT."""
    d = root / pol['paths']['approvals_dir']
    out = []
    if not d.is_dir():
        return out
    for p in sorted(d.iterdir()):
        if p.suffix not in ('.yaml', '.yml'):
            continue
        try:
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
        except Exception as exc:
            raise ControlError('APPROVAL_CORRUPT', f'{p.name} unparseable ({type(exc).__name__})')
        if not isinstance(data, dict):
            raise ControlError('APPROVAL_CORRUPT', f'{p.name} is not a mapping')
        out.append((p, data))
    return out


def validate_approval(root, pol, path, appr, now=None):
    """Raise ControlError unless the approval is well-formed, human-completed, committed, and unexpired."""
    now = now or _now()
    missing = [k for k in _APPROVAL_KEYS if k not in appr]
    if missing:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: missing {", ".join(missing)}')
    for k in _APPROVAL_KEYS:
        v = appr[k]
        if isinstance(v, str) and _PLACEHOLDER.search(v):
            raise ControlError('APPROVAL_INVALID', f'{path.name}: {k} still holds a placeholder')
    if appr['status'] != 'APPROVED':
        raise ControlError('APPROVAL_NOT_APPROVED', f'{path.name}: status {appr["status"]!r}')
    if path.stem != appr['approval_id']:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: file name does not match approval_id')
    if appr['project_version'] != pol['project_version']:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: project_version {appr["project_version"]!r}')
    if appr['phase'] not in pol['known_phases']:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: unknown phase {appr["phase"]!r}')
    if not isinstance(appr['approver'], str) or not appr['approver'].strip():
        raise ControlError('APPROVAL_INVALID', f'{path.name}: approver missing')
    approved_at = _ts(appr['approved_at'], 'approved_at')
    if approved_at > now:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: approved_at is in the future')
    if appr['expires_at'] is not None and _ts(appr['expires_at'], 'expires_at') <= now:
        raise ControlError('APPROVAL_EXPIRED', f'{path.name}: expired at {appr["expires_at"]}')
    env = appr['environment']
    if env is not None and not _registered_environment(_environments(root, pol), env):
        raise ControlError('APPROVAL_INVALID', f'{path.name}: environment {env!r} is not registered')
    allowed, forbidden, _ = approval_scope(appr)
    unknown = [a for a in allowed + forbidden if a not in pol['actions']]
    if unknown:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: unknown scope actions {unknown}')
    if set(allowed) & set(forbidden):
        raise ControlError('APPROVAL_INVALID', f'{path.name}: actions both allowed and forbidden')
    commit = appr['approved_commit']
    if not isinstance(commit, str) or not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise ControlError('APPROVAL_INVALID', f'{path.name}: approved_commit must be a full 40-hex commit id')
    rel = str(path.relative_to(root))
    if _git(root, 'ls-files', '--error-unmatch', '--', rel)[0] != 0:
        raise ControlError('APPROVAL_NOT_COMMITTED', f'{rel} is not committed')
    if _git(root, 'diff', '--quiet', 'HEAD', '--', rel)[0] != 0:
        raise ControlError('APPROVAL_NOT_COMMITTED', f'{rel} has uncommitted modifications')
    if _git(root, 'merge-base', '--is-ancestor', commit, 'HEAD')[0] != 0:
        raise ControlError('APPROVAL_INVALID', f'{path.name}: approved_commit is not an ancestor of HEAD')


def select_approval(root, pol, approvals, phase, study, approval_id=None, now=None):
    cands = [(p, a) for p, a in approvals if a.get('phase') == phase and a.get('study') == study
             and (approval_id is None or a.get('approval_id') == approval_id)]
    if not cands:
        raise ControlError('NO_APPROVAL', f'no approval artifact for {phase}/{study}'
                           + (f' with id {approval_id}' if approval_id else ''))
    valid, errors = [], []
    for p, a in cands:
        try:
            validate_approval(root, pol, p, a, now)
            valid.append((p, a))
        except ControlError as e:
            errors.append(e)
    if not valid:
        raise errors[0]
    if len(valid) > 1:
        raise ControlError('AMBIGUOUS_APPROVAL', f'{len(valid)} valid approvals for {phase}/{study}; name one')
    return valid[0][1]


# ------------------------------------------------------------------------------------------------ decision log

def read_log(root, pol):
    p = root / pol['paths']['decision_log']
    if not p.exists():
        return []
    out = []
    for n, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                raise ControlError('LOG_CORRUPT', f'{p.name} line {n} is not JSON')
    return out


def _log_path(root, pol):
    return root / (pol['paths']['decision_log'] if pol else DEFAULT_LOG)


def _append_log(root, pol, record):
    p = _log_path(root, pol)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, sort_keys=True, default=str) + '\n')


def _record(decision, executor_called, **extra):
    r = {'record_type': 'DECISION', **asdict(decision), 'executor_called': executor_called}
    r['reason'] = f'{decision.reason_code}: {decision.reason}'
    r.update(extra)
    return r


def check_state_provenance(root, pol, state, pc, approvals, now=None):
    """A state other than PLANNED must be the result of a logged canonical transition backed by a valid approval.
    PLANNED is the least-privileged state and needs no provenance."""
    if state['active_phase_state'] == 'PLANNED':
        return None
    h = gate_hash(pol, state, pc)
    trs = [r for r in read_log(root, pol) if r.get('record_type') == 'TRANSITION' and r.get('decision') == 'ALLOW'
           and r.get('phase') == state['current_phase']]
    if not trs or trs[-1].get('new_gate_hash') != h:
        raise ControlError('STATE_PROVENANCE_INVALID',
                           f'{state["current_phase"]} {state["active_phase_state"]} has no matching canonical transition '
                           'record: gate fields were changed outside hlsdse.control.transition()')
    select_approval(root, pol, approvals, state['current_phase'], state['current_study'], trs[-1].get('approval_id'), now)
    return trs[-1]


# ---------------------------------------------------------------------------------------------------- decision

def _caller(depth=2):
    try:
        f = inspect.stack()[depth]
        return f'{Path(f.filename).name}:{f.function}'
    except Exception:
        return 'unknown'


def _seal(d: Decision):
    return hmac.new(_PROCESS_KEY, json.dumps(asdict(d), sort_keys=True).encode(), 'sha256').hexdigest()


def _argv_hash(argv):
    return _sha256(json.dumps([str(a) for a in argv]).encode()) if argv is not None else None


def _decide(root, action, phase, study, environment, *, actor, caller, argv=None, approval_id=None, now=None):
    root = Path(root or ROOT)
    now = now or _now()
    ctx = dict(request_id=str(uuid.uuid4()), timestamp_utc=now.isoformat(), actor=str(actor), caller=str(caller),
               action=action, category=None, phase=phase, study=study, environment=environment, approval_id=None,
               project_version=None, policy_version=None, state_schema_version=None, approval_schema_version=None,
               contract_version=None, repository_commit=None, state_hash=None, argv_sha256=_argv_hash(argv))
    pol = None

    def out(decision, code, reason):
        return Decision(decision=decision, reason_code=code, reason=reason, **ctx), pol

    try:
        pol = load_policy(root)
        ctx.update(policy_version=str(pol['policy_version']), project_version=pol['project_version'],
                   approval_schema_version=str(pol['approval_schema_version']))
        try:
            ctx['contract_version'] = str(_load_yaml(root / pol['canonical_contract'], 'CONTRACT_INVALID').get('schema_version'))
        except ControlError:
            ctx['contract_version'] = None
        rc, head = _git(root, 'rev-parse', 'HEAD')
        ctx['repository_commit'] = head if rc == 0 else None
        if action not in pol['actions']:
            return out('DENY', 'UNKNOWN_ACTION', f'action {action!r} is not defined in {POLICY_PATH}')
        cat_name = pol['actions'][action]
        cat = pol['categories'][cat_name]
        ctx['category'] = cat_name
        try:
            state, pc, sh = load_state(root, pol)
        except ControlError as e:
            return out('DENY', 'STATE_INVALID', f'{e.code}: {e.detail}' if e.code != 'STATE_INVALID' else e.detail)
        ctx.update(state_hash=sh, state_schema_version=str(state['state_schema_version']))
        if phase not in pol['known_phases']:
            return out('DENY', 'UNKNOWN_PHASE', f'phase {phase!r} is not a known phase')
        reg = _registry(root, pol)
        if not isinstance(study, str) or study not in reg['reserved']:
            return out('DENY', 'UNKNOWN_STUDY', f'study {study!r} is not in the study registry')
        if phase == 'P1' and state['p1_authorized'] is not True:
            return out('DENY', 'P1_NOT_AUTHORIZED', 'P1 is not authorized (p1_authorized: false)')
        if phase != state['current_phase']:
            return out('DENY', 'PHASE_MISMATCH', f'request phase {phase} != current phase {state["current_phase"]}')
        if study != state['current_study']:
            return out('DENY', 'STUDY_MISMATCH', f'request study {study} != current study {state["current_study"]}')
        envs = _environments(root, pol)
        if environment is not None and not _registered_environment(envs, environment):
            return out('DENY', 'UNKNOWN_ENVIRONMENT', f'environment {environment!r} is not registered')
        try:
            approvals = load_approvals(root, pol)
            check_state_provenance(root, pol, state, pc, approvals, now)
        except ControlError as e:
            return out('DENY', e.code, e.detail)
        if not cat['gated']:
            return out('ALLOW', 'UNGATED_CATEGORY', f'{cat_name} needs a valid policy and state only')

        if state['active_phase_state'] not in cat['allowed_phase_states']:
            return out('DENY', 'PHASE_STATE_NOT_ACTIVE',
                       f'{cat_name} is not permitted while {phase} is {state["active_phase_state"]}')
        if ctx['repository_commit'] is None:
            return out('DENY', 'REPOSITORY_UNKNOWN', 'cannot determine the repository commit')
        try:
            appr = select_approval(root, pol, approvals, phase, study, approval_id, now)
        except ControlError as e:
            return out('DENY', e.code, e.detail)
        ctx['approval_id'] = appr['approval_id']
        allowed, forbidden, _ = approval_scope(appr)
        if action in forbidden:
            return out('DENY', 'OUT_OF_SCOPE', f'{action} is forbidden by {appr["approval_id"]}')
        if action not in allowed:
            return out('DENY', 'OUT_OF_SCOPE', f'{action} is not in the allowed scope of {appr["approval_id"]}')
        active_env = state['active_environment']
        if appr['environment'] != active_env:
            return out('DENY', 'ENVIRONMENT_MISMATCH',
                       f'approval environment {appr["environment"]!r} != active_environment {active_env!r}')
        if cat.get('requires_environment'):
            if environment is None:
                return out('DENY', 'ENVIRONMENT_REQUIRED', f'{cat_name} requires an environment; none given')
            if environment != active_env:
                return out('DENY', 'ENVIRONMENT_NOT_ACTIVE', f'{environment} is not the active environment ({active_env!r})')
        elif environment is not None and environment != active_env:
            return out('DENY', 'ENVIRONMENT_NOT_ACTIVE', f'{environment} is not the active environment ({active_env!r})')
        if cat.get('requires_hardware'):
            dev = (envs.get(environment) or {}).get('device') or {}
            if dev.get('hardware_available') is not True:
                return out('DENY', 'HARDWARE_NOT_AVAILABLE', f'{environment} has no hardware available')
        st = (reg.get('study_status') or {}).get(study) or {}
        if st.get('status') not in EXECUTABLE_STUDY_STATUSES:
            return out('DENY', 'STUDY_NOT_EXECUTABLE', f'{study} registry status {st.get("status")!r}')
        return out('ALLOW', 'AUTHORIZED', f'{action} within {appr["approval_id"]} for {phase}/{study}')
    except ControlError as e:
        return out('DENY', e.code, e.detail)
    except Exception as e:                                   # never let an unexpected error become ALLOW
        return out('DENY', 'INTERNAL_ERROR', f'{type(e).__name__}: {e}')


def authorize(action, phase, study, environment, *, actor, caller=None, argv=None, approval_id=None, root=None):
    """Decide and log. Returns a Decision; never executes anything. A decision that cannot be logged is DENY."""
    root = Path(root or ROOT)
    d, pol = _decide(root, action, phase, study, environment, actor=actor, caller=caller or _caller(),
                     argv=argv, approval_id=approval_id)
    try:
        _append_log(root, pol, _record(d, False))
    except OSError as e:
        d = replace(d, decision='DENY', reason_code='LOG_UNAVAILABLE', reason=f'decision log not writable: {e}')
    return d


def _execute(decision, argv, *, cwd=None, stdout=None, stderr=None, env=None):
    """The only tool executor. Refuses anything but a sealed, unused ALLOW decision bound to this exact argv."""
    if not isinstance(decision, Decision) or decision.decision != 'ALLOW':
        raise ExecutionDenied('no ALLOW decision')
    seal = _ISSUED.pop(decision.request_id, None)
    if seal is None or not hmac.compare_digest(seal, _seal(decision)):
        raise ExecutionDenied('decision was not issued for execution by run_authorized (forged or reused)')
    if decision.argv_sha256 != _argv_hash(argv):
        raise ExecutionDenied('argv differs from the authorized command')
    return subprocess.run([str(a) for a in argv], shell=False, cwd=cwd, stdout=stdout, stderr=stderr, env=env).returncode


@dataclass(frozen=True)
class ExecutionResult:
    decision: Decision
    executor_called: bool
    returncode: int | None
    log_error: str | None = None          # the tool ran but its post-execution record could not be written


def run_authorized(argv, *, action, phase, study, environment, actor, caller=None, approval_id=None, root=None,
                   cwd=None, stdout=None, stderr=None, env=None, resolve=None):
    """Authorize, then execute argv (a list; never a shell string) only on ALLOW. DENY never reaches subprocess.
    `resolve(argv) -> argv` may map a tool name to its verified path after ALLOW; a ControlError from it is DENY."""
    root = Path(root or ROOT)
    caller = caller or _caller()
    if isinstance(argv, (str, bytes)) or not argv or not all(isinstance(a, (str, os.PathLike)) for a in argv):
        d, pol = _decide(root, None, phase, study, environment, actor=actor, caller=caller)
        d = replace(d, decision='DENY', reason_code='INVALID_REQUEST', reason='argv must be a non-empty list, not a shell string')
    else:
        argv = [str(a) for a in argv]
        d, pol = _decide(root, action, phase, study, environment, actor=actor, caller=caller, argv=argv,
                         approval_id=approval_id)
        if d.allowed and resolve is not None:
            try:
                argv = [str(a) for a in resolve(argv)]
                d = replace(d, argv_sha256=_argv_hash(argv))
            except ControlError as e:
                d = replace(d, decision='DENY', reason_code=e.code, reason=e.detail)
    if not d.allowed:
        try:
            _append_log(root, pol, _record(d, False))
        except OSError:
            pass                                              # still DENY; nothing ran
        return ExecutionResult(d, False, None)
    try:
        log = _log_path(root, pol)
        log.parent.mkdir(parents=True, exist_ok=True)
        log.open('a').close()                                 # an unloggable ALLOW must not execute
    except OSError as e:
        d = replace(d, decision='DENY', reason_code='LOG_UNAVAILABLE', reason=f'decision log not writable: {e}')
        return ExecutionResult(d, False, None)
    _ISSUED[d.request_id] = _seal(d)
    rc, err = None, None
    try:
        rc = _execute(d, argv, cwd=cwd, stdout=stdout, stderr=stderr, env=env)
    except ExecutionDenied as e:                              # refused inside the executor: nothing ran
        try:
            _append_log(root, pol, _record(replace(d, decision='DENY', reason_code='EXECUTION_REFUSED', reason=str(e)), False))
        except OSError:
            pass
        raise
    except OSError as e:                                      # the executor was called; the program did not start
        err = f'{type(e).__name__}: {e}'
    finally:
        _ISSUED.pop(d.request_id, None)
    try:
        _append_log(root, pol, _record(d, True, executor_returncode=rc, executor_error=err))
    except OSError as e:                                      # the tool already ran: report, do not hide its result
        print(f'HLSDSE_CONTROL_WARNING: post-execution record for {d.request_id} not written: {e}', file=sys.stderr)
        return ExecutionResult(d, True, rc, log_error=f'{type(e).__name__}: {e}')
    return ExecutionResult(d, True, rc)


# -------------------------------------------------------------------------------------------------- transition

def _set_scalar(text, key, old, new, fname):
    pat = re.compile(rf'^{re.escape(key)}:[ \t]*{re.escape(old)}[ \t]*$', re.M)
    if len(pat.findall(text)) != 1:
        raise ControlError('STATE_INVALID', f'{fname}: expected exactly one "{key}: {old}" line')
    return pat.sub(f'{key}: {new}', text)


def transition(to_state, *, approval_id, actor, reason, to_phase=None, root=None):
    """The canonical phase-state transition. Enforces PHASE_CONTROL.yaml transition_rules and
    CONTROL_PLANE_POLICY transition_requirements, rewrites only the state fields, and logs a TRANSITION record.
    Never changes the phase, P1 authorization, the human-gate fields or active_environment."""
    root = Path(root or ROOT)
    now = _now()
    rec = {'record_type': 'TRANSITION', 'request_id': str(uuid.uuid4()), 'timestamp_utc': now.isoformat(),
           'actor': actor, 'reason': reason, 'approval_id': approval_id, 'to_state': to_state, 'to_phase': to_phase,
           'executor_called': False}
    pol = None
    try:
        pol = load_policy(root)
        rec.update(policy_version=str(pol['policy_version']), project_version=pol['project_version'])
        rec['repository_commit'] = _git(root, 'rev-parse', 'HEAD')[1] or None
        sp, pp = root / pol['paths']['state'], root / pol['paths']['phase_control']
        state, pc, old_sha = load_state(root, pol)
        approvals = load_approvals(root, pol)
        check_state_provenance(root, pol, state, pc, approvals, now)
        phase, study, cur = state['current_phase'], state['current_study'], state['active_phase_state']
        rec.update(phase=phase, study=study, old_state=cur, state_schema_version=str(state['state_schema_version']),
                   old_state_sha256=old_sha, old_gate_hash=gate_hash(pol, state, pc))
        if to_phase is not None and to_phase != phase:
            raise ControlError('PHASE_ADVANCE_FORBIDDEN', f'{phase} -> {to_phase}: a phase change is a human gate decision, '
                               'not an automated transition')
        rule = next((r for r in pc['transition_rules'] if r.get('from') == cur and r.get('to') == to_state), None)
        if rule is None:
            raise ControlError('INVALID_TRANSITION', f'{cur} -> {to_state} is not in the PHASE_CONTROL transition table')
        req = pol['transition_requirements'].get(rule.get('requires'))
        if req == 'human_only':
            raise ControlError('HUMAN_ONLY_TRANSITION', f'{cur} -> {to_state} requires {rule["requires"]} by the researcher')
        if req != 'valid_approval':
            raise ControlError('INVALID_TRANSITION', f'unknown requirement {rule.get("requires")!r}')
        appr = select_approval(root, pol, approvals, phase, study, approval_id, now)
        if appr['environment'] != state['active_environment']:
            raise ControlError('ENVIRONMENT_MISMATCH', f'approval environment {appr["environment"]!r} != '
                               f'active_environment {state["active_environment"]!r}; set by a human gate commit')
        s_old, p_old = sp.read_text(encoding='utf-8'), pp.read_text(encoding='utf-8')
        s_new = _set_scalar(_set_scalar(s_old, 'status', cur, to_state, sp.name), 'active_phase_state', cur, to_state, sp.name)
        p_new = _set_scalar(p_old, 'state', cur, to_state, pp.name)
        ns, npc = yaml.safe_load(s_new), yaml.safe_load(p_new)
        changed = {k for k in set(state) | set(ns) if state.get(k) != ns.get(k)}
        changed_pc = {k for k in set(pc) | set(npc) if pc.get(k) != npc.get(k)}
        if changed != {'status', 'active_phase_state'} or changed_pc != {'state'}:
            raise ControlError('STATE_INVALID', f'transition would change unexpected fields: {sorted(changed | changed_pc)}')
        validate_state(root, pol, ns, npc)
        _write_pair(((sp, s_old, s_new), (pp, p_old, p_new)))
        rec.update(decision='ALLOW', reason_code='TRANSITIONED', new_state=to_state, approval_id=appr['approval_id'],
                   requires=rule['requires'], new_state_sha256=_sha256(s_new.encode()),
                   new_gate_hash=gate_hash(pol, ns, npc))
        try:
            _append_log(root, pol, rec)
        except OSError:
            _write_pair(((sp, s_new, s_old), (pp, p_new, p_old)))
            raise ControlError('LOG_UNAVAILABLE', 'transition rolled back: decision log not writable')
        return rec
    except Exception as exc:                                  # any failure is a logged DENY, never a partial ALLOW
        e = exc if isinstance(exc, ControlError) else ControlError('INTERNAL_ERROR', f'{type(exc).__name__}: {exc}')
        rec.update(decision='DENY', reason_code=e.code, reason=f'{e.code}: {e.detail} (requested by {actor}: {reason})')
        try:
            _append_log(root, pol, rec)
        except OSError:
            pass
        if e is exc:
            raise
        raise e from exc


def _write_pair(files):
    """Replace several files as one unit: every new text is written to a temp file first, then each is moved into
    place; if any replace fails, the files already replaced are restored to their old text."""
    tmps = []
    try:
        for path, _old, new in files:
            tmp = path.with_suffix(path.suffix + '.tmp')
            tmp.write_text(new, encoding='utf-8')
            tmps.append(tmp)
        done = []
        try:
            for (path, old, _new), tmp in zip(files, tmps):
                os.replace(tmp, path)
                done.append((path, old))
        except OSError:
            for path, old in done:
                path.write_text(old, encoding='utf-8')
            raise ControlError('STATE_WRITE_FAILED', 'state files could not be replaced; previous state restored')
    finally:
        for tmp in tmps:
            if tmp.exists():
                tmp.unlink()


# ------------------------------------------------------------------------------------------- repository checks

def repository_control_errors(root=None, now=None):
    """Checks shared with scripts/validate_project.py: policy, state machine, provenance, approvals, log."""
    try:
        return _repository_control_errors(Path(root or ROOT), now)
    except Exception as e:
        return [f'INTERNAL_ERROR: {type(e).__name__}: {e}']


def _repository_control_errors(root, now):
    errs = []
    try:
        pol = load_policy(root)
    except ControlError as e:
        return [f'{e.code}: {e.detail}']
    try:
        auto = _load_yaml(root / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml', 'POLICY_INVALID')
        prot = {f: list(v) for f, v in auto['protected_state']['files'].items()}
        if prot != {f: list(v) for f, v in pol['gate_fields'].items()}:
            errs.append('POLICY_INVALID: CONTROL_PLANE_POLICY gate_fields differ from AUTO_PUSH_POLICY protected_state')
    except (ControlError, KeyError, TypeError) as e:
        errs.append(f'POLICY_INVALID: AUTO_PUSH_POLICY.yaml protected_state unreadable ({e})')
    try:
        state, pc, _ = load_state(root, pol)
    except ControlError as e:
        return errs + [f'{e.code}: {e.detail}']
    try:
        read_log(root, pol)
    except ControlError as e:
        errs.append(f'{e.code}: {e.detail}')
    try:
        approvals = load_approvals(root, pol)
    except ControlError as e:
        return errs + [f'{e.code}: {e.detail}']
    for p, a in approvals:
        try:
            validate_approval(root, pol, p, a, now)
        except ControlError as e:
            errs.append(f'{e.code}: {e.detail}')
    try:
        check_state_provenance(root, pol, state, pc, approvals, now)
    except ControlError as e:
        errs.append(f'{e.code}: {e.detail}')
    if state['active_phase_state'] in ACTIVE_GATE_STATES:
        try:
            appr = select_approval(root, pol, approvals, state['current_phase'], state['current_study'], None, now)
            if appr['environment'] != state['active_environment']:
                errs.append(f'ENVIRONMENT_MISMATCH: approval {appr["approval_id"]} environment {appr["environment"]!r} '
                            f'!= active_environment {state["active_environment"]!r}')
        except ControlError as e:
            errs.append(f'{e.code}: {state["current_phase"]} is {state["active_phase_state"]} without a valid approval ({e.detail})')
    return errs


# --------------------------------------------------------------------------------------------- launcher gate

def classify_tool(pol, tool, args):
    """Map a tool invocation to an action by executable identity; pure version/help queries are discovery."""
    entry = pol['tools'].get(tool)
    if entry is None:
        return None
    rest = list(args)
    mode = None
    if len(rest) >= 2 and rest[0] == '--mode':
        mode, rest = rest[1], rest[2:]
    if rest and all(a in pol['discovery_flags'] for a in rest):
        return 'environment_discovery'
    if isinstance(entry, dict):
        return entry.get(f'mode_{mode}', entry['default']) if mode else entry['default']
    return entry


def _resolver(tool, shim_dir, tool_root):
    def resolve(argv):
        if not tool_root:
            raise ControlError('TOOL_NOT_RESOLVED', 'HLSDSE_XILINX_ROOT not set (tool gate used outside the launcher)')
        troot = os.path.realpath(tool_root)
        for entry in os.environ.get('PATH', '').split(os.pathsep):
            if not entry or os.path.realpath(entry) == os.path.realpath(shim_dir):
                continue
            cand = os.path.join(entry, tool)
            if os.path.isfile(cand) and os.access(cand, os.X_OK):
                real = os.path.realpath(cand)
                if os.path.commonpath([real, troot]) != troot:
                    raise ControlError('TOOL_NOT_RESOLVED', f'{tool} resolves outside {troot}: {real}')
                return [cand, *argv[1:]]
        raise ControlError('TOOL_NOT_RESOLVED', f'{tool} not found on PATH behind the gate')
    return resolve


def tool_gate_main(args=None):
    """Entry point for environments/xilinx_2025_2_1/bin/<tool>:
       tool_gate --root R --tool T --shim-dir D -- <args...>   -> tool exit code, or 126 on DENY."""
    args = list(sys.argv[1:] if args is None else args)
    try:
        sep = args.index('--')
        opts = dict(zip(args[:sep:2], args[1:sep:2]))
        root, tool, shim_dir, targs = Path(opts['--root']), opts['--tool'], opts['--shim-dir'], args[sep + 1:]
    except (ValueError, KeyError):
        print('HLSDSE_CONTROL_DENY: INVALID_REQUEST usage: --root R --tool T --shim-dir D -- args', file=sys.stderr)
        return 126
    action, phase, study = None, None, None
    try:
        pol = load_policy(root)
        action = classify_tool(pol, tool, targs) or f'unclassified_tool:{tool}'
        s = yaml.safe_load((root / pol['paths']['state']).read_text(encoding='utf-8')) or {}
        phase, study = s.get('current_phase'), s.get('current_study')
    except Exception:
        pass                                                   # _decide re-checks and denies
    res = run_authorized([tool, *targs], action=action, phase=phase, study=study,
                         environment=os.environ.get('HLSDSE_ENVIRONMENT_ID') or None,
                         actor=os.environ.get('USER', 'unknown'), caller=f'launcher-gate:{tool}', root=root,
                         resolve=_resolver(tool, shim_dir, os.environ.get('HLSDSE_XILINX_ROOT')))
    if not res.executor_called:
        d = res.decision
        print(f'HLSDSE_CONTROL_DENY: {d.reason_code}: {d.reason} (action={d.action} request_id={d.request_id})',
              file=sys.stderr)
        return 126
    return res.returncode if res.returncode is not None else 126


if __name__ == '__main__':
    raise SystemExit(tool_gate_main())
