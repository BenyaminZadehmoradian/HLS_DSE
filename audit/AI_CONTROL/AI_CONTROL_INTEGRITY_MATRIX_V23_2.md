# AI_CONTROL Integrity Matrix — V23.2

**Date:** 2026-09-25 · **HEAD:** `91f14bb` · **Evidence:** `evidence/control_probe.py` →
`evidence/control_probe_results.json` (sha256 `dbde289ab215…`; probe run 2026-09-25T16:17:50Z against a
`git archive HEAD` copy, mock tools only).

**Levels:**

| Level | Name | Meaning |
|---|---|---|
| D | Documented | a policy text states the rule |
| C | Configured | a machine-readable field or flag encodes it |
| V | Validated | a checker reports a violation, statically and after the fact |
| RE | Runtime enforced | code on the execution path refuses the action |
| NT | Negative test | a synthetic unauthorized request was attempted |

"Bypass possible" means the action reaches the (mock) tool without passing any check.

| Control requirement | Documented | Configured | Validated | Runtime enforced | Negative test | Bypass possible | Status |
|---|---|---|---|---|---|---|---|
| Human Gate | YES (`AI_PHASE_GATE_POLICY.md`, MASTER) | YES (`human_gate_required: true`) | PARTIAL (validator errors only if the flag ≠ true; F5) | **NO** | A, D | **YES** (tool reached) | NOT ENFORCED |
| P0 authorization | YES | PARTIAL (`active_phase_state: PLANNED`; no authorization field or approval record) | PARTIAL (validator requires P0 = PLANNED; detects a P0 state change after the fact; C, G) | **NO** | A | **YES** | NOT ENFORCED |
| P1 authorization | YES | YES (`p1_authorized: false`) | **NO** (validator never reads `p1_authorized`; F3/F3b pass with the field removed or `true`) | **NO** | B, F3b | **YES** | NOT ENFORCED |
| Automatic-advance prevention | YES (`PHASE_CONTROL.yaml` forbidden list) | YES (`automatic_advance: false`) | PARTIAL (a transition away from P0/PLANNED is flagged afterwards; C) | **NO** (any writer can edit the state; the executor ignores it) | C | **YES** | NOT ENFORCED |
| Phase transition | YES (`PHASE_CONTROL.yaml` transition_rules) | YES | PARTIAL (only "P0 not PLANNED"; `current_phase` is unchecked, F4) | **NO** (no transition API exists) | G | **YES** | NOT ENFORCED |
| Study scope | YES (`AI_SCOPE_POLICY.yaml`, study contracts) | PARTIAL (`current_study`) | **NO** (`current_study: S01` passes; F8) | **NO** (`RunRecord.study_id` is never checked) | B, F8 | **YES** | NOT ENFORCED |
| Environment scope | YES (`require_environment_fingerprint: true`) | PARTIAL (`active_environment: null`; registry entry) | **NO** (an unknown environment passes; F6) | PARTIAL: the launcher enforces the toolchain identity (L1, L2), but nothing ties a run to `active_environment` and `environment_id=None` runs (E) | E, L1, L2 | **YES** (outside the launcher; E) | PARTIAL (toolchain only) |
| Device scope | YES (DEVICE_REFERENCE_CONTRACT) | YES (`fixed_reference_device`) | YES (validator checks the part in state and contracts) | **NO** (the executor takes no device argument) | — (no device parameter to test) | N/A at the executor | VALIDATED ONLY |
| Tool execution | YES (`AI_TOOL_POLICY.yaml`) | YES | NO | **NO** (`flow.run_command` → `subprocess.run(shell=True)` unguarded) | F, H, P3, P4 | **YES** | NOT ENFORCED |
| Direct adapter invocation | implied ("hard barrier") | NO | NO | **NO** (no adapter or orchestrator layer exists; `run_command` is the lowest layer and is importable) | H | **YES** | NOT ENFORCED |
| Fail-closed behaviour | implied by `AI_STOP_CONDITIONS.md` | NO | PARTIAL (validator fails closed only for malformed state, F2, and bad gate flag, F5) | **NO** (executor unaffected by any corruption; F1–F8) | F1–F8 | **YES** | FAIL-OPEN at runtime |
| Audit logging | YES (`require_command_record`, AI_CHANGE_CONTROL fields) | NO | NO | **NO** (no control-decision log exists; `run_command` writes only the tool's stdout) | all | — | NOT IMPLEMENTED |
| Policy versioning | PARTIAL (contracts have `contract_version`; state has `state_schema_version`) | PARTIAL (no `AI_CONTROL` file carries a version) | NO | **NO** (no decision records policy version or commit; only `StageDecision.policy_version="1.0"`, hard-coded) | — | — | NOT IMPLEMENTED |

**Only runtime-enforced controls found (not part of AI_CONTROL):**
1. **Toolchain environment guard** in `environments/xilinx_2025_2_1/run_in_env.sh`: it fails closed on a vendor-hash
   mismatch (L1), a polluted PATH (L2), foreign tool resolution, and wrong `XILINX_*` variables.
2. **Data-record validators:** `staged.validate_stage_decision` (V1) and `provenance.build_metric`. These reject
   invalid records; they do not gate execution.
