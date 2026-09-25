# S100 — Runtime Memory-Interference Residual on Zynq-7020

**Status:** PLANNED (phase P3) — BLOCKED: no hardware board registered. No execution is authorized by this document; the study runs only after its phase gate.

## Why this study
Measures whether co-resident accelerators change each other's (and the CPU's) runtime through the shared ACP or HP memory path on the reference device, and whether that changes the runtime-Pareto ranking. BLOCKED until a physical board is registered: the current platform contract has no board.

## Core question
On an xc7z020 board, does the runtime of an HLS kernel measured alone differ from its runtime when co-resident kernels share the ACP or HP data path, by more than run-to-run variation, and does that change the Pareto front or ranking obtained from local runtime measurements?

## Hypotheses
- **H0:** Co-residence changes kernel runtime by less than run-to-run variation for the chosen workloads.
- **H1:** For memory-bound kernels (low operational intensity) co-residence produces a runtime residual that exceeds variation, differs between ACP and HP paths, and changes the runtime-Pareto ranking.

## What will be measured
- runtime residual (joint - local) per kernel and data path with CI
- residual vs operational intensity
- ranking/Pareto changes between local-runtime and joint-runtime fronts

## Notes
Published measurements (DATE 2021/2022, IEEE TC 2023, FPGAworld 2013) report slowdowns up to 10-16x on FPGA SoCs; none feeds that effect into an HLS DSE decision.

## Dependencies and overlaps
- Depends on: hardware board registration, S98
- Overlaps (recorded in `contracts/STUDY_ID_REGISTRY.yaml` overlap_review): S73 (memory/data movement), S83 (end-to-end latency), S84 (CPU-FPGA overlap)

## Evidence
No evidence exists yet. Missing measurements are `UNKNOWN/NOT_MEASURED`; they are never estimated and presented as measured.

## Gate
Retained only if it produces reproducible evidence with an effect above the noise floor, a decision impact, or a
scientifically useful negative result. Full contract: `studies/S100/CONTRACT.yaml`.
