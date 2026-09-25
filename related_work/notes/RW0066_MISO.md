# RW0066 — Multi-Information Source Optimization

> **Relevance (2026-09-25 web-search update): HOLD** — Knowledge-gradient value-of-information acquisition across several information sources with different cost and unknown model discrepancy (bias). Mathematical template for choosing cheap-biased local vs expensive joint evidence. Primary Studies: S99 S05 S16 S33. Prior-art boundary: METHOD FOUNDATIONAL (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Poloczek, Matthias; Wang, Jialei; Frazier, Peter I.
- Year / venue: 2017 / NeurIPS 2017
- DOI: none recorded · URL: https://arxiv.org/abs/1603.00389

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Bayesian optimization when cheaper approximations with unknown, input-dependent bias are available.

## 2. Method
Model discrepancy between sources modelled explicitly; acquisition extends the Knowledge Gradient to multiple sources: each sample maximizes predicted benefit per unit cost.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Synthetic + RL / engineering / science benchmarks (details NOT_REPORTED in abstract)
- Hardware: NOT_APPLICABLE
- Metrics: Objective value found vs exploration cost

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): consistently outperforms other state-of-the-art techniques, finding better designs at lower exploration cost.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S99 S05 S16 S33)

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
