# RW0068 — Constrained Bayesian Optimisation with Multiple Information Sources

> **Relevance (2026-09-25 web-search update): HOLD** — Multi-source extension of constrained max-value entropy search; balances evaluation cost and information gain when feasible regions are small. Primary Studies: S99 S14. Prior-art boundary: METHOD FOUNDATIONAL (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Maathuis, Hauke; De Breuker, Roeland; Castro, Saullo; Osborne, Maike
- Year / venue: 2026 / arXiv 2607.00865
- DOI: none recorded · URL: https://arxiv.org/abs/2607.00865

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Constrained BO with small feasible regions, where auxiliary cheaper sources could support early exploration.

## 2. Method
Multi-source constrained Max-value Entropy Search capturing inter-source correlation.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Synthetic and physics-based benchmarks
- Hardware: NOT_APPLICABLE
- Metrics: Feasible optimum found vs cost

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): efficiently identifies feasible and optimal solutions even with weakly correlated auxiliary data; outperforms existing methods, especially early.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S99 S14)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Abstract/highlights only. |
| measured interactions | NOT_APPLICABLE | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
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
