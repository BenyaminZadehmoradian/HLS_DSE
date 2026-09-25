# RW0085 — ASPO: Constraint-Aware Bayesian Optimization for FPGA-based Soft Processors

> **Relevance (2026-09-25 web-search update): HOLD** — Constraint-aware BO for FPGA soft processors that penalizes the acquisition by expected evaluation time and reuses synthesis checkpoints: cost-aware acquisition and evidence reuse in an FPGA flow. Primary Studies: S99 S87. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** PARTIAL (authors not retrieved).
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: NOT_RETRIEVED (see URL)
- Year / venue: 2025 / arXiv 2506.06817
- DOI: none recorded · URL: https://arxiv.org/abs/2506.06817

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Standard BO cannot handle constraints on categorical parameters; optimization time grows with processor complexity.

## 2. Method
Disjunctive-form constraints with a custom covariance kernel; evaluation-time-penalized acquisition; FPGA synthesis checkpoint reuse.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Seven RISC-V benchmarks on RocketChip, BOOM, EL2 VeeR
- Hardware: FPGA soft processors
- Metrics: Execution time; design time

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): up to 35% lower execution time (BOOM multiply) vs default; up to 74% lower design time vs Boomerang.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S99 S87)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | YES | Abstract/highlights only. |
| cost/fidelity modeling | YES | Abstract/highlights only. |
| lifecycle/configuration cost | PARTIAL | Abstract/highlights only. |
| physical implementation in the loop | PARTIAL | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
