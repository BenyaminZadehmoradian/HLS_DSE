# RW0084 — Pipeline Stage Resolved Timing Characterization of FPGA and ASIC Implementations of a RISC V Processor

> **Relevance (2026-09-25 web-search update): HOLD** — Thirty-seed FPGA implementation study: routing-induced timing variability is non-Gaussian and heavy-tailed. Evidence for the P&R noise floor the S04/S98 oracles must replicate. Primary Studies: S81 S98 S04. Prior-art boundary: RELEVANT BUT DIFFERENT (candidate).
> **Identity:** PARTIAL (authors not retrieved).
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: NOT_RETRIEVED (see URL)
- Year / venue: 2025 / arXiv 2512.13866
- DOI: none recorded · URL: https://arxiv.org/abs/2512.13866

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Characterize timing variability of FPGA/ASIC implementations per pipeline stage.

## 2. Method
Implementations across thirty routing seeds; per-stage slack distributions.

## 3. Benchmarks / hardware / metrics
- Benchmarks: RISC-V processor
- Hardware: FPGA (details NOT_REPORTED in highlights)
- Metrics: Slack distribution; Fmax envelope

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (highlights): per-stage slack std up to about +/-210 ps; Fmax envelope across seeds about 38 MHz; heavy-tailed, non-Gaussian distributions.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S81 S98 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | YES | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | YES | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
RELEVANT BUT DIFFERENT (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
