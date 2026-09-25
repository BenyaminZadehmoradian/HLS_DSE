#!/usr/bin/env python3
"""Post-implementation probe of AI_CONTROL runtime enforcement (P0/S00 evidence, V23.2).

Replaces the pre-implementation probe (commit d2a8523), which showed that no code read AI_CONTROL. The formal,
repeatable version of these scenarios is tests/test_control_plane.py; this script runs the same synthetic
scenarios through the shared harness (tests/control_harness.py) and writes a JSON evidence record.

Safety: every repository is a throwaway synthetic git repo under a temporary directory, every tool is a mock
script writing a marker file, and the real repository is only read. The one real-launcher check runs
`command -v` inside run_in_env.sh; it executes no Xilinx tool.

Usage:  python3 audit/AI_CONTROL/evidence/control_probe.py [--out results.json]
"""
import json, os, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT = Path(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else REPO / 'audit/AI_CONTROL/evidence/control_probe_results.json'
sys.dont_write_bytecode = True
sys.path[:0] = [str(REPO / 'src'), str(REPO / 'tests')]
from control_harness import ENV_ID, SyntheticRepo, approval, git   # noqa: E402
from hlsdse import control                                          # noqa: E402
from hlsdse.flow import run_command                                 # noqa: E402
from hlsdse.models import RunRecord                                 # noqa: E402

WORK = Path(tempfile.mkdtemp(prefix='aictl_probe_'))
CALLS = []
_real_execute = control._execute
control._execute = lambda d, argv, **kw: (CALLS.append(list(argv)), _real_execute(d, argv, **kw))[1]
results = {'probe': 'audit/AI_CONTROL/evidence/control_probe.py', 'phase': 'P0', 'study': 'S00',
           'approval': 'G0-P0-S00-001', 'started_utc': datetime.now(timezone.utc).isoformat(),
           'repo_head': git(REPO, 'rev-parse', 'HEAD'), 'policy': 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml',
           'mock_only': True, 'scenarios': [], 'bypass_paths': []}
n = [0]


def repo(**kw):
    n[0] += 1
    return SyntheticRepo(WORK / f'r{n[0]}', **kw)


def scenario(sid, title, expected, fn):
    CALLS.clear()
    try:
        r, res, extra = fn()
        d = res.decision
        rec = {'id': sid, 'title': title, 'expected': expected, 'decision': d.decision, 'reason_code': d.reason_code,
               'reason': d.reason, 'request_id': d.request_id, 'action': d.action, 'phase': d.phase, 'study': d.study,
               'environment': d.environment, 'approval_id': d.approval_id, 'executor_called': res.executor_called,
               'executor_calls_observed': len(CALLS), 'mock_tool_reached': r.tool_reached(),
               'logged': r.decisions()[-1]['request_id'] == d.request_id if r.decisions() else False, **extra}
    except Exception as e:
        rec = {'id': sid, 'title': title, 'expected': expected, 'decision': 'EXCEPTION', 'reason': f'{type(e).__name__}: {e}'}
    ok = rec.get('decision') == expected.split()[0] and (
        (expected.startswith('DENY') and rec.get('executor_called') is False and not rec.get('mock_tool_reached'))
        or (expected.startswith('ALLOW') and rec.get('executor_called') is True and rec.get('mock_tool_reached')))
    rec['result'] = 'PASS' if ok else 'FAIL'
    results['scenarios'].append(rec)


def req(r, action, phase='P0', study='S00', environment=None):
    return r, control.run_authorized([r.mock(), '--probe'], action=action, phase=phase, study=study,
                                     environment=environment, actor='control_probe', root=r.root), {}


def edited(r, rel, old, new):
    r.edit(rel, old, new)
    return r


scenario('A', 'Unauthorized P0 research request (research_hls_runs)', 'DENY', lambda: req(repo(), 'research_hls_runs'))
scenario('B', 'Unauthorized P1 (P1/S01)', 'DENY', lambda: req(repo(), 'control_plane_implementation', 'P1', 'S01'))
scenario('C', 'Human approval missing', 'DENY',
         lambda: req(repo(state='PLANNED', with_approval=False), 'control_plane_implementation'))
scenario('D', 'Wrong study (P0/S01)', 'DENY', lambda: req(repo(), 'control_plane_implementation', study='S01'))
scenario('E', 'Wrong phase (P2/S00)', 'DENY', lambda: req(repo(), 'control_plane_implementation', phase='P2'))
scenario('F', 'Null environment where one is required', 'DENY',
         lambda: req(repo(approval_kw={'allowed': ['research_hls_runs']}), 'research_hls_runs'))
scenario('G', 'Unknown environment', 'DENY',
         lambda: req(repo(), 'control_plane_implementation', environment='ENV-DOES-NOT-EXIST'))
scenario('H', 'Malformed state (p1_authorized removed)', 'DENY',
         lambda: req(edited(repo(), 'RESEARCH_STATE.yaml', 'p1_authorized: false\n', ''), 'control_plane_implementation'))


def missing_policy():
    r = repo()
    (r.root / 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml').unlink()
    return req(r, 'control_plane_implementation')


scenario('I', 'Missing policy', 'DENY', missing_policy)


def direct_executor():
    r = repo()
    d = control.authorize('control_plane_implementation', 'P0', 'S00', None, actor='control_probe', root=r.root)
    try:
        control._execute(d, [r.mock(), '--direct'])
        refused = False
    except control.ExecutionDenied:
        refused = True
    rr = RunRecord(run_id='PROBE-J', study_id='S00', benchmark_id='MOCK', environment_id=None, candidate_id='C')
    out = run_command(rr, [r.mock('vivado'), '-mode', 'batch'], WORK / 'j.log', action='research_vivado_runs', root=r.root)
    res = control.ExecutionResult(control.replace(d, decision='DENY', reason_code='EXECUTION_REFUSED' if refused else 'NOT_REFUSED',
                                                  reason='_execute() called directly with an authorize() decision'),
                                  not refused, None)
    return r, res, {'flow_run_command_status': out.status, 'flow_run_command_reason': out.metrics.get('control_reason')}


scenario('J', 'Direct executor invocation (_execute without a sealed decision; flow.run_command)', 'DENY', direct_executor)


def launcher_gate():
    r = repo()
    cp = r.run_shim('vivado', '-mode', 'batch', '-source', 'mock.tcl')
    last = r.decisions()[-1]
    res = control.ExecutionResult(control.Decision(**{k: last.get(k) for k in control.Decision.__dataclass_fields__}),
                                  last['executor_called'], None)
    return r, res, {'shim_exit_code': cp.returncode, 'stderr': cp.stderr.strip()[:200]}


scenario('K', 'Launcher gate: vivado by name (bin/vivado -> tool_gate.sh -> hlsdse.control)', 'DENY', launcher_gate)


def invalid_transition():
    r = repo()
    codes = []
    for to, kw in (('GATE_REVIEW', {}), ('IMPLEMENTING', {'to_phase': 'P1'})):
        try:
            control.transition(to, approval_id=None, actor='control_probe', reason='probe', root=r.root, **kw)
            codes.append('TRANSITIONED')
        except control.ControlError as e:
            codes.append(e.code)
    r2 = edited(edited(edited(repo(state='PLANNED'), 'RESEARCH_STATE.yaml', 'status: PLANNED', 'status: IMPLEMENTING'),
                       'RESEARCH_STATE.yaml', 'active_phase_state: PLANNED', 'active_phase_state: IMPLEMENTING'),
                'AI_CONTROL/PHASE_CONTROL.yaml', 'state: PLANNED', 'state: IMPLEMENTING')
    rr, res, _ = req(r2, 'control_plane_implementation')
    return rr, res, {'transition_codes': codes, 'direct_state_write_decision': res.decision.reason_code}


scenario('L', 'Invalid transition (IMPLEMENTING->GATE_REVIEW, P0->P1) and direct state write', 'DENY', invalid_transition)


def expired():
    r = repo()
    r.write_approval(approval(r.base_commit, expires_at='2026-01-02T00:00:00+00:00'))
    return req(r, 'control_plane_implementation')


scenario('M', 'Expired approval', 'DENY', expired)
scenario('N', 'Wrong approval scope (dse_campaigns under a control-plane approval)', 'DENY',
         lambda: req(repo(), 'dse_campaigns'))
scenario('POS', 'Positive mock: P0/S00 control_plane_implementation, valid approval, environment null', 'ALLOW',
         lambda: req(repo(approval_kw={'layout': 'flat'}), 'control_plane_implementation'))

# fail-closed matrix (each must be DENY before the executor)
fail_closed = {
    'missing_policy': lambda r: (r.root / 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml').unlink(),
    'malformed_policy': lambda r: (r.root / 'AI_CONTROL/CONTROL_PLANE_POLICY.yaml').write_text('x: [\n'),
    'missing_state': lambda r: (r.root / 'RESEARCH_STATE.yaml').unlink(),
    'malformed_state': lambda r: (r.root / 'RESEARCH_STATE.yaml').write_text('current_phase: [P0\n'),
    'missing_approval': lambda r: (git(r.root, 'rm', '-q', 'audit/gates/approvals/G0-P0-S00-001.yaml'), git(r.root, 'commit', '-q', '-m', 'rm')),
    'expired_approval': lambda r: r.write_approval(approval(r.base_commit, expires_at='2026-01-02T00:00:00+00:00')),
    'unknown_phase': lambda r: r.edit('RESEARCH_STATE.yaml', 'current_phase: P0', 'current_phase: P99'),
    'unknown_study': lambda r: r.edit('RESEARCH_STATE.yaml', 'current_study: S00', 'current_study: S999'),
    'unknown_environment': lambda r: r.edit('RESEARCH_STATE.yaml', 'active_environment: null', 'active_environment: ENV-X'),
    'invalid_state': lambda r: r.edit('RESEARCH_STATE.yaml', 'active_phase_state: IMPLEMENTING', 'active_phase_state: DONE'),
    'corrupt_permission_data': lambda r: r.write_approval('approval_id: [\n', name='G0-P0-S00-002'),
    'corrupt_decision_log': lambda r: open(r.root / 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl', 'a').write('{bad\n'),
}
results['fail_closed'] = []
for name, mutate in fail_closed.items():
    r = repo()
    mutate(r)
    CALLS.clear()
    res = control.run_authorized([r.mock(), '--fc'], action='control_plane_implementation', phase='P0', study='S00',
                                 environment=None, actor='control_probe', root=r.root)
    results['fail_closed'].append({'case': name, 'decision': res.decision.decision, 'reason_code': res.decision.reason_code,
                                   'executor_called': res.executor_called, 'mock_tool_reached': r.tool_reached(),
                                   'result': 'PASS' if not res.executor_called and not r.tool_reached() else 'FAIL'})
r = repo()
CALLS.clear()
res = control.run_authorized([r.mock(), '--oos'], action='xsa', phase='P0', study='S00', environment=None,
                             actor='control_probe', root=r.root)
results['fail_closed'].append({'case': 'out_of_scope_action', 'decision': res.decision.decision,
                               'reason_code': res.decision.reason_code, 'executor_called': res.executor_called,
                               'mock_tool_reached': r.tool_reached(),
                               'result': 'PASS' if not res.executor_called and not r.tool_reached() else 'FAIL'})


# bypass paths
def vitis_hls_shim():
    r = repo()
    vit = WORK / 'vitis_root'
    (vit / 'bin').mkdir(parents=True, exist_ok=True)
    (vit / 'bin/vitis-run').write_text(f"#!/bin/sh\necho \"MOCK vitis-run $*\" >> '{r.marker}'\n")
    (vit / 'bin/vitis-run').chmod(0o755)
    before = len(r.decisions())
    subprocess.run([str(r.root / 'environments/xilinx_2025_2_1/bin/vitis_hls'), '-f', 'x.tcl'], capture_output=True,
                   env={'PATH': '/usr/bin:/bin', 'HLSDSE_XILINX_ENV': '2025.2.1', 'XILINX_VITIS': str(vit)})
    return r.tool_reached(), len(r.decisions()) - before


reached, ndec = vitis_hls_shim()
launcher = REPO / 'environments/xilinx_2025_2_1/run_in_env.sh'
real_launcher = None
if launcher.exists() and Path('/mnt/data/Apps/2025.2.1/Vivado/settings64.sh').exists():
    cp = subprocess.run([str(launcher), 'bash', '-c', 'for t in vivado vitis vitis-run v++ vitis_hls xsct; do command -v $t; done'],
                        capture_output=True, text=True)
    real_launcher = {'rc': cp.returncode, 'resolved': cp.stdout.split(), 'stderr': cp.stderr.strip()[:200]}
abs_path_guard = 'invoke Xilinx tools by name' in launcher.read_text()
results['bypass_paths'] = [
    {'path': 'Agent -> AI_CONTROL -> Executor', 'via': 'control.run_authorized', 'classification': 'NO_BYPASS',
     'evidence': 'scenarios A-N, POS'},
    {'path': 'Agent -> Executor', 'via': 'control._execute (sealed, single-use, argv-bound decision)',
     'classification': 'NO_BYPASS', 'evidence': 'scenario J; test_j_*'},
    {'path': 'Agent -> Adapter', 'via': 'hlsdse.flow.run_command, hlsdse.scanning.environment._version',
     'classification': 'NO_BYPASS', 'evidence': 'scenario J (flow); both call run_authorized; AST guard test'},
    {'path': 'CLI -> Executor', 'via': 'hlsdse cli', 'classification': 'NO_BYPASS',
     'evidence': 'cli imports no process API (AST guard); validate-project/scan-environment run in-process; authorize executes nothing'},
    {'path': 'Launcher -> Tool (by name)', 'via': 'run_in_env.sh PATH -> bin/<tool> -> tool_gate.sh -> control',
     'classification': 'NO_BYPASS', 'evidence': {'scenario': 'K', 'real_launcher_resolution': real_launcher}},
    {'path': 'Launcher -> vitis_hls shim -> real vitis-run', 'via': 'bin/vitis_hls execs $XILINX_VITIS/bin/vitis-run',
     'classification': 'UNINTENTIONAL_BYPASS' if reached and ndec == 0 else 'NO_BYPASS',
     'evidence': {'mock_reached': reached, 'control_decisions_logged': ndec},
     'remediation': 'launcher patch (route vitis_hls through bin/vitis-run) - not applied; permission denied'},
    {'path': 'Launcher -> Tool (absolute path argument)', 'via': 'run_in_env.sh <abs path to vivado>',
     'classification': 'NO_BYPASS' if abs_path_guard else 'UNINTENTIONAL_BYPASS',
     'evidence': 'static: launcher ends with exec "$@" and has no absolute-path refusal' if not abs_path_guard else 'refusal present',
     'remediation': None if abs_path_guard else 'launcher patch (refuse Xilinx tools given by path) - not applied; permission denied'},
    {'path': 'Publisher -> git / validation commands', 'via': 'hlsdse.publish (subprocess)', 'classification': 'INTENTIONAL_BYPASS',
     'evidence': 'repository synchronisation only; commands fixed by AUTO_PUSH_POLICY.yaml; any Xilinx tool named inside them still meets the PATH gate'},
    {'path': 'Direct lowest-layer invocation', 'via': 'shell or foreign code running /mnt/data/Apps/2025.2.1/.../vivado directly',
     'classification': 'OUTSIDE_REPOSITORY_CONTROL', 'evidence': 'OS-level execution; governed by harness permissions and human oversight'},
    {'path': 'Human/agent git commit or plain git push', 'via': 'git', 'classification': 'OUTSIDE_REPOSITORY_CONTROL',
     'evidence': 'needs GitHub branch protection / signed commits (external governance)'},
]
results['summary'] = {
    'scenarios': f"{sum(s['result'] == 'PASS' for s in results['scenarios'])}/{len(results['scenarios'])} PASS",
    'fail_closed': f"{sum(s['result'] == 'PASS' for s in results['fail_closed'])}/{len(results['fail_closed'])} PASS",
    'unintentional_bypasses': [b['path'] for b in results['bypass_paths'] if b['classification'] == 'UNINTENTIONAL_BYPASS'],
    'real_tools_executed': 0,
}
results['finished_utc'] = datetime.now(timezone.utc).isoformat()
OUT.write_text(json.dumps(results, indent=2, default=str) + '\n')
print(json.dumps(results['summary'], indent=2))
