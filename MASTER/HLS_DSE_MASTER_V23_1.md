# HLS-DSE MASTER V23.1 — AI-Controlled Research Program

## Status
Canonical project master and navigation document.

## Preservation rule
The complete V21 master is preserved unchanged under `archive/V21/`.
V22 adds a multi-report structure and an AI Research Control Layer. No historical study,
hypothesis, extension, implementation idea, or prior version is deleted.

## Canonical reports
- R01 — Research Master
- R02 — Research Program & Phases
- R03 — Experimental Methodology
- R04 — System & Software Architecture
- R05 — Related Work & Literature Evidence
- R06 — Study Specifications & Execution Registry
- R07 — Research Extensions
- R08 — Historical Archive

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

## Fixed Reference Device and Artifact Isolation — V23.1

The current reference device is fixed to `xc7z020clg484`.

Every Vivado/Vitis experiment is isolated by `STUDY_ID/RUN_ID`. Hardware and software artifacts are provenance-controlled. The canonical contracts are:

- `contracts/DEVICE_REFERENCE_CONTRACT.yaml`
- `contracts/HARDWARE_PLATFORM_CONTRACT.yaml`
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
- `MEMORY_PATH_CONTRACT.yaml`
- `CONCURRENCY_FAIRNESS_CONTRACT.yaml`
- `REPRODUCTION_CONTRACT.yaml`
- `DATA_LEAKAGE_CONTRACT.yaml`
- `CACHE_CONTRACT.yaml`
- `FAILURE_AND_RETRY_CONTRACT.yaml`
- `EXTERNAL_BASELINE_CONTRACT.yaml`
- `P1_IMPLEMENTATION_CONTRACT.yaml`

P1 begins with environment/project preflight and a single end-to-end smoke benchmark. No large DSE campaign is permitted before the smoke flow passes and the P1 Gate is reviewed.
