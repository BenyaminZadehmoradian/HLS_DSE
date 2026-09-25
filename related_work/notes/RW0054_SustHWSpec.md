# RW0054 — Sustainable Hardware Specialization

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Dangi, Pranav; Bandara, Thilini Kaushalya; Sheikhpour, Saeideh; Mitra, Tulika; Eeckhout, Lieven
- Year / venue: 2024 / ICCAD
- DOI: 10.1145/3676536.3676777 · URL: https://doi.org/10.1145/3676536.3676777
- Metadata source: PDF first page (ICCAD '24 copyright block, DOI) + web search (also arXiv 2411.09315)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/energy_sustainability/RW0054_Dangi2024_SustHWSpec_ICCAD.pdf`
- SHA-256: `62ee8d8e756cab136829c8a6ee8f7f80fbfd3b5ed96d8265c5553a585ee02bc4`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/Sustainable_Hardware_Specialization_2024.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Dark-silicon style seas of dedicated accelerators raise embodied carbon; can a reconfigurable fabric amortize embodied footprint across kernels and be more sustainable?

## 2. Problem setting
SoC-level comparison of N domain-specific accelerators (ASIC DSAs) vs one reconfigurable fabric (CGRA) using FOCAL proxies.

## 3. Search space
Number of DSAs replaced, alpha (embodied/operational weight), relative DSA area/energy; iso-performance DSA design points

## 4. Evaluation method
RTL synthesis of CGRA (40 nm, 100 MHz) + Morpher mapping for performance; Aladdin (40 nm) for DSA area/power; analytical carbon model.

## 5. Benchmarks
MachSuite kernels (GeMM, KNN, Conv2D, Stencil3D, Viterbi, FFT, FIR, AES) with Visual Wake Words-sized inputs

## 6. Hardware
Modeled: 8x8 CGRA and ASIC DSAs in UMC 40 nm

## 7. Toolchain
Morpher CGRA compiler, Aladdin, ASIC synthesis (tool versions NOT_REPORTED)

## 8. Metrics
Normalized carbon footprint, area, energy, critical DSA count

## 9. Baselines
Sea of dedicated ASIC DSAs

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: reconfigurable fabric is more sustainable; as few as a handful to a dozen accelerators can be replaced by a CGRA; replacing a sea of accelerators with a CGRA reduces environmental footprint by 2.5x to 7.6x.

## 11. Limitations
Abstract model; Aladdin estimates; single technology node and iso-performance point; CGRA not FPGA.

## 12. What the paper does NOT evaluate
FPGA fabrics; reconfiguration time/energy; HLS DSE; measured silicon.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S85 S86 S94
- Partial (dimension = PARTIAL): S07 S15 S43 S45 S59 S61 S65 S73 S78 S81 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Considers concurrent kernels per application sharing a fabric (conservatively n-times area). |
| measured interactions | NO |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | YES | Embodied footprint amortization via reconfiguration across kernels. |
| physical implementation in the loop | PARTIAL | CGRA RTL synthesis; no P&R reported. |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | PARTIAL | Sensitivity of CDC to alpha/A/E and iso-performance point discussed. |
| energy/power | YES | Energy from synthesis/Aladdin. |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | Shared 256 KB banked memory modeled for CGRA. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Also on arXiv as 2411.09315.
