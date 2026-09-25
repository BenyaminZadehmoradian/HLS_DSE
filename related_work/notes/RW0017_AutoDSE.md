# RW0017 — AutoDSE: Enabling Software Programmers to Design Efficient FPGA Accelerators

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Sohrabizadeh, Atefeh; Yu, Cody Hao; Gao, Min; Cong, Jason
- Year / venue: 2022 / ACM TODAES
- DOI: 10.1145/3494534 · URL: https://doi.org/10.1145/3494534
- Metadata source: PDF first page (ACM reference format: ACM Trans. Des. Autom. Electron. Syst. 27(4), Article 32, Feb 2022); arXiv 2009.14381 existence confirmed via web search

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0017_Sohrabizadeh2022_AutoDSE_TODAES.pdf`
- SHA-256: `6e32d9176c76c0554e40ad28e4b1f2b52ffb875eeb5e48d236429ec8f9866f4f`
- Source: /home/benyamin/Desktop/AutoDSE/docs/paper/AutoDSE_FPGA_Accelerators.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/AutoDSE ; Merlin Compiler: https://github.com/Xilinx/merlin-compiler

## 1. Research question
Software programmers cannot easily obtain high-QoR FPGA accelerators from HLS C because pragma tuning is laborious and learning/analytical models of HLS tools are inaccurate and version-dependent.

## 2. Problem setting
Push-button single-kernel HLS pragma DSE on top of the Merlin Compiler, treating the HLS tool as a black box.

## 3. Search space
Merlin pragmas per loop/array: coarse-/fine-grained PARALLEL factors, PIPELINE mode (off/cg/fg), TILING factors; list-comprehension design-space representation prunes invalid combinations (24.65x on average).

## 4. Evaluation method
HLS synthesis estimates (Merlin + Xilinx HLS reports, 60-min HLS timeout) guide the search; final designs built to bitstreams and run on AWS F1 FPGA. P&R explicitly not used inside the loop.

## 5. Benchmarks
MachSuite and Rodinia kernels (11 kernels, plus an AlexNet conv layer); 33 vision kernels from Xilinx Vitis Libraries

## 6. Hardware
AWS EC2 r4.4xlarge (DSE host); AWS F1 f1.2xlarge with Xilinx Virtex UltraScale+ VU9P

## 7. Toolchain
Merlin Compiler (open-sourced by Xilinx) over Xilinx HLS/Vitis (SDAccel/Vivado HLS); exact tool versions NOT_REPORTED

## 8. Metrics
Speedup over single-thread Xeon CPU core, speedup vs manual designs and vs other DSE tools, DSE runtime, number of pragmas

## 9. Baselines
Original coordinate descent; S2FA (OpenTuner-based); lattice-traversing DSE (ICCD'18); GP-based Bayesian optimization (DATE'21); manual Merlin designs; Xilinx Vitis library manual kernels

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 19.9x geometric-mean speedup over one CPU core on MachSuite/Rodinia (0.93x of manual designs, ~1.1 h DSE); outperforms S2FA, lattice-traversing DSE and GP-BO by 3.45x, 4.23x, 17.92x (geo-mean); matches Vitis vision kernels with 26.38x fewer optimization pragmas in ~0.3 h.

## 11. Limitations
Relies on HLS/Merlin cycle breakdown (inaccurate for unbounded/while loops); QoR from synthesis, not P&R; restricted to Merlin pragmas (no DATAFLOW/STREAM, cannot set II); single-objective (performance under resource constraints).

## 12. What the paper does NOT evaluate
Joint/multi-kernel or system-level evaluation; post-route timing/QoR in the loop; power/energy; multi-fidelity cost modeling; Pareto stability; reconfiguration/lifecycle cost; CPU-FPGA transfer overheads beyond on-board runtime.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S02 S04 S05 S06 S20 S21 S23 S33 S36 S37 S56 S71 S72 S73 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Each kernel explored independently. |
| measured interactions | PARTIAL | Pragma interactions handled heuristically (parameter ordering, partitions); not quantified across kernels. |
| staged evaluation | NO | Single HLS-synthesis fidelity per candidate; on-board only for final designs. |
| adaptive evidence acquisition | PARTIAL | Next candidate chosen from bottleneck analysis of evaluated points, but no explicit evidence/fidelity acquisition policy. |
| cost/fidelity modeling | PARTIAL | HLS timeout and parallel thread reallocation manage cost; no explicit cost/fidelity model. |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NO | Authors state P&R too time-consuming; synthesis results used; bitstreams only for final evaluation. |
| multi-benchmark transfer | NO | Many benchmarks evaluated, but no knowledge transfer between them. |
| decision/Pareto stability | NO |  |
| energy/power | NO |  |
| CPU-FPGA interaction | PARTIAL | End-to-end on-board speedup vs CPU on AWS F1; host interaction not studied. |
| memory/data movement | PARTIAL | Bottleneck analyzer distinguishes memory-transfer vs compute cycles; TILING/cg PIPELINE target memory transfer. |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: measured interactions; adaptive evidence acquisition; cost/fidelity modeling; CPU-FPGA interaction; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; staged evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/AutoDSE ; Merlin Compiler: https://github.com/Xilinx/merlin-compiler

## Open questions / reviewer notes
This is the 27-page ACM TODAES journal version. A different 11-page version exists at /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/AutoDSE_Enabling_Software_Programmers_Design_Efficient_FPGA_Accelerators_2020.pdf (sha256 25d253c6d11454bf4d8abc276cf4c2b68d643463e5160c9774eea4086ab461fd): 'AutoDSE: Enabling Software Programmers Design Efficient FPGA Accelerators', 'Conference'20, Sep 2020' ACM template, describes a 'bottleneck-guided gradient optimizer' and Xilinx SDx; it matches the arXiv preprint 2009.14381 (Sep 2020) era and is treated as the preprint of the same work (no separate record). Exact identity of that file to arXiv v1 not byte-verified.
