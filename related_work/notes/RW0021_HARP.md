# RW0021 — Robust GNN-based Representation Learning for HLS

> **Relevance (2026-09-25 correction audit): SUPPORTING** — GNN representation for HLS QoR prediction used for DSE; surrogate foundation for constraint-vs-QoR prediction. Primary Studies: S89 S10. Prior-art boundary: METHOD FOUNDATIONAL.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Sohrabizadeh, Atefeh; Bai, Yunsheng; Sun, Yizhou; Cong, Jason
- Year / venue: 2023 / ICCAD
- DOI: 10.1109/ICCAD57390.2023.10323853 · URL: https://doi.org/10.1109/ICCAD57390.2023.10323853
- Metadata source: PDF first page (IEEE Xplore header with DOI, ICCAD 2023)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0021_Sohrabizadeh2023_HARP_ICCAD.pdf`
- SHA-256: `7471b30ba41a696e8817d61990ed495e57faf7d0160a28cf48e2a082abc8ccf6`
- Source: /home/benyamin/Desktop/Library/Robust GNN-based Representation Learning for HLS.pdf

## Code / dataset / artifact provenance
Materials: https://github.com/UCLA-VAST/HARP

## 1. Research question
GNN surrogates of HLS tools struggle with long-range program dependencies and tightly coupled program/pragma representations, limiting accuracy, DSE quality and transfer to new HLS tool versions.

## 2. Problem setting
Surrogate modeling (validity, latency, resources) of Merlin-pragma HLS designs and model-based DSE, including transfer between SDx 2018.3 and Vitis 2020.2.

## 3. Search space
Merlin PIPELINE (off/cg/fg), PARALLEL and TILE factors per loop (up to >17 trillion points for 3mm)

## 4. Evaluation method
Test-set RMSE/MAE/Kendall tau against HLS reports; DSE designs verified by Merlin + HLS synthesis.

## 5. Benchmarks
40 MachSuite and PolyBench kernels (AutoDSE-generated database; v1: SDx 2018.3, v2: Vitis 2020.2; 35 and 27 kernels in DSE)

## 6. Hardware
Xilinx Alveo U200 @250 MHz (synthesis target)

## 7. Toolchain
Merlin Compiler; SDAccel/SDx 2018.3; Vitis 2020.2; PyTorch on NVIDIA V100

## 8. Metrics
RMSE, MAE, Kendall's tau of perf ranking, classification accuracy, DSE speedup vs AutoDSE best design

## 9. Baselines
GNN-DSE, AutoDSE (25 h/kernel), model ablations M1-M5

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: in DSE HARP achieves an average 2.54x performance improvement over AutoDSE with a 25x smaller time limit, and after transfer learning outperforms GNN-DSE by 1.31x on average (1.33x geo-mean).

## 11. Limitations
Tied to Merlin pragma space; latency/resource labels from HLS estimates; BFS exploration heuristic; transfer requires fine-tuning data from the new tool version.

## 12. What the paper does NOT evaluate
Post-route/on-board QoR; power; multi-kernel system designs; unseen-kernel generalization beyond shared kernels; cost-aware sampling.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S32 S34 S36 S37 S56 S71 S72 S85 S86 S88 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single kernels |
| measured interactions | PARTIAL | NPT models pragma interactions via merge MLP |
| staged evaluation | PARTIAL | Surrogate DSE then top-10 HLS verification |
| adaptive evidence acquisition | NO | No active acquisition |
| cost/fidelity modeling | PARTIAL | Surrogate vs HLS runtime contrast (1 h vs 25 h) |
| lifecycle/configuration cost | PARTIAL | Tool-version change handled via fine-tuning |
| physical implementation in the loop | NO | HLS reports only |
| multi-benchmark transfer | YES | Transfer from SDx 2018.3 to Vitis 2020.2 |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NO | Not analyzed (Merlin handles caching) |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; adaptive evidence acquisition; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Materials: https://github.com/UCLA-VAST/HARP

## Open questions / reviewer notes
Paper introduces HARP; key chosen as 'HARP'.
