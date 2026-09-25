# AI PHASE GATE POLICY

The machine-readable truth is `CONTROL_PLANE_POLICY.yaml` (phases, states, transition requirements) and
`PHASE_CONTROL.yaml` (transition table); the runtime control plane enforces both. This document explains them.
It also absorbs the former `AI_SCOPE_POLICY.yaml`, the gate part of `AI_REPORTING_POLICY.md` and
`PHASE_GATE_REPORT_TEMPLATE.md`.

## Fundamental rule

The AI MUST NOT implement the entire research project in one pass.

Exactly one Phase may be in the `IMPLEMENTING` state at a time.

The next Phase may remain specified, documented, and planned, but its executable
implementation must not be created or executed until the current Phase passes its Gate.

## Allowed states

```text
PLANNED
  ↓
IMPLEMENTING
  ↓
VALIDATING
  ↓
GATE_REVIEW
  ├── PASS → APPROVED_FOR_NEXT_PHASE   (human only)
  └── FAIL → BLOCKED
```

Remediation is work done while a Phase is `BLOCKED`; it is not a separate state. `PHASE_CONTROL.yaml` has no
automated transition out of `BLOCKED`: leaving it is a human-authored state change.

A Phase in `PLANNED` state may have:
- contract
- acceptance criteria
- required inputs
- expected outputs
- test plan
- report template
- plot specification

It may NOT have executable implementation work performed ahead of its Gate.

## Gate authority

A Phase Gate is a hard barrier.

The AI cannot approve its own Phase Gate.

The user/researcher must explicitly approve the Gate before the next Phase enters
`IMPLEMENTING`.

## What happens after a failure

If validation fails:

1. stop progression;
2. preserve all outputs and logs;
3. create a failure report;
4. identify failed acceptance criteria;
5. propose remediation;
6. wait for approval before modifying the Phase;
7. re-run validation after remediation.

The AI must not silently repair a failed Phase and continue.

## No speculative implementation

The AI must not:
- implement future Studies "because they will be needed later";
- create all experiment scripts upfront;
- create all plotting scripts upfront beyond declared templates/contracts;
- execute future benchmarks;
- populate future evidence;
- fabricate placeholder measurements;
- silently create infrastructure that materially implements future research phases.

Shared infrastructure may be created only when required by the currently active Phase
and explicitly recorded as shared infrastructure.

## Phase completion package

Before requesting a Gate, the active Phase must produce:

1. implementation status;
2. required experiments;
3. raw logs/artifacts;
4. normalized evidence;
5. derived metrics;
6. required plots;
7. validation results;
8. Phase report;
9. known limitations/failures;
10. reproducibility information.

## Gate report

Every active Phase ends with a Gate Report, written with `REPORT_TEMPLATE.md` (report_type `GATE`). Its Gate
section must contain:

```text
phase_id
status
acceptance_criteria            # one row per criterion: required evidence | result | PASS/FAIL
criterion_results
required_outputs               # implementation, raw logs/artifacts, evidence, derived metrics,
produced_outputs               # required plots, validation, phase report, reproducibility record
validation_summary
failed_checks
known_limitations
reproducibility_status
recommendation_for_gate        # PASS / FAIL / REMEDIATION_REQUIRED (AI recommendation only)
human_gate_decision            # PENDING / APPROVED / REJECTED (written by the human)
```

A report without evidence for a criterion is not a PASS. The AI may recommend PASS or FAIL based on evidence,
but only the user/researcher may authorize progression: the next Phase may start only when
`human_gate_decision = APPROVED` and a human-authored approval exists in `audit/gates/approvals/`.

## Critical-path behavior

The project follows:

```text
P0 → Gate G0 → P1 → Gate G1 → P2 → Gate G2 → ...
```

For the core path:

```text
P0 → P1 → P2 → P3 → P4 → P5 → P6 → P7 → P15
```

No phase may be skipped merely because the AI predicts that its outcome will be positive.

## Scope
- The core path above is fixed; every extension (studies outside it) requires its own Gate.
- Future work is never executable before its Gate.
- The historical archive (`archive/`) is read-only.

## Restart behavior

A new conversation/session must read `RESEARCH_STATE.yaml` and determine the active
Phase and Gate before doing implementation work.

If the active Phase is already in `GATE_REVIEW`, the AI must not start the next Phase.
It must continue Gate review/remediation only.
