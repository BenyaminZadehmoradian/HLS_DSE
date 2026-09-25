from __future__ import annotations
import os, platform, shutil, subprocess, sys
from pathlib import Path

TOOLS = {
    'vivado': 'vivado',
    'vitis': 'vitis',
    'vitis_hls': 'vitis_hls',
    'git': 'git',
}

def _version(cmd: str):
    exe = shutil.which(cmd)
    if not exe:
        return {'present': False, 'path': None, 'version': None}
    try:
        flag = '--version' if cmd == 'git' else '-version'
        p = subprocess.run([exe, flag], capture_output=True, text=True, timeout=10)
        text = (p.stdout or p.stderr).strip().splitlines()
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
