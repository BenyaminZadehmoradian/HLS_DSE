from __future__ import annotations
import os, platform, shutil, sys, tempfile
from pathlib import Path

TOOLS = {
    'vivado': 'vivado',
    'vitis': 'vitis',
    'vitis_hls': 'vitis_hls',
    'git': 'git',
}

def _version(cmd: str):
    """Version query through the control plane (action environment_discovery); DENY runs nothing."""
    from .. import control
    exe = shutil.which(cmd)
    if not exe:
        return {'present': False, 'path': None, 'version': None}
    try:
        import yaml
        state = yaml.safe_load((control.ROOT / 'RESEARCH_STATE.yaml').read_text()) or {}
        flag = '--version' if cmd == 'git' else '-version'
        with tempfile.TemporaryFile('w+') as out:
            res = control.run_authorized([exe, flag], action='environment_discovery', phase=state.get('current_phase'),
                                         study=state.get('current_study'), environment=None,
                                         actor=os.environ.get('USER', 'unknown'), caller='scan_environment',
                                         stdout=out, stderr=out)
            if not res.executor_called:
                return {'present': True, 'path': exe, 'version': None,
                        'control': f'DENY {res.decision.reason_code}'}
            out.seek(0)
            text = out.read().strip().splitlines()
        return {'present': True, 'path': exe, 'version': text[0] if text else 'UNKNOWN'}
    except Exception as exc:
        return {'present': True, 'path': exe, 'version': 'UNKNOWN', 'error': type(exc).__name__}

def scan_environment():
    return {
        'python': {'version': platform.python_version(), 'executable': sys.executable},
        'os': {'system': platform.system(), 'release': platform.release(), 'machine': platform.machine()},
        'cpu_count': os.cpu_count(),
        'tools': {name: _version(cmd) for name, cmd in TOOLS.items()},
        'device_support': {'reference_device': 'xc7z020clg484', 'verified': False},
    }
