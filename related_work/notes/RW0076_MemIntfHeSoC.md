# RW0076 — Understanding and Mitigating Memory Interference in FPGA-based HeSoCs

> **Relevance (2026-09-25 web-search update): HOLD** — In-depth measurement of memory interference on two commercial FPGA SoCs and Controlled Memory Request Injection (CMRI). Primary Studies: S100 S73. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Brilli, Gianluca; Capotondi, Alessandro; Burgio, Paolo; Marongiu, Andrea
- Year / venue: 2022 / DATE 2022, pp. 1335-1340
- DOI: 10.23919/DATE54114.2022.9774768 · URL: https://ieeexplore.ieee.org/document/9774768/

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Resource contention on shared interconnect / DRAM controller in FPGA-based SoCs affects program timing.

## 2. Method
Interference analysis on two commercial FPGA SoCs; CMRI architectural support.

## 3. Benchmarks / hardware / metrics
- Benchmarks: NOT_REPORTED in abstract
- Hardware: Two commercial FPGA SoCs
- Metrics: CPU slowdown; usable FPGA memory bandwidth

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): interference slows CPU tasks by up to 16x; CMRI exploits >40% of FPGA-available bandwidth with slowdown below 10%.

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
