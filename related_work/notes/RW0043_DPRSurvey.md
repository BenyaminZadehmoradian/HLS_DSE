# RW0043 — FPGA Dynamic and Partial Reconfiguration: A Survey of Architectures, Methods, and Applications

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Survey of dynamic/partial reconfiguration architectures and overheads (reconfiguration time, tool runtime). Primary Studies: S85 S86. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** Key renamed from placeholder DFX1.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Vipin, Kizheppatt; Fahmy, Suhaib A.
- Year / venue: 2018 / ACM Computing Surveys
- DOI: 10.1145/3193827 · URL: https://doi.org/10.1145/3193827
- Metadata source: PDF first page (author copy) + Crossref (CSUR 51(4), 2018, 39 pp.)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (accepted)
- Canonical path: `related_work/papers/lifecycle_dfx/RW0043_Vipin2018_DPRSurvey_CSUR_accepted.pdf`
- SHA-256: `1c448e055d986641c1a2e562184f51a04cbd53d4b8488cb0fc02293a90ed8c67`
- Source: https://vipinkizheppatt.github.io/publications/pr_survey.pdf

## Code / dataset / artifact provenance
NOT_APPLICABLE

## 1. Research question
Why dynamic and partial reconfiguration (PR) sees limited use despite extensive study; surveys architectures, design flows, overhead-reduction methods and applications, and identifies challenges.

## 2. Problem setting
Survey of FPGA DPR across commercial/academic architectures, tool flows, runtime management and applications.

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
NOT_APPLICABLE (survey; compiles reported controller throughputs and resource numbers from literature)

## 5. Benchmarks
NOT_APPLICABLE

## 6. Hardware
NOT_APPLICABLE (surveys Xilinx/Intel device families)

## 7. Toolchain
NOT_APPLICABLE

## 8. Metrics
Reconfiguration time/throughput (MB/s), resource overhead (as surveyed)

## 9. Baselines
NOT_APPLICABLE

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: the two major PR overheads are resource wastage and reconfiguration time; modern FPGAs take 'several milliseconds or even seconds' to reconfigure; vendor PR implementation runs can take 'hours or even days'; partitioning choices (modules per region) can increase reconfiguration time dramatically; ICAP theoretical limit ~400 MB/s while vendor controllers achieve far less.

## 11. Limitations
Survey snapshot (circa 2017); no new experiments; device-specific numbers may be dated.

## 12. What the paper does NOT evaluate
HLS pragma-level DSE interaction with PR partitioning; quantitative lifecycle cost models integrated with DSE (only referenced, e.g., Papadimitriou et al. 2011).

## 13. Relationship to our Studies
- Direct (dimension = YES): S59 S61 S78 S81 S85 S86 S94
- Partial (dimension = PARTIAL): S04 S06 S19 S20 S21 S72 S73 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Survey. |
| measured interactions | NOT_APPLICABLE | Survey. |
| staged evaluation | NOT_APPLICABLE | Survey. |
| adaptive evidence acquisition | NOT_APPLICABLE | Survey. |
| cost/fidelity modeling | PARTIAL | Discusses reconfiguration-time cost models and tool runtime as overheads (Sec. 4). |
| lifecycle/configuration cost | YES | Central topic: reconfiguration time, bitstream size/compression, controller throughput, PR tool runtime. |
| physical implementation in the loop | YES | Floorplanning, PR region shaping, bitstream generation discussed. |
| multi-benchmark transfer | NOT_APPLICABLE | Survey. |
| decision/Pareto stability | NOT_APPLICABLE | Survey. |
| energy/power | PARTIAL | Power/cost reduction discussed as application motivation. |
| CPU-FPGA interaction | PARTIAL | Processor-based runtime reconfiguration management (Sec. 5.2) discussed. |
| memory/data movement | PARTIAL | Bitstream storage/transfer to configuration port discussed. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; physical implementation in the loop

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_APPLICABLE

## Open questions / reviewer notes
Chosen as DFX1: widely cited survey that explicitly treats reconfiguration time and PR tool runtime as design overheads, and PR partitioning as a decision affecting configuration time — directly relevant to lifecycle/configuration cost in design decisions. PDF is the authors' copy with ACM template placeholders (2017, Vol 1 No 1); final published CSUR 51(4) 2018 may differ slightly; pdf_version set to 'accepted' (author version) — uncertain.
