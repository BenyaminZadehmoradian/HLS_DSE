# HLS-DSE MASTER V23.2 — AI-Controlled Research Program

## Status
Canonical project master and navigation document.

## Core research question
Under a fixed expensive-evaluation budget, does selecting between local and joint evidence improve discovery of the global feasible Pareto frontier in concurrent HLS DSE?

## Scientific core
1. User/benchmark designer defines a bounded legal pragma/design space.
2. Candidate generation creates concrete configurations inside that space.
3. Local evidence is acquired first where appropriate.
4. Joint evidence is acquired selectively when it can change a decision.
5. Physical evidence is treated as a separate fidelity/stage, not conflated with logical interaction.
6. All decisions are evaluated against explicit cost and, where possible, an exhaustive small-space oracle.

## What is not novelty by itself
Automatic pragma generation, Bayesian optimization, GNN/RL, multi-fidelity, Pareto search, multi-kernel deployment, and physical-aware DSE are established research directions and are treated as baselines/components rather than standalone novelty claims.

## Canonical execution chain
Benchmark contract → Pragma Space → Candidate Generator → Legality → Correctness → Local HLS → Joint HLS/Synthesis → Physical implementation when authorized → Evidence → Metrics → Decision Selection → Oracle/Reference → Report.

## Evidence classes
The canonical metric statuses are defined once in `contracts/METRIC_PROVENANCE_CONTRACT.yaml`
(MEASURED, TOOL_REPORTED, DERIVED, ESTIMATED, PREDICTED, LITERATURE_REPORTED, REPRODUCED, REFERENCE_ORACLE, UNKNOWN).
These classes must never be silently mixed.

## Preservation rule
Earlier masters (V22, V22.8, V23, V23.1) and release manifests are kept under `archive/`. The original V21
master is **not** retained in this repository: `archive/V21/` holds only a placeholder (the original's SHA-256
is recorded in `archive/manifests/V22_MANIFEST.json`).

## Canonical reports
Current reports in `REPORTS/`:
- R03 — Experimental Methodology
- R05 — Related Work & Literature Evidence (index; the registry lives in `related_work/`)
- R06 — Study Specifications & Execution Registry (with `contracts/STUDY_ID_REGISTRY.yaml`)
- R07 — Research Extensions
- R09 — Pragma Space and Candidate Generation
- R11 — Research Program and Study Portfolio
- R12 — Cross-Layer Study Matrix

Retired stubs (R01, R02, R04, R08) are in `archive/reports_retired/`; per-version release notes (R10, R13, R14) are in
`archive/release_notes/`; the V19 research master formerly embedded in R07 is in `archive/V19/`.

## AI Control Layer
The AI_CONTROL directory governs agents, tools, plugins, skills, permissions,
evidence, change control, no-guessing, stop conditions, and escalation.

## Core execution path
P0 → P1 → P2 → P3 → P4 → P5 → P6 → P7 → P15

## Evidence rule
No experimental claim may be reported as measured unless a valid execution artifact
and provenance chain exist.

## State rule
`RESEARCH_STATE.yaml` is the project-level execution state. Study workspaces are isolated.

## Strict Sequential Phase Execution

This project is NOT intended to be implemented as one monolithic AI task.

The AI must implement exactly one active Phase, validate it, generate its required
evidence/plots/report, and stop at the Phase Gate.

Progression is:

`Phase N → implementation → validation → Gate review → explicit human approval → Phase N+1`

The AI cannot approve its own Gate and cannot automatically advance.

Future phases may be specified and planned, but their executable implementation and
experiments are blocked until the preceding Gate is approved.

## Pragma Space and Candidate Generation

The framework separates user-defined pragma-space constraints from automatically generated concrete candidates. Candidate generation is versioned and provenance-tracked; automatic generation does not silently expand the declared search space.

## External Baseline Reproduction
S71 is a controlled external-baseline study. It does not replace the core local-vs-joint evidence-selection question. It provides a reproducible bridge to prior HLS-DSE methods and prevents unsupported cross-paper numerical comparisons.


## Research Program and Study Portfolio

The project is a gated research program, not a pre-committed paper contribution. Independent Studies test multi-benchmark interaction, lifecycle/configuration/programming cost, search algorithms, evidence selection, physical effects, power/energy, CPU–FPGA/DMA, DFX/PR, and advanced learning. Study results are classified as CORE, SUPPORTING, EXTENSION, DROP, or NEGATIVE_RESULT only after measured evidence. See `REPORTS/R11_RESEARCH_PROGRAM_AND_STUDY_PORTFOLIO.md`.

### Search Algorithm Study

`S72` evaluates Exhaustive-when-feasible, Random, Bayesian Optimization, and Evolutionary Search under controlled conditions. It separately measures search overhead, HLS/SYN/P&R/bitstream cost, FPGA programming/configuration, initialization, execution, total wall-clock time, and decision quality.


## Fixed CPU–FPGA–Shared-Cache Architecture

The default experimental architecture is: CPU-owned FPGA programming/configuration and invocation; FPGA input data supplied through the shared-cache path. DMA, DDR bypass, cache level, coherence, and result-return mechanisms are not assumed unless explicitly declared and measured.

See `contracts/SYSTEM_ARCHITECTURE_CONTRACT.yaml` and `REPORTS/R12_CROSS_LAYER_STUDY_MATRIX.md`.

## Expanded Independent Studies

S73–S96 are registered as independent research questions. They are gated, isolated, and not automatically part of the final paper.

S97–S100 (added 2026-09-25 from the web-search literature update) sharpen the core question: S97 tests the
compositional (local-Pareto-first) assumption against an oracle, S98 measures the joint-minus-local interaction
residual across fidelities and is the go/no-go for S99, S99 is the decision-centric multi-source acquisition of
local vs joint evidence, and S100 measures runtime memory interference (blocked until a board exists).

## Fixed Reference Device and Artifact Isolation — V23.2

The current reference device is fixed to `xc7z020clg484`.

Every Vivado/Vitis experiment is isolated by `STUDY_ID/RUN_ID`. Hardware and software artifacts are provenance-controlled. The canonical contracts are:

- `contracts/HARDWARE_PLATFORM_CONTRACT.yaml` (reference device, platform and toolchain identity)
- `contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`

The required run workspace is:

```text
runs/<STUDY_ID>/<RUN_ID>/
├── manifest.yaml
├── config/
├── vivado/
│   ├── project/
│   ├── design/
│   ├── exports/
│   ├── reports/{synthesis,implementation,timing,utilization,power}/
│   └── logs/
├── vitis/
│   ├── platform/
│   ├── domain/
│   ├── application/
│   ├── build/
│   ├── binaries/{elf,boot}/
│   ├── reports/
│   └── logs/
├── bitstreams/
├── measurements/
├── raw/
├── normalized/
├── logs/
└── report/
```

A completed Run is immutable. Shared artifacts are read-only and must be referenced by identity and SHA-256 rather than copied into mutable Study workspaces.

## V23.1 Pre-Implementation Hardening

Before implementation, the following contracts are mandatory and validated by `scripts/validate_project.py`:

- `SEARCH_ALGORITHM_CONTRACT.yaml`
- `MEASUREMENT_CONTRACT.yaml`
- `SYSTEM_ARCHITECTURE_CONTRACT.yaml` (includes the memory-path rules)
- `CONCURRENCY_FAIRNESS_CONTRACT.yaml`
- `REPRODUCTION_CONTRACT.yaml`
- `DATA_LEAKAGE_CONTRACT.yaml`
- `CACHE_CONTRACT.yaml`
- `FAILURE_AND_RETRY_CONTRACT.yaml`
- `EXTERNAL_BASELINE_CONTRACT.yaml`
- `P1_IMPLEMENTATION_CONTRACT.yaml`

P1 begins with environment/project preflight and a single end-to-end smoke benchmark. No large DSE campaign is permitted before the smoke flow passes and the P1 Gate is reviewed.


## V23.2 Staged Evaluation and Metric Provenance

The reference execution path remains the full HLS → synthesis → implementation → bitstream → programming → runtime flow. V23.2 adds a controlled staged-evaluation policy: a candidate may stop before an expensive later stage when explicit evidence satisfies a recorded decision rule. Estimates and predictions may guide which candidate or stage is evaluated next, but they are never reported as measured values.

Every reported numeric metric must carry machine-traceable provenance to its Run, Candidate, benchmark, device, tool, tool version, source artifact, artifact SHA-256, and source field or measurement. Stage decisions are immutable records with explicit reason codes and evidence IDs.

See `contracts/STAGED_EVALUATION_CONTRACT.yaml`, `contracts/STAGE_DECISION_CONTRACT.yaml`, and `contracts/METRIC_PROVENANCE_CONTRACT.yaml`.
