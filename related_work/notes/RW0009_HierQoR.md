# RW0009 — Hierarchical Source-to-Post-Route QoR Prediction in High-Level Synthesis with GNNs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Gao, Mingzhe; Zhao, Jieru; Lin, Zhe; Guo, Minyi
- Year / venue: 2024 / DATE
- DOI: 10.23919/DATE58400.2024.10546555 · URL: https://doi.org/10.23919/DATE58400.2024.10546555
- Metadata source: PDF first page (arXiv:2401.08696v1) + IEEE Xplore landing page (doc 10546555) for venue/DOI

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/multifidelity/RW0009_Gao2024_HierQoR_DATE_arxiv.pdf`
- SHA-256: `27f0e3e78596eb1cac6ec91f7c88c988d2f888090e264f7df2260c84d579c5fb`
- Source: /home/benyamin/Desktop/Library/Hierarchical Source-to-Post-Route QoR Prediction.pdf

## Code / dataset / artifact provenance
Code and models: https://github.com/sjtu-zhao-lab/hierarchical-gnn-for-hls

## 1. Research question
Obtaining post-route QoR requires a full C-to-bitstream flow per pragma change; prior predictors estimate post-HLS metrics or require running HLS, and handle pragmas/loop hierarchies poorly.

## 2. Problem setting
Predict post-route latency and resource usage (LUT/FF/DSP) of pragma-annotated C/C++ kernels directly from source, and use it for Pareto DSE.

## 3. Search space
Loop pipelining, loop flattening, unroll factors {1,2,4,8,16}, array partition factors matched to unroll (DSE experiment; up to 2796 configurations per app)

## 4. Evaluation method
MAPE vs post-route (Vivado) resources and HLS-report latency; DSE on unseen apps compared against exhaustively implemented exact Pareto set (ADRS).

## 5. Benchmarks
16 applications from PolyBench, MachSuite, CHStone (12 train/test; unseen bicg, symm, mvt, syrk for DSE)

## 6. Hardware
AMD UltraScale+ MPSoC ZCU102

## 7. Toolchain
Vitis HLS 2022.1, Vivado 2022.1; Clang/LLVM; ProGraML; GCN/GAT/GraphSAGE/TransformerConv/PNA

## 8. Metrics
MAPE for latency, iteration latency, LUT, FF, DSP; ADRS; DSE runtime

## 9. Baselines
Wu et al. (DAC'22 GNN post-route predictor), GNN-DSE

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: prediction error below 10% for latency and all resource types (e.g., latency 8.54%, DSP 6.94%, FF 9.99%, LUT 9.65% at application level); DSE ADRS of 6.91% on unseen apps vs 13.94% (Wu et al.) and 10.96% (GNN-DSE), with DSE time reduced from tens of days to tens of minutes.

## 11. Limitations
Latency labels come from HLS reports (not measured); two-level hierarchy abstraction; small design spaces (<=2796 points) and single device; timing/Fmax not predicted.

## 12. What the paper does NOT evaluate
Fmax/timing closure; power; multi-kernel or dataflow designs; on-board runtime; transfer across devices/toolchains.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S10 S11 S21 S59 S61 S72 S78 S81 S90
- Partial (dimension = PARTIAL): S02 S32 S34 S36 S37 S43 S45 S56 S71 S73 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single-kernel applications |
| measured interactions | PARTIAL | Inner-loop predictions composed into outer hierarchy; interactions learned not measured |
| staged evaluation | PARTIAL | Hierarchical local->global prediction; DSE uses model only |
| adaptive evidence acquisition | NO | No acquisition loop |
| cost/fidelity modeling | YES | Predicts high-fidelity post-route QoR from source to avoid HLS+implementation cost |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Resource labels and exact Pareto sets from post-route implementation |
| multi-benchmark transfer | YES | DSE on four unseen applications |
| decision/Pareto stability | PARTIAL | ADRS vs exact Pareto set reported |
| energy/power | NO | Not estimated |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Memory-port nodes for array partitioning |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; physical implementation in the loop; multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; adaptive evidence acquisition; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code and models: https://github.com/sjtu-zhao-lab/hierarchical-gnn-for-hls

## Open questions / reviewer notes
Local filename truncated (full title ends 'in High-Level Synthesis with GNNs'). DOI confirmed from IEEE Xplore page.
