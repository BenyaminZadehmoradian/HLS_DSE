# RW0070 — Fovea: Physical-Implication-Aware Wafer-Scale DSE with Decision-Domain-Guided Cross-Fidelity Refinement

> **Relevance (2026-09-25 web-search update): HOLD** — Decision-domain-guided cross-fidelity refinement: expensive reference evaluation only for candidates that may remain reference-optimal given measured analytical-vs-reference disagreement. Decision-centric evidence acquisition in hardware DSE (wafer-scale, not HLS). Primary Studies: S99 S16 S97. Prior-art boundary: PARTIAL OVERLAP (candidate; different domain).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Li, Jinxi; Wang, Huizheng; Deng, Jinyi; Hu, Yang; Yin, Shouyi
- Year / venue: 2026 / arXiv 2608.03285
- DOI: none recorded · URL: https://arxiv.org/abs/2608.03285

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Detailed evaluation too expensive for the whole wafer-scale architecture space; analytical-to-reference ranking inversions make a fixed shortlist unreliable.

## 2. Method
Physical-implication-aware space formulation; paired in-domain calibration estimates analytical-to-reference disagreement, inducing a Decision Domain evaluated with the reference backend.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Ten reference-verifiable design spaces x seven LLM-training workloads
- Hardware: Wafer-scale systems (modelled)
- Metrics: Recovery of reference optimum; end-to-end speedup

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): with 10% paired calibration recovers the exhaustive reference optimum in all 70 pairs; 4.13x average, 7.80x max speedup.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S99 S16 S97)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | YES | Abstract/highlights only. |
| adaptive evidence acquisition | YES | Abstract/highlights only. |
| cost/fidelity modeling | YES | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | PARTIAL | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | PARTIAL | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate; different domain)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
