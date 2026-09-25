# AI_CONTROL P0/S00 Runtime Control-Plane Implementation Report — V23.2

**Date:** 2026-09-25.
**Base:** `f6b111a6e7f7680e10c1ed998a38990ccef33bad` (= `origin/main` at start).
**Scope:** P0 / S00 runtime control-plane implementation only.

No scientific execution of any kind took place. See §13.

## 1. Approval

| Item | Value |
|---|---|
| Artifact | `audit/gates/approvals/G0-P0-S00-001.yaml` (not modified by this run) |
| approval_id | G0-P0-S00-001 |
| project_version / phase / study | V23.2 / P0 / S00 |
| approver | Benyamin |
| approved_at | 2026-09-25T18:44:00+02:00 |
| approved_commit | `0cbfc1cd01073b7d6fb3736f5abe9c939179069e` (ancestor of HEAD) |
| expires_at | null (no expiry) |
| status | APPROVED |
| environment | null |
| Committed by | BenyaminZadehmoradian, commits `c532a67` + `f6b111a` |
| Allowed scope | control_plane_implementation, mock_validation, unit_tests, integration_tests, negative_control_tests, bypass_tests, validator_tests, control_decision_logging, auto_push_policy_validation |
| Forbidden scope | scientific_experiments, research_hls_runs, research_vivado_runs, research_vitis_runs, dse_campaigns, xsa, bitstream, elf, hardware_programming, hardware_execution, p1_implementation |

**Validation result: VALID.** `hlsdse.control.validate_approval` checks, and the artifact passes, all of the following:
- all fields present;
- no placeholders;
- `status: APPROVED`;
- file name equals `approval_id`;
- project version matches;
- timestamp is ISO-8601 with a timezone and not in the future;
- not expired;
- scope tokens are all known and disjoint;
- the file is committed and clean;
- `approved_commit` is an ancestor of HEAD.

**Layout note:** in the artifact, `allowed:` and `forbidden:` are not indented under `scope:`, so YAML parses them as
top-level keys with `scope: null`. The validator accepts exactly this indentation-collapsed form, which is unambiguous,
alongside the nested form. It rejects both forms at once.

The artifact was not edited. If you prefer the nested form, re-indent it in a human commit.

## 2. State transition: NOT PERFORMED (pending human action)

| | Value |
|---|---|
| Contract | `AI_PHASE_GATE_POLICY.md` says the researcher must approve before a phase enters `IMPLEMENTING`. `PHASE_CONTROL.yaml` has `PLANNED → IMPLEMENTING` requiring `start_active_phase`. |
| Mapping | `CONTROL_PLANE_POLICY.transition_requirements.start_active_phase: valid_approval` |
| Conclusion | The approval artifact is sufficient; no separate transition authorization is required. |
| Mechanism | `hlsdse.control.transition()`, CLI `hlsdse transition` (built in this run) |
| Before | P0 / S00 / `PLANNED`; `RESEARCH_STATE.yaml` sha256 `562136aff9b2d5201b1c7d3fab441320ad22f80dab7073f2d491f91a3bd5f139` |
| After (this run) | **unchanged**: P0 / S00 / `PLANNED` |

**Why it was not performed:** the transition command below was run once against the real repository. The Claude Code
harness's permission check denied it, and it was not retried or worked around.

The same command, run in a throwaway clone, produced the expected result:
- `status` and `active_phase_state` changed `PLANNED → IMPLEMENTING`, and `PHASE_CONTROL.state` changed to
  `IMPLEMENTING`;
- nothing else changed;
- a TRANSITION record was written, with new state sha256 `da92522d…` and requirement `start_active_phase`.

**To perform it** (researcher, from the repository root):

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m hlsdse transition --to IMPLEMENTING \
    --approval G0-P0-S00-001 --actor Benyamin --reason "start P0/S00 control-plane implementation (G0-P0-S00-001)"
python3 scripts/validate_project.py        # must report errors=0
git add RESEARCH_STATE.yaml AI_CONTROL/PHASE_CONTROL.yaml audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl
git commit -m "gate: p0 s00 planned to implementing (G0-P0-S00-001)" && git push origin main
```

The auto-publisher refuses gate-field changes (`PROTECTED_STATE_CHANGE`) by design, so this commit is yours.
`active_environment` stays `null`, and P1 stays unauthorized.

Until the transition is committed, the runtime is fail-closed:
- every gated action in the real repository is DENIED with `PHASE_STATE_NOT_ACTIVE`, including control-plane
  actions;
- ungated discovery and read-only actions are allowed.

## 3. Runtime architecture (post-implementation)

```text
flow.run_command ─┐
scanner._version ─┼─► control.run_authorized ─► control._decide ─► DENY ─► log(executor_called=false) ─► return
launcher bin/<tool> → tool_gate.sh → tool_gate_main ─┘                  └► ALLOW ─► log-writability check
                                                                                   ─► seal ─► control._execute
                                                                                   ─► subprocess (argv, no shell)
                                                                                   ─► log(executor_called=true, rc)
```

`_decide` evaluates, in order:
1. policy;
2. action and category;
3. state + PHASE_CONTROL;
4. phase and study;
5. P1 authorization;
6. environment registered;
7. state provenance.

An ungated action is ALLOWed at that point. A gated action continues with:
1. phase state;
2. repository commit;
3. approval (selection and validation);
4. scope;
5. approval environment = active environment;
6. environment requirement;
7. hardware availability;
8. study registry status.

The decision is ALLOW only if all pass. Any exception is `INTERNAL_ERROR` DENY.

## 4. Enforcement points

| File | Function | Boundary |
|---|---|---|
| `src/hlsdse/control.py` | `_decide` / `authorize` | the single authorization decision; logged |
| `src/hlsdse/control.py` | `run_authorized` | DENY never reaches subprocess; an unloggable ALLOW is DENY |
| `src/hlsdse/control.py` | `_execute` | the only tool executor; sealed (per-process HMAC), single-use, argv-bound ALLOW |
| `src/hlsdse/control.py` | `transition` | the only state-transition writer; PHASE_CONTROL table; human-only gate exit; no phase advance |
| `src/hlsdse/control.py` | `check_state_provenance` | a non-PLANNED state needs a matching TRANSITION record |
| `src/hlsdse/flow.py` | `run_command` | run executor → `run_authorized` (argv, never `shell=True`) |
| `src/hlsdse/scanning/environment.py` | `_version` | tool version queries → `run_authorized` (`environment_discovery`) |
| `src/hlsdse/cli.py` | `validate-project`, `scan-environment`, `authorize`, `transition` | no process API left in the CLI (`runpy` in-process) |
| `environments/xilinx_2025_2_1/bin/<tool>` (10 tools), `tool_gate.sh` | `tool_gate_main` | launcher PATH gate; exit 126 on DENY |
| `scripts/validate_project.py` | `repository_control_errors` | static state machine / approval / provenance / policy consistency |
| `AI_CONTROL/CONTROL_PLANE_POLICY.yaml` | — | versioned policy (1.0): actions, categories, tools, transitions, gate fields |

## 5. Negative tests (A–N)

Sources:
- `tests/test_control_plane.py`;
- probe `evidence/control_probe_results.json`.

Each test uses mock tools. "DENY" in the table means all of the following were confirmed:
- `executor_called=false`;
- the spy saw 0 executor calls;
- the mock marker file is absent;
- the decision was logged.

| # | Request | Reason code | Result |
|---|---|---|---|
| A | P0 research (`research_hls_runs`, `research_vivado_runs`, `scientific_experiments`) | OUT_OF_SCOPE | PASS |
| B | P1/S01; `p1_implementation` | P1_NOT_AUTHORIZED; OUT_OF_SCOPE | PASS |
| C | approval missing (PLANNED; transition without approval; approval removed) | PHASE_STATE_NOT_ACTIVE; NO_APPROVAL | PASS |
| D | wrong study (S01; unknown S99X) | STUDY_MISMATCH; UNKNOWN_STUDY | PASS |
| E | wrong phase (P2; unknown P42) | PHASE_MISMATCH; UNKNOWN_PHASE | PASS |
| F | null environment where required | ENVIRONMENT_REQUIRED | PASS |
| G | unknown / template-only / non-active environment | UNKNOWN_ENVIRONMENT; ENVIRONMENT_NOT_ACTIVE | PASS |
| H | malformed state (11 variants), missing state, PHASE_CONTROL inconsistent | STATE_INVALID | PASS |
| I | missing / malformed / incomplete / bad-category policy | POLICY_INVALID | PASS |
| J | direct `_execute` (forged, from `authorize()`, None); argv tampering; `flow.run_command`; shell string | ExecutionDenied; DENIED; INVALID_REQUEST | PASS |
| K | launcher gate shim (`vivado`, `vitis-run --mode hls`, outside launcher, unresolved tool root) | OUT_OF_SCOPE; exit 126; TOOL_NOT_RESOLVED | PASS |
| L | invalid transitions (→GATE_REVIEW, →APPROVED, →RUNNING, P0→P1, GATE_REVIEW→APPROVED); direct state writes (PLANNED→IMPLEMENTING, P0→P1) | INVALID_TRANSITION; PHASE_ADVANCE_FORBIDDEN; HUMAN_ONLY_TRANSITION; STATE_PROVENANCE_INVALID; STATE_INVALID | PASS |
| M | expired approval; placeholder, PENDING, future, naive-timezone, non-ancestor commit, wrong version, uncommitted, corrupt approval | APPROVAL_EXPIRED; APPROVAL_INVALID; APPROVAL_NOT_APPROVED; APPROVAL_NOT_COMMITTED; APPROVAL_CORRUPT | PASS |
| N | wrong scope (`dse_campaigns`, `xsa`, `bitstream`, `elf`, hardware; narrow approval); unknown action | OUT_OF_SCOPE; UNKNOWN_ACTION | PASS |

**Negative tests:** 14/14 PASS.

## 6. Positive mock test

Request: P0 / S00 / `control_plane_implementation`, environment `null`, approval G0-P0-S00-001 in the same flat
layout as the real artifact.

| Check | Result |
|---|---|
| Decision | **ALLOW** (`AUTHORIZED`) |
| Executor | `executor_called=true`; spy saw exactly one call with the authorized argv |
| Mock tool | `mock_control_step` ran; `executor_returncode=0` |
| Decision log | contains every required field |

**Result: PASS.** No HLS, Vivado or Vitis binary was resolved or executed.

A synthetic research approval with an active environment also produced ALLOW through the launcher shim, with only the
mock `vivado` behind it (`test_k_launcher_gate_allows_only_authorized_and_resolved_tools`).

## 7. Bypass tests

See `AI_CONTROL_BYPASS_AUDIT_V23_2.md`.

| Path | Classification |
|---|---|
| Agent → AI_CONTROL → Executor | NO_BYPASS |
| Agent → Executor | NO_BYPASS |
| Agent → Adapter | NO_BYPASS |
| CLI → Executor | NO_BYPASS |
| Launcher → Tool (by name) | NO_BYPASS |
| Publisher | INTENTIONAL_BYPASS (repository synchronisation) |
| Direct OS-level tool execution, plain git | OUTSIDE_REPOSITORY_CONTROL |
| **Launcher → `vitis_hls` → real `vitis-run`** | **UNINTENTIONAL_BYPASS** |
| **Launcher → Tool (absolute path argument)** | **UNINTENTIONAL_BYPASS** |

Both unintentional paths need the launcher patch described in the bypass audit. The harness's permission check
denied that edit in this run.

## 8. Fail-closed tests

All 13 cases were DENY before the executor (`evidence/control_probe_results.json` → `fail_closed`):

1. missing policy;
2. malformed policy;
3. missing state;
4. malformed state;
5. missing approval;
6. expired approval;
7. unknown phase;
8. unknown study;
9. unknown environment;
10. invalid state;
11. corrupt permission data;
12. corrupt decision log;
13. out-of-scope action.

The test suite adds:
- an internal exception → `INTERNAL_ERROR` DENY;
- an unwritable decision log → DENY, with nothing executed.

**Fail-closed: PASS.**

## 9. Logging

The log is `audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl`, append-only JSONL. It holds two kinds of record.

**`DECISION` records** contain:
- request and caller: `request_id`, `timestamp_utc`, `actor`, `caller`;
- the request: `action`, `category`, `phase`, `study`, `environment`;
- provenance: `state_hash`, `approval_id`, `repository_commit`;
- versions: `state_schema_version`, `policy_version`, `approval_schema_version`, `project_version`,
  `contract_version`;
- the outcome: `decision`, `reason`, `executor_called`, plus `executor_returncode` and `executor_error` after an
  ALLOW;
- `argv_sha256`. Arguments are hashed, never stored in clear (tested).

**`TRANSITION` records** contain `old_state`, `new_state`, `approval_id`, `timestamp_utc`, `reason`, `actor`, the
old/new state sha256 and the old/new gate hash.

DENY always has `executor_called: false`. ALLOW is written after execution, with the real outcome. No decision was
logged in the real repository during this run. The log file will first appear with the researcher's transition
command (§2).

## 10. Validator

`scripts/validate_project.py` no longer hard-codes `active_phase_state == PLANNED`. It now calls
`hlsdse.control.repository_control_errors`, the same code the runtime uses, which checks:
- the full state machine: project/schema version, known phase, consistent `status`/`active_phase_state` and
  PHASE_CONTROL, boolean gate fields, `p1_authorized`/`p1_gate_required` rules in P0, human-gate fields,
  `active_environment` null or registered, study registered with a consistent contract phase;
- every approval artifact;
- that a non-PLANNED state has a matching transition record;
- that IMPLEMENTING, VALIDATING and GATE_REVIEW have a valid approval whose environment equals `active_environment`;
- that the decision log parses;
- that `CONTROL_PLANE_POLICY.gate_fields` equals `AUTO_PUSH_POLICY.protected_state`;
- that the AI_CONTROL policy files are present.

Legal PLANNED, IMPLEMENTING, VALIDATING and GATE_REVIEW states are accepted (tested).

**Result on the real repository:** `errors=0 warnings=0`.

## 11. Auto-push

This change set is published by the canonical publisher (`hlsdse publish`). The pipeline is:
1. validation (diff check, validator, approved pytest);
2. secret, artifact and PDF scans (including unpushed history);
3. staged-set verification;
4. commit;
5. divergence check;
6. push;
7. `AUTO_PUSH_LOG.jsonl`.

`RESEARCH_STATE.yaml` and `PHASE_CONTROL.yaml` are not part of this change set; they are unchanged. The existing
throwaway-remote suite covers:
- validation failure;
- secrets;
- restricted PDF;
- forbidden artifacts;
- remote divergence;
- push rejection;
- empty changes.

New in this run: `test_publisher_never_publishes_a_canonical_transition`. The publisher refuses a transitioned
state (`PROTECTED_STATE_CHANGE`).

**Where the outcome is recorded:** the push result and commit hash are in `audit/git/AUTO_PUSH_LOG.jsonl` and the
operator summary. A report cannot contain its own commit hash.

## 12. Security

- No license file was read, and no credential was printed or logged. Decision logs hash the arguments.
- No `*.lic`, `*.key` or `*.pem` files were staged, nor restricted PDFs, XSA, BIT, ELF or tool artifacts; the
  publisher's scans enforce this.
- No force push, history rewrite, or blind staging (explicit `--path` list).
- The approval artifact was not modified. No approval artifact was created in the real repository. Synthetic test
  approvals exist only in temporary directories and are marked `SYNTHETIC_TEST_FIXTURE`.

## 13. Research safety

No scientific execution took place:
- no real Vitis HLS, Vivado or Vitis research run;
- no synthesis or implementation;
- no DSE campaign or benchmark evaluation;
- no XSA, bitstream or ELF;
- no hardware programming or execution;
- no scientific measurement.

All tool calls in tests and the probe were mock scripts. The only real-environment interaction was
`run_in_env.sh bash -c 'command -v …'`, which resolves names and executes no Xilinx tool. User-launched Vivado or Vitis
GUI processes, if any, were not touched, attached to or reused.

**P1:** NOT AUTHORIZED. No S01 or later study was authorized, no future environment was selected, and there was no
automatic advance.

## 14. Remaining limitations

1. **The P0 `PLANNED → IMPLEMENTING` transition is not yet recorded** (§2). The researcher must run it and commit it.
   Until then, the runtime correctly denies all gated work in the real repository.
2. **Two launcher paths are unintentional bypasses:** `bin/vitis_hls`, and an absolute tool path given to
   `run_in_env.sh`. The fix is specified in the bypass audit; it was not applied because the edit was denied. Until it
   is applied:
   - the launcher does not export the tool root, so named tools under the launcher fail closed (`TOOL_NOT_RESOLVED`),
     `-version` queries included;
   - a strict-xfail test tracks the open `vitis_hls` path.
3. **Approval authenticity rests on git.** It relies on a committed, clean file, an ancestor `approved_commit`, and
   the publisher refusing approvals. A locally committed forged approval is outside repository control. Signed
   commits and branch protection are external governance.
4. **The decision log can be forged by a writer of the working tree.** It is append-only by convention, not
   cryptographically. Any provenance record must still reference a valid approval.
5. **Direct OS-level execution of a tool binary**, outside `hlsdse` and outside the launcher, cannot be prevented by
   the repository.
6. **Actor roles are recorded but not checked** (`AI_PERMISSION_MATRIX.csv`). **Per-run device arguments** are not
   yet part of requests.
7. **The S00 study checks are not produced by this run:** `audit/p0_validation.json` and `studies/S00/report.md`
   (canonical version, schemas, S09/S71 and so on). This run delivered the control plane that S00 validates.
8. **One temporary clone was not deleted:** `…/scratchpad/trycopy`, in the session scratch directory outside the
   repository. The deletion was refused by the harness safety check and left to the user.
