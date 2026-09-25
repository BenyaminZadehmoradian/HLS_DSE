# RW0025 — HLPerf: Demystifying the Performance of HLS-based Graph Neural Networks with Dataflow Architectures

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Zhao, Chenfeng; Faber, Clayton J.; Chamberlain, Roger D.; Zhang, Xuan
- Year / venue: 2024 / ACM TRETS
- DOI: 10.1145/3655627 · URL: https://doi.org/10.1145/3655627
- Metadata source: Full text of ACM open-access PDF (extracted via Firecrawl PDF parser) + OpenAlex

## PDF provenance
- Status: `NOT_FOUND` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
Open source: https://github.com/ChenfengZhao/HLPerf; GNNHLS benchmark https://github.com/ChenfengZhao/GNNHLS

## 1. Research question
Evaluating the dynamic, input-dependent performance of HLS dataflow architectures (GNN kernels) is too slow via RTL simulation or on-board runs, hindering DSE (task partitioning, FIFO depth tuning, bottleneck identification).

## 2. Problem setting
Performance estimation for multi-stage HLS dataflow kernels whose behaviour depends on graph input data, targeting Xilinx Alveo FPGAs.

## 3. Search space
NOT_APPLICABLE (performance evaluator; supports user-driven tuning of pragmas, FIFO sizes, code paradigms, task partitioning)

## 4. Evaluation method
Predicted execution time compared against on-board FPGA execution (Alveo U280) and RTL simulation; simulation speed compared to RTL sim and reported speeds of cycle-accurate simulators.

## 5. Benchmarks
GNNHLS (GCN, GraphSage, GIN, GAT, MoNet, GatedGCN) on four Open Graph Benchmark datasets (abbreviated MH, MT, AX, PT in Table 2; e.g., OGBG-MOLTOX21) plus five general-purpose applications

## 6. Hardware
Xilinx Alveo U280 (Open Cloud Testbed); simulator on Intel i7-8850H

## 7. Toolchain
Vitis 2023.1; PyPy3 + SimPy

## 8. Metrics
Execution-time prediction error vs FPGA/RTL sim; simulation elapsed time/speedup

## 9. Baselines
RTL simulation; reported speeds of LightningSim, Flash, FastSim

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'over 10,000x average simulation acceleration relative to RTL simulation and over 400x acceleration relative to state-of-the-art cycle-accurate tools at the cost of 7% mean error rate relative to actual FPGA implementation performance.'

## 11. Limitations
Model conversion and pragma pattern modelling limited to loop pragmas common in GNN kernels; generalization beyond GNNs is future work; not cycle-accurate; no automatic DSE loop; speed comparisons to other simulators use their reported numbers.

## 12. What the paper does NOT evaluate
Automated search/optimization, resource or power/energy estimation, physical-implementation effects on frequency, multi-objective trade-offs.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S07 S15 S36 S37 S56 S65
- Partial (dimension = PARTIAL): S04 S06 S10 S11 S21 S32 S34 S59 S61 S71 S72 S73 S78 S81 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Simulates the whole dataflow pipeline of interconnected kernels jointly to identify bottleneck stages. |
| measured interactions | YES | Inter-kernel FIFO/stall interactions and input-dependent bottlenecks are modelled and shown to differ between regular vs power-law graphs. |
| staged evaluation | PARTIAL | Positioned as a fast stage between C emulation and RTL sim/on-board runs; no automated staged policy. |
| adaptive evidence acquisition | NO | No adaptive selection of evaluations. |
| cost/fidelity modeling | PARTIAL | Explicit speed/accuracy trade-off vs RTL sim and cycle-accurate simulators quantified, but not used in an optimizer. |
| lifecycle/configuration cost | NO | Not addressed; notes 4.5-12 h hardware compilation cost. |
| physical implementation in the loop | PARTIAL | Ground truth from on-board execution of implemented bitstreams; the estimator itself is pre-implementation. |
| multi-benchmark transfer | PARTIAL | Evaluated on 6 GNN models x 4 datasets and 5 general-purpose apps; no learning-based transfer. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | NO | Performance only. |
| CPU-FPGA interaction | NO | Kernel execution time; host interaction not modelled. |
| memory/data movement | PARTIAL | Models dataflow/FIFO streaming and data-dependent memory access patterns of graph data (U280 HBM platform). |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Open source: https://github.com/ChenfengZhao/HLPerf; GNNHLS benchmark https://github.com/ChenfengZhao/GNNHLS

## Open questions / reviewer notes
PDF is open access (CC license, ACM hybrid OA; also NSF PAR 10500905) but download failed: dl.acm.org returned HTTP 403 to curl and par.nsf.gov timed out, so no local file. Full text read via Firecrawl PDF parsing of https://dl.acm.org/doi/pdf/10.1145/3655627 (26 pages). ACM reference format says Vol. 18, No. 1, Article 2 (Dec 2024); some listings give March 2025. Not an 'HLS performance prediction' ML model: it is a simulation-based evaluator for GNN dataflow kernels; no other paper named HLPerf found.
