# RW0078 — Energy and performance exploration of accelerator coherency port using Xilinx ZYNQ

> **Relevance (2026-09-25 web-search update): HOLD** — ACP vs HP memory sharing on XC7Z020 (the project device): measured bandwidth and energy, effect of background DRAM/cache traffic. Primary Studies: S100 S73 S84. Prior-art boundary: RELEVANT BUT DIFFERENT (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Sadri, MohammadSadegh; Weis, Christian; Wehn, Norbert; Benini, Luca
- Year / venue: 2013 / FPGAworld 2013
- DOI: 10.1145/2513683.2513688 · URL: https://dl.acm.org/doi/10.1145/2513683.2513688

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Performance and energy of processor-accelerator memory sharing schemes on Zynq.

## 2. Method
Infrastructure stressing ACP and HP AXI interfaces; image-filtering case study.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Image filtering task
- Hardware: XC7Z020-1 (Zynq-7000)
- Metrics: Bandwidth; speedup; energy per byte

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (highlights): >1.6 GB/s full-duplex on HP and ACP at 125 MHz on XC7Z020-1; CPU-ACP 1.2x faster than CPU-HP; >20% (2.5 nJ/byte) energy improvement.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S100 S73 S84)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Abstract/highlights only. |
| measured interactions | YES | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | YES | Abstract/highlights only. |
| CPU-FPGA interaction | YES | Abstract/highlights only. |
| memory/data movement | YES | Abstract/highlights only. |

## 7. Possible overlap
RELEVANT BUT DIFFERENT (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
