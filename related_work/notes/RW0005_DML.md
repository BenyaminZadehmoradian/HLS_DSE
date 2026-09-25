# RW0005 — DML: Dynamic Partial Reconfiguration With Scalable Task Scheduling for Multi-Applications on FPGAs

> **Relevance (2026-09-25 correction audit): HOLD** — DPR task scheduling for multi-application FPGAs; abstract-only review. Primary Studies: S85 S93. Prior-art boundary: UNRESOLVED.
> **HOLD:** reviewed from the abstract only; no legitimate open full text found (OpenAlex: closed). Classification to be revisited when full text is available.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_ABSTRACT_ONLY`.

## Bibliographic identity
- Authors: Dhar, Ashutosh; Richter, Edward; Yu, Mang; Zuo, Wei; Wang, Xiaohao; Kim, Nam Sung; Chen, Deming
- Year / venue: 2022 / IEEE Transactions on Computers
- DOI: 10.1109/TC.2021.3137785 · URL: https://doi.org/10.1109/TC.2021.3137785
- Metadata source: Crossref (vol. 71, no. 10, pp. 2577-2591) + Semantic Scholar abstract

## PDF provenance
- Status: `METADATA_ONLY_PAYWALLED` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Scheduling heterogeneous tasks from one or multiple applications onto FPGA partially reconfigurable regions in a resource-efficient way while hiding dynamic partial reconfiguration (DPR) latency.

## 2. Problem setting
Edge (Zedboard) and data-center-like (ZCU106) FPGAs with DPR, running batches of work from multiple applications.

## 3. Search space
Task-to-region/time schedule (ILP), including IP-level pipelining and parallelization and multi-application resource sharing strategies.

## 4. Evaluation method
Real-world benchmarks run on Zedboard and ZCU106 (per abstract); details NOT_REPORTED (full text not accessed).

## 5. Benchmarks
NOT_REPORTED in abstract ('real world benchmarks')

## 6. Hardware
Zedboard (Zynq-7000), Xilinx ZCU106

## 7. Toolchain
NOT_REPORTED

## 8. Metrics
Speedup (vs bulk-batching baseline); scalability of scheduler

## 9. Baselines
Bulk-batching baseline

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'average speedup of 5X and up to 7.65X on a ZCU106 over a bulk-batching baseline via our scheduling strategies'.

## 11. Limitations
NOT_REPORTED (abstract only); ILP scalability claimed but details not verified.

## 12. What the paper does NOT evaluate
From abstract: HLS design-space choices of the IPs, energy, joint pragma-level DSE; full text not accessed.

## 13. Relationship to our Studies
- Direct (dimension = YES): S85 S86 S94
- Partial (dimension = PARTIAL): S07 S15 S59 S61 S65 S78 S81

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Multiple applications scheduled jointly on shared FPGA; not HLS candidate co-evaluation. |
| measured interactions | NOT_REPORTED | Full text not accessed. |
| staged evaluation | NOT_REPORTED | Full text not accessed. |
| adaptive evidence acquisition | NOT_REPORTED | Full text not accessed. |
| cost/fidelity modeling | NOT_REPORTED | Full text not accessed. |
| lifecycle/configuration cost | YES | DPR latency explicitly considered and hidden by the scheduler (abstract). |
| physical implementation in the loop | PARTIAL | Evaluated on real boards per abstract; bitstreams implied by DPR. |
| multi-benchmark transfer | NOT_REPORTED | Full text not accessed. |
| decision/Pareto stability | NOT_REPORTED | Full text not accessed. |
| energy/power | NOT_REPORTED | Abstract mentions energy efficiency motivation only. |
| CPU-FPGA interaction | NOT_REPORTED | Full text not accessed. |
| memory/data movement | NOT_REPORTED | Full text not accessed. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
IEEE Xplore lists an author-accepted manuscript URL (ieeexplore.ieee.org/ielaam/12/9880482/9661327-aam.pdf) but it required login/returned 418/502; Semantic Scholar marks it CLOSED; recorded as paywalled. Earlier conference version: Dhar et al., 'Leveraging Dynamic Partial Reconfiguration with Scalable ILP Based Task Scheduling', VLSID 2020 (DOI 10.1109/VLSID49098.2020.00052).
