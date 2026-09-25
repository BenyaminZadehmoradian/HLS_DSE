# Automatic Publish (Auto-Push) Policy

**Machine-readable policy:** `AI_CONTROL/AUTO_PUSH_POLICY.yaml` (policy_version 1.0).
**Only implementation:** `src/hlsdse/publish.py` → `automatic_publish()`, exposed as `hlsdse publish`.
No other component commits or pushes on behalf of automation.

## Default

The repository owner made automatic commit + push the default (2026-09-25). After a successful, validated
execution that changes tracked files, the change is committed and pushed to `origin/main` without a separate
"push it" instruction.

## Auto-push is not authorization

Auto-push only synchronises the repository.
- It never grants, implies or replaces a Human Gate.
- It never authorizes P0, P1 or any Study.
- It never modifies research state to make a push succeed.

## Pipeline

Every step must pass. The first failure stops the run.

```text
load policy (missing / malformed / force_push≠false → fail closed)
→ branch == main, remote URL == policy remote_url, no merge/rebase in progress, nothing pre-staged
→ commit message format (<phase>/<study>: <change> or <area>: <change>; no meaningless subjects)
→ collect changes (no substantive change → NO_CHANGES: no empty commit, no push)
→ protected-state check
→ fetch origin; origin/main must exist (else REMOTE_REF_MISSING)
→ content scan of the new change set (working-tree copy) AND the committed content of every file added or
      modified by each commit in origin/main..HEAD (secrets, license files, forbidden artifacts/paths,
      binaries, size, PDFs). Deleting a previously committed file publishes no content and is not blocked.
→ `git ls-files '*.pdf'` must be empty (or allowlisted)
→ validation commands (git diff --check, validate_project.py, approved pytest)
→ stage exactly the selected paths; verify the staged set equals the selected set
→ commit
→ divergence check (origin/main must be an ancestor of HEAD)
→ git push origin HEAD:refs/heads/main   (never --force)
→ append the event to audit/git/AUTO_PUSH_LOG.jsonl
```

**Protected state:** a change to any gate field (listed in `protected_state` of the YAML policy) is never
auto-published. Files under `audit/gates/approvals/` are never auto-published either.
The human commits gate decisions.

## Blocking outcomes

| Condition | Outcome |
|---|---|
| Validation, security, PDF or artifact failure; protected state change; wrong branch/remote; bad message; unknown repository state | **No commit, no push** |
| Remote diverged | Local commit kept; push blocked: `AUTO-PUSH BLOCKED / REMOTE DIVERGED / HUMAN REVIEW REQUIRED` |
| Push rejected | Local commit kept; `push_status: FAILED`; no blind retry. The next publish run pushes the pending commits again, after re-validating. |

## PDFs and copyright

PDFs are blocked by default. A PDF may be published only if it is listed in `scan.pdf.allowlist` with its path,
SHA-256 and a verified redistributable license. That list is empty, so the Related Work local-only rule
(`related_work/README.md` §6) is unchanged.

## Emergency override

Set `enabled: false` in the policy file. That is a tracked, reviewable change. Validated commits are still created;
pushes are skipped. There is deliberately **no** CLI flag to skip validation or scanning, or to force a push.

## Audit log

`audit/git/AUTO_PUSH_LOG.jsonl` is append-only. Each attempt (except NO_CHANGES) records:
- time, repository, branch, the before/after commit, the pushed range and remote;
- validation, security, artifact and PDF scan status;
- the commit message, push status, actor and reason;
- provenance (phase, study, run_id, environment_id where available), policy version and blocker.

No credentials are logged.

A log line is written after its own push, so the entry for publish N is committed and pushed by publish N+1. A change
to the log alone does not trigger a publish.

## Known limitations

- The secret scan is pattern-based. It is a safety net, not a guarantee.
- Validation commands use the approved venv path from the environment registry, which is machine-specific.
- The publisher publishes the whole working-tree change set unless `--path` restricts it. Unrelated untracked files
  therefore block publication (fail-closed) instead of being silently included.
