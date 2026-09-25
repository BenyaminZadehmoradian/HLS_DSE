# RW0010 — CollectiveHLS: A Collaborative Approach to High-Level Synthesis Design Optimization

> **Relevance (2026-09-25 correction audit): SUPPORTING** — HLS DSE method listed as an S71 external-baseline candidate. Primary Studies: S71 S72. Prior-art boundary: PRIOR ART.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Ferikoglou, Aggelos; Kakolyris, Andreas; Masouros, Dimosthenis; Soudris, Dimitrios; Xydis, Sotirios
- Year / venue: 2024 / ACM TRETS
- DOI: 10.1145/3702005 · URL: https://doi.org/10.1145/3702005
- Metadata source: Published PDF first page (ACM TRETS 18(1), Article 11, Dec 2024) + Semantic Scholar/dblp

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (published)
- Canonical path: `related_work/papers/hls_dse/RW0010_Ferikoglou2024_CollectiveHLS_TRETS.pdf`
- SHA-256: `91a853ae675cd3dce59b1d22663d808f3453a8a6f99f9296f68913ec98e963a5`
- Source: https://web.archive.org/web/20250218071710id_/https://dl.acm.org/doi/pdf/10.1145/3702005

## Code / dataset / artifact provenance
Code: https://github.com/aferikoglou/CollectiveHLS (found via web; paper itself does not print the link). Open access CC BY 4.0.

## 1. Research question
Rapidly proposing latency-optimized, synthesizable HLS directive configurations for unseen applications without per-application QoR models or long meta-heuristic searches.

## 2. Problem setting
Knowledge-based HLS directive auto-tuning for single kernels, latency minimization under device resource feasibility, on a Xilinx MPSoC.

## 3. Search space
HLS directives at action points (loops, arrays, functions): pipeline, unroll, array_partition (as extracted by LLVM/Clang source analysis)

## 4. Evaluation method
Xilinx Vitis HLS 2021.1 synthesis reports (latency in cycles; BRAM/DSP/FF/LUT %), leave-one-out evaluation; feasibility = fits device resources / completes HLS within time limit

## 5. Benchmarks
~56-60 applications from Rodinia (RodiniaHLS), MachSuite and GitHub HLS repositories; case study on an MLP generator kernel; subset vs ScaleHLS

## 6. Hardware
Xilinx Zynq UltraScale+ MPSoC ZCU104 (300 MHz target)

## 7. Toolchain
Xilinx Vitis HLS 2021.1; LLVM 14.0.5; PyMOO NSGA-II

## 8. Metrics
Geometric-mean latency speedup vs no-directive Vitis baseline; synthesizability and feasibility rates; inference/optimization time; normalized resource efficiency

## 9. Baselines
Vitis default, Vitis_Opt, benchmark hand-tuned (Tuned), resource over-provisioning (MAX), knowledge-based SotA (KBOpt, Ferretti et al.), NSGA-II synthesis DSE (GenOpt), application-specific XGBoost model-based DSE (ModelOpt), ScaleHLS

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: average geometric-mean speedup up to 23.1x over source without directives, 100% synthesizability and 96.6% feasibility, and designs of comparable quality 14.6x faster on average than genetic-algorithm DSE and SotA approaches.

## 11. Limitations
Latency-focused (resources as feasibility constraints); HLS-report-level evaluation only; global cluster-level directive assignment lacks fine-tuning (lower synthesizability without re-proposal); knowledge base requires expensive offline NSGA-II characterization; slightly lower quality than application-specific model-based DSE (11% lower speedup).

## 12. What the paper does NOT evaluate
Post-place-and-route timing/resources, on-board execution, power/energy, multi-kernel system interactions, CPU-FPGA transfers.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S32 S34 S36 S37 S43 S45 S56 S71 S72 S73 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Each application optimized independently. |
| measured interactions | PARTIAL | Directive impact analysis per feature (e.g., Stencil 3D); no cross-kernel interaction. |
| staged evaluation | PARTIAL | Propose-then-synthesize with fallback re-proposal when non-synthesizable/infeasible. |
| adaptive evidence acquisition | NO | No iterative evidence acquisition online; offline NSGA-II characterization. |
| cost/fidelity modeling | PARTIAL | Reports optimization/inference time vs baselines; no fidelity model. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | NO | Vitis HLS synthesis reports only. |
| multi-benchmark transfer | YES | Core idea: transfer directive knowledge across applications; leave-one-out and knowledge-base ablation (Sec. 5.8). |
| decision/Pareto stability | PARTIAL | Robustness to removing applications from the knowledge base studied. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | PARTIAL | array_partition directives; no data-movement modeling. |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; adaptive evidence acquisition; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/aferikoglou/CollectiveHLS (found via web; paper itself does not print the link). Open access CC BY 4.0.

## Open questions / reviewer notes
ACM DL blocks scripted download (HTTP 403) although the article is CC-BY open access; the identical publisher PDF was retrieved via the Internet Archive Wayback Machine snapshot of the ACM PDF URL (title/DOI verified on page 1). Earlier short version: 'CollectiveHLS: Ultrafast Knowledge-Based HLS Design Optimization', IEEE Embedded Systems Letters vol. 16, 2024, DOI 10.1109/LES.2023.3330610.
