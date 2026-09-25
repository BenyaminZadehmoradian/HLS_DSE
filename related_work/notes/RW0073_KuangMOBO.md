# RW0073 — Multi-objective Design Space Exploration for High-Level Synthesis via Bayesian Optimization

> **Relevance (2026-09-25 web-search update): HOLD** — MOTPE + EHVI BO for HLS PPA compared with SA and NSGA-II by ADRS; companion of RW0022 HGBO-DSE. Primary Studies: S72. Prior-art boundary: PRIOR ART (candidate) for S72.
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Kuang, Huizhen; Wang, Lingli
- Year / venue: 2023 / ISEDA 2023
- DOI: 10.1109/ISEDA59274.2023.10218665 · URL: https://doi.org/10.1109/iseda59274.2023.10218665

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Multi-objective HLS DSE over PPA.

## 2. Method
Multi-objective Tree-structured Parzen Estimator surrogate + Expected Hypervolume Improvement.

## 3. Benchmarks / hardware / metrics
- Benchmarks: NOT_REPORTED in abstract
- Hardware: NOT_REPORTED
- Metrics: LPDA gain; ADRS

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): LPDA gains 66.30% / 41.25% vs SA / NSGA-II; ADRS improvement 94.72% / 69.58%.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | YES | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | PARTIAL | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PRIOR ART (candidate) for S72

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
