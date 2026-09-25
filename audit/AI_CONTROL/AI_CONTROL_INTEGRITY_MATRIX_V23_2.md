# AI_CONTROL Integrity Matrix — V23.2 (post-implementation, P0/S00)

**Date:** 2026-09-25 · **Base:** `f6b111a` + the P0/S00 control-plane change set.
**Evidence:**
- `tests/test_control_plane.py` (formal suite);
- `evidence/control_probe.py` → `evidence/control_probe_results.json` (probe run 2026-09-25T17:16:41Z; synthetic
  repositories, mock tools only).

**Approval:** `audit/gates/approvals/G0-P0-S00-001.yaml`.

The pre-implementation matrix, in which every row was NOT ENFORCED, is preserved at commit `d2a8523`.

**Level legend:**

| Level | Meaning |
|---|---|
| D | Documented |
| C | Configured (machine-readable) |
| V | Validated (`scripts/validate_project.py`, static) |
| RE | Runtime enforced (refused on the execution path, before the process starts) |
| NT | Negative-tested |

| Control requirement | D | C | V | RE (enforcement point) | NT | Bypass possible | Status |
|---|---|---|---|---|---|---|---|
| Human Gate | YES | YES (approval artifact schema, `CONTROL_PLANE_POLICY.yaml`) | YES (every approval validated; active state needs a valid approval) | YES (`control._decide` → `select_approval`) | C, M, corrupt data | NO in-repo; a local git commit of a forged approval is outside repository control | ENFORCED |
| P0 authorization | YES | YES | YES | YES (gated categories need phase state `IMPLEMENTING`, a valid approval and scope) | A, C, POS | NO (Python path, launcher-by-name) | ENFORCED |
| P1 authorization | YES | YES (`p1_authorized`) | YES (in P0 `p1_authorized` must be false; F3b-type edits are rejected) | YES (`P1_NOT_AUTHORIZED`, `PHASE_MISMATCH`, `p1_implementation` out of scope) | B, L | NO | ENFORCED |
| Automatic-advance prevention | YES | YES | YES | YES (`transition()` has no phase-advance path: `PHASE_ADVANCE_FORBIDDEN`; human-only gate exit) | L | NO | ENFORCED |
| Phase transition | YES | YES (PHASE_CONTROL table + `transition_requirements`) | YES (legal states accepted, provenance required) | YES (`control.transition`; direct writes → `STATE_PROVENANCE_INVALID`) | L | NO in-repo | ENFORCED |
| Study scope | YES | YES | YES (current study registered, contract phase consistent) | YES (`STUDY_MISMATCH`, `UNKNOWN_STUDY`, `STUDY_NOT_EXECUTABLE`) | D | NO | ENFORCED |
| Environment scope | YES | YES (`active_environment`, approval `environment`, registry) | YES (registered or null; approval env = active env) | YES (`ENVIRONMENT_REQUIRED`, `UNKNOWN_ENVIRONMENT`, `ENVIRONMENT_NOT_ACTIVE`, `ENVIRONMENT_MISMATCH`) | F, G | NO | ENFORCED |
| Device / hardware scope | YES | YES | YES (reference part) | PARTIAL (`HARDWARE` needs `hardware_available: true` in the environment; no per-run device argument yet) | N (hardware actions) | NO | ENFORCED FOR HARDWARE ACTIONS |
| Tool execution | YES | YES (`tools:` identity map) | YES (AST guard test) | YES (`run_authorized` → `_execute`; launcher PATH gate `bin/<tool>` → `tool_gate.sh`) | A, K | **YES, two launcher paths**: `bin/vitis_hls` → real `vitis-run`, and an absolute tool path given to `run_in_env.sh` | PARTIAL (launcher patch pending) |
| Direct executor / adapter invocation | YES | — | YES (AST guard: only `control.py` and `publish.py` start processes; no `shell=True`) | YES (sealed, single-use, argv-bound decisions) | J | NO in Python; OS-level direct execution is outside repository control | ENFORCED |
| Fail-closed behaviour | YES | YES | YES | YES (13 fail-closed cases → DENY before the executor; any exception → `INTERNAL_ERROR` DENY; an unloggable decision → DENY) | I, H, M, fail-closed matrix | NO | FAIL-CLOSED |
| Control-decision logging | YES | YES (`paths.decision_log`) | YES (log must parse) | YES (every decision; `executor_called` reflects reality; args hashed) | all | — | IMPLEMENTED |
| Policy versioning | YES | YES (`policy_version`, `state_schema_version`, `approval_schema_version`, contract `schema_version`) | YES (state/policy version match required) | YES (recorded in every decision with `repository_commit`, `state_hash`) | I | — | IMPLEMENTED |

**Suite result:** `82 passed, 1 xfailed` (full test suite).

The one expected failure (`test_k_vitis_hls_shim_is_gated`, strict xfail) documents the open `vitis_hls` path. It
will start failing, and so force an update, as soon as the launcher patch lands.
