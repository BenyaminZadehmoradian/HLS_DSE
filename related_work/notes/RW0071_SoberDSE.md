# RW0071 — SoberDSE: Sample-Efficient Design Space Exploration via Learning-Based Algorithm Selection

> **Relevance (2026-09-25 web-search update): HOLD** — Extensive HLS DSE study: no single DSE algorithm is Pareto-dominant across benchmarks; learned per-benchmark algorithm selection. Directly bounds the S72 question. Primary Studies: S72. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Xu, Lei; Wang, Shanshan; Xiao, Chenglong
- Year / venue: 2026 / arXiv 2603.00986
- DOI: none recorded · URL: https://arxiv.org/abs/2603.00986

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
No HLS DSE algorithm consistently dominates across problem instances.

## 2. Method
Learning-based recommendation of the DSE algorithm from benchmark characteristics.

## 3. Benchmarks / hardware / metrics
- Benchmarks: HLS DSE benchmarks (details NOT_REPORTED in abstract)
- Hardware: NOT_REPORTED
- Metrics: Pareto quality; classification accuracy

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): up to 5.7x over heuristic and 4.2x over learning-based SOTA DSE; +35.57% accuracy in small-sample learning vs conventional classifiers.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | PARTIAL | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | PARTIAL | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
