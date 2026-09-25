from __future__ import annotations
import os, platform, shutil, sys, tempfile

import yaml

# 2025.2.1 ships no standalone vitis_hls; HLS runs through `vitis-run --mode hls` (see ENVIRONMENT_REGISTRY.yaml).
TOOLS = ('vivado', 'vitis', 'vitis-run', 'git')


def _state(root):
    from .. import control
    pol = control.load_policy(root)
    return yaml.safe_load((root / pol['paths']['state']).read_text(encoding='utf-8')) or {}


def _version(cmd: str, root):
    """Version query through the control plane (action environment_discovery); DENY runs nothing."""
    from .. import control
    exe = shutil.which(cmd)
    if not exe:
        return {'present': False, 'path': None, 'version': None}
    try:
        state = _state(root)
        flag = '--version' if cmd in ('git', 'vitis-run') else '-version'
        with tempfile.TemporaryFile('w+') as out:
            res = control.run_authorized([exe, flag], action='environment_discovery', phase=state.get('current_phase'),
                                         study=state.get('current_study'), environment=None,
                                         actor=os.environ.get('USER', 'unknown'), caller='scan_environment',
                                         root=root, stdout=out, stderr=out)
            if not res.executor_called:
                return {'present': True, 'path': exe, 'version': None,
                        'control': f'DENY {res.decision.reason_code}'}
            out.seek(0)
            text = out.read().strip().splitlines()
        return {'present': True, 'path': exe, 'version': text[0] if text else 'UNKNOWN'}
    except Exception as exc:
        return {'present': True, 'path': exe, 'version': 'UNKNOWN', 'error': type(exc).__name__}


def _reference_device(root):
    try:
        hw = yaml.safe_load((root / 'contracts/HARDWARE_PLATFORM_CONTRACT.yaml').read_text(encoding='utf-8')) or {}
        return (hw.get('reference_device') or {}).get('part')
    except Exception:
        return None


def scan_environment(root=None):
    from .. import control
    from pathlib import Path
    root = Path(root or control.ROOT)
    return {
        'python': {'version': platform.python_version(), 'executable': sys.executable},
        'os': {'system': platform.system(), 'release': platform.release(), 'machine': platform.machine()},
        'cpu_count': os.cpu_count(),
        'tools': {name: _version(name, root) for name in TOOLS},
        # Part support is not probed here (that needs a gated Vivado run); it is recorded per registered environment.
        'device_support': {'reference_device': _reference_device(root), 'status': 'NOT_CHECKED',
                           'evidence': 'environments/ENVIRONMENT_REGISTRY.yaml'},
    }
