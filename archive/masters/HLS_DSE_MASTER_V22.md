# HLS-DSE MASTER V22 — AI-Controlled Research Program

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
