# AI NO-GUESSING POLICY
Categories must remain distinct:
- MEASURED: directly produced by an authorized experiment/tool.
- DERIVED: deterministically computed from measured evidence.
- PREDICTED: produced by a surrogate/ML model.
- ESTIMATED: heuristic or approximate calculation.
- ASSUMED: explicit experimental assumption.
- UNKNOWN: unavailable or unverifiable.

`UNKNOWN != ESTIMATED`, `ESTIMATED != MEASURED`, `PREDICTED != MEASURED`.

A missing Vivado/HLS result must never be replaced by an AI estimate in an experimental table.
