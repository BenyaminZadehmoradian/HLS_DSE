# RW0001 — CRYPTONITE: Scalable Accelerator Design for Cryptographic Primitives and Algorithms

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Maheswaran, Karthikeya Sharma; Bossut, Camille; Wanna, Andy; Zhang, Qirun; Hao, Cong
- Year / venue: 2025 / IEEE ASAP
- DOI: 10.1109/ASAP65064.2025.00013 · URL: https://doi.org/10.1109/ASAP65064.2025.00013
- Metadata source: arXiv PDF first page (2505.14657v1) + Crossref (ASAP 2025, pp. 17-24)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0001_Maheswaran2025_CRYPTONITE_ASAP_arxiv.pdf`
- SHA-256: `50310049e0a1c79620053787c1d870bd3c6d8d1cc52c1225dec08810dd5d8764`
- Source: https://arxiv.org/pdf/2505.14657

## Code / dataset / artifact provenance
Code released: https://github.com/KarthikeyaSharma16/Cryptonite (per paper footnote)

## 1. Research question
Straight-line (loop-free) C code of cryptographic primitives synthesizes via HLS into large, non-scalable hardware and offers no parameterizable constructs for HLS DSE; the paper seeks correct-by-construction restructuring that enables resource/latency trade-off exploration, including across multiple co-deployed primitives.

## 2. Problem setting
Automatic generation of HLS accelerators for elliptic-curve arithmetic primitives (Fiat Cryptography straight-line C) under resource/latency constraints on a single FPGA.

## 3. Search space
Loop transformations (interchange, padding, fusion, perfectization, branch elimination, strength reduction, tiling) on e-graph re-rolled code, combined with pragma configurations (array partitioning, unroll factors, pipeline II, loop flatten/merge, dependence pragmas); for multi-kernel, combinations of per-kernel Pareto designs.

## 4. Evaluation method
Analytical QoR estimator for pruning; reported results from Vitis HLS 2023.1 synthesis reports (latency cycles, DSP/LUT/FF/BRAM). No post-route or on-board measurements reported.

## 5. Benchmarks
Fiat Cryptography primitives (paper states 12 primitive types tested); reported: Curve25519, P521, P448, Secp256k1, P384 multiplication and square kernels.

## 6. Hardware
Xilinx xczu9eg-ffvb1156-2-e (ZCU102-class Zynq UltraScale+) as synthesis target

## 7. Toolchain
Vitis HLS 2023.1; egg e-graph library; SVF; GiNaC; clang AST

## 8. Metrics
Latency (cycles), DSP/LUT/FF/BRAM utilization, Normalized Performance Index (NPI, weighted normalized latency+resource), speedup

## 9. Baselines
Original straight-line code; rolled code; allocation pragma; manual DSE/rewriting; ScaleHLS

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'Cryptonite achieves scalable designs with up to 88.88% reduced resource usage and a 54.31% improvement in latency compared to naively synthesized designs'; single-kernel up to 2.75x speedup and 2.03x resource reduction; for a 3-kernel joint deployment DSP usage reduced ~62.21% and execution time by 27 cycles vs naive straight-line code.

## 11. Limitations
Effectiveness depends on e-graph loop re-rolling; for Secp256k1 and P384 transformations increased latency due to loop-carried carry chains; QoR estimator only predicts latency and DSP analytically; no RTL/post-implementation comparison; ScaleHLS failed on several primitives.

## 12. What the paper does NOT evaluate
Post-place-and-route timing/resources, on-board execution, power/energy, interaction effects between co-located kernels beyond summing resources and taking max latency, reconfiguration/lifecycle cost, CPU-FPGA interaction, estimator fidelity vs. synthesis.

## 13. Relationship to our Studies
- Direct (dimension = YES): S32 S34 S88
- Partial (dimension = PARTIAL): S04 S05 S06 S07 S15 S20 S21 S23 S33 S65 S71 S72 S73

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Multi-kernel DSE combines per-kernel Pareto designs; joint cost = sum of resources, latency = max over kernels (Sec. IV-B). |
| measured interactions | NO | Joint cost composed additively from isolated kernel results; no measured cross-kernel interaction. |
| staged evaluation | YES | Analytical QoR estimator prunes candidates before HLS synthesis; Pareto feedback loop. |
| adaptive evidence acquisition | PARTIAL | Pareto-front designs fed back to refine exploration near the front; no explicit budget-aware acquisition. |
| cost/fidelity modeling | PARTIAL | Low-fidelity analytical estimator vs HLS synthesis; evaluation cost not explicitly modeled. |
| lifecycle/configuration cost | NO | Not discussed. |
| physical implementation in the loop | NO | Results from Vitis HLS synthesis only. |
| multi-benchmark transfer | NO | Multiple primitives evaluated, but no transfer of models/knowledge across benchmarks. |
| decision/Pareto stability | NO | Not evaluated. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | NO | Not evaluated. |
| memory/data movement | PARTIAL | Array partitioning explored as a knob; no off-chip memory modeling. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code released: https://github.com/KarthikeyaSharma16/Cryptonite (per paper footnote)

## Open questions / reviewer notes
Reviewed arXiv v1 (May 2025); published version is ASAP 2025 (Crossref DOI 10.1109/ASAP65064.2025.00013, pp. 17-24). Published text may differ from arXiv v1. Hint 'joint multi-primitive accelerator design' matches Sec. IV-B (DSE on multiple cryptographic kernels). No other paper named CRYPTONITE found at ASAP 2025.
