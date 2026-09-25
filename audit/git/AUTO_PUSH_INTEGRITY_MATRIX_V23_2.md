# Auto-Push Integrity Matrix — V23.2

**Implementation:** `src/hlsdse/publish.py` (`automatic_publish`), `hlsdse publish`.
**Policy:** `AI_CONTROL/AUTO_PUSH_POLICY.yaml` 1.0.
**Tests:** `tests/test_auto_publish.py`. They use mock bare remotes in `tmp_path`; the real remote is never contacted,
and the pinned `remote_url` blocks any other target.

| Requirement | Implemented | Tested | Result |
|---|---|---|---|
| Automatic commit | `automatic_publish` commits after all gates pass | `test_a_success_commits_pushes_and_logs` | PASS |
| Automatic push | `git push origin HEAD:refs/heads/main` when `enabled: true` | `test_a_…` (remote head == local head) | PASS |
| Validation before push | the policy validation commands run before staging; any failure → no commit | `test_b_validation_failure_no_commit_no_push` | PASS |
| Secret protection | extension/name blocklist + 9 content patterns (private keys, AWS/GitHub/OpenAI/Slack tokens, password assignments, Xilinx license lines, HOSTID) | `test_c_secret_detected_no_push` (5 cases) | PASS |
| PDF protection | PDFs blocked unless allowlisted with SHA-256 + license (allowlist empty); `git ls-files '*.pdf'` must be empty | `test_d_restricted_pdf_no_push`, `test_real_policy_is_safe` | PASS |
| Artifact protection | forbidden extensions (`.xsa .bit .bin .elf .dcp` …), tool/cache path parts (`.Xil`, `__pycache__` …), binaries, files over 5 MB | `test_e_forbidden_artifact_no_push` (4 cases) | PASS |
| Unpushed-history scan | the scan covers `origin/main...HEAD`, not only the new change | `test_unpushed_history_is_scanned_too` | PASS |
| No force push | policy must say `force_push: false` (else POLICY_INVALID); the push command has no force flag | `test_missing_or_unsafe_policy_fails_closed` | PASS |
| Remote divergence protection | fetch, then `merge-base --is-ancestor`; diverged → commit kept, push blocked | `test_f_remote_divergence_no_force_push` (remote history untouched) | PASS |
| Push logging | append-only `audit/git/AUTO_PUSH_LOG.jsonl` with all required fields | `test_a_…`, `test_h_…` | PASS |
| Empty commit prevention | no substantive change → NO_CHANGES, no commit, no push, no log line | `test_g_empty_change_no_commit` | PASS |
| Failed push handling | `push_status: FAILED`, local commit kept, no retry | `test_h_push_failure_keeps_local_commit` (pre-receive hook rejects) | PASS |
| Human-gate independence | gate fields and `audit/gates/approvals/` are never auto-published; non-gate edits are allowed | `test_protected_state_change_is_never_auto_published`, `test_approval_artifacts_are_never_auto_published`, `test_non_gate_state_field_may_change` | PASS |
| Commit message policy | format regex + meaningless-subject list | `test_meaningless_commit_message_blocked` (4 cases) | PASS |
| Branch/remote verification | branch == main; remote URL == policy | `test_wrong_branch_and_wrong_remote_blocked` | PASS |
| Fail-closed policy load | missing, malformed or unsafe policy → blocked | `test_missing_or_unsafe_policy_fails_closed` | PASS |
| Staging discipline | refuses pre-staged changes; the staged set must equal the selected set | `test_prestaged_changes_refused` | PASS |
| Emergency override | `enabled: false` → commit, no push | `test_disabled_policy_commits_but_does_not_push` | PASS |

**Suite result:** `32 passed`. That is 28 auto-publish tests plus the 4 pre-existing project tests.
