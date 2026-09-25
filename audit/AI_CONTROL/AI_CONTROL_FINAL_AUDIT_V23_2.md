# AI_CONTROL Final Audit — V23.2

**Date:** 2026-09-25 · **Audited HEAD:** `91f14bbb59623b6296d8b880de3bea522161eab0` · **Audit only.** No research
execution, no real tool invocation, no state change.

**Companion documents:**
- `AI_CONTROL_INTEGRITY_MATRIX_V23_2.md`
- `AI_CONTROL_RUNTIME_TRACE_V23_2.md`
- `AI_CONTROL_BYPASS_AUDIT_V23_2.md`

**Evidence:**
- `evidence/control_probe.py`: reproducible; mock tools only; state mutations only in a temporary `git archive` copy.
- `evidence/control_probe_results.json`: sha256 `dbde289ab215…`.

# 1. Executive Result

```text
DOCUMENTATION_ONLY
```

> **Is `AI_CONTROL` an executable/enforceable control layer, or only documentation/configuration?**
> It is **documentation/configuration only**.
> - None of its 30 files is read by any executable code (static grep; runtime audit hook: 0 opens).
> - The execution primitive `hlsdse.flow.run_command` reached the (mock) tool for every unauthorized request tested:
>   P0, P1, human-gate bypass, null environment, invalid transition, and corrupted policy/state.

Maturity levels:

| Level | Meaning | Status |
|---|---|---|
| Level 0 | Documentation | reached, for AI_CONTROL |
| Level 1 | Configuration/schema validation | partial, but **outside** AI_CONTROL: `scripts/validate_project.py` checks some `RESEARCH_STATE.yaml` fields statically |
| Level 2 | Runtime checks exist | not reached for phase, gate or scope |
| Level 3 | Enforced at the execution boundary | not reached |
| Level 4 | Enforcement tested against bypass | not reached |

The only runtime-enforced guard in the repository is the toolchain **environment** guard in
`environments/xilinx_2025_2_1/run_in_env.sh`. It fails closed (L1, L2), but it is not part of AI_CONTROL and does not
check phase, gate or scope.

In practice, the controls that actually prevented research execution so far were:
1. the absence of any P0/P1 execution code (P0 is PLANNED);
2. the human operator;
3. the Claude Code harness permission prompts.

None of these is a repository control.

# 2. Actual Control Architecture

**Documented chain:**
```text
Human → Agent/CLI → AI_CONTROL → Policy → Permission → Phase Gate → Scope → Execution Manager → Adapter → Tool
```

**Chain that exists in code:**
```text
Human / Agent (Claude Code shell, Python import)
   ├── hlsdse CLI (src/hlsdse/cli.py)
   │     ├── status            → reads RESEARCH_STATE.yaml, prints only
   │     ├── validate-project  → subprocess: scripts/validate_project.py (static checker)
   │     ├── scan-environment  → subprocess: scripts/p0_preflight.py → scanning.environment → <tool> -version
   │     └── generate-candidates / validate-config (no execution)
   ├── hlsdse.flow.run_command(run, command, log)   ← the only generic executor
   │     └── subprocess.run(command, shell=True)    ← NO state, gate, scope, policy or environment check
   └── environments/xilinx_2025_2_1/run_in_env.sh <cmd>
         └── env -i + vendor settings + toolchain guards → exec "$@"  ← environment check only
AI_CONTROL/* : not on any path
```

**Layer by layer:**

| Documented layer | Component in code | Source | Input → output | Called by | Failure behaviour |
|---|---|---|---|---|---|
| AI_CONTROL / Policy | none | — | — | — | — |
| Permission check | none (`AI_PERMISSION_MATRIX.csv` is unread) | — | — | — | — |
| Phase gate | none at runtime. Static only: `validate_project.py` lines 19–23 | `scripts/validate_project.py` | state YAML → errors list, exit 1 | human, CLI `validate-project`, `p0_gate_check.sh` | fail-closed only for the checked fields |
| Scope check | none | — | — | — | — |
| Execution manager | `run_command` | `src/hlsdse/flow.py` | RunRecord, shell string → RunRecord.status | any importer | exceptions → `status=FAILED` (record only) |
| Tool adapter / launcher | `run_in_env.sh` | `environments/xilinx_2025_2_1/` | argv → exec | human/agent | exit 3 on environment violations (fail-closed) |

# 3. Enforcement Points

| Question | Answer (file:function) |
|---|---|
| Where is P0 authorization checked? | **Nowhere at runtime.** Statically, `validate_project.py` requires `active_phase_state == 'PLANNED'`; no authorization field exists. |
| Where is P1 authorization checked? | **Nowhere.** `p1_authorized` is read only by `cli.py status` (printed). The validator does not check it. |
| Where is the Human Gate checked? | **Nowhere at runtime.** The validator requires `human_gate_required is True`, but there is no approval record to check against. |
| Where is phase transition checked? | **Nowhere at runtime.** No transition API exists; `PHASE_CONTROL.yaml` transition_rules are unread. |
| Where is execution scope checked? | **Nowhere.** `RunRecord.study_id` and `environment_id` are free strings. |
| Where is research execution blocked? | **Nowhere by code.** It is blocked in practice only because no P0/P1 execution code exists yet. |
| Where is automatic advancement prevented? | **Nowhere.** The state file is writable, and the validator detects only departures from P0/PLANNED. |
| Where is unauthorized tool execution blocked? | **Nowhere by phase/gate.** `run_in_env.sh` blocks wrong *environments* only. |

# 4. Negative Test Results

Mock tool; results from `control_probe_results.json`.

| Test | Request | Expected (from contract) | Actual | Executor reached? | Result |
|---|---|---|---|---|---|
| A | Run S00 while P0 is PLANNED/unauthorized | BLOCKED | executed, `SUCCESS` | **YES** | FAIL |
| B | Run S01 (P1) while `p1_authorized: false` | BLOCKED | executed | **YES** | FAIL |
| C | Write P1/IMPLEMENTING (auto-advance), then run S01 | BLOCKED; no auto advance | write succeeded; executed; validator afterwards: `P0 state is not PLANNED` | **YES** | FAIL (detected afterwards only) |
| D | Human gate required, no approval | BLOCKED | executed | **YES** | FAIL |
| E | `environment_id=None`, `active_environment: null` | BLOCKED (`require_environment_fingerprint: true`) | executed | **YES** | FAIL |
| F | Research tool via the execution layer | BLOCKED before tool | executed | **YES** | FAIL |
| G | Write P0 PLANNED → P1 RUNNING, then run S01 | BLOCKED | executed; validator afterwards: `P0 state is not PLANNED` | **YES** | FAIL (detected afterwards only) |
| H | Direct call of the lowest layer | control required | executed | **YES** | CONTROL BYPASS POSSIBLE |
| V1 | Stage decision ADVANCE without evidence | rejected | `ValueError` | no | PASS (data validator, not a gate) |

# 5. Bypass Results

| Path | Result |
|---|---|
| Agent → AI_CONTROL → Executor | path does not exist |
| Agent → Executor (`run_command`) | **BYPASSABLE** |
| Agent → Adapter | **BYPASSABLE** (no adapter layer) |
| CLI → Executor | not reachable (no execution command; P1, exit 2) |
| CLI → Adapter | `scan-environment` runs `<tool> -version` unguarded (identity query; intentional) |
| Script (launcher) → Tool | **BYPASSABLE** for phase/gate (P3); environment-guarded (L1, L2) |
| Agent shell → Tool | outside repository control (P4) |

Full classification: `AI_CONTROL_BYPASS_AUDIT_V23_2.md`. There are 4 UNINTENTIONAL_BYPASS paths and 1 path outside
repository control.

# 6. Fail-Open / Fail-Closed Results

The runtime column concerns the executor; the static column concerns `validate_project.py`. Each case was tested in
a temporary copy.

| Case | Test | Static validator | Runtime executor |
|---|---|---|---|
| Policy file missing (`PHASE_CONTROL.yaml`) | F1 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| State file malformed | F2 | FAIL-CLOSED (6 errors) | **FAIL-OPEN** |
| Authorization field missing (`p1_authorized`) | F3 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| P1 authorization flipped to `true` | F3b | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| Unknown phase (`current_phase: P9`) | F4 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| Unknown gate status (`human_gate_required: maybe`) | F5 | FAIL-CLOSED | **FAIL-OPEN** |
| Control module crash | — | n/a (no control module exists) | n/a |
| Unknown environment (`active_environment: ENV-DOES-NOT-EXIST`) | F6 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| Unknown permission (permission matrix corrupted) | F7 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| Study scope expanded (`current_study: S01`) | F8 | **FAIL-OPEN** (PASS) | **FAIL-OPEN** |
| Launcher: vendor hash mismatch / polluted PATH | L1, L2 | — | **FAIL-CLOSED** (exit 3) |

# 7. Logging

A blocked or allowed request **cannot be reconstructed** from repository artifacts:
- no request ID, actor, caller, policy version, gate version, decision or reason is recorded;
- `run_command` writes only the tool's own stdout to `log_path`;
- the launcher writes a one-line error to stderr and nothing persistent.

`StageDecision` (in `staged.py`) has `decision_id`, `timestamp_utc`, `decision_source` and `policy_version`. It covers
candidate stage decisions only, and nothing persists it automatically. `EvidenceStore` is append-only JSONL, but it
is not used for control decisions.

**Missing:** a control-decision log carrying `request_id`, `timestamp`, `actor`, `requested_action`, `state
snapshot/hash`, `policy/contract versions`, `commit`, `decision`, `reason`, `caller`, and `executor_called`.

# 8. Policy / State Authority

- **Canonical source of truth:** `RESEARCH_STATE.yaml`, per `CANONICAL_PROJECT_CONTRACT.source_of_truth`.
  `AI_CONTROL/PHASE_CONTROL.yaml` duplicates the phase and state fields (`active_phase: P0`, `state: PLANNED`).
- **Competing sources:** no CLI flag, environment variable or Python constant overrides the state; there is no
  `--force-p0`.
- **But the state is not consumed** by any execution path, so its authority is declarative only.
- **Consistency of the two copies:** `PHASE_CONTROL.yaml` and `RESEARCH_STATE.yaml` currently agree, but nothing
  checks that they stay consistent.
- **Versioning:** the state has `state_schema_version: '1.0'` and contracts carry `contract_version`. No `AI_CONTROL`
  file has a version field, and no decision records a commit SHA.

**Human approval semantics:**
- The contracts require "explicit human approval" (MASTER; `AI_PHASE_GATE_POLICY.md`), and
  `AI_EXECUTION_POLICY.yaml` lists what a gate approval must reference.
- **No approval artifact is defined:** no approval field, file, token, command, timestamp, approver identity, scope or
  expiry exists in the state, schemas or code.
- Approval is therefore neither machine-checkable, nor scoped, nor persistent, nor auditable in the repository.
  Chat messages such as "continue" have no defined status.

# 9. Findings

| Severity | Finding |
|---|---|
| **CRITICAL** | No runtime enforcement of P0, P1, the human gate or phase transitions. The executor `hlsdse.flow.run_command` runs any shell command (`shell=True`) with no state or policy check (A, B, D, F, H). |
| **CRITICAL** | `run_in_env.sh` executes any command, including `vivado -mode batch`, with no phase/gate check (P3). It is the natural entry point for P0/P1 tool runs. |
| **HIGH** | No human-approval artifact is defined, so "authorized" cannot be verified by code or by an auditor. |
| **HIGH** | The static validator ignores `p1_authorized`, `current_phase`, `current_study`, `active_environment` and all `AI_CONTROL` files (F3, F3b, F4, F6, F7, F8 pass). |
| **HIGH** | Every control-input corruption fails open at runtime (F1–F8). |
| **MEDIUM** | There is no control-decision log or policy versioning, so the policy version behind a decision cannot be established. |
| **MEDIUM** | Environment scope is enforced only for the toolchain. Runs are not bound to `active_environment` (E), and `RunRecord.environment_id` accepts `None`. |
| **MEDIUM** | Phase state is duplicated in `RESEARCH_STATE.yaml` and `PHASE_CONTROL.yaml`, with no consistency check. |
| **LOW** | `validate_project.py` hard-codes `active_phase_state == 'PLANNED'`. It will report an error on a legitimately approved P0 (IMPLEMENTING), so it validates "pre-P0", not the state machine. |
| **LOW** | `scan-environment` / `p0_preflight` launch vendor binaries (`-version`) with no gate. This is intentional and non-research. |
| **INFO** | The toolchain environment guard is runtime-enforced and fail-closed (L1, L2). Data validators (`staged.py`, `provenance.py`) enforce record rules at runtime (V1). |
| **INFO** | The Vivado and Vitis processes running during this audit (PIDs 24342, 24434, 24886, 25316) started at 14:43–14:44 under the desktop session. They are the user's GUI sessions and were not started by this audit, whose probe ran at 18:17 local. |
| **INFO** | Test coverage: 4 unit tests (pragma space, stage decision, provenance). Phase gate, authorization, bypass, negative control and end-to-end mock tests: none. |

# 10. Corrections

**No control-layer code was changed.**
- `AI_PHASE_GATE_POLICY.md` forbids executable implementation work on a phase in `PLANNED`. Building the runtime
  control plane is S00/P0 work ("Validate the project control plane", `studies/S00/CONTRACT.yaml`).
- This audit therefore documents the minimal corrections and the tests that would prove them. They require human
  authorization of P0.

| # | Minimal required correction | Test that proves it |
|---|---|---|
| 1 | A single `authorize(action, study, environment)` check reading `RESEARCH_STATE.yaml`, called at the start of `flow.run_command` and by the launcher before `exec`. It fails **closed** on a missing, malformed or unknown state, phase, gate or environment. | Re-run `control_probe.py`: A–H, P3 and F1–F8 must show `executor_reached: false` |
| 2 | A defined approval artifact, e.g. `audit/gates/approvals/<gate_id>.yaml` with approver, timestamp, scope (phase/study/environment), commit and expiry, referenced by the state. | Approval missing, out of scope or expired → DENY |
| 3 | Extend `validate_project.py` to cover `p1_authorized`, `current_phase`/`current_study` consistency, `active_environment` ∈ registry, and `PHASE_CONTROL.yaml` ↔ state agreement. Replace the hard-coded `PLANNED` with the transition rules. | F3, F3b, F4, F6, F8 must fail |
| 4 | An append-only control-decision log (JSONL) recording request_id, actor, action, state hash, policy versions, commit, decision, reason and `executor_called`. | Every probe request produces one log line |
| 5 | Move `control_probe.py` into `tests/` as negative control tests once corrections 1–4 exist. They currently fail by design. | pytest green only when enforcement exists |

**Files added by this audit** (audit evidence only):
- `audit/AI_CONTROL/AI_CONTROL_INTEGRITY_MATRIX_V23_2.md`
- `audit/AI_CONTROL/AI_CONTROL_RUNTIME_TRACE_V23_2.md`
- `audit/AI_CONTROL/AI_CONTROL_BYPASS_AUDIT_V23_2.md`
- `audit/AI_CONTROL/AI_CONTROL_FINAL_AUDIT_V23_2.md`
- `audit/AI_CONTROL/evidence/control_probe.py`
- `audit/AI_CONTROL/evidence/control_probe_results.json`

`AI_CONTROL/`, `src/`, `scripts/`, `environments/` and `RESEARCH_STATE.yaml` are unchanged.

# 11. Validation

| Command | Result |
|---|---|
| `python3 audit/AI_CONTROL/evidence/control_probe.py` | 24 synthetic requests; mock only; temp copy removed; live state hash unchanged (`562136aff9b2…`) |
| `git diff --check` | clean |
| `python3 scripts/validate_project.py` | `errors=0 warnings=0` |
| `run_in_env.sh ~/.venvs/hls_dse_py312/bin/python -m pytest -q -p no:cacheprovider` | `4 passed` |
| Artifact scan (`*.xsa`, `*.bit`, `*.bin`, `*.elf`); `runs/`; `evidence/measured/` | none; `_TEMPLATE` only; empty |
| Real tool invocation by this audit | none: every tool call targeted the absolute-path mock; `scan-environment` ran with PATH restricted to the mock dir |

# 12. Git

| Item | Value |
|---|---|
| Parent | `91f14bbb59623b6296d8b880de3bea522161eab0` |
| New commit | `audit: verify AI control runtime enforcement` (hash reported in the operator summary; a report cannot contain its own commit hash) |
| Files changed | the 6 audit files listed in §10 |
| Push performed | **NO** |

# 13. Final Gate Status

`RESEARCH_STATE.yaml` holds:
- `status: PLANNED`, `active_phase_state: PLANNED`;
- `p1_authorized: false`;
- `human_gate_required: true`;
- `automatic_advance: false`;
- `active_environment: null`.

These were verified before and after the audit, with an identical hash.

```text
AI_CONTROL AUDIT COMPLETE
P0 NOT STARTED
P0 NOT AUTHORIZED
P1 NOT AUTHORIZED
WAITING FOR HUMAN GATE
```
