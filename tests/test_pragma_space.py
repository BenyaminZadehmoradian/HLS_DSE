from hlsdse.pragma_space import generate_cartesian
def test_cartesian():
    cs=list(generate_cartesian({'pipeline':['on','off'],'unroll':[1,2]},'b'))
    assert len(cs)==4


def test_invalid_spaces_and_cli_validate_config(tmp_path):
    import json, subprocess, sys
    from pathlib import Path
    import pytest
    from hlsdse.pragma_space import validate_space
    for bad in ({}, {'unroll': []}, {'unroll': 4}, []):
        with pytest.raises(ValueError):
            validate_space(bad)
    root = Path(__file__).resolve().parents[1]
    run = lambda p: subprocess.run([sys.executable, '-m', 'hlsdse', 'validate-config', str(p)], cwd=root,
                                   env={'PYTHONPATH': str(root / 'src'), 'PATH': '/usr/bin:/bin'}, capture_output=True, text=True)
    good = tmp_path / 'ok.json'; good.write_text(json.dumps({'unroll': [1, 2]}))
    bad = tmp_path / 'bad.json'; bad.write_text(json.dumps({'unroll': []}))
    assert run(good).returncode == 0
    assert run(bad).returncode == 1
    assert run(tmp_path / 'missing.yaml').returncode == 1


def test_scan_environment_reports_honest_device_status(monkeypatch):
    from pathlib import Path
    import hlsdse.scanning.environment as envmod
    from hlsdse.scanning.environment import scan_environment, TOOLS
    assert 'vitis_hls' not in TOOLS and 'vitis-run' in TOOLS
    root = Path(__file__).resolve().parents[1]
    monkeypatch.setattr(envmod.shutil, 'which', lambda c: None)            # no tool is executed
    env = scan_environment(root)
    assert all(v == {'present': False, 'path': None, 'version': None} for v in env['tools'].values())
    assert env['device_support'] == {'reference_device': 'xc7z020clg484', 'status': 'NOT_CHECKED',
                                     'evidence': 'environments/ENVIRONMENT_REGISTRY.yaml'}


def test_cli_generate_candidates_errors_are_clean(tmp_path):
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    bad = tmp_path / 'bad.json'; bad.write_text('{not json')
    cp = subprocess.run([sys.executable, '-m', 'hlsdse', 'generate-candidates', str(bad), 'B1', '--out', str(tmp_path / 'o.json')],
                        cwd=root, env={'PYTHONPATH': str(root / 'src'), 'PATH': '/usr/bin:/bin'}, capture_output=True, text=True)
    assert cp.returncode == 1 and 'GENERATE_FAILED' in cp.stdout and 'Traceback' not in cp.stderr
    good = tmp_path / 'ok.json'; good.write_text('{"unroll": [1, 2], "pipeline": ["on", "off"]}')
    cp = subprocess.run([sys.executable, '-m', 'hlsdse', 'generate-candidates', str(good), 'B1', '--out', str(tmp_path / 'o.json')],
                        cwd=root, env={'PYTHONPATH': str(root / 'src'), 'PATH': '/usr/bin:/bin'}, capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout.strip() == '4'
