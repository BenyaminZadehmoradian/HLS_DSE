# S00 — P0 Research Contract and Reproducibility Validation

**Status:** IMPLEMENTABLE; not yet executed.

## Objective
Validate the V23.2 control plane before any scientific experiment.

## Acceptance criteria
- Canonical version is V23.2.
- P0 is the only active implementation phase.
- Study IDs are unique and S71 is the external-baseline study.
- S09 is archived and cannot execute.
- Core JSON/YAML schemas parse.
- Candidate generation unit test passes.
- No measured evidence exists before experimental execution.

## Required checks
1. Validate YAML/JSON schemas.
2. Verify S71 is the only external-baseline ID.
3. Verify S09 is archived and not executable.
4. Verify raw evidence paths are write-once.
5. Verify report provenance fields exist.
6. Run unit tests for candidate generation.

## Exit gate
All checks pass; no unresolved HIGH severity consistency defect.

## Evidence
No measured evidence exists yet.

## Gate decision
PENDING HUMAN REVIEW.
