# RW0008 — HLSFactory: A Framework Empowering High-Level Synthesis Datasets for Machine Learning and Beyond

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Abi-Karam, Stefan; Sarkar, Rishov; Seigler, Allison; Lowe, Sean; Wei, Zhigang; Chen, Hanqiu; Rao, Nanditha; John, Lizy; Arora, Aman; Hao, Cong
- Year / venue: 2024 / MLCAD
- DOI: 10.1145/3670474.3685961 · URL: https://doi.org/10.1145/3670474.3685961
- Metadata source: arXiv v3 PDF first page (includes ACM reference format) + arXiv abs page

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/other/RW0008_AbiKaram2024_HLSFactory_MLCAD_arxiv.pdf`
- SHA-256: `d4a8be4b378d2e8285bc1106d8d28db6bb1dd3f8d6fbde196ef8a202efa6da5e`
- Source: https://arxiv.org/pdf/2405.00820

## Code / dataset / artifact provenance
Code https://github.com/sharc-lab/HLSFactory (Zenodo 10.5281/zenodo.12989544); artifact eval https://github.com/sharc-lab/hlsfactory-artifact-eval (10.5281/zenodo.13117886); datasets Zenodo 10.5281/zenodo.13117901; ACM artifact badges

## 1. Research question
Lack of large, standardized, multi-vendor, reproducible and extensible HLS datasets for ML-based QoR prediction and DSE.

## 2. Problem setting
Infrastructure for generating HLS design datasets by expanding base designs into directive design spaces, running vendor HLS/implementation flows in parallel, and aggregating standardized results.

## 3. Search space
Design space expansion (not optimization): Cartesian product of parameterized directives (loop unroll factors, pipeline, array partition) specified in OptDSL Tcl templates, with random sampling

## 4. Evaluation method
Vitis HLS synthesis reports and Vivado post-implementation reports (timing, resources, power estimate); Intel i++/Quartus for Intel flow; case studies use gradient-boosting QoR prediction and statistical comparisons

## 5. Benchmarks
PolyBench, MachSuite, Rosetta, CHStone, Kastner et al. Parallel Programming for FPGAs, AMD/Xilinx Vitis HLS introductory examples, Sharc Lab accelerators (LightningSim collection, FlowGNN, SkyNet, Edge-MoE); HLSyn data integrated

## 6. Hardware
NOT_REPORTED (target FPGA part not specified in paper; runs on 32-core CPU workstation)

## 7. Toolchain
AMD/Xilinx Vitis HLS 2023.1 and 2021.1, Vivado 2023.1 and 2021.1; Intel HLS Compiler (i++) 21.1.0 and Quartus Prime 21.1.0

## 8. Metrics
HLS latency/resources, post-implementation resources/timing/power, tool runtime; ML model R2 and relative absolute error; parallel speedup; Wilcoxon signed-rank p-values across tool versions

## 9. Baselines
Naive per-dataset parallelism (for parallel backend); HLS-reported estimates vs ML predictions; Vitis HLS 2021.1 vs 2023.1

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: design space expansion from 29 base designs to 257 improves ML post-implementation QoR prediction (higher R2, lower error) and design-space coverage; fine-grained parallelism gives >20% speedup over naive parallelism; framework supports Intel flow (1340 designs), external data integration and tool-version regression testing.

## 11. Limitations
Sampling is random/unguided (not DSE); no simulation-based metrics (vector-based power, simulated latency); dataset scale in case studies modest (hundreds of designs); target device details not reported.

## 12. What the paper does NOT evaluate
No DSE algorithm evaluated; no multi-kernel joint evaluation, no CPU-FPGA or on-board measurements, no staged/adaptive acquisition.

## 13. Relationship to our Studies
- Direct (dimension = YES): S59 S61 S78 S81
- Partial (dimension = PARTIAL): S04 S06 S10 S11 S19 S20 S21 S32 S34 S72 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Dataset framework; designs processed independently. |
| measured interactions | NO | No directive/kernel interaction analysis. |
| staged evaluation | PARTIAL | Flow separates HLS synthesis and implementation stages, but not used for staged screening. |
| adaptive evidence acquisition | NO | Random sampling; active learning only mentioned as future extension. |
| cost/fidelity modeling | PARTIAL | Collects both HLS-estimated and post-implementation metrics plus tool runtime; case study predicts post-impl QoR from HLS reports. |
| lifecycle/configuration cost | NO | Not considered (tool-version regression is about HLS tool versions, not deployment). |
| physical implementation in the loop | YES | Vivado implementation (placed-and-routed) reports collected for datasets. |
| multi-benchmark transfer | PARTIAL | Many suites and two vendors covered; cross-benchmark ML generalization not specifically studied. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | PARTIAL | Post-implementation power estimates collected; not analyzed in depth. |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | NO | Only array-partition directives in design spaces. |

## 14. Possible overlap
PARTIAL OVERLAP on: physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions; adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code https://github.com/sharc-lab/HLSFactory (Zenodo 10.5281/zenodo.12989544); artifact eval https://github.com/sharc-lab/hlsfactory-artifact-eval (10.5281/zenodo.13117886); datasets Zenodo 10.5281/zenodo.13117901; ACM artifact badges

## Open questions / reviewer notes
PDF is arXiv v3 (Dec 2024) which carries MLCAD'24 reference format; an author copy also exists at https://lca.ece.utexas.edu/pubs/HLSFactory_MLCAD_2024.pdf. Artifact checklist writes 'Vivado 2121.1' (typo for 2021.1).
