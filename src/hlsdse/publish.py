"""Canonical automatic publish: validate -> scan -> stage -> commit -> push, governed by AI_CONTROL/AUTO_PUSH_POLICY.yaml.

This is the only component that commits or pushes on behalf of automation. It never force-pushes, never rewrites
history, never publishes gate-controlled state changes, and is not an authorization mechanism.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

import yaml

POLICY_PATH = 'AI_CONTROL/AUTO_PUSH_POLICY.yaml'


class PublishBlocked(Exception):
    def __init__(self, code, detail):
        super().__init__(f'{code}: {detail}')
        self.code, self.detail = code, detail


def _git(root, *args, check=True):
    cp = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True)
    if check and cp.returncode != 0:
        raise PublishBlocked('GIT_ERROR', f"git {' '.join(args)}: {cp.stderr.strip()}")
    return cp.stdout.strip()


def load_policy(root, policy_path=POLICY_PATH):
    p = Path(root) / policy_path
    try:
        pol = yaml.safe_load(p.read_text(encoding='utf-8'))
    except Exception as exc:
        raise PublishBlocked('POLICY_UNREADABLE', f'{policy_path}: {type(exc).__name__}')
    required = ['policy_version', 'enabled', 'remote', 'remote_url', 'branch', 'force_push', 'rewrite_history',
                'validation_commands', 'commit_message', 'protected_state', 'scan', 'log']
    if not isinstance(pol, dict) or any(k not in pol for k in required):
        raise PublishBlocked('POLICY_INVALID', f'{policy_path} missing required keys')
    if pol['force_push'] is not False or pol['rewrite_history'] is not False:
        raise PublishBlocked('POLICY_INVALID', 'force_push and rewrite_history must be false')
    return pol


def _changed_paths(root):
    cp = subprocess.run(['git', '-C', str(root), 'status', '--porcelain=v1', '-z', '--untracked-files=all'],
                        capture_output=True, text=True)
    if cp.returncode != 0:
        raise PublishBlocked('GIT_ERROR', f'git status: {cp.stderr.strip()}')
    out = cp.stdout                                        # not stripped: the leading status column is significant
    paths, entries, i = [], out.split('\0'), 0
    while i < len(entries):
        e = entries[i]
        if not e:
            i += 1
            continue
        status, path = e[:2], e[3:]
        paths.append((status, path))
        if status[0] in 'RC' and i + 1 < len(entries):   # rename/copy: the next entry is the source path
            paths.append(('D ' if status[0] == 'R' else '  ', entries[i + 1]))
            i += 2
        else:
            i += 1
    return paths


def _check_message(pol, message):
    subject = message.splitlines()[0] if message else ''
    if not re.match(pol['commit_message']['pattern'], subject):
        raise PublishBlocked('COMMIT_MESSAGE_INVALID', subject or '<empty>')
    words = subject.split(':', 1)[1].strip().lower().split() if ':' in subject else []
    if len(words) <= 1 and (not words or words[0] in pol['commit_message']['forbidden_subjects']):
        raise PublishBlocked('COMMIT_MESSAGE_INVALID', f'meaningless subject: {subject}')


def _scan_file(root, rel, pol):
    """Scan the working-tree copy of a changed path. A deletion publishes no content and is never blocked."""
    full = Path(root) / rel
    return _scan_content(rel, full.read_bytes() if full.is_file() else None, pol)


def _scan_content(rel, data, pol):
    if data is None:
        return None
    s = pol['scan']
    p = PurePosixPath(rel)
    if any(part in s['forbidden_path_parts'] for part in p.parts[:-1]):
        return 'FORBIDDEN_PATH', rel
    if p.name in s['forbidden_names'] or p.suffix.lower() in s['forbidden_extensions']:
        return 'FORBIDDEN_ARTIFACT_OR_SECRET_FILE', rel
    if p.suffix.lower() == '.pdf':
        allowed = {(a['path'], a['sha256']) for a in s['pdf'].get('allowlist', [])}
        if (rel, hashlib.sha256(data).hexdigest()) not in allowed:
            return 'PDF_NOT_ALLOWLISTED', rel
        return None
    if len(data) > s['max_file_bytes']:
        return 'FILE_TOO_LARGE', f'{rel} ({len(data)} bytes)'
    if b'\0' in data[:8192] and p.suffix.lower() not in s['binary_allowed_extensions']:
        return 'BINARY_NOT_ALLOWED', rel
    text = data.decode('utf-8', errors='replace')
    for pat in s['secret_patterns']:
        if re.search(pat, text):
            return 'SECRET_PATTERN', f'{rel} (pattern {pat[:24]}...)'
    return None


def _unpushed_findings(root, pol, remote_ref):
    """Scan the committed content of every file added or modified by each commit in remote_ref..HEAD, so a secret
    that was committed and later edited away in the working tree is still caught (it would be pushed)."""
    findings = []
    for commit in _git(root, 'rev-list', f'{remote_ref}..HEAD').split():
        changed = _git(root, 'diff-tree', '-r', '--root', '--no-commit-id', '--name-only', '-z',
                       '--diff-filter=ACMRT', commit)
        for rel in filter(None, changed.split('\0')):
            cp = subprocess.run(['git', '-C', str(root), 'show', f'{commit}:{rel}'], capture_output=True)
            if cp.returncode != 0:
                raise PublishBlocked('GIT_ERROR', f'cannot read {rel} at {commit[:12]}')
            f = _scan_content(rel, cp.stdout, pol)
            if f:
                findings.append((f[0], f'{f[1]} (in unpushed commit {commit[:12]})'))
    return findings


def _protected_state_changes(root, pol, paths):
    changes = []
    for f, keys in pol['protected_state']['files'].items():
        if f not in paths:
            continue
        try:
            old = yaml.safe_load(_git(root, 'show', f'HEAD:{f}', check=False) or '{}') or {}
            new = yaml.safe_load((Path(root) / f).read_text(encoding='utf-8')) or {}
        except Exception:
            changes.append(f'{f}: unparseable')
            continue
        changes += [f'{f}:{k}' for k in keys if old.get(k) != new.get(k)]
    for prefix in pol['protected_state']['paths_never_auto_published']:
        changes += [p for p in paths if p.startswith(prefix)]
    return changes


def _append_log(root, pol, entry):
    p = Path(root) / pol['log']['path']
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(json.dumps(entry, sort_keys=True) + '\n')


def automatic_publish(root, message, *, reason, actor, provenance=None, paths=None, policy_path=POLICY_PATH):
    """Validate, scan, commit and push. Returns the log entry (dict). Never raises for a blocked publish."""
    root = Path(root)
    entry = {'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'repository': None, 'branch': None,
             'before_commit': None, 'after_commit': None, 'remote': None, 'validation_status': 'NOT_RUN',
             'security_scan_status': 'NOT_RUN', 'artifact_scan_status': 'NOT_RUN', 'pdf_scan_status': 'NOT_RUN',
             'commit_message': message.splitlines()[0] if message else '', 'commit_created': False,
             'push_status': 'NOT_ATTEMPTED', 'pushed_range': None, 'files': [], 'actor': actor, 'reason': reason,
             'provenance': provenance or {}, 'policy_version': None, 'result': None, 'blocker': None}
    pol = None
    try:
        pol = load_policy(root, policy_path)
        entry['policy_version'] = pol['policy_version']
        log_rel = pol['log']['path']
        entry['branch'] = _git(root, 'branch', '--show-current')
        entry['before_commit'] = _git(root, 'rev-parse', 'HEAD')
        entry['remote'] = pol['remote']
        url = _git(root, 'remote', 'get-url', pol['remote'], check=False)
        entry['repository'] = url
        if entry['branch'] != pol['branch']:
            raise PublishBlocked('WRONG_BRANCH', entry['branch'] or 'detached HEAD')
        if url != pol['remote_url']:
            raise PublishBlocked('WRONG_REMOTE', url or '<none>')
        gitdir = Path(_git(root, 'rev-parse', '--absolute-git-dir'))
        if any((gitdir / m).exists() for m in ('MERGE_HEAD', 'rebase-merge', 'rebase-apply', 'CHERRY_PICK_HEAD')):
            raise PublishBlocked('UNKNOWN_REPOSITORY_STATE', 'merge/rebase/cherry-pick in progress')
        if _git(root, 'diff', '--cached', '--name-only'):
            raise PublishBlocked('PRESTAGED_CHANGES', 'index already contains staged changes; refusing to mix them')
        _check_message(pol, message)

        changed = _changed_paths(root)
        selected = [p for _, p in changed if paths is None or p in set(paths)]
        if paths is not None and set(paths) - {p for _, p in changed}:
            raise PublishBlocked('UNKNOWN_PATHS', ', '.join(sorted(set(paths) - {p for _, p in changed})))
        substantive = [p for p in selected if p != log_rel]
        if not substantive and not pol['log'].get('log_only_changes_trigger_publish', False):
            entry['result'] = 'NO_CHANGES'
            entry['push_status'] = 'NOT_NEEDED'
            return entry                               # no empty commit, no push, no log line
        entry['files'] = selected

        prot = _protected_state_changes(root, pol, selected)
        if prot:
            raise PublishBlocked('PROTECTED_STATE_CHANGE', '; '.join(prot))

        # scan the new change set and everything already committed but not yet pushed
        remote_ref = f"{pol['remote']}/{pol['branch']}"
        if pol.get('fetch_before_push', True):
            _git(root, 'fetch', '--quiet', pol['remote'], pol['branch'])
        if subprocess.run(['git', '-C', str(root), 'rev-parse', '--verify', '--quiet', remote_ref],
                          capture_output=True).returncode != 0:
            raise PublishBlocked('REMOTE_REF_MISSING', f'{remote_ref} not found; cannot determine the unpushed range')
        findings = [f for f in (_scan_file(root, r, pol) for r in sorted(set(selected))) if f]
        findings += _unpushed_findings(root, pol, remote_ref)
        pdf = [f for f in findings if f[0] == 'PDF_NOT_ALLOWLISTED']
        sec = [f for f in findings if f[0] in ('SECRET_PATTERN', 'FORBIDDEN_ARTIFACT_OR_SECRET_FILE')]
        art = [f for f in findings if f[0] in ('FORBIDDEN_PATH', 'FILE_TOO_LARGE', 'BINARY_NOT_ALLOWED')]
        entry['pdf_scan_status'] = 'FAIL' if pdf else 'PASS'
        entry['security_scan_status'] = 'FAIL' if sec else 'PASS'
        entry['artifact_scan_status'] = 'FAIL' if art else 'PASS'
        tracked_pdfs = [p for p in _git(root, 'ls-files', '*.pdf', '*.PDF').splitlines() if p]
        allow = {a['path'] for a in pol['scan']['pdf'].get('allowlist', [])}
        if any(p not in allow for p in tracked_pdfs):
            entry['pdf_scan_status'] = 'FAIL'
            findings.append(('TRACKED_PDF', ', '.join(p for p in tracked_pdfs if p not in allow)))
        if findings:
            raise PublishBlocked(findings[0][0], '; '.join(f'{c}: {d}' for c, d in findings))

        # validation precedes staging; every command must pass
        for cmd in pol['validation_commands']:
            cp = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
            if cp.returncode != 0:
                entry['validation_status'] = f"FAIL: {' '.join(cmd)} (rc={cp.returncode})"
                raise PublishBlocked('VALIDATION_FAILED', entry['validation_status'] + ' ' + (cp.stdout + cp.stderr)[-300:])
        entry['validation_status'] = 'PASS'

        _git(root, 'add', '-A', '--', *selected)
        staged = set(_git(root, 'diff', '--cached', '--name-only', '--no-renames').splitlines())
        if staged != set(selected):
            _git(root, 'reset', '-q')
            raise PublishBlocked('STAGED_SET_MISMATCH', f'staged={sorted(staged)} selected={sorted(set(selected))}')
        _git(root, 'commit', '-q', '-m', message)
        entry['commit_created'] = True
        entry['after_commit'] = _git(root, 'rev-parse', 'HEAD')

        if not pol['enabled']:
            entry['push_status'] = 'SKIPPED_POLICY_DISABLED'
            entry['result'] = 'COMMITTED_NOT_PUSHED'
            return entry
        remote_head = _git(root, 'rev-parse', remote_ref)
        if subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', remote_head, 'HEAD']).returncode != 0:
            entry['push_status'] = 'BLOCKED_REMOTE_DIVERGED'
            raise PublishBlocked('REMOTE_DIVERGED', f'{remote_ref}={remote_head} is not an ancestor of HEAD; human review required')
        entry['pushed_range'] = f'{remote_head}..{entry["after_commit"]}'
        cp = subprocess.run(['git', '-C', str(root), 'push', pol['remote'], f"HEAD:refs/heads/{pol['branch']}"],
                            capture_output=True, text=True)
        if cp.returncode != 0:
            entry['push_status'] = 'FAILED'
            entry['result'] = 'COMMITTED_PUSH_FAILED'
            entry['blocker'] = {'code': 'PUSH_FAILED', 'detail': cp.stderr.strip()[-300:]}
            return entry
        entry['push_status'] = 'SUCCESS'
        entry['result'] = 'PUSHED'
        return entry
    except PublishBlocked as b:
        entry['blocker'] = {'code': b.code, 'detail': b.detail}
        entry['result'] = 'COMMITTED_NOT_PUSHED' if entry['commit_created'] else 'BLOCKED'
        if entry['push_status'] == 'NOT_ATTEMPTED':
            entry['push_status'] = 'BLOCKED'
        return entry
    finally:
        if pol is not None and entry.get('result') not in (None, 'NO_CHANGES'):
            _append_log(root, pol, entry)
