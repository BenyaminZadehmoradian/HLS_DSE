"""Runtime control-plane tests (P0/S00, approval G0-P0-S00-001 scope: control-plane, mock, negative, bypass,
validator tests). Mock tools only; every repository is synthetic (tests/control_harness.py)."""
import ast
import json
from pathlib import Path

import pytest

from control_harness import ENV_ID, REPO, SyntheticRepo, approval, git
from hlsdse import control
from hlsdse.control import ControlError, Decision, ExecutionDenied
from hlsdse.flow import run_command
from hlsdse.models import RunRecord

REQUIRED_LOG_FIELDS = ('request_id', 'timestamp_utc', 'actor', 'action', 'phase', 'study', 'environment', 'state_hash',
                       'state_schema_version', 'policy_version', 'approval_id', 'repository_commit', 'decision',
                       'reason', 'caller', 'executor_called', 'project_version', 'contract_version')


@pytest.fixture
def spy(monkeypatch):
    calls = []
    real = control._execute

    def wrapped(decision, argv, **kw):
        calls.append(list(argv))
        return real(decision, argv, **kw)
    monkeypatch.setattr(control, '_execute', wrapped)
    return calls


def run(repo, action, phase='P0', study='S00', environment=None, tool=None, **kw):
    return control.run_authorized([repo.mock(tool or 'mock_control_step'), '--mock'], action=action, phase=phase,
                                  study=study, environment=environment, actor='pytest', root=repo.root, **kw)


def assert_denied(repo, res, spy, code=None):
    assert res.decision.decision == 'DENY', res.decision
    assert res.executor_called is False and res.returncode is None
    assert spy == [] and not repo.tool_reached()
    rec = repo.decisions()[-1]
    assert rec['decision'] == 'DENY' and rec['executor_called'] is False
    assert rec['request_id'] == res.decision.request_id
    if code:
        assert res.decision.reason_code == code, res.decision.reason
    return rec


# ------------------------------------------------------------------------------------ A-N negative tests

def test_a_unauthorized_p0_research_request(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    assert_denied(repo, run(repo, 'research_hls_runs'), spy, 'OUT_OF_SCOPE')
    assert_denied(repo, run(repo, 'research_vivado_runs', environment=ENV_ID, tool='vivado'), spy, 'OUT_OF_SCOPE')
    assert_denied(repo, run(repo, 'scientific_experiments'), spy, 'OUT_OF_SCOPE')


def test_b_unauthorized_p1(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    assert_denied(repo, run(repo, 'control_plane_implementation', phase='P1', study='S01'), spy, 'P1_NOT_AUTHORIZED')
    assert_denied(repo, run(repo, 'p1_implementation'), spy, 'OUT_OF_SCOPE')


def test_c_human_approval_missing(tmp_path, spy):
    repo = SyntheticRepo(tmp_path, state='PLANNED', with_approval=False)
    # PLANNED: gated work is not permitted at all
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'PHASE_STATE_NOT_ACTIVE')
    # a transition cannot start without an approval
    with pytest.raises(ControlError) as e:
        control.transition('IMPLEMENTING', approval_id=None, actor='pytest', reason='no approval', root=repo.root)
    assert e.value.code == 'NO_APPROVAL'
    # an approval that disappears after the transition: every gated request is denied
    repo2 = SyntheticRepo(tmp_path / 'b')
    git(repo2.root, 'rm', '-q', 'audit/gates/approvals/G0-P0-S00-001.yaml'); git(repo2.root, 'commit', '-q', '-m', 'rm')
    assert_denied(repo2, run(repo2, 'control_plane_implementation'), spy, 'NO_APPROVAL')


def test_d_wrong_study(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    assert_denied(repo, run(repo, 'control_plane_implementation', study='S01'), spy, 'STUDY_MISMATCH')
    assert_denied(repo, run(repo, 'control_plane_implementation', study='S99X'), spy, 'UNKNOWN_STUDY')


def test_e_wrong_phase(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    assert_denied(repo, run(repo, 'control_plane_implementation', phase='P2'), spy, 'PHASE_MISMATCH')
    assert_denied(repo, run(repo, 'control_plane_implementation', phase='P42'), spy, 'UNKNOWN_PHASE')


def test_f_null_environment_where_required(tmp_path, spy):
    # even an approval that allowed HLS runs could not run them without an environment
    repo = SyntheticRepo(tmp_path, approval_kw={'allowed': ['research_hls_runs']})
    assert_denied(repo, run(repo, 'research_hls_runs', environment=None), spy, 'ENVIRONMENT_REQUIRED')


def test_g_unknown_environment(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    assert_denied(repo, run(repo, 'control_plane_implementation', environment='ENV-DOES-NOT-EXIST'), spy,
                  'UNKNOWN_ENVIRONMENT')
    assert_denied(repo, run(repo, 'control_plane_implementation', environment='ENV-001'), spy,   # template only
                  'UNKNOWN_ENVIRONMENT')
    # a registered environment that is not the approved/active one (active_environment is null)
    assert_denied(repo, run(repo, 'control_plane_implementation', environment=ENV_ID), spy, 'ENVIRONMENT_NOT_ACTIVE')


@pytest.mark.parametrize('old,new', [
    ('p1_authorized: false\n', ''),                                      # missing security field
    ('p1_authorized: false', 'p1_authorized: true'),                      # unauthorized value
    ('human_gate_required: true', 'human_gate_required: maybe'),          # malformed value
    ('automatic_advance: false', 'automatic_advance: true'),
    ('current_phase: P0', 'current_phase: P9'),                           # inconsistent with active_phase
    ('active_phase_state: IMPLEMENTING', 'active_phase_state: RUNNING'),  # unknown state
    ('active_environment: null', 'active_environment: ENV-NOPE'),         # unregistered environment
    ('active_environment: null\n', ''),                                   # missing field
    ('state_schema_version: \'1.0\'', 'state_schema_version: \'9.9\''),
    ('project_version: V23.2', 'project_version: V99'),
    ('current_phase: P0', 'current_phase: [P0'),                          # unparseable YAML
])
def test_h_malformed_state(tmp_path, spy, old, new):
    repo = SyntheticRepo(tmp_path)
    repo.edit('RESEARCH_STATE.yaml', old, new)
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'STATE_INVALID')
    assert control.repository_control_errors(repo.root)


def test_h_state_file_missing_and_phase_control_inconsistent(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    repo.edit('AI_CONTROL/PHASE_CONTROL.yaml', 'state: IMPLEMENTING', 'state: PLANNED')
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'STATE_INVALID')
    (repo.root / 'RESEARCH_STATE.yaml').unlink()
    assert_denied(repo, run(repo, 'environment_discovery'), spy, 'STATE_INVALID')


@pytest.mark.parametrize('mutation', ['missing', 'malformed', 'incomplete', 'bad_category'])
def test_i_missing_or_malformed_policy(tmp_path, spy, mutation):
    repo = SyntheticRepo(tmp_path)
    p = repo.root / 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml'
    if mutation == 'missing':
        p.unlink()
    elif mutation == 'malformed':
        p.write_text('policy_version: [1.0\n')
    elif mutation == 'incomplete':
        p.write_text('policy_version: "1.0"\n')
    else:
        repo.edit('AI_CONTROL/CONTROL_PLANE_POLICY.yaml', 'control_plane_implementation: CONTROL_PLANE',
                  'control_plane_implementation: SUPERUSER')
    res = run(repo, 'control_plane_implementation')
    assert_denied(repo, res, spy, 'POLICY_INVALID')
    assert res.decision.policy_version is None
    assert_denied(repo, run(repo, 'environment_discovery'), spy, 'POLICY_INVALID')   # ungated also fails closed


def test_j_direct_executor_invocation(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    argv = [repo.mock(), '--direct']
    forged = Decision(decision='ALLOW', reason_code='AUTHORIZED', reason='forged', request_id='forged-1',
                      timestamp_utc='now', actor='attacker', caller='x', action='control_plane_implementation',
                      category='CONTROL_PLANE', phase='P0', study='S00', environment=None, approval_id='G0-P0-S00-001',
                      project_version='V23.2', policy_version='1.0', state_schema_version='1.0',
                      approval_schema_version='1.0', contract_version='1.0', repository_commit=None, state_hash=None,
                      argv_sha256=control._argv_hash(argv))
    with pytest.raises(ExecutionDenied):
        control._execute(forged, argv)
    # a genuine ALLOW from authorize() is a decision, not an execution permit
    real = control.authorize('control_plane_implementation', 'P0', 'S00', None, actor='pytest', root=repo.root)
    assert real.allowed
    with pytest.raises(ExecutionDenied):
        control._execute(real, argv)
    with pytest.raises(ExecutionDenied):
        control._execute(None, argv)
    assert not repo.tool_reached()
    # the run-level executor (hlsdse.flow.run_command) goes through the control plane
    rr = RunRecord(run_id='R-J', study_id='S00', benchmark_id='MOCK', environment_id=None, candidate_id='C')
    out = run_command(rr, [repo.mock('vivado'), '-mode', 'batch'], tmp_path / 'j.log', action='research_vivado_runs',
                      root=repo.root)
    assert out.status == 'DENIED' and out.metrics['control_decision'] == 'DENY'
    assert not repo.tool_reached() and repo.decisions()[-1]['executor_called'] is False
    # a shell string is never handed to a shell
    res = control.run_authorized(f'{repo.mock()} ; touch {tmp_path}/pwned', action='control_plane_implementation',
                                 phase='P0', study='S00', environment=None, actor='pytest', root=repo.root)
    assert res.decision.reason_code == 'INVALID_REQUEST' and not (tmp_path / 'pwned').exists()


def test_j_argv_is_bound_to_the_decision(tmp_path, monkeypatch):
    repo = SyntheticRepo(tmp_path)
    real_decide = control._decide
    # tamper with the argv after the decision: the executor refuses
    monkeypatch.setattr(control, '_decide', lambda *a, **k: (lambda d, p: (control.replace(d, argv_sha256='0' * 64), p))(*real_decide(*a, **k)))
    with pytest.raises(ExecutionDenied):
        run(repo, 'control_plane_implementation')
    assert not repo.tool_reached()


def test_k_launcher_gate_denies_before_tool(tmp_path):
    repo = SyntheticRepo(tmp_path)
    cp = repo.run_shim('vivado', '-mode', 'batch', '-source', 'mock.tcl')
    assert cp.returncode == 126 and 'HLSDSE_CONTROL_DENY: OUT_OF_SCOPE' in cp.stderr
    assert not repo.tool_reached()
    rec = repo.decisions()[-1]
    assert rec['action'] == 'research_vivado_runs' and rec['caller'] == 'launcher-gate:vivado'
    assert rec['executor_called'] is False and rec['environment'] == ENV_ID
    cp = repo.run_shim('vitis-run', '--mode', 'hls', '--tcl', 'x.tcl')
    assert cp.returncode == 126 and repo.decisions()[-1]['action'] == 'research_hls_runs'
    # outside run_in_env.sh the gate refuses outright
    cp = repo.run_shim('vivado', '-mode', 'batch', xilinx_env=None)
    assert cp.returncode == 126 and not repo.tool_reached()


def test_k_launcher_gate_allows_only_authorized_and_resolved_tools(tmp_path):
    # synthetic approval with research scope + active environment: the mock tool behind the gate runs
    repo = SyntheticRepo(tmp_path, active_environment=ENV_ID,
                         approval_kw={'allowed': ['research_vivado_runs'], 'environment': ENV_ID})
    cp = repo.run_shim('vivado', '-mode', 'batch', '-source', 'mock.tcl')
    assert cp.returncode == 0, cp.stderr
    assert repo.tool_reached() and 'MOCK vivado -mode batch' in repo.marker.read_text()
    assert repo.decisions()[-1]['executor_called'] is True and repo.decisions()[-1]['executor_returncode'] == 0
    repo.marker.unlink()
    # a tool root that does not contain the tool: resolution fails closed
    cp = repo.run_shim('vivado', '-mode', 'batch', tool_root=False)
    assert cp.returncode == 126 and 'TOOL_NOT_RESOLVED' in cp.stderr and not repo.tool_reached()


def test_k_version_query_is_environment_discovery(tmp_path):
    repo = SyntheticRepo(tmp_path)
    cp = repo.run_shim('vivado', '-version')
    assert cp.returncode == 0 and repo.decisions()[-1]['action'] == 'environment_discovery'
    assert repo.decisions()[-1]['decision'] == 'ALLOW'


@pytest.mark.xfail(strict=True, reason='bin/vitis_hls execs $XILINX_VITIS/bin/vitis-run directly; the launcher '
                   'patch that routes it through the gated vitis-run shim was not applied (see implementation report)')
def test_k_vitis_hls_shim_is_gated(tmp_path):
    repo = SyntheticRepo(tmp_path)
    vit = tmp_path / 'vitis_root'
    (vit / 'bin').mkdir(parents=True)
    (vit / 'bin/vitis-run').write_text(f"#!/bin/sh\necho \"MOCK vitis-run $*\" >> '{repo.marker}'\n")
    (vit / 'bin/vitis-run').chmod(0o755)
    import subprocess
    subprocess.run([str(repo.root / 'environments/xilinx_2025_2_1/bin/vitis_hls'), '-f', 'x.tcl'], capture_output=True,
                   env={'PATH': '/usr/bin:/bin', 'HLSDSE_XILINX_ENV': '2025.2.1', 'XILINX_VITIS': str(vit)})
    assert not repo.tool_reached()


def test_l_invalid_phase_transitions(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    for to, kw, code in [('GATE_REVIEW', {}, 'INVALID_TRANSITION'),
                         ('APPROVED_FOR_NEXT_PHASE', {}, 'INVALID_TRANSITION'),
                         ('RUNNING', {}, 'INVALID_TRANSITION'),
                         ('IMPLEMENTING', {'to_phase': 'P1'}, 'PHASE_ADVANCE_FORBIDDEN')]:
        with pytest.raises(ControlError) as e:
            control.transition(to, approval_id=None, actor='pytest', reason='negative', root=repo.root, **kw)
        assert e.value.code == code
    denied = [r for r in repo.log() if r['record_type'] == 'TRANSITION' and r['decision'] == 'DENY']
    assert len(denied) == 4
    gate = SyntheticRepo(tmp_path / 'g', state='GATE_REVIEW')
    with pytest.raises(ControlError) as e:
        control.transition('APPROVED_FOR_NEXT_PHASE', approval_id=None, actor='pytest', reason='self-approve',
                           root=gate.root)
    assert e.value.code == 'HUMAN_ONLY_TRANSITION'


def test_l_direct_state_write_is_not_authorization(tmp_path, spy):
    repo = SyntheticRepo(tmp_path, state='PLANNED')
    repo.edit('RESEARCH_STATE.yaml', 'status: PLANNED', 'status: IMPLEMENTING')
    repo.edit('RESEARCH_STATE.yaml', 'active_phase_state: PLANNED', 'active_phase_state: IMPLEMENTING')
    repo.edit('AI_CONTROL/PHASE_CONTROL.yaml', 'state: PLANNED', 'state: IMPLEMENTING')
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'STATE_PROVENANCE_INVALID')
    assert any('STATE_PROVENANCE_INVALID' in e for e in control.repository_control_errors(repo.root))
    # a direct P0 -> P1 rewrite is rejected too
    repo2 = SyntheticRepo(tmp_path / 'b')
    for f in ('current_phase', 'active_phase'):
        repo2.edit('RESEARCH_STATE.yaml', f'{f}: P0', f'{f}: P1')
    repo2.edit('RESEARCH_STATE.yaml', 'p1_authorized: false', 'p1_authorized: true')
    repo2.edit('AI_CONTROL/PHASE_CONTROL.yaml', 'active_phase: P0', 'active_phase: P1')
    assert_denied(repo2, run(repo2, 'control_plane_implementation', phase='P1', study='S00'), spy, 'STATE_INVALID')


def test_m_expired_or_unusable_approval(tmp_path, spy):
    repo = SyntheticRepo(tmp_path, approval_kw={'expires_at': '2099-01-01T00:00:00+00:00'})
    assert run(repo, 'control_plane_implementation').decision.allowed
    spy.clear(); repo.marker.unlink()
    repo.write_approval(approval(repo.base_commit, expires_at='2026-01-02T00:00:00+00:00'))
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'APPROVAL_EXPIRED')
    assert any('APPROVAL_EXPIRED' in e for e in control.repository_control_errors(repo.root))


@pytest.mark.parametrize('over,commit,code', [
    ({'approver': '<YOUR_NAME>'}, True, 'APPROVAL_INVALID'),
    ({'status': 'PENDING'}, True, 'APPROVAL_NOT_APPROVED'),
    ({'approved_at': '2999-01-01T00:00:00+00:00'}, True, 'APPROVAL_INVALID'),
    ({'approved_at': '2026-01-01T00:00:00'}, True, 'APPROVAL_INVALID'),          # no timezone
    ({'approved_commit': '0' * 40}, True, 'APPROVAL_INVALID'),                    # not an ancestor
    ({'project_version': 'V22'}, True, 'APPROVAL_INVALID'),
    ({}, False, 'APPROVAL_NOT_COMMITTED'),                                        # written, never committed
])
def test_m_approval_validation(tmp_path, spy, over, commit, code):
    repo = SyntheticRepo(tmp_path)
    repo.write_approval(approval(repo.base_commit, **over), commit=commit)
    if not commit:
        repo.edit('audit/gates/approvals/G0-P0-S00-001.yaml', 'SYNTHETIC_TEST_FIXTURE', 'SOMEONE_ELSE')
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, code)


def test_m_corrupt_permission_data(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    repo.write_approval('approval_id: [broken\n', name='G0-P0-S00-002')
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'APPROVAL_CORRUPT')


def test_n_wrong_approval_scope(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    for action in ('dse_campaigns', 'xsa', 'bitstream', 'elf', 'hardware_programming', 'hardware_execution'):
        assert_denied(repo, run(repo, action, environment=None), spy, 'OUT_OF_SCOPE')
    assert_denied(repo, run(repo, 'launch_missiles'), spy, 'UNKNOWN_ACTION')
    narrow = SyntheticRepo(tmp_path / 'narrow', approval_kw={'allowed': ['unit_tests']})
    assert_denied(narrow, run(narrow, 'control_plane_implementation'), spy, 'OUT_OF_SCOPE')


# ------------------------------------------------------------------------------------ positive mock test

def test_positive_mock_control_plane_request(tmp_path, spy):
    repo = SyntheticRepo(tmp_path, approval_kw={'layout': 'flat'})     # the layout of the real G0-P0-S00-001
    res = run(repo, 'control_plane_implementation')
    assert res.decision.decision == 'ALLOW' and res.decision.reason_code == 'AUTHORIZED'
    assert res.executor_called is True and res.returncode == 0
    assert spy == [[repo.mock(), '--mock']] and repo.tool_reached()
    assert 'MOCK mock_control_step --mock' in repo.marker.read_text()
    rec = repo.decisions()[-1]
    assert rec['decision'] == 'ALLOW' and rec['executor_called'] is True and rec['executor_returncode'] == 0
    assert rec['approval_id'] == 'G0-P0-S00-001' and rec['environment'] is None
    for f in REQUIRED_LOG_FIELDS:
        assert f in rec, f
    assert rec['repository_commit'] == git(repo.root, 'rev-parse', 'HEAD')
    # ungated discovery and validation-scope actions in the same state
    assert run(repo, 'environment_discovery').decision.allowed
    assert run(repo, 'unit_tests').decision.allowed


# ------------------------------------------------------------------------------------ fail-closed extras

def test_fail_closed_internal_error_and_unloggable_decisions(tmp_path, spy, monkeypatch):
    repo = SyntheticRepo(tmp_path)
    monkeypatch.setattr(control, '_registry', lambda *a: 1 / 0)
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'INTERNAL_ERROR')
    monkeypatch.undo()
    log = repo.root / 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl'
    log.rename(tmp_path / 'saved.jsonl'); log.mkdir()                 # log path unusable
    res = run(repo, 'control_plane_implementation')
    assert res.decision.decision == 'DENY' and res.executor_called is False and not repo.tool_reached()


def test_fail_closed_corrupt_decision_log(tmp_path, spy):
    repo = SyntheticRepo(tmp_path)
    with open(repo.root / 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl', 'a') as f:
        f.write('{not json\n')
    assert_denied(repo, run(repo, 'control_plane_implementation'), spy, 'LOG_CORRUPT')


def test_log_contains_no_raw_arguments(tmp_path):
    repo = SyntheticRepo(tmp_path)
    secret = 'pass' + 'word=' + 'x' * 12
    control.run_authorized([repo.mock(), secret], action='control_plane_implementation', phase='P0', study='S00',
                           environment=None, actor='pytest', root=repo.root)
    assert secret not in (repo.root / 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl').read_text()


# ------------------------------------------------------------------------------------ transition + validator

def test_canonical_transition_records_provenance(tmp_path):
    repo = SyntheticRepo(tmp_path, state='PLANNED')
    import hashlib
    before = hashlib.sha256((repo.root / 'RESEARCH_STATE.yaml').read_bytes()).hexdigest()
    rec = control.transition('IMPLEMENTING', approval_id='G0-P0-S00-001', actor='pytest', reason='start', root=repo.root)
    for k in ('old_state', 'new_state', 'approval_id', 'timestamp_utc', 'reason', 'old_state_sha256',
              'new_state_sha256', 'old_gate_hash', 'new_gate_hash'):
        assert rec[k]
    assert rec['old_state_sha256'] == before and rec['old_state'] == 'PLANNED' and rec['new_state'] == 'IMPLEMENTING'
    diff = git(repo.root, 'diff', '-U0', '--', 'RESEARCH_STATE.yaml', 'AI_CONTROL/PHASE_CONTROL.yaml')
    changed = [l for l in diff.splitlines() if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    assert sorted(changed) == sorted(['-status: PLANNED', '+status: IMPLEMENTING', '-active_phase_state: PLANNED',
                                      '+active_phase_state: IMPLEMENTING', '-state: PLANNED', '+state: IMPLEMENTING'])
    assert control.repository_control_errors(repo.root) == []


def test_validator_accepts_legal_states_and_rejects_illegal_ones(tmp_path):
    for i, st in enumerate(('PLANNED', 'IMPLEMENTING', 'VALIDATING', 'GATE_REVIEW')):
        assert control.repository_control_errors(SyntheticRepo(tmp_path / str(i), state=st).root) == [], st
    repo = SyntheticRepo(tmp_path / 'x')
    repo.edit('RESEARCH_STATE.yaml', 'p1_authorized: false', 'p1_authorized: true')
    assert any('STATE_INVALID' in e for e in control.repository_control_errors(repo.root))


def test_real_repository_passes_control_checks():
    assert control.repository_control_errors(REPO) == []


# ------------------------------------------------------------------------------------ structural bypass guards

def test_only_the_control_plane_and_publisher_start_processes():
    allowed = {'control.py', 'publish.py'}
    offenders = []
    for p in (REPO / 'src/hlsdse').rglob('*.py'):
        tree = ast.parse(p.read_text())
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or '']
            elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == 'os' \
                    and (node.attr in ('system', 'popen') or node.attr.startswith(('exec', 'spawn'))):
                names = ['os.' + node.attr]
            if any(n.split('.')[0] in ('subprocess', 'pty', 'multiprocessing') or n.startswith('os.') for n in names) \
                    and p.name not in allowed:
                offenders.append(f'{p.relative_to(REPO)}: {names}')
            if isinstance(node, ast.keyword) and node.arg == 'shell' and getattr(node.value, 'value', False) is True:
                offenders.append(f'{p.relative_to(REPO)}: shell=True')
    assert offenders == []


def test_every_policy_tool_has_a_gate_shim():
    import yaml
    pol = yaml.safe_load((REPO / 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml').read_text())
    for tool in pol['tools']:
        shim = REPO / 'environments/xilinx_2025_2_1/bin' / tool
        assert shim.is_file() and 'tool_gate.sh' in shim.read_text(), tool


def test_publisher_never_publishes_a_canonical_transition(tmp_path):
    from test_auto_publish import make_repo, publish
    work, _ = make_repo(tmp_path)
    (work / 'RESEARCH_STATE.yaml').write_text((work / 'RESEARCH_STATE.yaml').read_text()
                                              .replace('current_phase: P0', 'current_phase: P0\nactive_phase_state: IMPLEMENTING'))
    e = publish(work)
    assert e['result'] == 'BLOCKED' and e['blocker']['code'] == 'PROTECTED_STATE_CHANGE'
