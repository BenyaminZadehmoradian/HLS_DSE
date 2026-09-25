# RW0069 — Constrained multi-fidelity Bayesian optimization with automatic stop condition

> **Relevance (2026-09-25 web-search update): HOLD** — Cost-aware constrained multi-fidelity BO where constraints may differ across sources, with a systematic stopping criterion. Primary Studies: S99 S32. Prior-art boundary: METHOD FOUNDATIONAL (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Zanjani Foumani, Zahra; Bostanabad, Ramin
- Year / venue: 2025 / arXiv 2503.01126
- DOI: none recorded · URL: https://arxiv.org/abs/2503.01126

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Minimize sampling cost in constrained BO using cheap low-fidelity sources while ensuring feasibility; lack of BO stopping criteria.

## 2. Method
Constrained cost-aware multi-fidelity BO (GP+ package) with automatic stop condition.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Multiple benchmark problems
- Hardware: NOT_APPLICABLE
- Metrics: Sampling cost; feasibility

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): framework validated on multiple benchmarks; publicly available.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S99 S32)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Abstract/highlights only. |
| measured interactions | NOT_APPLICABLE | Abstract/highlights only. |
| staged evaluation | PARTIAL | Abstract/highlights only. |
| adaptive evidence acquisition | YES | Abstract/highlights only. |
| cost/fidelity modeling | YES | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_APPLICABLE | Abstract/highlights only. |
| physical implementation in the loop | NOT_APPLICABLE | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_APPLICABLE | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_APPLICABLE | Abstract/highlights only. |

## 7. Possible overlap
METHOD FOUNDATIONAL (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
