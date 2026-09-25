"""Synthetic-repository harness for the runtime control plane, shared by tests/test_control_plane.py and
audit/AI_CONTROL/evidence/control_probe.py.

Every repository is a throwaway git repo under a temporary directory, built from copies of the canonical
control files. Approvals written here are SYNTHETIC TEST FIXTURES (approver SYNTHETIC_TEST_FIXTURE); they never
touch the real audit/gates/approvals/. Every "tool" is a mock shell script that appends to a marker file; no
real HLS/Vivado/Vitis binary is ever resolved or executed.
"""
import os
import shutil
import subprocess
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
ENV_ID = 'ENV-2025.2.1-XC7Z020-1'
CONTROL_FILES = ['AI_CONTROL/CONTROL_PLANE_POLICY.yaml', 'AI_CONTROL/PHASE_CONTROL.yaml',
                 'AI_CONTROL/AUTO_PUSH_POLICY.yaml', 'RESEARCH_STATE.yaml', 'contracts/STUDY_ID_REGISTRY.yaml',
                 'contracts/CANONICAL_PROJECT_CONTRACT.yaml', 'environments/ENVIRONMENT_REGISTRY.yaml',
                 'studies/S00/CONTRACT.yaml', 'studies/S01/CONTRACT.yaml']
CONTROL_PLANE_SCOPE = ['control_plane_implementation', 'mock_validation', 'unit_tests', 'integration_tests',
                       'negative_control_tests', 'bypass_tests', 'validator_tests', 'control_decision_logging',
                       'auto_push_policy_validation']
FORBIDDEN_SCOPE = ['scientific_experiments', 'research_hls_runs', 'research_vivado_runs', 'research_vitis_runs',
                   'dse_campaigns', 'xsa', 'bitstream', 'elf', 'hardware_programming', 'hardware_execution',
                   'p1_implementation']


def git(cwd, *a, check=True):
    return subprocess.run(['git', '-C', str(cwd), *a], capture_output=True, text=True, check=check).stdout.strip()


def approval(base_commit, *, allowed=None, forbidden=None, environment=None, expires_at=None, phase='P0',
             study='S00', approval_id='G0-P0-S00-001', layout='nested', **over):
    a = {'approval_id': approval_id, 'project_version': 'V23.2', 'phase': phase, 'study': study,
         'environment': environment, 'approver': 'SYNTHETIC_TEST_FIXTURE', 'approved_at': '2026-01-01T00:00:00+00:00',
         'approved_commit': base_commit, 'expires_at': expires_at, 'status': 'APPROVED'}
    allowed = list(CONTROL_PLANE_SCOPE if allowed is None else allowed)
    forbidden = list(FORBIDDEN_SCOPE if forbidden is None else forbidden)
    forbidden = [f for f in forbidden if f not in allowed]
    if layout == 'flat':
        a.update(scope=None, allowed=allowed, forbidden=forbidden)
    else:
        a['scope'] = {'allowed': allowed, 'forbidden': forbidden}
    a.update(over)
    return a


class SyntheticRepo:
    def __init__(self, base: Path, *, state='IMPLEMENTING', active_environment=None, approval_kw=None,
                 with_approval=True):
        self.root = base / 'repo'
        self.mock_dir = base / 'mock_tools'
        self.marker = base / 'TOOL_REACHED'
        self.root.mkdir(parents=True)
        for rel in CONTROL_FILES:
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / rel, self.root / rel)
        # the launcher gate and the control code, so the bin/ shims can run against this repository
        shutil.copytree(REPO / 'src/hlsdse', self.root / 'src/hlsdse', ignore=shutil.ignore_patterns('__pycache__'))
        envd = self.root / 'environments/xilinx_2025_2_1'
        shutil.copytree(REPO / 'environments/xilinx_2025_2_1/bin', envd / 'bin')
        shutil.copy2(REPO / 'environments/xilinx_2025_2_1/tool_gate.sh', envd / 'tool_gate.sh')
        st = self.root / 'RESEARCH_STATE.yaml'
        t = st.read_text()
        if active_environment is not None:
            t = t.replace('active_environment: null', f'active_environment: {active_environment}')
        st.write_text(t)
        git(self.root.parent, 'init', '-q', '-b', 'main', str(self.root))
        git(self.root, 'config', 'user.name', 'Synthetic'); git(self.root, 'config', 'user.email', 'synthetic@example.invalid')
        git(self.root, 'add', '-A'); git(self.root, 'commit', '-q', '-m', 'synthetic baseline')
        self.base_commit = git(self.root, 'rev-parse', 'HEAD')
        if with_approval:
            self.write_approval(approval(self.base_commit, **(approval_kw or {})))
        self.mock_dir.mkdir()
        for tool in ('vivado', 'vitis-run', 'mock_control_step'):
            m = self.mock_dir / tool
            m.write_text(f"#!/bin/sh\necho \"MOCK {tool} $*\" >> '{self.marker}'\nexit 0\n")
            m.chmod(0o755)
        if state != 'PLANNED':
            from hlsdse import control
            path = {'IMPLEMENTING': ['IMPLEMENTING'], 'VALIDATING': ['IMPLEMENTING', 'VALIDATING'],
                    'GATE_REVIEW': ['IMPLEMENTING', 'VALIDATING', 'GATE_REVIEW']}[state]
            for s in path:
                control.transition(s, approval_id=None, actor='synthetic-harness', reason='fixture', root=self.root)

    def write_approval(self, data, *, commit=True, name=None):
        d = self.root / 'audit/gates/approvals'
        d.mkdir(parents=True, exist_ok=True)
        p = d / f'{name or data["approval_id"]}.yaml'
        p.write_text(yaml.safe_dump(data, sort_keys=False) if isinstance(data, dict) else data)
        if commit:
            git(self.root, 'add', '-A'); git(self.root, 'commit', '-q', '-m', f'synthetic approval {p.stem}')
        return p

    def edit(self, rel, old, new):
        p = self.root / rel
        t = p.read_text()
        assert old in t, f'{old!r} not in {rel}'
        p.write_text(t.replace(old, new))

    def log(self):
        import json
        p = self.root / 'audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl'
        out = []
        for x in (p.read_text().splitlines() if p.exists() else []):
            try:
                out.append(json.loads(x))
            except json.JSONDecodeError:
                pass                                    # deliberately corrupted lines in fail-closed tests
        return out

    def decisions(self):
        return [r for r in self.log() if r.get('record_type') == 'DECISION']

    def tool_reached(self):
        return self.marker.exists()

    def mock(self, tool='mock_control_step'):
        return str(self.mock_dir / tool)

    def run_shim(self, tool, *args, xilinx_env='2025.2.1', environment_id=ENV_ID, tool_root=True):
        """Invoke environments/xilinx_2025_2_1/bin/<tool> the way run_in_env.sh exposes it: gate dir first on
        PATH, the (mock) tool directory behind it."""
        env = {'PATH': f'{self.root}/environments/xilinx_2025_2_1/bin:{self.mock_dir}:/usr/bin:/bin',
               'HOME': os.environ.get('HOME', '/tmp'), 'USER': 'synthetic'}
        if xilinx_env:
            env['HLSDSE_XILINX_ENV'] = xilinx_env
        if environment_id:
            env['HLSDSE_ENVIRONMENT_ID'] = environment_id
        if tool_root:
            env['HLSDSE_XILINX_ROOT'] = str(self.mock_dir)
        return subprocess.run([str(self.root / 'environments/xilinx_2025_2_1/bin' / tool), *args],
                              capture_output=True, text=True, env=env)
