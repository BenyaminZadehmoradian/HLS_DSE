---
report_metadata:
  report_id: "R05_Related_Work"
  report_type: "STUDY"
  title: "R05_Related_Work"
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

# R05 — Related Work & Literature Evidence

## Purpose
A controlled literature record for the HLS-DSE project.

## Important status rule
The initial registry contains candidate related work identified during project development.
PDF, code, dataset, artifact, and reading statuses are intentionally not assumed to be verified.
They must be populated by evidence collection.

## PDF naming standard
`RW<4-digit>_<FirstAuthor><Year>_<ShortKey>_<Venue>.pdf`

Example:
`RW0001_Cryptonite2025_Cryptonite_ASAP.pdf`

## Evidence statuses
PDF: missing / collected / verified
Code: none_found / paper_code / official_repo / third_party_repo / partial / unknown / not_checked
Dataset/artifacts: none_found / official / supplementary / third_party / partial / unknown / not_checked
Reading: not_started / screened / read / deep_reviewed / reproduced

## Registry
See `../related_work/RELATED_WORK_REGISTRY.csv`.

## Per-paper evidence
Each paper should have a note under `related_work/notes/` containing bibliographic identity,
PDF provenance, code provenance, dataset/artifact provenance, benchmark, device/tool,
method, results, relation to our work, and reproduction status.

## No-guessing rule
If code, PDF, dataset, or artifact cannot be verified, mark it as unknown/not_checked rather
than inferring availability from memory or search snippets.
