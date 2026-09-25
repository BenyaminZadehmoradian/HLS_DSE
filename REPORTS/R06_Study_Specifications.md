---
report_metadata:
  report_id: "R06_Study_Specifications"
  report_type: "STUDY"
  title: "R06_Study_Specifications"
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

# R06 — Study Specifications & Execution Registry

This report is the canonical index for S00–S70. Each Study must have a self-contained contract, isolated workspace, explicit inputs/outputs, evidence requirements, stop conditions, and a generated report. The canonical no-loss Study registry is reproduced below.

# 19. Canonical Study Registry — No-Loss Mapping

| Study | Canonical role | Status |
|---|---|---|
| S00 | Project contract | CORE |
| S01 | Flow validation / single-benchmark foundation | CORE |
| S02 | Multi-benchmark / interaction pilot depending on historical definition | VALIDATION |
| S03 | Decision relevance / transfer depending on historical definition | VALIDATION |
| S04 | Oracle / multi-fidelity benchmark depending on historical definition | CORE |
| S05 | Evidence selection / physical feasibility depending on historical definition | CORE + EXTENSION |
| S06 | Budget scaling / lifecycle-aware selection | VALIDATION + EXTENSION |
| S07 | Joint task-candidate-fidelity selection | CORE |
| S08 | Full framework | FINAL CORE |
| S09 | Historical/legacy allocation; no new execution (ID collision; former meaning "Learning efficiency"; external-baseline role moved to S71) | ARCHIVED |
| S10 | Shared vs per-benchmark model | EXTENSION |
| S11 | Cross-benchmark transfer | EXTENSION |
| S12 | Online learning | EXTENSION |
| S13 | Uncertainty-aware scheduling | EXTENSION |
| S14 | Feasibility learning | VALIDATION |
| S15 | Joint concurrent HLS DSE | CORE |
| S16 | Decision-change prediction | CORE |
| S17 | No-joint certificate / CPU-FPGA historical variants | EXTENSION / ARCHIVED |
| S18 | Budget allocation / DMA historical variants | EXTENSION |
| S19 | Evidence portfolio / power-energy historical variants | EXTENSION |
| S20 | Cost-aware evidence selection / carbon historical variants | CORE + EXTENSION |
| S21 | Adaptive fidelity / no-joint historical variants | EXTENSION |
| S22 | Minimum joint evidence | EXTENSION |
| S23 | Adaptive fidelity ladder | EXTENSION |
| S24 | Large workload scaling | EXTENSION |
| S25 | Distributed execution | EXTENSION |
| S26 | Provenance/storage | INFRASTRUCTURE EXTENSION |
| S27 | Advanced controller comparison | FUTURE |
| S32 | Adaptive evaluation stopping | EXTENSION |
| S33 | Stage-wise VOI | EXTENSION |
| S34 | Dominance-based early termination | EXTENSION |
| S35 | Error-budgeted evaluation | EXTENSION |
| S36 | Sparse interaction discovery | VALIDATION |
| S37 | Interaction screening | VALIDATION |
| S38 | Higher-order interaction discovery | ADVANCED |
| S39 | Interaction-order selection | ADVANCED |
| S40 | Counterfactual interaction analysis | VALIDATION |
| S41 | Interaction decomposition | VALIDATION |
| S42 | Interaction fingerprinting | ADVANCED |
| S43 | Pareto frontier stability | VALIDATION |
| S44 | Pareto rank stability | EXTENSION |
| S45 | Decision stability | VALIDATION |
| S46 | Pareto frontier uncertainty | EXTENSION |
| S47 | Frontier coverage | VALIDATION |
| S48 | Asynchronous evidence scheduling | EXTENSION |
| S49 | Straggler-aware DSE | EXTENSION |
| S50 | Portfolio scheduling | EXTENSION |
| S51 | Robust DSE | EXTENSION |
| S52 | QoR variability | EXTENSION |
| S53 | Replication-aware DSE | EXTENSION |
| S54 | Risk-aware Pareto | EXTENSION |
| S55 | Directive sensitivity map | ADVANCED |
| S56 | Directive interaction modeling | ADVANCED |
| S57 | Dynamic search-space reduction | ADVANCED |
| S58 | Region-level DSE | ADVANCED |
| S59 | Pre-P&R physical interaction prediction | EXTENSION / ARCHIVED |
| S60 | Routing-risk prediction | EXTENSION |
| S61 | Physical feasibility boundary learning | EXTENSION |
| S62 | Bottleneck switching | VALIDATION |
| S63 | Bottleneck transition modeling | EXTENSION |
| S64 | Resource opportunity cost | EXTENSION |
| S65 | Joint candidate selection | CORE |
| S66 | Joint Pareto composition failure | CORE |
| S67 | Minimum joint evidence | EXTENSION |
| S68 | Interaction-driven benchmark grouping | EXTENSION |
| S69 | Meta-DSE | FUTURE |
| S70 | Study selection / meta-study | FUTURE |

> **Registry rule:** A Study ID is immutable. If its historical meaning changed across
> revisions, the historical definition remains in the archive and the canonical table
> records the current execution role. No historical Study is silently overwritten.

---



## Study workspace contract
Each Study owns `config/`, `inputs/`, `runs/`, `logs/`, `outputs/`, `artifacts/`, `scanner/`, and `report.md`. Cross-study writes are forbidden unless explicitly authorized by the project contract.
