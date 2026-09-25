# Plotting — S21

Plotting is isolated from experiment execution.

- `code/`: study-specific plotting scripts
- `generated/`: generated figures
- `manifests/`: plot/data provenance manifests

Each plot script must read declared evidence/derived outputs and must not invent
or silently impute experimental values.
