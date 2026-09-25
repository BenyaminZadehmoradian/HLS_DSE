# S00 — P0 Research Contract & Reproducibility

## Objective
Validate that the repository has one canonical state, immutable Study IDs, isolated evidence, traceable reports, and no-guessing behavior.

## Entry criteria
- V23.2 state file exists
- canonical project contract exists
- no future phase is executable

## Required checks
1. Validate YAML/JSON schemas.
2. Verify S71 is the only external-baseline ID.
3. Verify S09 is archived and not executable.
4. Verify raw evidence paths are write-once.
5. Verify report provenance fields exist.
6. Run unit tests for candidate generation.

## Exit gate
All checks pass; no unresolved HIGH severity consistency defect.
