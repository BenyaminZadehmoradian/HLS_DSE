# S97 — Compositional-Assumption Test

**Status:** PLANNED (phase P5). No execution is authorized by this document; the study runs only after its phase gate.

## Why this study
Compositional HLS DSE (Liu/Petracca/Carloni DATE 2012; COSMOS 2017; PG-DSE 2023; EtoE-DSE 2024) prunes each component to its local Pareto front before system-level search. This study tests that assumption against an exhaustive joint post-route oracle on multi-kernel designs at low, medium and high utilization of an xc7z020.

## Core question
On multi-kernel designs sharing one xc7z020, how often does the true joint Pareto front (post-P&R) contain a kernel implementation that is NOT on that kernel's local Pareto front, and how often is a composition of locally feasible, locally Pareto-optimal implementations jointly infeasible?

## Hypotheses
- **H0:** Local Pareto pruning loses no joint-Pareto design and admits no jointly infeasible composition (the compositional assumption holds).
- **H1:** At high joint utilization, local pruning loses joint-Pareto designs and/or admits jointly infeasible compositions at a rate above the P&R noise floor.
- **note:** A result supporting H0 is a publishable NEGATIVE_RESULT and is preserved.

## What will be measured
- pareto_loss_rate — joint-Pareto designs removed by local pruning
- false_feasible_rate — locally feasible compositions that fail jointly
- ADRS of the pruned space vs the oracle
- every rate compared with its Vivado-seed noise floor (S81)

## Notes
A result supporting the assumption (H0) is kept as a NEGATIVE_RESULT; it would show that local pruning is safe on this platform.

## Dependencies and overlaps
- Depends on: S01 (flow works), S81 (noise floor)
- Overlaps (recorded in `contracts/STUDY_ID_REGISTRY.yaml` overlap_review): S04 (oracle benchmark), S66 (composition failure)

## Evidence
No evidence exists yet. Missing measurements are `UNKNOWN/NOT_MEASURED`; they are never estimated and presented as measured.

## Gate
Retained only if it produces reproducible evidence with an effect above the noise floor, a decision impact, or a
scientifically useful negative result. Full contract: `studies/S97/CONTRACT.yaml`.
