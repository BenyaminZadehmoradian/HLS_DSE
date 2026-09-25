# RW0084 — Pipeline-Stage-Resolved Timing Characterization of FPGA and ASIC Implementations of a RISC-V Processor

> **Relevance (2026-09-25 full-text review): SUPPORTING** — A 30-seed place-and-route sweep of one fixed RTL design on an AMD 20 nm UltraScale device, reporting the Fmax range and per-stage slack spread: weak but direct empirical support for the S81 implementation-variability noise floor. Hand-written RTL on a different device family, so only an order-of-magnitude reference for S81/S98. Primary Studies: S81 S98. Prior-art boundary: RELEVANT BUT DIFFERENT.
> **Identity:** Sole author Mostafa Darvishi (ETS Montreal / Evolution Optiks R&D). Manuscript 'Submitted To IEEE Transactions on VLSI Systems, TVLSI-01194-2025' (under review); arXiv 2512.13866. FPGA device AMD XQRKU060 (20 nm).

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Darvishi, Mostafa
- Year / venue: 2025 / arXiv 2512.13866 (submitted to IEEE TVLSI)
- DOI: none recorded · URL: https://arxiv.org/abs/2512.13866

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv (submitted to IEEE TVLSI)
- Canonical path: `related_work/papers/physical/RW0084_Darvishi2025_SeedTiming_arXiv.pdf` (local only, gitignored)
- SHA-256: `30cb2c4899ea239c210b0b34ed1bccacf96bb489ce8687685c2869edddf3f112`
- Source: https://arxiv.org/pdf/2512.13866

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
How do timing behaviour and timing variability of the same RV32I five-stage RISC-V core differ between a 20 nm FPGA and a 7 nm FinFET ASIC, per pipeline-stage transition and by logic/routing/clock delay?

## 2. Problem setting / 3. Search space / 4. Evaluation method
One synthesisable Verilog RV32I five-stage core with identical RTL on both platforms. FPGA: timing-driven synthesis, place-and-route with 30 randomised tool seeds under identical constraints, post-route STA; paths decomposed into logic/routing/clocking and binned per pipeline transition. ASIC: commercial 7 nm FinFET flow, MMMC STA with AOCV/LVF.

## 5. Benchmarks
One design: a generic RV32I five-stage RISC-V core.

## 6. Hardware
AMD XQRKU060 RT Kintex UltraScale (20 nm); unnamed commercial 7 nm FinFET library.

## 7. Toolchain
NOT_REPORTED by name ('vendor-signoff models'); seed mechanism, directives and clock constraint NOT_REPORTED.

## 8. Metrics
Fmax distribution across seeds; critical-path delay; delay split routing/logic/clock; per-stage slack standard deviation; ASIC frequency per corner.

## 9. Baselines
None (FPGA vs ASIC comparison).

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 30 place-and-route seeds. FPGA Fmax 472-510 MHz, mean 493 MHz (Fig. 5, Table 1): ~38 MHz envelope (~7.7% of mean peak-to-peak); no Fmax standard deviation. Critical path 1.96 ns (EX->MEM); routing 62-74% of delay. Per-stage slack std across seeds: IF->ID ~120 ps, ID->EX ~160 ps, EX->MEM ~210 ps, MEM->WB ~130 ps; asymmetric, heavy-tailed. ASIC: 1.85 GHz TT, 1.63 GHz SS; LVF slack std 8-17 ps.

## 11. Limitations
AUTHOR-STATED: only a five-stage in-order core. REVIEWER: single author and single design; tools, versions, clock constraint and seed mechanism unnamed (not reproducible); statistics internally inconsistent (a 210 ps slack std on a ~2 ns path would imply an Fmax spread beyond the reported 38 MHz; Table 1 '±38 MHz' vs text '38 MHz envelope'); histograms only; 20 nm UltraScale, not 28 nm 7-series; not HLS; seed noise on one netlist only.

## 12. What the paper does NOT evaluate
HLS designs; 7-series/Zynq; multiple designs or utilisation levels; directive/tool-version variability; confidence intervals; on-board timing; power; DSE or decision stability.

## 13. Relationship to our Studies (S81 S98)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | one processor core |
| measured interactions | NO |  |
| staged evaluation | NO | post-route STA only |
| adaptive evidence acquisition | NO |  |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | YES | post-route STA over 30 place-and-route seeds |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | PARTIAL | seed-induced Fmax/slack dispersion (472-510 MHz; slack std 120-210 ps), not linked to decisions; internally inconsistent |
| energy/power | NO |  |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | BRAM/LUTRAM effects on MEM-stage timing discussed qualitatively |

## 14. Possible overlap
RELEVANT BUT DIFFERENT

## 15. Possible research gap (not a novelty claim)
For S81/S98 only an order-of-magnitude prior: on one fixed netlist, 30 seeds gave ~8% peak-to-peak Fmax spread, so joint-minus-local timing residuals of a few percent may lie inside seed noise. S81 must measure its own seed noise floor on xc7z020 with HLS kernels; this number must not be used as the S98 threshold. It supports comparing residuals against a measured seed distribution rather than single runs.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
