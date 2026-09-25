# RW0032 — A Unified Framework for Automated Code Transformation and Pragma Insertion

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Pouget, Stéphane; Pouchet, Louis-Noël; Cong, Jason
- Year / venue: 2025 / FPGA
- DOI: 10.1145/3706628.3708873 · URL: https://doi.org/10.1145/3706628.3708873
- Metadata source: PDF first page (arXiv:2405.03058v6 with embedded ACM reference format for FPGA '25)

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0032_Pouget2025_Sisyphus_FPGA_arxiv.pdf`
- SHA-256: `ff9f6545572f50e730d2ffe9ce4efb9c0fcfacb6f90d399ce440827b5c165847`
- Source: /home/benyamin/Desktop/Library/A Unified Framework for Automated Code Transformation and Pragma Insertion.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code URL found in the paper)

## 1. Research question
Code transformations (loop distribution, permutation, tiling), tile-size selection for on-chip caching, and HLS pragma insertion are usually handled separately, which fragments and restricts the explored design space and yields suboptimal QoR.

## 2. Problem setting
Single affine (polyhedral) loop-nest kernel compiled with AMD Vitis HLS under user-given DSP and on-chip memory constraints; objective is minimum latency.

## 3. Search space
Joint space of loop distribution/permutation (level-0 order), two-level strip-mining trip counts (fine-grained unroll, pipeline, coarse-grained unroll/tiling), on-chip buffer placement/size, array partition factors, burst width.

## 4. Evaluation method
Vitis HLS 2023.2 synthesis reports (vitis-flow incl. off-chip transfers); a subset placed-and-routed and run on-board on a single SLR of Alveo U200.

## 5. Benchmarks
PolyBench/C 4.2.1 (medium size, 13+ kernels), a CNN layer, BERT-like matrix multiplications (bert_n_m)

## 6. Hardware
AMD/Xilinx Alveo U200 @250 MHz

## 7. Toolchain
Vitis HLS 2023.2; Gurobi 11.0.0 with AMPL; PoCC; ISCC; HARP run with Vitis 2021.1

## 8. Metrics
Throughput (GF/s), speedup, resource utilization (BRAM/DSP/LUT/FF), NLP solve time, latency prediction error

## 9. Baselines
AutoDSE, NLP-DSE, ScaleHLS, HARP

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: with tree reduction Sisyphus reports geometric-mean speedups of 9.17x, 3.47x and 16.15x over AutoDSE, NLP-DSE and ScaleHLS; without tree reduction geo-mean 18.50x (AutoDSE) and 4.49x (NLP-DSE); model latency error 8% average (3% geo-mean); NLP solve time 455 s average, 6.7 s geo-mean.

## 11. Limitations
Restricted to affine loop nests; no loop fusion; objective targets compute-bound kernels (memory-bound kernels may be better served by communication-minimizing approaches); post-optimizations break the NLP lower-bound guarantee; II can be mispredicted (syrk/syr2k errors 49%/32%); on-board evaluation only on a subset and a single SLR.

## 12. What the paper does NOT evaluate
Multi-kernel / multi-accelerator joint optimization; post-route timing effects inside the optimization loop; power/energy; CPU-host interaction; non-affine code (only suggested via combination with AutoDSE/HARP/TAPA).

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S21 S72 S73
- Partial (dimension = PARTIAL): S02 S10 S11 S36 S37 S56 S59 S61 S78 S81 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Optimizes one kernel at a time; multiple loop bodies inside a kernel are modeled jointly |
| measured interactions | PARTIAL | Explicitly models interdependence of transformations and pragmas within a kernel; no cross-kernel interaction |
| staged evaluation | NO | Single analytical NLP solve followed by HLS; no multi-stage filtering |
| adaptive evidence acquisition | NO | No iterative evidence acquisition; one or two designs synthesized |
| cost/fidelity modeling | YES | Analytical latency/resource model embedded in NLP; prediction error reported |
| lifecycle/configuration cost | NOT_REPORTED | NLP solve time and design generation time reported; no lifecycle/reconfiguration cost |
| physical implementation in the loop | PARTIAL | Bitstream generation and on-board runs for a subset on one SLR; not used in optimization loop |
| multi-benchmark transfer | PARTIAL | Evaluated across PolyBench kernels, CNN, BERT GEMMs; no learned transfer |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Host interaction not modeled |
| memory/data movement | YES | Models off-chip/on-chip transfers, tiling for on-chip caching, burst width |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; adaptive evidence acquisition; staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code URL found in the paper)

## Open questions / reviewer notes
Local file is the arXiv v6 version (2405.03058) carrying the FPGA '25 ACM reference and DOI.
