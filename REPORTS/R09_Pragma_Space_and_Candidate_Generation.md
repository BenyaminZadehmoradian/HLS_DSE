---
report_metadata:
  report_id: "R09-PRAGMA-SPACE"
  report_type: "METHODOLOGY"
  title: "Pragma Space, Automatic Candidate Generation, and Candidate Provenance"
  project: "HLS-DSE"
  project_version: "V22.8"
  phase_id: "P2"
  status: "PLANNED"

authorship:
  generated_by_ai: true
  ai_model: "GPT-5.6 Luna"
  ai_role: "Research architecture / methodology"
  human_researcher:
  human_approval_required: true
  human_approval_status:

dates:
  created_date: "2026-09-25"
  last_updated: "2026-09-25"

versioning:
  report_version: "1.0"
  revision: 0

classification:
  evidence_level: "METHODOLOGY"
  publication_ready: false
---

# 1. Executive Summary

The project will support both user-defined pragma spaces and framework-generated concrete pragma configurations. The user/benchmark owner defines the legal search space; the DSE system generates and selects concrete candidates within that space.

# 2. Layer Separation

The project distinguishes:

`Pragma Space Definition → Candidate Generation → Candidate Evaluation → Evidence Selection`

Pragma-space definition answers what is allowed. Candidate generation answers which concrete configurations are proposed. Evidence selection answers which proposed configuration should receive local, joint, synthesis, implementation, or other evidence.

# 3. Scientific Boundary

Automatic pragma generation is not claimed as the primary novelty because prior HLS-DSE literature already studies automated directive insertion and selection. It is an infrastructure capability that enables the project's main investigation of evidence selection.

# 4. User-Defined Space

A benchmark may explicitly declare directive families, source locations, parameter ranges, legal combinations, and hard constraints. These declarations are versioned.

# 5. Framework-Generated Candidates

The framework may use exhaustive enumeration, random sampling, Bayesian optimization, evolutionary search, or rule-based generation. The generator, version, seed, and pragma-space version must be recorded.

# 6. No Silent Search-Space Expansion

A configuration outside the declared space is not silently accepted. It is recorded as an out-of-space candidate and requires an explicit space-version change before evaluation as a valid candidate.

# 7. Relation to Local/Joint Evidence

The same concrete candidate can be evaluated locally for workload A and, separately, jointly with workload B. Therefore candidate identity and evidence identity are separate objects.

# 8. Required Provenance

Every candidate must be traceable to source version, pragma-space version, generator, seed, configuration, legality status, and evaluation records.

# 9. Gate Implication

The implementation of this layer belongs to the appropriate active phase only. Future phases must not be implemented before their phase gate is approved.
