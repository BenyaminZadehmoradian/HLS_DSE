---
report_metadata:
  report_id: "R11-RESEARCH-PROGRAM-PORTFOLIO"
  report_type: "METHODOLOGY"
  title: "Research Program and Study Portfolio"
  project: "HLS-DSE"
  project_version: "V23.0"
  phase_id: ""
  study_id: ""
  gate_id: ""
  status: "PLANNED"
authorship:
  generated_by_ai: true
  ai_model: "GPT-5.6 Luna"
  ai_role: "Research documentation"
  human_researcher: ""
  human_approval_required: true
  human_approval_status: "PENDING"
dates:
  created_date: "2026-09-25"
  last_updated: "2026-09-25"
versioning:
  report_version: "1.0"
  revision: 0
provenance:
  source_studies: []
  source_runs: []
  source_evidence: []
  source_artifacts: []
  source_scripts: []
  source_plot_scripts: []
reproducibility:
  reproducibility_status: "NOT_RUN"
validation:
  validation_status: "NOT_RUN"
classification:
  evidence_level: "PLANNED"
  publication_ready: false
---

# R11 — Research Program and Study Portfolio

## 1. Purpose

This document defines the project as a **research program**, not as a single pre-committed paper contribution. Each scenario is tested as an independent Study. Only after measured evidence is available is a Study classified for the eventual paper.

The project therefore asks first **which effects are real, reproducible, decision-relevant, and sufficiently general**, and only then decides which effects belong in the main paper.

## 2. Core Research Program

The program investigates several potentially interacting dimensions of HLS-based FPGA DSE:

1. Multi-benchmark / concurrent design decisions.
2. Local versus joint evaluation and interaction.
3. Lifecycle/build/configuration/programming cost.
4. Search-algorithm choice and search overhead.
5. Selective evidence acquisition under expensive evaluation budgets.
6. Physical feasibility and post-P&R interaction.
7. Power/energy and sustainability trade-offs.
8. CPU–FPGA and DMA costs where relevant.
9. Partial reconfiguration / DFX and lifecycle extensions where relevant.
10. Transfer, learning, advanced search, and meta-DSE as optional extensions.

None of these is assumed to be a final contribution before its Study is evaluated.

## 3. Study-to-Paper Decision Pipeline

```text
Research Question
      ↓
Hypothesis
      ↓
Independent Study
      ↓
Measured Evidence
      ↓
Effect present?
   ┌──┴─────────────┐
   │                │
  NO               YES
   │                │
 DROP        Decision impact?
                  ┌┴───────────┐
                  │             │
                 NO            YES
                  │             │
             SUPPORTING     Cross-study validation
                                │
                         ┌──────┴──────┐
                         │             │
                       CORE       EXTENSION
```

Allowed final classifications:

- `CORE` — direct contribution to the main paper;
- `SUPPORTING` — evidence supporting another contribution;
- `EXTENSION` — scientifically useful but not required for the main paper;
- `DROP` — insufficient effect, decision impact, generality, or cost-effectiveness;
- `NEGATIVE_RESULT` — measured result that rules out a proposed direction.

## 4. Candidate Study Portfolio

### A. Infrastructure and local evidence

- S00 — Project Contract
- S01 — Flow Smoke Test
- S02 — Interaction Pilot
- S03 — Decision Relevance
- S04 — Oracle Benchmark

### B. Evidence selection and budget

- S05 — Evidence Selection
- S06 — Budget Scaling
- S07 — Joint Task/Candidate/Fidelity Selection
- S08 — Full Framework
- S16 — Decision-Change Prediction
- S22 — Minimum Joint Evidence
- S23 — Adaptive Fidelity Ladder
- S32–S35 — Stopping, VOI, Early Termination, Error Budget

### C. Multi-benchmark and interaction

- S15 — Joint Concurrent HLS DSE
- S36–S42 — Interaction Discovery, Screening, Higher-Order Interaction, Decomposition, Fingerprinting
- S65–S68 — Joint Candidate Selection, Composition Failure, Benchmark Grouping

### D. Pareto and decision stability

- S43 — Pareto Frontier Stability
- S44 — Pareto Rank Stability
- S45 — Decision Stability
- S46 — Frontier Uncertainty
- S47 — Frontier Coverage

### E. Lifecycle / configuration / programming cost

This family is explicitly retained as an experimental branch. It is not assumed to be part of the final contribution.

Questions include:

- Does programming/configuration time materially affect DSE decisions?
- Does minimizing the number of FPGA programming/configuration events create useful QoR/lifecycle trade-offs?
- Does multi-benchmark deployment change the preferred configuration when lifecycle cost is included?
- Does build time dominate or become negligible relative to programming/execution in realistic scenarios?

Relevant existing studies include S12, S17, S18 and S06; these must be interpreted through their actual contracts rather than assumed to answer the new questions completely.

### F. Search algorithm and end-to-end cost

- **S72 — Search Algorithm and End-to-End Cost Comparison**

S72 explicitly compares search strategy, search overhead, expensive evaluation count, programming/configuration events, execution cost, and final decision quality.

Initial controlled algorithms:

- Exhaustive when feasible;
- Random Search;
- Bayesian Optimization;
- Evolutionary Search.

Optional algorithms such as RL/ML/GNN/LLM-guided search are deferred until the controlled baseline study justifies them.

### G. Physical implementation

- S59–S61 — Physical interaction, routing, feasibility
- S62–S64 — Bottleneck and opportunity-cost analyses

### H. Robustness and risk

- S51–S54 — Robustness, variability, uncertainty, risk
- S09 — Historical/legacy allocation; no new execution
- S71 — External baseline reproduction and cross-paper comparison

### I. Power, energy, sustainability

- S19 — Power/Energy vs Resource
- S20 — Energy/Cost/Carbon
- Additional sustainability trade-off Studies may be created only with immutable new IDs.

### J. CPU–FPGA, DMA, DFX/lifecycle

- S12 — Lifecycle time
- S13 — CPU–FPGA trade-off
- S14 — DMA transfer time
- S17/S18 — certificate/budget-DMA branches
- DFX/PR and lifecycle extensions remain conditional Studies, not guaranteed paper contributions.

### K. Advanced learning and search

- S55–S58 — Directive sensitivity, search-space and region studies
- S69 — Meta-DSE
- S70 — Study selection / meta-study
- Transfer learning, GNN, RL, LLM/agentic search, and multi-fidelity remain extension branches unless earlier evidence establishes a concrete need.

## 5. Common Evaluation Dimensions

Every Study that compares methods should distinguish at least:

### Search computation
\[
T_{search}
\]

### Expensive design evaluation
\[
T_{eval}=T_{HLS}+T_{SYN}+T_{PNR}+T_{BITSTREAM}
\]

### FPGA configuration/programming
\[
N_{program}T_{program}
\]

### Runtime execution
\[
N_{exec}T_{exec}
\]

### End-to-end cost
\[
T_{total}=T_{search}+T_{HLS}+T_{SYN}+T_{PNR}+T_{BITSTREAM}+T_{PROGRAM}+T_{INIT}+T_{EXEC}
\]

The exact applicable terms depend on the Study contract, but omitted terms must be explicitly marked rather than silently ignored.

## 6. Search Algorithm Is an Experimental Variable

The project must not treat the search algorithm as an invisible implementation detail. Different algorithms may generate different candidate sequences, use different numbers of evaluations, incur different search overhead, and reach different quality levels at different times.

Therefore, when S72 is active, the primary comparison is not simply:

> Which algorithm finds the best configuration?

It is:

> How does each algorithm trade off search overhead, expensive evaluation budget, lifecycle/configuration cost, and decision quality?

Required views include:

- quality vs total wall-clock time;
- hypervolume vs elapsed time;
- hypervolume vs evaluation budget;
- search overhead vs evaluation cost;
- evaluation count vs total time;
- programming time vs number of configurations;
- lifecycle time breakdown;
- time-to-target quality.

## 7. Paper Selection Rule

The final paper contribution must be derived from Study evidence. The project must not force every implemented Study into the paper.

A Study becomes a candidate for `CORE` only when:

1. its measurements are reproducible;
2. its comparison is controlled;
3. the observed effect is larger than relevant measurement variability;
4. the effect changes a meaningful DSE decision or provides a necessary explanation;
5. the result survives cross-benchmark or sensitivity validation where applicable;
6. the added experimental cost is justified by the scientific conclusion.

## 8. Negative Results Are Preserved

A Study that finds no meaningful effect is not deleted. Its report, runs, logs, evidence, and plots remain part of the archive and can justify why a branch was not included in the final paper.

## 9. Relationship to Phase Gates

The Research Program is a portfolio, but execution remains strictly sequential:

`one active Phase → implementation → validation → Gate Review → human approval → next Phase`

A Study may be planned in this portfolio before its Phase is active, but executable implementation and experiments remain blocked until the Phase Gate policy authorizes them.

## 10. Current Status

The current phase, study and gate state are recorded only in `RESEARCH_STATE.yaml`. S72 is registered as `PLANNED`; its implementation is not authorized merely by adding it to the portfolio.

## 11. Fixed System Architecture for CPU–FPGA Studies

The default hardware/software architecture is now explicitly constrained:

```text
CPU --(program/configure/invoke)--> FPGA
                                      ^
                                      |
                               shared cache data
```

The CPU owns FPGA programming/configuration. FPGA input data is supplied through the shared-cache path. DMA, DDR bypass, cache hierarchy, coherence, and result-return mechanisms are not assumed and must be declared/measured. See `contracts/SYSTEM_ARCHITECTURE_CONTRACT.yaml` and `REPORTS/R12_CROSS_LAYER_STUDY_MATRIX.md`.

## 12. Expanded Independent Study Portfolio

The following Studies are registered as independent questions. They are not automatically part of the final paper:

| ID | Question | Initial classification |
|---|---|---|
| S73 | Memory-system and data-movement cost | candidate |
| S74 | Input/workload sensitivity | candidate |
| S75 | Search-space sensitivity | candidate |
| S76 | Hierarchical DSE | candidate |
| S77 | Frequency-constrained DSE | candidate |
| S78 | HLS × physical co-DSE | candidate |
| S79 | Multi-die / SLR-aware DSE | supporting candidate |
| S80 | Toolchain robustness | supporting candidate |
| S81 | Implementation variability | candidate |
| S82 | Accuracy-aware DSE | extension |
| S83 | End-to-end system latency | candidate |
| S84 | CPU–FPGA overlap | candidate |
| S85 | Configuration-strategy DSE | candidate |
| S86 | Bitstream/configuration-size cost | supporting candidate |
| S87 | Evidence reuse/cache value | candidate |
| S88 | Early stopping / staged evaluation | candidate |
| S89 | Constraint-vs-QoR prediction | supporting candidate |
| S90 | Workload taxonomy/generalization | candidate |
| S91 | Cross-device generalization | candidate |
| S92 | Objective/utility sensitivity | candidate |
| S93 | Invocation-distribution-aware DSE | candidate |
| S94 | Lifecycle-robust DSE | candidate |
| S95 | Resource fragmentation / spatial packing | supporting candidate |
| S96 | Sustained execution / thermal behavior | extension |
| S97 | Compositional-assumption test (oracle) | core candidate |
| S98 | Cross-fidelity interaction residual (go/no-go for S99) | core candidate |
| S99 | Decision-centric multi-source acquisition of local vs joint evidence | core candidate |
| S100 | Runtime memory-interference residual on Zynq-7020 (needs a board) | candidate (blocked) |

All IDs are immutable once registered. A Study may be dropped without deleting its contract or evidence history.
