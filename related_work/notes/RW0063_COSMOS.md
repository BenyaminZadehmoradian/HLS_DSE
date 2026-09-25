# RW0063 — COSMOS: Coordination of High-Level Synthesis and Memory Optimization for Hardware Accelerators

> **Relevance (2026-09-25 web-search update): HOLD** — Compositional system-level DSE of multi-component HLS accelerators: per-component Pareto sets composed at system level. The compositional assumption S97 tests. Primary Studies: S97 S15 S66. Prior-art boundary: POTENTIAL OVERLAP.
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Piccolboni, Luca; Mantovani, Paolo; Di Guglielmo, Giuseppe; Carloni, Luca P.
- Year / venue: 2017 / ACM TECS 16(5s) Art. 150 (CODES+ISSS 2017)
- DOI: none recorded · URL: https://arxiv.org/abs/1912.10823

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (arXiv; not downloaded)

## 1. Research question
Navigating the system-level Pareto space of complex accelerators built from many HLS components.

## 2. Method
Per-component co-design of datapath (HLS) and memory, producing component Pareto sets; compositional system-level exploration to converge to a target cost/performance trade-off.

## 3. Benchmarks / hardware / metrics
- Benchmarks: WAMI (wide-area motion imagery) accelerator
- Hardware: NOT_REPORTED in abstract
- Metrics: Pareto coverage; number of HLS invocations

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): explores the design space as completely as exhaustive search while reducing HLS-tool invocations by up to 14.6x.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S97 S15 S66)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | PARTIAL | Abstract/highlights only. |
| adaptive evidence acquisition | PARTIAL | Abstract/highlights only. |
| cost/fidelity modeling | YES | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_REPORTED | Abstract/highlights only. |
| memory/data movement | YES | Abstract/highlights only. |

## 7. Possible overlap
POTENTIAL OVERLAP

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
