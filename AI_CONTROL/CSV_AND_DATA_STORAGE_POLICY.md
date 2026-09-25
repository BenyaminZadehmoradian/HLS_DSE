# CSV and Experimental Data Storage Policy

## Decision

CSV remains supported, but it is **not the canonical source of truth** for the research project.

## Canonical evidence

The canonical evidence chain is:

`raw tool output → normalized evidence → derived metrics → analysis tables → plots → report`

Structured evidence should be stored in machine-readable formats that preserve nested configuration and provenance, such as JSON/JSONL (or an explicitly versioned database where appropriate). YAML is used for configuration and contracts.

## Role of CSV

CSV is a **flat analysis/export format**. It is recommended for:

- plotting datasets
- pandas/R/Matlab analysis
- simple benchmark-by-candidate tables
- sharing compact tabular results
- paper-ready numerical tables

CSV should be generated from canonical evidence rather than manually edited as the authoritative record.

## What should not rely on CSV alone

Do not use CSV as the only storage for:

- nested pragma configurations
- provenance
- tool logs
- per-stage timing provenance
- raw HLS/Vivado reports
- multiple evidence levels
- event histories
- error details

## Recommended representation

| Data | Canonical format | CSV export |
|---|---|---|
| Run metadata | JSON/JSONL | Yes, flattened |
| Pragma space | YAML | Optional |
| Candidate configuration | JSON | Yes, flattened |
| Raw tool output | Original logs/reports | No |
| Normalized measurements | JSON/JSONL | Yes |
| Derived metrics | JSON/JSONL | Yes |
| Plot input tables | CSV | Yes |
| Experiment events | JSONL | Optional |
| Final report | Markdown | No |

## Rule

There should be one authoritative evidence record. CSV is a reproducible view/export of that record, not a second database that can diverge from it.
