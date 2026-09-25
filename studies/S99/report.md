# S99 — Decision-Centric Multi-Source Acquisition of Local vs Joint Evidence

**Status:** PLANNED (phase P6). No execution is authorized by this document; the study runs only after its phase gate.

## Why this study
Treats local and joint evaluation at each fidelity as information sources with different cost and bias and buys joint evidence only when it is expected to change Pareto membership or feasibility. Builds on multi-information-source value-of-information methods (MISO knowledge gradient, constrained multi-source BO); runs as a real test only if S98 finds a residual above noise.

## Core question
Under a fixed expensive-evaluation budget, does a decision-centric acquisition rule over {local, joint} x {HLS, synthesis, post-route} find the global feasible Pareto front of multi-kernel designs better (ADRS, feasible-front recall) or cheaper than always-local, always-joint and cost-aware multi-fidelity baselines?

## Hypotheses
- **H0:** The rule is not better than the best baseline at equal budget.
- **H1:** The rule reaches equal ADRS with fewer expensive evaluations (or better ADRS at equal budget), and the gain disappears when the S98 residual is zero (it comes from decision gating, not from extra fidelity).

## What will be measured
- ADRS vs the S97 oracle and feasible-front recall
- cost by source/fidelity, in both evaluation hours and counts
- decision_change_rate of joint evaluations
- time-to-target ADRS
- ablation isolating decision gating from extra fidelity

## Notes
Baselines: always-local + composition, always-joint, CMMFO-style multi-fidelity BO, the same model without the residual term, AutoDSE-style search, random, and the S72 algorithms.

## Dependencies and overlaps
- Depends on: S97 (oracle), S98 (residual), S72 (search baselines), S81 (noise)
- Overlaps (recorded in `contracts/STUDY_ID_REGISTRY.yaml` overlap_review): S05 (evidence selection), S16 (decision-change prediction), S22 (minimum joint evidence), S07 (joint task-candidate-fidelity selection)

## Evidence
No evidence exists yet. Missing measurements are `UNKNOWN/NOT_MEASURED`; they are never estimated and presented as measured.

## Gate
Retained only if it produces reproducible evidence with an effect above the noise floor, a decision impact, or a
scientifically useful negative result. Full contract: `studies/S99/CONTRACT.yaml`.
