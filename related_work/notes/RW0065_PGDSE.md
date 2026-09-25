# RW0065 — Efficient System-Level Design Space Exploration for High-Level Synthesis Using Pareto-Optimal Subspace Pruning

> **Relevance (2026-09-25 full-text review): CORE** — Jointly selects alternatives for dozens of HLS multicycle computations across up to 10 components under shared timing and frequency constraints: boundary (a). Its PSP step is a local per-MCC Pareto pruning claimed not to remove the best system configurations, evaluated only by recombining pre-characterized per-MCC data, never by implementing systems jointly. Primary Studies: S97 S72 S04. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Correct: ASP-DAC '23, pp. 567-572, DOI 10.1145/3566097.3567841. The Arizona repository cover sheet cites a different paper (GLSVLSI 2024) and lists IEEE as publisher; ignore those cover-sheet fields.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Liao, Yuchao; Adegbija, Tosiron; Lysecky, Roman
- Year / venue: 2023 / ASP-DAC 2023, pp. 567-572
- DOI: 10.1145/3566097.3567841 · URL: https://doi.org/10.1145/3566097.3567841

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: published (University of Arizona repository copy)
- Canonical path: `related_work/papers/core/RW0065_Liao2023_PGDSE_ASPDAC.pdf` (local only, gitignored)
- SHA-256: `7febed14089e4a59246d0ff0ac0a2b03c2c16b584b2d56403d2283b5ec35a6a4`
- Source: https://repository.arizona.edu/handle/10150/674670

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Post-HLS system-level DSE for timing-constrained multi-component, multi-MCC embedded systems (spaces up to 1e104).

## 2. Problem setting / 3. Search space / 4. Evaluation method
Periodic State Machines containing MCCs with HLS alternatives. PSP (Alg. 1): per global frequency combination, assign valid frequencies, scale energy, prune each MCC to its (E, A) Pareto set. PEGA (Alg. 2): parallel GA with Pareto elitism per frequency combination. COMPOSITION OPERATOR: not formally stated; implicit aggregation of per-MCC energy/area (consistent with a sum); timing enforced per PSM period.

## 5. Benchmarks
ADAS subsystem (10 PSMs, 52 MCCs, 244 alternatives; 7.12e66 configurations) and three synthetic systems recombining a database of HLS/Vivado MCC records (2.61e11, 1.71e49, 1.49e104).

## 6. Hardware
Xilinx Artix-7 (source of per-MCC data); exploration in C++ on a 44-core host.

## 7. Toolchain
Xilinx Vitis HLS / Vivado for per-MCC data; PG-DSE in C++.

## 8. Metrics
Design-space size before/after pruning, system energy and area, ADRS vs reference set, runtime.

## 9. Baselines
GA of Gao & Carrion Schafer (ISCAS 2021); unpruned/serial/parallel PG-DSE. References: exhaustive search (Synth1 only), exhaustive search of the PSP-pruned space (Synth2), long GA runs (Synth3, ADAS).

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: PSP reduces spaces by 2.72e9x (Synth1, to 96 configurations), 4.43e37x, 1.51e80x, 1.68e49x (ADAS). On Synth1 pruned search reproduces the exhaustive front (ADRS 0) vs 0.29% for the prior GA. Average ADRS improvement over the prior GA 40.2x / 58.1x / 66.2x (unpruned / serial / parallel); parallel version cuts runtime 82.6%.

## 11. Limitations
AUTHOR-STATED: homogeneous PSM-level timing only; subsystem interactions left to future work. REVIEWER: 'no loss from pruning' verified only on Synth1 (27 alternatives); Synth2 reference is circular (exhaustive over the already pruned space); Synth3/ADAS references are GA runs; systems are recombinations of per-MCC records, never jointly synthesized or implemented; composition operator and per-MCC fidelity unstated; energy model not validated on hardware.

## 12. What the paper does NOT evaluate
Joint HLS/implementation of any composed system; composed-vs-measured comparison; loss of system-optimal designs under non-additive effects (shared resources, routing, clocking); board energy; variability.

## 13. Relationship to our Studies (S97 S72 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | joint selection, analytical recombination of per-MCC data |
| measured interactions | NO | explicitly deferred to future work |
| staged evaluation | PARTIAL | prune-then-search over precomputed data |
| adaptive evidence acquisition | NO | GA over a precomputed table |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NOT_REPORTED | per-MCC data 'implemented with Vivado' but fidelity unstated; systems never implemented |
| multi-benchmark transfer | PARTIAL | four systems, no knowledge transfer |
| decision/Pareto stability | NO | ADRS averaged over five runs only |
| energy/power | YES | primary objective via frequency-scaled power x time model |
| CPU-FPGA interaction | NO |  |
| memory/data movement | NO |  |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
S97: PSP is a recent local-Pareto-pruning rule claimed lossless, with lossless evidence from one small synthetic system under the paper's own composed model; S97's exhaustive joint oracle directly tests that claim. S72: PEGA is a relevant search baseline but its ADRS gains rest on weak/circular references.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
