# RW0080 — FADO: Floorplan-Aware Directive Optimization Based on Synthesis and Analytical Models for High-Level Synthesis Designs on Multi-Die FPGAs

> **Relevance (2026-09-25 web-search update): HOLD** — Journal extension of RW0037 FADO: FADO 2.0 replaces the synthesis-based per-function QoR library with a calibrated analytical QoR model. Primary Studies: S98 S59 S15. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** PARTIAL (DOI/title verified; authors not verified).
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Du, Linfeng; et al. (full author list to verify)
- Year / venue: 2024 / ACM TRETS
- DOI: 10.1145/3653458 · URL: https://doi.org/10.1145/3653458

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (author site; not downloaded)

## 1. Research question
Directive optimization on multi-die FPGAs ignores per-die resources and die-crossing timing; QoR library generation is slow.

## 2. Method
FADO 1.0 (synthesis-based library) and FADO 2.0 (analytical QoR model) incremental directive/floorplan co-search.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Mixed dataflow and non-dataflow designs
- Hardware: Multi-die FPGA (details NOT_REPORTED in highlights)
- Metrics: Design performance; runtime

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (highlights): FADO 2.0 is 2.66x better than analytical DSE with global floorplanning and 1.40x better than FADO 1.0 on average.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S98 S59 S15)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Abstract/highlights only. |
| measured interactions | PARTIAL | Abstract/highlights only. |
| staged evaluation | PARTIAL | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | YES | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | YES | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
