# Human Gate Request — P0 / S00 (V23.2)

**Prepared:** 2026-09-25 by Claude Code (AI).
**This is a request, not an approval.** Nothing in this document authorizes anything. Only an approval artifact
authored and committed by the human researcher can open the gate. The AI must not create that artifact, and
`AI_CONTROL/AUTO_PUSH_POLICY.yaml` refuses to auto-publish anything under `audit/gates/approvals/`.

## 1. Current state

Verified from the repository at HEAD `0cbfc1cd01073b7d6fb3736f5abe9c939179069e` (= `origin/main`):

| Field (`RESEARCH_STATE.yaml`, sha256 `562136aff9b2…`) | Value |
|---|---|
| `project_version` | V23.2 |
| `current_phase` / `active_phase` | P0 |
| `current_study` | S00 |
| `status` / `active_phase_state` | PLANNED |
| `p1_authorized` | false |
| `human_gate_required` | true |
| `automatic_advance` | false |
| `active_environment` | null |
| `AI_CONTROL/PHASE_CONTROL.yaml` | `active_phase: P0`, `state: PLANNED` |
| `audit/gates/approvals/` | **does not exist**; no approval artifact anywhere in the repository or its history |

**Readiness evidence:**
- `audit/environment/FINAL_PRE_P0_READINESS_AUDIT_V23_2.md` (technical prerequisites PASS);
- `audit/gates/HUMAN_GATE_PACKAGE_V23_2.md`;
- `audit/gates/PRE_P0_CORRECTION_AUDIT_V23_2.md`;
- `audit/AI_CONTROL/AI_CONTROL_FINAL_AUDIT_V23_2.md`. Its result is DOCUMENTATION_ONLY: no runtime enforcement
  exists yet, which is what this P0 scope would build.

## 2. Proposed approval scope

P0/S00 limited to **implementing and validating the control plane** (S00 purpose: "Validate the project control
plane before any scientific experiment"). Specifically:
- a runtime authorization API, with approval, state, phase, study and environment validation;
- enforcement before `subprocess` in `hlsdse.flow.run_command` and in the toolchain launcher;
- a canonical phase-transition function;
- an append-only control-decision log;
- validator repair;
- negative, bypass, fail-closed and mock-positive tests;
- auto-push integration tests.

**No scientific execution of any kind.**

## 3. Decisions required from you

| # | Decision | Options |
|---|---|---|
| D1 | Approve P0/S00 for the scope above? | approve / reject / approve with a narrower scope |
| D2 | Active environment for this gate | `ENV-2025.2.1-XC7Z020-1` (registered) or `null`. With `null`, control-plane tests use a synthetic mock environment only, and the runtime layer will DENY any environment-requiring action until an environment is approved. |
| D3 | State transition (§5) | commit the transition together with the approval (policy-conformant; recommended), or approve now and transition later |
| D4 | Device-contract interpretation (speed grade `-1`, board `NONE` as resolved placeholders; from the earlier gate package) | confirm / reject |
| D5 | Expiry of the approval | a date, or `null` for no expiry |
| D6 | Archived `studies/S09/CONTRACT.yaml` malformed `study_id` | leave / correct |

## 4. The artifact you must author

Create `audit/gates/approvals/G0-P0-S00-001.yaml` and commit it yourself, with your own git identity and a plain
`git commit`. The auto-publisher will not publish this path.

Fields marked `<HUMAN>` must be filled in by you; the AI must not fill them.

```yaml
approval_id: G0-P0-S00-001
project_version: V23.2
phase: P0
study: S00
environment: <HUMAN: ENV-2025.2.1-XC7Z020-1 or null>        # decision D2

scope:
  allowed:
    - control_plane_implementation
    - mock_validation
    - unit_tests
    - integration_tests
    - negative_control_tests
    - bypass_tests
    - validator_tests
    - control_decision_logging
    - auto_push_policy_validation

  forbidden:
    - scientific_experiments
    - research_hls_runs
    - research_vivado_runs
    - research_vitis_runs
    - dse_campaigns
    - xsa
    - bitstream
    - elf
    - hardware_programming
    - hardware_execution
    - p1_implementation

approver: <HUMAN: your name>
approved_at: <HUMAN: ISO-8601 timestamp with timezone>
approved_commit: <HUMAN: the commit you reviewed; currently 0cbfc1cd01073b7d6fb3736f5abe9c939179069e>
expires_at: <HUMAN: ISO-8601 timestamp, or null>             # decision D5

status: APPROVED
```

## 5. State transition you are asked to approve

Per `AI_CONTROL/AI_PHASE_GATE_POLICY.md` ("The user/researcher must explicitly approve the Gate before the next
Phase enters `IMPLEMENTING`") and `AI_CONTROL/PHASE_CONTROL.yaml` (transition `PLANNED → IMPLEMENTING` requires
`start_active_phase`):

```text
P0  PLANNED  →  IMPLEMENTING      (S00, control-plane scope only)
```

If you choose D3 = commit together, make these edits in the same commit as the approval:

| File | Field | From | To |
|---|---|---|---|
| `RESEARCH_STATE.yaml` | `status` | `PLANNED` | `IMPLEMENTING` |
| `RESEARCH_STATE.yaml` | `active_phase_state` | `PLANNED` | `IMPLEMENTING` |
| `RESEARCH_STATE.yaml` | `active_environment` | `null` | per D2 |
| `AI_CONTROL/PHASE_CONTROL.yaml` | `state` | `PLANNED` | `IMPLEMENTING` |

Every other gate field stays unchanged: `p1_authorized: false`, `human_gate_required: true`,
`automatic_advance: false`, `next_phase_implementation_allowed: false`, `future_phase_implementation_allowed: false`.

**Known consequence:** `scripts/validate_project.py` currently hard-codes `active_phase_state == PLANNED`. It will
report `P0 state is not PLANNED` after this transition, until the validator repair lands. Repairing it is inside
the approved scope.

Until then, the auto-publisher's validation step fails and **auto-push stays blocked**. That is fail-closed and
expected: the repair must be the first change of the implementation run.

## 6. Explicitly forbidden, even after approval

- Scientific experiments, DSE campaigns and benchmark evaluations.
- Real HLS, Vivado or Vitis research runs. Negative and positive control tests use mock tools only.
- XSA, bitstream or ELF generation; FPGA programming; any hardware execution.
- Any P1 implementation, or setting `p1_authorized` or `next_phase_implementation_allowed`.
- Automatic advance to any later phase. A successful S00 is **not** P1 authorization.
- The AI creating, editing or auto-publishing approval artifacts or gate-field state changes.

## After you commit the artifact

Ask for the P0/S00 control-plane implementation again. The run will begin by validating this artifact:
- file present and well-formed;
- `status: APPROVED`, `phase: P0`, `study: S00`, `project_version: V23.2`;
- `approved_commit` is an ancestor of HEAD;
- not expired;
- scope includes `control_plane_implementation` and excludes scientific execution;
- the state is consistent with the approved transition.

It will stop if any check fails.
