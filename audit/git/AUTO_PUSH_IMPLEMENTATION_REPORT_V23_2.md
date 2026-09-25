# Auto-Push Implementation Report — V23.2

**Date:** 2026-09-25

## 1. Current Git state (before this run)

| Item | Value |
|---|---|
| Branch | `main` |
| HEAD | `d2a8523288cde6a1ccf6f26823d292c21c532cdb` |
| `origin/main` | `db5326642d956a5d257d90e9f2045d399b5d178d` |
| Unpushed local commits | 6: `ada921f`, `0f65dba`, `34061c8`, `6a08f53`, `91f14bb`, `d2a8523` |
| Remote | `origin` → `https://github.com/BenyaminZadehmoradian/HLS_DSE.git` |
| Divergence | none (fetched; `origin/main` is an ancestor of HEAD) |

**P0 approval check:** `audit/gates/approvals/` does not exist, and no approval artifact exists anywhere in the
repository or its history.

```text
P0 CONTROL-PLANE IMPLEMENTATION NOT STARTED
P0 IMPLEMENTATION BLOCKED — NO VALID HUMAN APPROVAL ARTIFACT
```

The auto-push mechanism is repository tooling. It executes no research, and it was built independently of the
blocked control plane.

## 2. Auto-push policy

`AI_CONTROL/AUTO_PUSH_POLICY.yaml` (1.0), documented in `AI_CONTROL/AUTO_PUSH_POLICY.md`:
- `enabled: true`, `mode: automatic`;
- `remote: origin` (URL pinned), `branch: main`;
- `force_push: false`, `rewrite_history: false`, `retry_failed_push: false`;
- `on_remote_divergence: block`.

Auto-push is the default after validated executions. **It is not authorization.**

## 3. Implementation location

One canonical component, with no other push logic in the repository:
- `src/hlsdse/publish.py` → `automatic_publish(root, message, *, reason, actor, provenance, paths)`.
- CLI entry: `hlsdse publish -m <msg> --reason <r> --actor <a> [--path P …] [--provenance JSON]`.
  Exit codes: 0 = pushed or no changes; 3 = blocked; 4 = committed but not pushed; 5 = push failed.
- There is no force, skip or no-verify flag.

## 4. Validation chain (before staging)

1. `git diff --check`
2. `python3 scripts/validate_project.py`
3. `environments/xilinx_2025_2_1/run_in_env.sh ~/.venvs/hls_dse_py312/bin/python -m pytest -q -p no:cacheprovider`

The preceding gates run first:
- policy load (fails closed);
- branch and remote check;
- repository state (no merge/rebase, nothing pre-staged);
- commit-message format;
- protected-state check (gate fields and approvals are never auto-published);
- content scans.

After staging, the staged set must equal the selected set.

## 5. Security checks

- Blocked file extensions and names: `.lic .key .pem .p12 .pfx .token .kdbx`, `id_rsa`, `.env`, `credentials*`,
  `.netrc`, `.pypirc`.
- Content patterns: private-key headers, AWS keys, GitHub tokens/PATs, `sk-` keys, Slack tokens, password/secret/api-key
  assignments, Xilinx license `INCREMENT|FEATURE … xilinxd` lines, license host-ID assignments.
- Scope: every file in the new change set **and** every file changed in `origin/main...HEAD`.

## 6. PDF checks

- Every `.pdf` is blocked unless it is on the allowlist (path + SHA-256 + license). The allowlist is empty.
- `git ls-files '*.pdf'` must return no non-allowlisted file.
- The Related Work rule (publisher PDFs are local-only and gitignored) is unchanged.

## 7. Artifact checks

- Blocked extensions: `.xsa .bit .bin .elf .dcp .wdb .vcd .fst .wlf .jou .pb .rpx .db .sqlite`, and archives.
- Blocked path parts: `__pycache__`, `.pytest_cache`, `.Xil`, `.runs`, `.cache`, `.hw`, `.ip_user_files`, `.sim`.
- Binary files are blocked (except `.png`/`.svg`), as is any file over 5 MB.
- A root `.gitignore` for Python bytecode was added.

## 8. Mock test results

All tests use mock bare remotes in `tmp_path`; the real remote was never used for tests.

| Test | Scenario | Result |
|---|---|---|
| A | success → commit + push + log | PASS |
| B | validation failure → no commit, no push | PASS |
| C | secret detected (5 variants) → no push | PASS |
| D | restricted PDF → no push | PASS |
| E | forbidden binary/artifact (4 variants) → no push | PASS |
| F | remote diverged → commit kept, no force push, remote untouched | PASS |
| G | empty change → no commit | PASS |
| H | push rejected → local commit preserved, `FAILED` logged | PASS |
| + | protected state, approvals, non-gate edits, message policy, branch/remote, fail-closed policy, disabled policy, unpushed-history scan, pre-staged refusal, real-policy safety | PASS |

**Total:** `32 passed` (28 auto-publish + 4 existing).

A real bug was found and fixed during testing: git porcelain output was being stripped, which corrupted the first
path (` M RESEARCH_STATE.yaml` became `ESEARCH_STATE.yaml`).

The first real publish attempt (2026-09-25T16:34:21Z) was **blocked by the publisher itself**
(`SECRET_PATTERN`). This report quoted the literal license host-ID assignment text, which matched the pattern. The
text was reworded; the pattern was not weakened. The blocked attempt is the first line of `AUTO_PUSH_LOG.jsonl`.

A pre-publish dry scan of the real repository found no findings across the 7 changed and 75 unpushed files, no
tracked PDFs and no protected-state changes.

## 9–11. Push result, commit hash, remote hash

- **Method:** this change set was published by the canonical publisher itself (`hlsdse publish`), which pushes the
  6 pending commits plus the new one.
- **Where the outcome is recorded:** the result, the new commit hash and the remote hash are in the first line of
  `audit/git/AUTO_PUSH_LOG.jsonl` and in the operator summary. A report cannot contain its own commit hash.
- **When that log line reaches the remote:** by design, it is committed and pushed by the next publish run.

## 12. Remaining limitations

- The secret scan is pattern-based: a safety net, not a guarantee.
- The validation commands contain the machine-specific approved venv path.
- The log line for publish N is committed with publish N+1.
- Auto-push relies on callers invoking `hlsdse publish`. A human or agent can still run plain `git push`, which is
  outside repository control.
- The runtime **AI_CONTROL** phase-gate enforcement is still not implemented. It remains blocked on the missing P0
  approval artifact (see `audit/AI_CONTROL/AI_CONTROL_FINAL_AUDIT_V23_2.md`).
