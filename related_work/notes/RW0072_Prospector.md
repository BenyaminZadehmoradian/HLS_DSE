# RW0072 — Bayesian Optimization for Efficient Accelerator Synthesis

> **Relevance (2026-09-25 full-text review): SUPPORTING** — Single-kernel multi-objective Bayesian optimization (GP + PESMO) of HLS directives with each sample evaluated through HLS and place-and-route: methodological base for adaptive acquisition (S99) and a BO baseline for S72. No fidelity or local-vs-joint selection; its heterogeneous-accelerator case study composes kernel resources additively without jointly implementing the mixes. Primary Studies: S99 S72 S04. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** none (Mehrabi, Manocha, Lee, Sorin; ACM TACO 18(1), Article 4, December 2020, DOI 10.1145/3427377; extension of the earlier Prospector conference paper).

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Mehrabi, Atefeh; Manocha, Aninda; Lee, Benjamin C.; Sorin, Daniel J.
- Year / venue: 2020 / ACM TACO 18(1), Art. 4
- DOI: 10.1145/3427377 · URL: https://doi.org/10.1145/3427377

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: accepted (author site)
- Canonical path: `related_work/papers/hls_dse/RW0072_Mehrabi2020_Prospector_TACO_accepted.pdf` (local only, gitignored)
- SHA-256: `6aff13e1ee1d6b6a0e850b41589bc6836fa917bb6b110f6dbbc5c935c10f6673`
- Source: https://www.engineering.upenn.edu/~leebcc/documents/mehrabi20-taco.pdf

## Code provenance
NOT_REPORTED (third-party Spearmint PESM branch)

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Find Pareto-efficient HLS directive placements and configurations (latency vs FF/LUT/DSP/BRAM) with few expensive HLS + P&R evaluations.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Directive placement as per-directive bitmaps + configuration parameters; independent GPs per output; PESMO acquisition via Spearmint; failed synthesis assigned high latency; co-simulation failures discarded. Case study with gem5/PAAS + discrete-event simulator for an 8-core + integrated FPGA system; accelerator mixes fitted into FPGA budgets by summing per-accelerator synthesis-report resources (not jointly implemented).

## 5. Benchmarks
PolyBench fdtd-2d (6,561 points), 2mm (15,625), heat-3d (2,304); MachSuite fft (36,000), bbgemm (960), stencil-3d (960); every space exhaustively evaluated for the golden front.

## 6. Hardware
Xilinx FPGA via Vivado (device NOT_REPORTED); simulated 8-core + integrated Zynq-like FPGA.

## 7. Toolchain
Vivado HLS + Vivado (P&R, bitstream), Spearmint (PESM), DEAP, gem5/PAAS, Verilator; versions NOT_REPORTED.

## 8. Metrics
Latency, FF, LUT, DSP, BRAM; normalized distance of golden-front points to the estimated front; resource increase at latency targets; case-study task throughput.

## 9. Baselines
Random search, simulated annealing (latency only), genetic algorithm (DEAP, 1D/2D/5D), Prospector-1D/2D; equal iterations / wall-clock.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Fig. 11: alternative methods' fronts are 1.74x farther from the golden 5D front than Prospector's on average. Table 4 (fdtd-2d): alternatives need 35% more resources at equal latency targets; Prospector-1D up to 191% more. Case study: heterogeneous mixes beat all-large/all-small by up to 24% (fdtd-2d) and 20% (heat-3d).

## 11. Limitations
AUTHOR-STATED: GA/SA have limited multi-objective support. REVIEWER: BO budget and number of seeds not given, no variance; independent per-output GPs; P&R noise not studied; small exhaustively enumerable spaces; heterogeneous mixes evaluated by simulation plus summed resources, never co-implemented.

## 12. What the paper does NOT evaluate
Multi-fidelity or cost-aware acquisition; joint multi-kernel DSE or co-resident implementation; interaction residuals; transfer; implementation variability; energy; measured CPU-FPGA behaviour.

## 13. Relationship to our Studies (S99 S72 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | single-kernel DSE; mixes composed analytically |
| measured interactions | NO |  |
| staged evaluation | NO | one stage (HLS + P&R) |
| adaptive evidence acquisition | YES | multi-objective BO with PESMO |
| cost/fidelity modeling | NO | uniform cost |
| lifecycle/configuration cost | PARTIAL | reconfiguration amortization discussed, not modelled in DSE |
| physical implementation in the loop | YES | place-and-route per evaluated design |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | NOT_REPORTED |  |
| energy/power | NO |  |
| CPU-FPGA interaction | PARTIAL | simulated CPU + coherent integrated FPGA |
| memory/data movement | PARTIAL | array partitioning; simulated shared-L2 model |

## 14. Possible overlap
METHOD FOUNDATIONAL

## 15. Possible research gap (not a novelty claim)
S99: PESMO/GP BO is the single-source acquisition baseline the multi-source local-vs-joint policy must extend and beat at equal cost. S72: BO arm with 5D objectives; its 1.74x advantage comes from small single-kernel spaces with unspecified budget. Its additive accelerator-mix assumption is another unchecked instance of what S97 tests.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED (third-party Spearmint PESM branch).
