"""Mock tests for hlsdse.publish.automatic_publish. Every test uses throwaway git repos under tmp_path;
the real project remote is never contacted. Fake secrets are assembled at runtime so this file itself
passes the publisher's secret scan."""
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from hlsdse.publish import automatic_publish

REPO = Path(__file__).resolve().parents[1]
MSG = 'p0/s00: add mock control evidence file'


def git(cwd, *a):
    return subprocess.run(['git', '-C', str(cwd), *a], capture_output=True, text=True, check=True).stdout.strip()


def make_repo(tmp_path, validation=(('true',),), enabled=True, name='w'):
    remote = tmp_path / 'remote.git'
    if not remote.exists():
        subprocess.run(['git', 'init', '-q', '--bare', '-b', 'main', str(remote)], check=True)
    work = tmp_path / name
    subprocess.run(['git', 'init', '-q', '-b', 'main', str(work)], check=True)
    git(work, 'config', 'user.name', 'Test'); git(work, 'config', 'user.email', 'test@example.invalid')
    git(work, 'remote', 'add', 'origin', str(remote))
    pol = yaml.safe_load((REPO / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').read_text())
    pol['remote_url'] = str(remote)
    pol['validation_commands'] = [list(c) for c in validation]
    pol['enabled'] = enabled
    (work / 'AI_CONTROL').mkdir()
    (work / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').write_text(yaml.safe_dump(pol))
    (work / 'RESEARCH_STATE.yaml').write_text('current_phase: P0\np1_authorized: false\nnote: a\n')
    git(work, 'add', '-A'); git(work, 'commit', '-q', '-m', 'init: baseline repository')
    git(work, 'push', '-q', 'origin', 'HEAD:refs/heads/main'); git(work, 'fetch', '-q', 'origin')
    return work, remote


def publish(work, **kw):
    return automatic_publish(work, kw.pop('message', MSG), reason='mock test', actor='pytest', **kw)


def remote_head(remote):
    return git(remote, 'rev-parse', 'main')


def log_lines(work):
    p = work / 'audit/git/AUTO_PUSH_LOG.jsonl'
    return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def test_a_success_commits_pushes_and_logs(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'evidence.md').write_text('mock evidence\n')
    e = publish(work, provenance={'phase': 'P0', 'study': 'S00'})
    assert e['result'] == 'PUSHED' and e['push_status'] == 'SUCCESS'
    assert remote_head(remote) == e['after_commit'] == git(work, 'rev-parse', 'HEAD')
    rec = log_lines(work)[-1]
    for k in ('timestamp_utc', 'repository', 'branch', 'before_commit', 'after_commit', 'remote', 'validation_status',
              'security_scan_status', 'artifact_scan_status', 'pdf_scan_status', 'commit_message', 'push_status',
              'actor', 'reason', 'provenance', 'policy_version'):
        assert k in rec
    assert rec['validation_status'] == 'PASS' and rec['provenance']['study'] == 'S00'


def test_b_validation_failure_no_commit_no_push(tmp_path):
    work, remote = make_repo(tmp_path, validation=(('false',),))
    before = git(work, 'rev-parse', 'HEAD')
    (work / 'evidence.md').write_text('x\n')
    e = publish(work)
    assert e['result'] == 'BLOCKED' and e['blocker']['code'] == 'VALIDATION_FAILED'
    assert git(work, 'rev-parse', 'HEAD') == before == remote_head(remote)
    assert git(work, 'diff', '--cached', '--name-only') == ''


@pytest.mark.parametrize('name,content', [
    ('notes.md', 'key: ' + 'AKIA' + 'ABCDEFGHIJKLMNOP' + '\n'),
    ('deploy.md', '-----BEGIN ' + 'OPENSSH PRIVATE KEY-----\nabc\n'),
    ('conf.md', 'pass' + 'word = hunter2hunter2\n'),
    ('Xilinx.lic', 'anything\n'),
    ('lic.txt', 'INCREMENT' + ' Synthesis xilinxd 2025.11 permanent\n'),
])
def test_c_secret_detected_no_push(tmp_path, name, content):
    work, remote = make_repo(tmp_path)
    before = remote_head(remote)
    (work / name).write_text(content)
    e = publish(work)
    assert e['result'] == 'BLOCKED' and e['security_scan_status'] == 'FAIL'
    assert remote_head(remote) == before and git(work, 'rev-parse', 'HEAD') == before


def test_d_restricted_pdf_no_push(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'paper.pdf').write_bytes(b'%PDF-1.7\n%\xe2\xe3\n1 0 obj\n')
    e = publish(work)
    assert e['blocker']['code'] == 'PDF_NOT_ALLOWLISTED' and e['pdf_scan_status'] == 'FAIL'
    assert remote_head(remote) == git(work, 'rev-parse', 'HEAD')


@pytest.mark.parametrize('name,data', [('design.bit', b'\x00\x09bitstream'), ('app.elf', b'\x7fELF\x00\x00'),
                                        ('dump.dat', b'\x00\x01\x02' * 10), ('run/.Xil/tmp.txt', b'x')])
def test_e_forbidden_artifact_no_push(tmp_path, name, data):
    work, remote = make_repo(tmp_path)
    (work / name).parent.mkdir(parents=True, exist_ok=True)
    (work / name).write_bytes(data)
    e = publish(work)
    assert e['result'] == 'BLOCKED'
    assert e['artifact_scan_status'] == 'FAIL' or e['security_scan_status'] == 'FAIL'
    assert remote_head(remote) == git(work, 'rev-parse', 'HEAD')


def test_f_remote_divergence_no_force_push(tmp_path):
    work, remote = make_repo(tmp_path)
    other = tmp_path / 'other'
    subprocess.run(['git', 'clone', '-q', str(remote), str(other)], check=True)
    git(other, 'config', 'user.name', 'O'); git(other, 'config', 'user.email', 'o@example.invalid')
    (other / 'theirs.md').write_text('remote change\n'); git(other, 'add', '-A')
    git(other, 'commit', '-q', '-m', 'other: remote change'); git(other, 'push', '-q', 'origin', 'main')
    theirs = remote_head(remote)
    (work / 'mine.md').write_text('local change\n')
    e = publish(work)
    assert e['blocker']['code'] == 'REMOTE_DIVERGED' and e['push_status'] == 'BLOCKED_REMOTE_DIVERGED'
    assert e['commit_created'] is True and remote_head(remote) == theirs      # remote history untouched


def test_g_empty_change_no_commit(tmp_path):
    work, remote = make_repo(tmp_path)
    before = git(work, 'rev-parse', 'HEAD')
    e = publish(work)
    assert e['result'] == 'NO_CHANGES' and git(work, 'rev-parse', 'HEAD') == before
    assert log_lines(work) == []


def test_h_push_failure_keeps_local_commit(tmp_path):
    work, remote = make_repo(tmp_path)
    hook = remote / 'hooks/pre-receive'
    hook.write_text('#!/bin/sh\necho rejected-by-mock-hook >&2\nexit 1\n'); hook.chmod(0o755)
    before_remote = remote_head(remote)
    (work / 'evidence.md').write_text('x\n')
    e = publish(work)
    assert e['result'] == 'COMMITTED_PUSH_FAILED' and e['push_status'] == 'FAILED' and e['commit_created']
    assert git(work, 'rev-parse', 'HEAD') == e['after_commit'] != before_remote == remote_head(remote)
    assert log_lines(work)[-1]['push_status'] == 'FAILED'


def test_protected_state_change_is_never_auto_published(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'RESEARCH_STATE.yaml').write_text('current_phase: P0\np1_authorized: true\nnote: a\n')
    e = publish(work)
    assert e['blocker']['code'] == 'PROTECTED_STATE_CHANGE' and 'p1_authorized' in e['blocker']['detail']
    assert remote_head(remote) == git(work, 'rev-parse', 'HEAD')


def test_approval_artifacts_are_never_auto_published(tmp_path):
    work, _ = make_repo(tmp_path)
    (work / 'audit/gates/approvals').mkdir(parents=True)
    (work / 'audit/gates/approvals/G0.yaml').write_text('status: APPROVED\n')
    assert publish(work)['blocker']['code'] == 'PROTECTED_STATE_CHANGE'


def test_non_gate_state_field_may_change(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'RESEARCH_STATE.yaml').write_text('current_phase: P0\np1_authorized: false\nnote: b\n')
    assert publish(work)['result'] == 'PUSHED'


@pytest.mark.parametrize('msg', ['update', 'misc: update', 'fix', 'P0: Bad Case Subject'])
def test_meaningless_commit_message_blocked(tmp_path, msg):
    work, _ = make_repo(tmp_path)
    (work / 'evidence.md').write_text('x\n')
    assert publish(work, message=msg)['blocker']['code'] == 'COMMIT_MESSAGE_INVALID'


def test_wrong_branch_and_wrong_remote_blocked(tmp_path):
    work, _ = make_repo(tmp_path)
    (work / 'evidence.md').write_text('x\n')
    git(work, 'checkout', '-q', '-b', 'feature')
    assert publish(work)['blocker']['code'] == 'WRONG_BRANCH'
    git(work, 'checkout', '-q', 'main')
    git(work, 'remote', 'set-url', 'origin', str(tmp_path / 'elsewhere.git'))
    assert publish(work)['blocker']['code'] == 'WRONG_REMOTE'


def test_missing_or_unsafe_policy_fails_closed(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'evidence.md').write_text('x\n')
    (work / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').unlink()
    assert publish(work)['blocker']['code'] == 'POLICY_UNREADABLE'
    pol = yaml.safe_load((REPO / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').read_text()); pol['force_push'] = True
    (work / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').write_text(yaml.safe_dump(pol))
    assert publish(work)['blocker']['code'] == 'POLICY_INVALID'
    assert git(remote, 'log', '--oneline').count('\n') == 0          # remote still has only the baseline


def test_disabled_policy_commits_but_does_not_push(tmp_path):
    work, remote = make_repo(tmp_path, enabled=False)
    before = remote_head(remote)
    (work / 'evidence.md').write_text('x\n')
    e = publish(work)
    assert e['result'] == 'COMMITTED_NOT_PUSHED' and e['push_status'] == 'SKIPPED_POLICY_DISABLED'
    assert remote_head(remote) == before


def test_unpushed_history_is_scanned_too(tmp_path):
    work, remote = make_repo(tmp_path)
    (work / 'leak.md').write_text('AKIA' + 'QRSTUVWXYZ012345\n'); git(work, 'add', '-A')
    git(work, 'commit', '-q', '-m', 'test: earlier unpushed commit')     # committed outside the publisher
    (work / 'clean.md').write_text('fine\n')
    e = publish(work)
    assert e['security_scan_status'] == 'FAIL' and remote_head(remote) != git(work, 'rev-parse', 'HEAD')


def test_prestaged_changes_refused(tmp_path):
    work, _ = make_repo(tmp_path)
    (work / 'a.md').write_text('a\n'); git(work, 'add', 'a.md')
    assert publish(work)['blocker']['code'] == 'PRESTAGED_CHANGES'


def test_real_policy_is_safe():
    pol = yaml.safe_load((REPO / 'AI_CONTROL/AUTO_PUSH_POLICY.yaml').read_text())
    assert pol['force_push'] is False and pol['rewrite_history'] is False and pol['branch'] == 'main'
    assert pol['remote_url'] == 'https://github.com/BenyaminZadehmoradian/HLS_DSE.git'
    assert pol['scan']['pdf']['default'] == 'block' and pol['scan']['pdf']['allowlist'] == []
    assert 'p1_authorized' in pol['protected_state']['files']['RESEARCH_STATE.yaml']
