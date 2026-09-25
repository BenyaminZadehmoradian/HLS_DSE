# RW0063 — COSMOS: Coordination of High-Level Synthesis and Memory Optimization for Hardware Accelerators

> **Relevance (2026-09-25 full-text review): CORE** — COSMOS jointly chooses HLS knobs (unrolls, PLM ports) of the 12+ components of one accelerator (WAMI) under a system throughput target while minimizing total area: boundary (a). It composes per-component characterizations analytically (TMG cycle time plus summed area) and never synthesizes or implements the composed system, i.e. exactly the local-evidence-only approach the central question challenges. Primary Studies: S97 S98 S99 S72 S04. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Read the arXiv version (1912.10823); its header 'Article 1 (December 2017)' is a placeholder. Presented at CODES+ISSS 2017, ESWEEK-TECS special issue. Matches the registry.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Piccolboni, Luca; Mantovani, Paolo; Di Guglielmo, Giuseppe; Carloni, Luca P.
- Year / venue: 2017 / ACM TECS 16(5s) Art. 150 (CODES+ISSS 2017)
- DOI: none recorded · URL: https://arxiv.org/abs/1912.10823

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv
- Canonical path: `related_work/papers/core/RW0063_Piccolboni2017_COSMOS_TECS_arxiv.pdf` (local only, gitignored)
- SHA-256: `bdabfd90e240dd7d403ab91a717bf4bef86cf7f0eb2067cb96c17be33097519c`
- Source: https://arxiv.org/pdf/1912.10823

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
System-level DSE for accelerators made of many HLS components with exponential knob combinations and unpredictable HLS; obtain the system area-vs-throughput Pareto curve with few HLS invocations.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Component characterization (Alg. 1): per PLM port count (1..16) synthesize the max-latency/min-area and min-latency/max-area extremes (lambda-constraint, Eq. 1), giving rectangular regions; PLM area from the Mnemosyne generator added. Synthesis planning: theta-constrained LP over a timed-marked-graph system model, min sum f_i(tau_i) s.t. A*sigma + M0/theta >= tau (Eq. 2), f_i convex piecewise-linear; theta swept by (1+delta). Mapping via an Amdahl-law inverse (Eqs. 4-5). COMPOSITION OPERATOR: system cost = SUM of component areas (logic + PLM); throughput = 1 / TMG minimum cycle time from component effective latencies; latency-insensitive 256-bit channels, communication not explored.

## 5. Benchmarks
One case study: WAMI accelerator (PERFECT suite; ~7000 lines SystemC; Debayer, Grayscale, Gradient, Hessian, SD-Update, Matrix ops, Steepest-Descent, Change-Detection, Warp).

## 6. Hardware
Industrial 32 nm ASIC library (SRAM PLMs); FPGA possible but not evaluated.

## 7. Toolchain
Cadence C-to-Silicon, Mnemosyne, GLPK.

## 8. Metrics
Component effective latency and area, system throughput (frames/s), latency/area span, HLS invocations, planned-vs-mapped area mismatch.

## 9. Baselines
'No Memory' characterization (dual-port memories only); exhaustive per-component knob synthesis (invocation count only).

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table 1 average latency span 4.06x and area span 2.58x vs 1.73x/1.22x without memory co-design. Fig. 11: HLS invocations reduced 6.7x on average, up to 14.6x per component vs exhaustive per-component synthesis. Fig. 10: planned vs mapped area mismatch 0.1-2.5% for most points, 11.9% and 13.0% for two points. System-level combinations exceed 9e12.

## 11. Limitations
AUTHOR-STATED: TMGs cannot capture data-dependent behaviour; the lambda-constraint does not guarantee Pareto-optimal points and discards some; LP curve is theoretical; interconnect not explored. REVIEWER: 'mapped' system points are still sums of individually synthesized components plus TMG throughput; the integrated accelerator is never synthesized/implemented, so the 13% is a planning error, not a composition error. 'As complete as exhaustive search' refers only to per-component invocation counts; no system-level exhaustive search is run. Single ASIC case study, no layout, no variance.

## 12. What the paper does NOT evaluate
Joint synthesis/implementation of the composed accelerator; composed-vs-joint comparison; whether per-component pruning drops system-optimal combinations; FPGA, P&R, timing closure, congestion, contention; power; variability; other benchmarks.

## 13. Relationship to our Studies (S97 S98 S99 S72 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | joint knob choice via LP, but compositional evaluation (summed area + TMG throughput); no joint synthesis |
| measured interactions | NO | components assumed independent apart from TMG timing |
| staged evaluation | PARTIAL | characterization then targeted mapping synthesis, same HLS fidelity |
| adaptive evidence acquisition | PARTIAL | LP plans which component syntheses to run; deterministic, not value-driven |
| cost/fidelity modeling | PARTIAL | HLS invocations as cost; no fidelity model |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NO | HLS logic area + generated PLM area on 32 nm ASIC |
| multi-benchmark transfer | NO | single case study |
| decision/Pareto stability | NO |  |
| energy/power | NO |  |
| CPU-FPGA interaction | NO | software component modelled as fixed latency |
| memory/data movement | YES | datapath/PLM co-design is central; interconnect bandwidth fixed |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
S97: prior art for local characterization + additive/TMG composition that never tests the composition against a jointly synthesized system; its 0.1-13% mismatch must not be cited as composition fidelity. ASIC numbers do not transfer to xc7z020 post-route. S99/S72: the LP 'plan local syntheses' planner is the natural local-evidence-only baseline.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
