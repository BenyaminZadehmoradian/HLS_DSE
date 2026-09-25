project_version: V23.2

# R14 — V23.2 Staged Evaluation and Metric Provenance

## Purpose

This report freezes two implementation-level requirements before real tool execution:

1. the evaluation flow is capable of conditional stage advancement rather than forcing every candidate through the full expensive path;
2. every numeric result is traceable to the exact producing tool/artifact and Run.

## Scientific reference flow

The full flow remains the reference:

`Candidate → HLS → Synthesis → Implementation → Bitstream → Programming → Runtime`

Staging does not redefine a missing later measurement as success. If a candidate stops at HLS, later stages are `NOT_RUN`, not failed or measured.

## Stage decisions

Allowed decisions are `ADVANCE`, `DROP`, `KEEP`, `DEFER`, and `BLOCKED`. Every decision records the candidate, Run, current stage, reason codes, evidence IDs, next stage, decision source, timestamp, and policy version.

An estimator-assisted decision additionally records estimator identity, version, confidence, input evidence IDs, and uncertainty.

## Estimates

An estimate can be used to prioritize the next candidate or justify a stage transition when the configured policy permits it. It must remain classified as `ESTIMATED` or `PREDICTED`; it cannot become `MEASURED` by propagation into a report.

## Metric provenance

For every numeric metric the minimum provenance chain is:

`metric → status → stage → Run → Candidate → benchmark/device → tool + version → source artifact → SHA-256 → source field/measurement`.

Derived metrics additionally list their input metric IDs. Predicted metrics identify their model/estimator and confidence.

## Decision-impact study requirement

Staged evaluation is not assumed to be a contribution. A later Study must measure whether it reduces expensive evaluations and total cost without unacceptable loss of decision quality or false elimination of useful candidates.

## Gate status

- Architecture: COMPLETE
- Contracts: COMPLETE
- Schemas: COMPLETE
- Unit tests: COMPLETE
- Real tool execution: NOT YET PERFORMED
- Human gate: REQUIRED before P1
