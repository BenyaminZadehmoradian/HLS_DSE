# RW0077 — Bounding Memory Access Times in Multi-Accelerator Architectures on FPGA SoCs

> **Relevance (2026-09-25 web-search update): HOLD** — Worst-case memory access time bounds for multiple HLS/HW accelerators sharing AXI interconnect, validated with real traces on Zynq-7000 and Zynq UltraScale+ (the project device family). Primary Studies: S100 S73 S49. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Restuccia, Francesco; Pagani, Marco; Biondi, Alessandro; Marinoni, Mauro; Buttazzo, Giorgio
- Year / venue: 2023 / IEEE Transactions on Computers 72(1):154-167
- DOI: 10.1109/TC.2022.3214117 · URL: https://ieeexplore.ieee.org/document/9917304/

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Unpredictable accelerator response time under AXI contention on FPGA SoCs.

## 2. Method
Modeling and analysis of arbitrary AXI bus structures; schedulability analysis.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Real execution traces + simulation
- Hardware: Xilinx Zynq-7000 and Zynq UltraScale+
- Metrics: Worst-case memory access / response time

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): bounds validated on real traces from Zynq-7000 and Zynq UltraScale+.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S100 S73 S49)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Abstract/highlights only. |
| measured interactions | YES | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | PARTIAL | Abstract/highlights only. |
| memory/data movement | YES | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
