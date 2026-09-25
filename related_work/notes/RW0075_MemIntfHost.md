# RW0075 — Analyzing Memory Interference of FPGA Accelerators on Multicore Hosts in Heterogeneous Reconfigurable SoCs

> **Relevance (2026-09-25 web-search update): HOLD** — Measured interference of FPGA accelerators on multicore hosts through shared main memory; extended roofline. Evidence that co-resident (joint) runtime behaviour differs from isolated (local) behaviour. Primary Studies: S100 S73. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Mattheeuws, Maxim; Forsberg, Björn; Kurth, Andreas; Benini, Luca
- Year / venue: 2021 / DATE 2021, pp. 1152-1155
- DOI: none recorded · URL: https://ieeexplore.ieee.org/document/9473925/

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Controlling shared-memory interference in reconfigurable heterogeneous SoCs for reliable performance.

## 2. Method
Characterization methodology for accelerator-induced interference; roofline extended with performance degradation.

## 3. Benchmarks / hardware / metrics
- Benchmarks: NOT_REPORTED in abstract
- Hardware: Xilinx UltraScale+ SoC (Cortex-A + Kintex-grade FPGA)
- Metrics: Host slowdown vs operational intensity

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): programs below 5 flop/byte can suffer slowdowns of up to an order of magnitude.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S100 S73)

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
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | YES | Abstract/highlights only. |
| memory/data movement | YES | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
