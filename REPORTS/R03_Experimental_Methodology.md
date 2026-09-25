---
report_metadata:
  report_id: "R03_Experimental_Methodology"
  report_type: "STUDY"
  title: "R03_Experimental_Methodology"
  project: "HLS-DSE"
  project_version: "V22.8"
  phase_id: ""
  study_id: ""
  gate_id: ""
  status: "DRAFT"
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
  supersedes_report_id: ""
provenance:
  source_studies: [""]
  source_runs: []
  source_evidence: []
  source_artifacts: []
  source_data_versions: []
  source_scripts: []
  source_plot_scripts: []
reproducibility:
  environment_id: ""
  tool_versions: []
  hardware: []
  random_seeds: []
  commands_or_entrypoints: []
  reproducibility_status: "NOT_CHECKED"
validation:
  validation_status: "NOT_RUN"
  validation_tests: []
  acceptance_criteria: []
  failed_criteria: []
  known_limitations: []
classification:
  evidence_level: "MIXED"
  publication_ready: false
---

# R03 — Experimental Methodology

## Purpose
Defines how experiments are measured, compared, validated, falsified, and reported.
It separates measured evidence, derived evidence, prediction, assumptions, and unknowns.

## Canonical methodology path
Interaction → decision relevance → oracle → evidence selection → budget scaling → robustness.

# 6. Phase 3 — Concurrent / Joint Interaction Characterization

### Goal
Determine whether separately evaluated components can be composed safely, and quantify
where joint evaluation produces evidence that local evaluation cannot provide.

### Core concepts
```text
local evidence
joint evidence
composition model
interaction residual
logical interaction
physical interaction
decision-changing joint evaluation
```

### Core Studies
- S15 — Joint Concurrent HLS DSE
- S16 — Decision-Change Prediction
- S36 — Sparse Interaction Discovery
- S37 — Interaction Screening
- S40 — Counterfactual Interaction Analysis
- S41 — Interaction Decomposition
- S42 — Interaction Fingerprinting
- S65 — Joint Candidate Selection
- S66 — Joint Pareto Composition Failure
- S68 — Interaction-Driven Benchmark Grouping

### Advanced interaction studies
- S38 — Higher-Order Interaction Discovery
- S39 — Interaction Order Selection

### Gate
The project should not assume interaction is important. It must be measured and shown
to affect decisions or frontier quality before interaction-aware scheduling becomes a core claim.

---

# 7. Phase 4 — Decision Relevance & Pareto Stability

### Goal
Move from prediction accuracy to decision impact.

### Main measurements
```text
Hypervolume
Pareto regret/loss
Frontier coverage
Decision change
Decision stability
Pareto rank stability
Frontier uncertainty
```

### Studies
- S16 — Decision-Change Prediction
- S43 — Pareto Frontier Stability
- S44 — Pareto Rank Stability
- S45 — Decision Stability
- S46 — Pareto Frontier Uncertainty
- S47 — Frontier Coverage Instead of Prediction Accuracy

### Supporting concepts
A model can improve prediction while failing to change the selected design.
Therefore decision-level metrics are required alongside QoR prediction metrics.

### Gate
Joint evidence must demonstrate measurable decision relevance, not merely lower prediction error.

---

# 8. Phase 5 — Oracle / Reference Evaluation

### Goal
Create a controlled small design space in which an exhaustive or sufficiently complete
reference can be established.

### Main outputs
```text
reference Pareto frontier
reference feasibility
reference hypervolume
decision-loss ground truth
candidate ranking/reference
```

### Study
- S04 — Oracle Benchmark

### Gate
Only benchmarks for which the reference can be defended should be used for exact
oracle-based claims. Large non-exhaustive spaces must not be presented as ground truth.

---

# 9. Phase 6 — Evidence Selection & Joint Scheduling

### Goal
Select between local, joint, and different-fidelity evaluations according to expected
decision value and evaluation cost.

### Canonical action
```text
action = (scope, configuration, fidelity)

scope ∈ {local, joint}
fidelity ∈ {HLS, synthesis, implementation, ...}
```

### Core studies
- S05 — Evidence Selection
- S07 — Joint Task + Candidate + Fidelity Selection
- S08 — Full Framework

### Supporting/advanced studies
- S13 — Uncertainty-Aware Scheduling
- S18 — Budget Allocation
- S19 — Evidence Portfolio
- S20 — Cost-Aware Evidence Selection
- S48 — Asynchronous Evidence Scheduling
- S49 — Straggler-Aware DSE
- S50 — Portfolio Scheduling
- S27 — Advanced Controller Comparison

### Core decision principle
```text
expected decision improvement / evaluation cost
```

### Gate
The proposed scheduler is admitted to the main framework only after S03–S05 establish
that the selected evidence can change decisions and that its cost is justified.

---

# 11. Phase 8 — Multi-Benchmark, Shared Learning & Transfer

### Goal
Test whether knowledge learned on one benchmark transfers to another without data
leakage and whether shared models are preferable to per-benchmark models under
controlled conditions.

### Studies
- S02 — Multi-Benchmark Independent
- S03 — Cross-Benchmark Transfer
- S10 — Per-Benchmark vs Shared Model
- S11 — Cross-Benchmark Transfer
- S12 — Online Learning
- S09 — Model Learning Efficiency

### Required controls
```text
knowledge scope
train scope
validation scope
test scope
shared vs per-benchmark model
transfer on/off
```

### Gate
Transfer claims require explicit held-out benchmarks and leakage-safe evaluation.

---

# 12. Phase 9 — Physical Interaction & Feasibility

### Goal
Separate logical interaction from physical interaction and measure the effects introduced
by placement, routing, timing, congestion, and physical feasibility.

### Studies
- S05 — Physical Feasibility
- S14 — Feasibility Learning
- S59 — Pre-P&R Physical Interaction Prediction
- S60 — Routing-Risk Prediction
- S61 — Physical Feasibility Boundary Learning

### Historical status
S59 was previously marked for removal in one historical revision; it is **preserved here**
because the complete-master policy is no-loss. Its current status is EXTENSION/ARCHIVED
until the physical evidence justifies promotion.

### Gate
Do not conflate logical resource interaction with post-place/post-route interaction.

---


## Methodology source of truth
For detailed historical methodological definitions and earlier alternatives, see:
`R08_Historical_Archive.md` and the V17 source embedded there.
Current methodology must follow the active Study contract and experiment configuration.

## Execution-Time and FPGA Programming Accounting

Every benchmark/design evaluation must distinguish the time required to construct the
design from the time required to configure and execute it.

Required stages:

| Stage | Field |
|---|---|
| HLS | `t_hls_s` |
| RTL synthesis | `t_synthesis_s` |
| Place & route / implementation | `t_pnr_s` |
| Bitstream generation | `t_bitstream_s` |
| FPGA programming/configuration | `t_program_s` |
| Initialization | `t_init_s` |
| Benchmark/kernel execution | `t_execution_s` |
| Declared end-to-end boundary | `t_total_s` |

Bitstream generation and FPGA programming are separate measurements.

The run also records `n_program`, `n_bitstream_build`, and `n_invocation`, because
evaluation count alone does not determine actual wall-clock cost.

For lifecycle-oriented Studies, the Study contract must explicitly define the accounting
boundary and equation. A generic form is:

`T_lifecycle = T_build + N_program * T_program + N_invocation * T_execution`

No timing value may be silently estimated. Missing instrumentation is recorded as
`UNKNOWN` or `NOT_MEASURED`.

The comparison of DSE strategies therefore reports both expensive-evaluation counts and
actual elapsed execution cost.

## Plot and Visualization Methodology

Each Study has an isolated plotting directory:

`plots/code/` — one plotting script per declared plot  
`plots/generated/` — generated figures  
`plots/manifests/` — data/script/provenance manifests

Plotting is a separate analysis stage. Experiment execution code must not contain
publication plotting logic.

Every Study contract declares its mandatory plots. A figure is accepted only when
its source data, script, Study, and data version are traceable.

The project distinguishes measured, derived, oracle/reference, and predicted data in
plot metadata. Predictions must never be presented as measurements.

The final paper figures must therefore be reproducible by rerunning the corresponding
Study-specific plotting script.
