#!/usr/bin/env python3
"""P0/S00 validation: runs every required check of studies/S00/CONTRACT.yaml and every criterion of
audit/gates/P0_EXIT_CRITERIA.md, and writes the S00 output audit/p0_validation.json.

Each check records PASS, FAIL or NOT_VERIFIABLE_IN_P0 with the evidence it used. Nothing is inferred: a check that
cannot be executed in P0 is reported as such, never as PASS. This script decides nothing about the gate."""
import json
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from hlsdse.control import repository_control_errors  # noqa: E402

PY = '/home/benyamin/.venvs/hls_dse_py312/bin/python'
LAUNCHER = str(ROOT / 'environments/xilinx_2025_2_1/run_in_env.sh')
FIRST_COMMIT_REGISTRY = ('28f98fa', 'contracts/STUDY_ID_REGISTRY.yaml')
DEVICE = 'xc7z020clg484'


def y(rel):
    return yaml.safe_load((ROOT / rel).read_text(encoding='utf-8')) or {}


def sh(*cmd):
    cp = subprocess.run(list(cmd), cwd=ROOT, capture_output=True, text=True)
    return cp.returncode, (cp.stdout + cp.stderr).strip()


checks = []


def check(cid, source, fn):
    try:
        status, evidence, detail = fn()
    except Exception as e:
        status, evidence, detail = 'FAIL', None, f'check raised {type(e).__name__}: {e}'
    checks.append({'id': cid, 'source': source, 'status': status, 'evidence': evidence, 'detail': detail})


def canonical_version():
    st, pol, can = y('RESEARCH_STATE.yaml'), y('AI_CONTROL/CONTROL_PLANE_POLICY.yaml'), y('contracts/CANONICAL_PROJECT_CONTRACT.yaml')
    vals = {'state': st.get('project_version'), 'policy': pol.get('project_version'),
            'canonical_contract': can.get('canonical_version'), 'pyproject': re.search(
                r'^version = "(\d+)\.(\d+)', (ROOT / 'pyproject.toml').read_text(), re.M).expand(r'V\1.\2')}
    ok = len(set(vals.values())) == 1 and (ROOT / st['canonical_source']).is_file()
    return ('PASS' if ok else 'FAIL'), vals, f'canonical_source {st.get("canonical_source")}'


def immutable_study_ids():
    reg = y('contracts/STUDY_ID_REGISTRY.yaml')
    rc, old_txt = sh('git', 'show', f'{FIRST_COMMIT_REGISTRY[0]}:{FIRST_COMMIT_REGISTRY[1]}')
    old = (yaml.safe_load(old_txt) or {}).get('reserved', {}) if rc == 0 else None
    if old is None:
        return 'FAIL', None, 'initial registry not readable from git history'
    removed = sorted(set(old) - set(reg['reserved']))
    retitled = sorted(k for k in old if k in reg['reserved'] and old[k] != reg['reserved'][k])
    folders = {}
    for p in (ROOT / 'studies').glob('S*/CONTRACT.yaml'):
        folders.setdefault((yaml.safe_load(p.read_text()) or {}).get('study_id'), []).append(p.parent.name)
    dup = {k: v for k, v in folders.items() if len(v) > 1}
    mism = {v[0]: k for k, v in folders.items() if len(v) == 1 and v[0] != k}
    ok = reg.get('ids_immutable') is True and not removed and not retitled and not dup and not mism
    return ('PASS' if ok else 'FAIL'), {'ids_in_initial_registry': len(old), 'ids_now': len(reg['reserved']),
            'removed': removed, 'retitled': retitled, 'duplicate_folder_ids': dup, 'folder_id_mismatch': mism}, \
        f'compared with {FIRST_COMMIT_REGISTRY[1]} at {FIRST_COMMIT_REGISTRY[0]}'


def s09_s71():
    reg = y('contracts/STUDY_ID_REGISTRY.yaml')['study_status']
    s09, s71 = y('studies/S09/CONTRACT.yaml'), y('studies/S71/CONTRACT.yaml')
    ok = (reg['S09']['status'] == 'ARCHIVED' and s09.get('status') == 'ARCHIVED_ID_COLLISION'
          and s09.get('executable') is False and s09.get('superseded_by') == 'S71'
          and reg['S71']['status'] == 'PLANNED' and s71.get('study_id') == 'S71')
    return ('PASS' if ok else 'FAIL'), {'S09': [reg['S09']['status'], s09.get('status')], 'S71': reg['S71']['status']}, \
        'S09 archived and not executable; S71 is the external-baseline study'


def schemas():
    out = {}
    for p in sorted((ROOT / 'schemas').iterdir()):
        try:
            (json.loads if p.suffix == '.json' else yaml.safe_load)(p.read_text(encoding='utf-8'))
            out[p.name] = 'PARSED'
        except Exception as e:
            out[p.name] = f'ERROR {type(e).__name__}'
    return ('PASS' if all(v == 'PARSED' for v in out.values()) else 'FAIL'), out, \
        'run-template conformance to RUN_MANIFEST_SCHEMA is checked by the validator'


def no_measured_evidence():
    found = [str(p.relative_to(ROOT)) for d in ('evidence/measured', 'evidence/derived', 'evidence/verified')
             for p in (ROOT / d).rglob('*') if p.is_file()]
    runs = [p.name for p in (ROOT / 'runs').iterdir() if p.is_dir() and p.name != '_TEMPLATE']
    return ('PASS' if not found and not runs else 'FAIL'), {'evidence_files': found, 'run_dirs': runs}, \
        'no measured/derived evidence and no run workspace exist before experimental execution'


def report_metadata():
    missing = [p.name for p in (ROOT / 'REPORTS').glob('*.md')
               if 'project_version:' not in (t := p.read_text(encoding='utf-8')) and 'Historical' not in t]
    return ('PASS' if not missing else 'FAIL'), {'reports_without_metadata': missing}, 'REPORTS/*.md'


def pytest_run(*targets):
    rc, out = sh(LAUNCHER, PY, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', *targets)
    last = out.splitlines()[-1] if out else ''
    return ('PASS' if rc == 0 else 'FAIL'), {'command': f'run_in_env.sh python -m pytest -q {" ".join(targets)}'.strip(),
                                             'returncode': rc, 'summary': last}, ''


def validator():
    rc, out = sh(sys.executable, 'scripts/validate_project.py')
    return ('PASS' if rc == 0 and out.splitlines()[0] == 'errors=0 warnings=0' else 'FAIL'), \
        {'returncode': rc, 'output': out.splitlines()[:5]}, 'scripts/validate_project.py'


def control_plane():
    errs = repository_control_errors(ROOT)
    return ('PASS' if not errs else 'FAIL'), {'repository_control_errors': errs}, \
        'policy, state machine, approvals, transition provenance, decision log'


def device_fixed():
    vals = {
        'HARDWARE_PLATFORM_CONTRACT': y('contracts/HARDWARE_PLATFORM_CONTRACT.yaml')['reference_device']['part'],
        'ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT': y('contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml')['reference_device']['part'],
        'RUN_MANIFEST_SCHEMA.device_part.const': json.loads((ROOT / 'schemas/RUN_MANIFEST_SCHEMA.json').read_text())['properties']['device_part']['const'],
        'RESEARCH_STATE.fixed_reference_device': y('RESEARCH_STATE.yaml')['fixed_reference_device'],
        'configs/preflight/default.yaml': y('configs/preflight/default.yaml')['reference_device'],
        'runs/_TEMPLATE/manifest.yaml': y('runs/_TEMPLATE/manifest.yaml')['device_part'],
    }
    envs = [e['device']['part'] for e in y('environments/ENVIRONMENT_REGISTRY.yaml')['environments'] if e.get('status') == 'registered']
    vals['registered_environments'] = sorted(set(envs))
    ok = all(v == DEVICE for k, v in vals.items() if k != 'registered_environments') and vals['registered_environments'] == [DEVICE]
    return ('PASS' if ok else 'FAIL'), vals, 'enforced by the RUN_MANIFEST_SCHEMA const and the validator'


def contracts_exist():
    need = {'benchmark contract': 'BENCHMARK_CONTRACT.yaml', 'baseline reproduction contract': 'EXTERNAL_BASELINE_CONTRACT.yaml',
            'reproduction contract': 'REPRODUCTION_CONTRACT.yaml', 'failure/retry policy': 'FAILURE_AND_RETRY_CONTRACT.yaml',
            'cache/reuse policy': 'CACHE_CONTRACT.yaml', 'leakage policy': 'DATA_LEAKAGE_CONTRACT.yaml',
            'concurrency/fairness policy': 'CONCURRENCY_FAIRNESS_CONTRACT.yaml', 'P1 implementation contract': 'P1_IMPLEMENTATION_CONTRACT.yaml',
            'measurement provenance rules': 'METRIC_PROVENANCE_CONTRACT.yaml'}
    res = {}
    for label, f in need.items():
        p = ROOT / 'contracts' / f
        try:
            res[label] = 'PRESENT' if p.is_file() and yaml.safe_load(p.read_text()) else 'EMPTY_OR_MISSING'
        except Exception as e:
            res[label] = f'UNPARSEABLE {type(e).__name__}'
    return ('PASS' if all(v == 'PRESENT' for v in res.values()) else 'FAIL'), res, 'contracts/'


def run_isolation():
    art = y('contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml')
    ev = {'run_layout_defined': bool(art.get('run_layout')), 'manifest_schema': art.get('manifest_schema'),
          'run_workspaces_present': [p.name for p in (ROOT / 'runs').iterdir() if p.is_dir() and p.name != '_TEMPLATE']}
    return 'NOT_VERIFIABLE_IN_P0', ev, ('The isolation rules, layout and manifest schema exist and the template conforms, '
                                        'but no Run has been executed, so isolation between real Runs cannot be observed '
                                        'until the first P1 run.')


def write_once():
    return 'NOT_VERIFIABLE_IN_P0', {'evidence_store_implementation': None}, (
        'Required by studies/S00/report.md (check 4). No evidence store exists yet (the earlier stub had no callers and '
        'was removed); write-once raw evidence is enforced only by policy until the P1 evidence store is implemented.')


check('canonical_version', 'S00 CONTRACT', canonical_version)
check('immutable_study_ids', 'S00 CONTRACT; P0 exit: Study IDs are unique', immutable_study_ids)
check('S09_archived_S71_active_for_external_baselines', 'S00 CONTRACT', s09_s71)
check('schema_parseability', 'S00 CONTRACT; P0 exit: manifest schema validates', schemas)
check('no_measured_evidence_before_experiment', 'S00 CONTRACT; P0 exit', no_measured_evidence)
check('report_metadata', 'S00 CONTRACT', report_metadata)
check('candidate_generator_unit_test', 'S00 CONTRACT', lambda: pytest_run('tests/test_pragma_space.py'))
check('validator_errors_zero', 'P0 exit: validator exits with errors=0; project contracts validate', validator)
check('control_plane_consistency', 'S00 purpose: validate the control plane', control_plane)
check('full_test_suite', 'S00 purpose: validate the control plane', lambda: pytest_run())
check('reference_device_fixed_and_enforced', 'P0 exit: XC7Z020CLG484 is fixed and enforced', device_fixed)
check('required_contracts_exist', 'P0 exit: provenance/benchmark/baseline/failure/cache/leakage/concurrency/P1 contracts', contracts_exist)
check('run_isolation_validated', 'P0 exit: Run isolation is validated', run_isolation)
check('raw_evidence_write_once', 'studies/S00/report.md required check 4', write_once)

state = y('RESEARCH_STATE.yaml')
rc, head = sh('git', 'rev-parse', 'HEAD')
_, dirty = sh('git', 'status', '--porcelain')
counts = {s: sum(c['status'] == s for c in checks) for s in ('PASS', 'FAIL', 'NOT_VERIFIABLE_IN_P0')}
result = {
    'study_id': 'S00', 'phase_id': 'P0', 'project_version': state.get('project_version'),
    'generated_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'generator': 'scripts/p0_validation.py',
    'repository_commit': head if rc == 0 else None,
    'working_tree_clean_except_publish_log': all(l.endswith('audit/git/AUTO_PUSH_LOG.jsonl') for l in dirty.splitlines()),
    'environment': {'python': platform.python_version(), 'platform': platform.platform()},
    'phase_state_at_validation': {k: state.get(k) for k in ('current_phase', 'current_study', 'active_phase_state',
                                                              'p1_authorized', 'active_environment')},
    'summary': counts,
    'checks': checks,
    'gate_note': 'This file is evidence for the human P0 gate. It decides nothing and authorizes nothing.',
}
out = ROOT / 'audit/p0_validation.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
for c in checks:
    print(f'{c["status"]:22} {c["id"]}')
print(f'summary={counts} -> {out.relative_to(ROOT)}')
sys.exit(1 if counts['FAIL'] else 0)
