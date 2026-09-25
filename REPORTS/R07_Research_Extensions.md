---
report_metadata:
  report_id: "R07_Research_Extensions"
  report_type: "STUDY"
  title: "R07_Research_Extensions"
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

# R07 — Research Extensions

## Purpose
Preserved research directions beyond the minimum core. They are not silently promoted to the core
contribution until their evidence gates are passed.

# 10. Phase 7 — Budget, Cost & Fidelity Scaling

### Goal
Measure how much expensive evidence is needed and how performance changes as the
joint/implementation budget increases.

### Studies
- S06 — Budget Scaling
- S18 — Budget Allocation
- S20 — Cost-Aware Evidence Selection
- S21 — Adaptive Fidelity
- S22 — Minimum Joint Evidence
- S23 — Adaptive Fidelity Ladder
- S32 — Adaptive Evaluation Stopping
- S33 — Stage-Wise Value of Information
- S34 — Dominance-Based Early Termination
- S35 — Error-Budgeted Evaluation

### Important interpretation rule
No universal minimum number of joint evaluations is assumed. Any threshold is
benchmark-, device-, tool-, and objective-dependent unless experimentally demonstrated
otherwise.

### Gate
Budget scaling must show a measurable trade-off among expensive evaluations, cost,
frontier quality, and decision quality.

---

# 13. Phase 10 — Robustness, Variability & Risk

### Goal
Determine whether the framework remains useful under input variation, tool variation,
replication, and uncertain QoR.

### Studies
- S51 — Robust DSE
- S52 — QoR Variability Study
- S53 — Replication-Aware DSE
- S54 — Risk-Aware Pareto

### Gate
These remain extensions until the core scheduler has demonstrated value on deterministic
and reproducible conditions.

---

# 14. Phase 11 — Advanced Search & Learning

### Goal
Evaluate more sophisticated search, surrogate, interaction, and controller mechanisms
only after the simpler evidence-selection framework has been validated.

### Studies
- S55 — Directive Sensitivity Map
- S56 — Directive Interaction Modeling
- S57 — Dynamic Search-Space Reduction
- S58 — Region-Level DSE
- S69 — Meta-DSE
- S70 — Study Selection

### Advanced model families retained from the historical archive
```text
RF / XGBoost
GNN
Bayesian optimization / MOTPE
Multi-fidelity optimization
RL
Transformer / learned controller
LLM / agentic candidate generation
Meta-controller
```

### Rule
Model complexity is never treated as a contribution by itself. Each model must beat an
appropriate simpler baseline on decision quality, sample efficiency, evaluation cost,
or another pre-registered criterion.

---

# 15. Phase 12 — Lifecycle, Configuration, CPU–FPGA & DMA

### Goal
Extend static concurrent DSE toward runtime/lifecycle-aware system decisions.

### Studies / retained research
- S06 — Lifecycle-Aware Selection
- S17 — No-Joint-Evaluation Certificate
- S18 — DMA/data movement
- S17 — CPU–FPGA allocation
- DFX / Partial Reconfiguration
- configuration cost
- bitstream cost
- reconfiguration time
- CPU/FPGA partitioning
- overlap and scheduling
- lifetime-aware evaluation

### Historical implementation phases mapped here
- Phase 7 — Configuration
- Phase 9 — Lifecycle
- Phase P6 — bitstream/configuration/DFX
- Phase P7 — lifecycle/DMA/CPU-FPGA
- Phase P8 — hardware calibration

### Gate
This phase is separate from the static concurrent-placement core and must not silently
change the definition of the main research problem.

---

# 16. Phase 13 — Power, Energy & Sustainability

### Goal
Study energy/resource trade-offs and sustainability consequences of DSE decisions.

### Retained research topics
- power-aware DSE
- energy-aware DSE
- carbon-aware DSE
- energy/resource trade-offs
- configuration energy
- execution energy
- measurement vs analytical estimation
- sustainability metrics

### Current status
EXTENSION until a reproducible measurement protocol is frozen.

### Required evidence
```text
measurement method
measurement point
sampling rate
workload duration
replication
idle/baseline power
dynamic power
energy per task
energy per solution
```

---

# 17. Phase 14 — Large-Scale, Distributed & Meta-DSE

### Goal
Scale the validated framework after its scientific value has been demonstrated.

### Retained studies
- S24 — Large Workload Scaling
- S25 — Distributed Execution
- S26 — Provenance/Storage
- S27 — Advanced Controller Comparison
- S69 — Meta-DSE
- S70 — Study Selection

### Supporting infrastructure
```text
distributed execution
concurrency
locking
event sourcing
advanced provenance
large-scale storage
artifact management
checkpointing
```

### Gate
Infrastructure scaling must not precede scientific validation of the core method.

---

## Historical V19 research directions
The V19 research master that was embedded here (restored directions, deferred studies and the old §27
study map) is preserved verbatim in `archive/V19/HLS_DSE_V19_RESEARCH_MASTER.md`. Its study numbering
predates `contracts/STUDY_ID_REGISTRY.yaml`, which is authoritative.
