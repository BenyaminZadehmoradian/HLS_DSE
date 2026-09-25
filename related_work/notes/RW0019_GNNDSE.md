# RW0019 — Automated Accelerator Optimization Aided by Graph Neural Networks

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Sohrabizadeh, Atefeh; Bai, Yunsheng; Sun, Yizhou; Cong, Jason
- Year / venue: 2022 / DAC
- DOI: 10.1145/3489517.3530409 · URL: https://doi.org/10.1145/3489517.3530409
- Metadata source: PDF first page (ACM reference format)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0019_Sohrabizadeh2022_GNNDSE_DAC.pdf`
- SHA-256: `d6410662a86ce13ab538782b5200f8ff253155fe6de0ef38446bee632a5cb9c5`
- Source: /home/benyamin/Desktop/Library/Automated Accelerator Optimization Aided by Graph Neural.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/GNN-DSE

## 1. Research question
HLS tool evaluation of each pragma configuration takes minutes to hours, and prior learned models are per-application or ignore program semantics, so they cannot transfer across kernels.

## 2. Problem setting
Pragma-level DSE for single C kernels through the Merlin Compiler targeting a Xilinx FPGA, minimizing latency under resource-utilization thresholds.

## 3. Search space
Merlin pragmas per loop: pipeline (off/cg/fg), parallel factor, tile factor

## 4. Evaluation method
Surrogate predictions during DSE; top-10 designs verified with Merlin Compiler + HLS (synthesis estimates).

## 5. Benchmarks
MachSuite and PolyBench kernels; unseen kernels bicg, doitgen, gesummv, 2mm

## 6. Hardware
Xilinx Virtex UltraScale+ VCU1525

## 7. Toolchain
Merlin Compiler + Xilinx HLS (version NOT_REPORTED); PyTorch

## 8. Metrics
RMSE of latency/DSP/BRAM/LUT/FF, classification accuracy/F1, DSE runtime speedup, design speedup

## 9. Baselines
AutoDSE; MLP pragma-only model (after Kwon et al.); GCN/GAT variants

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: on unseen kernels GNN-DSE reaches designs within -2%/+5% (mean +1%) of AutoDSE run for up to 21 h, while accelerating the optimization process by up to 79x (average 48x).

## 11. Limitations
Dataset construction is the main bottleneck; exhaustive search only feasible for small spaces (heuristic for mvt/2mm); relies on Merlin; predicts HLS-report QoR only.

## 12. What the paper does NOT evaluate
Post-route QoR/timing; power; multi-kernel joint designs; host/memory-system interaction; Pareto stability.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S02 S04 S05 S06 S20 S21 S23 S32 S33 S34 S36 S37 S56 S71 S72 S88

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single kernel per DSE |
| measured interactions | PARTIAL | GNN learns pragma interactions implicitly; not measured explicitly |
| staged evaluation | PARTIAL | Surrogate-based search then HLS verification of top-10 |
| adaptive evidence acquisition | PARTIAL | Rounds of database augmentation with DSE-selected (mispredicted) top designs |
| cost/fidelity modeling | PARTIAL | Surrogate (ms) vs HLS (minutes-hours) cost contrast; not a formal fidelity model |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | HLS estimates only |
| multi-benchmark transfer | YES | Generalization to 4 unseen PolyBench kernels |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NOT_REPORTED | Merlin handles memory coalescing/burst; not analyzed |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/GNN-DSE

## Open questions / reviewer notes
Local filename is truncated ('...Graph Neural'); full title ends with 'Networks'.
