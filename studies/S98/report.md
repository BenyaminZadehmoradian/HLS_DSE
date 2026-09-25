# S98 — Cross-Fidelity Interaction Residual

**Status:** PLANNED (phase P3). No execution is authorized by this document; the study runs only after its phase gate.

## Why this study
Measures the residual between jointly measured QoR/feasibility and the composition of individually measured QoR, at HLS report, RTL co-simulation, post-synthesis and post-route, over a utilization sweep. It decides whether joint evidence carries any information that local evidence does not — the go/no-go for S99.

## Core question
For kernels co-resident on one xc7z020, is the residual between jointly measured QoR/feasibility and the composition of their individually measured QoR larger than run-to-run noise at HLS-report, RTL co-simulation and post-route fidelity, and how does it scale with joint utilization?

## Hypotheses
- **H0:** The residual is within the noise floor at every fidelity (joint evidence is redundant).
- **H1:** The residual is zero at HLS-report fidelity (additive reports) but exceeds the noise floor at post-route (routing congestion, Fmax loss, placement failure) and grows with utilization.
- **H2:** For dataflow-coupled kernels the residual is already visible at RTL co-simulation (FIFO/back-pressure effects), consistent with Stream-HLS observations.

## What will be measured
- residual per objective and fidelity with bootstrap CI
- residual / noise-floor ratio
- residual-vs-utilization knee
- decision-change indicator (does the residual flip Pareto membership or feasibility?)

## Notes
Expected pattern to test: zero residual in additive HLS reports, non-zero at post-route (congestion, Fmax, placement failure), and at RTL co-simulation for dataflow-coupled kernels.

## Dependencies and overlaps
- Depends on: S01, S81
- Overlaps (recorded in `contracts/STUDY_ID_REGISTRY.yaml` overlap_review): S02 (interaction pilot), S36, S41 (interaction discovery/decomposition), S59 (physical interaction)

## Evidence
No evidence exists yet. Missing measurements are `UNKNOWN/NOT_MEASURED`; they are never estimated and presented as measured.

## Gate
Retained only if it produces reproducible evidence with an effect above the noise floor, a decision impact, or a
scientifically useful negative result. Full contract: `studies/S98/CONTRACT.yaml`.
