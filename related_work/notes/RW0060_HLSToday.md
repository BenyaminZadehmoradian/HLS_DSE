# RW0060 — FPGA HLS Today: Successes, Challenges, and Opportunities

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Cong, Jason; Lau, Jason; Liu, Gai; Neuendorffer, Stephen; Pan, Peichen; Vissers, Kees; Zhang, Zhiru
- Year / venue: 2022 / ACM TRETS
- DOI: 10.1145/3530775 · URL: https://doi.org/10.1145/3530775
- Metadata source: PDF first page (ACM reference: ACM Trans. Reconfigurable Technol. Syst. 15(4), Article 51, Aug 2022)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/other/RW0060_Cong2022_HLSToday_TRETS.pdf`
- SHA-256: `f851f669cec22fbae56b88b60266643348683694741f480151cc9e75c49840e7`
- Source: /home/benyamin/Desktop/Library/FPGA HLS Today: Successes, Challenges, and Opportunities.pdf

## Code / dataset / artifact provenance
NOT_APPLICABLE

## 1. Research question
Assesses a decade of FPGA HLS deployment since 2011 and identifies remaining challenges and research opportunities.

## 2. Problem setting
Survey/perspective article on FPGA HLS technology and applications.

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
NOT_APPLICABLE (reports results from cited works, e.g., AutoBridge post-route frequencies, Merlin vs manual HLS on Vitis OpenCV functions)

## 5. Benchmarks
NOT_APPLICABLE (case studies drawn from cited works)

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
NOT_APPLICABLE (discusses Vivado/Vitis HLS, Merlin, Intel HLS, open-source HLS)

## 8. Metrics
NOT_APPLICABLE

## 9. Baselines
NOT_APPLICABLE

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: argues HLS has moved to deployment with successes in several domains, and highlights frequency gaps (e.g., AutoBridge raising average frequency from 147 to 297 MHz over 43 designs), pragma complexity (Merlin replacing >20 HLS pragmas with ~1 Merlin pragma on average in Vitis OpenCV functions), and a need for efficient multi-objective HLS DSE and minute-scale physical design closure.

## 11. Limitations
Perspective article; results are summarized from cited works rather than new experiments; authors from the tools discussed (Xilinx/Falcon/UCLA).

## 12. What the paper does NOT evaluate
No new DSE method or empirical comparison.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S19 S20 S59 S61 S73 S78 S81 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Survey |
| measured interactions | NOT_APPLICABLE | Survey |
| staged evaluation | NOT_APPLICABLE | Survey |
| adaptive evidence acquisition | NOT_APPLICABLE | Survey |
| cost/fidelity modeling | NOT_APPLICABLE | Survey |
| lifecycle/configuration cost | NOT_APPLICABLE | Survey |
| physical implementation in the loop | PARTIAL | Discusses physical-aware HLS (AutoBridge) and fast physical closure as opportunity |
| multi-benchmark transfer | NOT_APPLICABLE | Survey |
| decision/Pareto stability | NOT_APPLICABLE | Survey |
| energy/power | PARTIAL | Mentions power as a DSE objective only |
| CPU-FPGA interaction | PARTIAL | Discusses host/FPGA code separation and system integration burden |
| memory/data movement | PARTIAL | Discusses Merlin burst/coalescing, data reuse, prefetching, memory banking |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: physical implementation in the loop; energy/power; CPU-FPGA interaction; memory/data movement

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_APPLICABLE

## Open questions / reviewer notes
Authors listed alphabetically per the paper.
