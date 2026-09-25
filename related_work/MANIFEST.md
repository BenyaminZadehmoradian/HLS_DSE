# Related Work Manifest — HLS-DSE V23.2 (corrected 2026-09-25)

This inventory is repository-derived from `RELATED_WORK_REGISTRY.csv`, `EXCLUSION_REGISTER.csv` and
`PDF_PROVENANCE.csv`. The collection is curated. **It is not a systematic review.**

## Relevance gate (88 papers reviewed)

| Class | Count | Where recorded |
|---|---|---|
| CORE | 6 | registry; PDFs in `papers/core/` |
| SUPPORTING | 30 | registry; PDFs in `papers/<category>/` |
| HOLD | 29 | registry (metadata only; abstract-only review; 23 added by the 2026-09-25 web search) |
| ADJACENT | 20 | `EXCLUSION_REGISTER.csv` (not canonical) |
| EXCLUDE | 3 | `EXCLUSION_REGISTER.csv` (not canonical) |

## Canonical PDFs

- 36 canonical PDFs, all **local only** (gitignored; the repository is public). **0 PDFs are tracked by git.**
- Metadata only: 29 (the HOLD papers). The 6 original HOLD papers have no legitimate open copy; several of the 23 added
  2026-09-25 do have open copies (arXiv/author sites) that were not downloaded — see `pdf_availability`.
- The reported open license of each paper's open-access version is in the registry column `license_reported`.
  A reported open license does not change the local-only policy.

| Category (canonical) | Papers | PDFs |
|---|---|---|
| core | 6 | 6 |
| concurrent_multikernel | 2 | 2 |
| hls_dse | 13 | 13 |
| multifidelity | 3 | 3 |
| bo_mobo | 2 | 2 |
| physical | 1 | 1 |
| lifecycle_dfx | 3 | 3 |
| energy_sustainability | 6 | 6 |

## Canonical inventory

| ID | Key | Year | Venue | Class | Category | Canonical PDF | SHA-256 (prefix) | Review | Prior-art label | Primary Studies |
|---|---|---|---|---|---|---|---|---|---|---|
| RW0006 | CMMFO | 2021 | DATE | CORE | core | `core/RW0006_Sun2021_CMMFO_DATE_accepted.pdf` | 6de6884b3a23 | full text | PRIOR ART | S04 S05 S07 S21 S23 |
| RW0011 | StreamHLS | 2025 | FPGA | CORE | core | `core/RW0011_Basalama2025_StreamHLS_FPGA.pdf` | 83570565411d | full text | PARTIAL OVERLAP | S15 S65 S36 |
| RW0031 | Prometheus | 2025 | ACM TODAES | CORE | core | `core/RW0031_Pouget2025_Prometheus_TODAES.pdf` | 2027336b4b0a | full text | PARTIAL OVERLAP | S15 S65 S66 |
| RW0033 | FIFOAdvisor | 2026 | ASP-DAC | CORE | core | `core/RW0033_AbiKaram2026_FIFOAdvisor_ASPDAC.pdf` | 8f57ad7f0cf5 | full text | PARTIAL OVERLAP | S15 S36 S65 |
| RW0037 | FADO | 2023 | FPGA | CORE | core | `core/RW0037_Du2023_FADO_FPGA_arxiv.pdf` | 4e63512b5bd8 | full text | PARTIAL OVERLAP | S15 S65 S78 |
| RW0050 | EtoEDSE | 2024 | IEEE TCAD | CORE | core | `core/RW0050_Liao2024_EtoEDSE_TCAD_arxiv.pdf` | db1a8c2a44ff | full text | PARTIAL OVERLAP | S15 S65 S66 |
| RW0001 | CRYPTONITE | 2025 | IEEE ASAP | SUPPORTING | hls_dse | `hls_dse/RW0001_Maheswaran2025_CRYPTONITE_ASAP_arxiv.pdf` | 50310049e0a1 | full text | RELEVANT BUT DIFFERENT | S66 S65 |
| RW0003 | MultiFPGAAlloc | 2019 | DAC | SUPPORTING | concurrent_multikernel | `concurrent_multikernel/RW0003_Shan2019_MultiFPGAAlloc_DAC_accepted.pdf` | 07bce8536ccb | full text | RELEVANT BUT DIFFERENT | S95 S15 |
| RW0004 | EnergyOptAlloc | 2022 | IEEE TCAD | SUPPORTING | concurrent_multikernel | `concurrent_multikernel/RW0004_Shan2022_EnergyOptAlloc_TCAD_accepted.pdf` | e52ff84e7a15 | full text | RELEVANT BUT DIFFERENT | S95 S19 |
| RW0008 | HLSFactory | 2024 | MLCAD | SUPPORTING | hls_dse | `hls_dse/RW0008_AbiKaram2024_HLSFactory_MLCAD_arxiv.pdf` | d4a8be4b378d | full text | METHOD FOUNDATIONAL | S71 S90 S80 |
| RW0009 | HierQoR | 2024 | DATE | SUPPORTING | multifidelity | `multifidelity/RW0009_Gao2024_HierQoR_DATE_arxiv.pdf` | 27f0e3e78596 | full text | METHOD FOUNDATIONAL | S04 S21 S89 |
| RW0010 | CollectiveHLS | 2024 | ACM TRETS | SUPPORTING | hls_dse | `hls_dse/RW0010_Ferikoglou2024_CollectiveHLS_TRETS.pdf` | 91a853ae675c | full text | PRIOR ART | S71 S72 |
| RW0012 | MTBO | 2013 | NeurIPS (NIPS 2013) | SUPPORTING | multifidelity | `multifidelity/RW0012_Swersky2013_MTBO_NeurIPS.pdf` | 294123432b98 | full text | METHOD FOUNDATIONAL | S07 S10 S11 |
| RW0013 | CMOBOOCE | 2025 | AISTATS 2025 (PMLR 258) | SUPPORTING | bo_mobo | `bo_mobo/RW0013_Li2025_CMOBOOCE_AISTATS.pdf` | ea366cbae1c5 | full text | METHOD FOUNDATIONAL | S14 S72 |
| RW0014 | CoopBO | 2025 | Structural and Multidiscipl… | SUPPORTING | bo_mobo | `bo_mobo/RW0014_Pretsch2025_CoopBO_SMO.pdf` | 62192a8fbea6 | full text | METHOD FOUNDATIONAL | S15 S65 |
| RW0017 | AutoDSE | 2022 | ACM TODAES | SUPPORTING | hls_dse | `hls_dse/RW0017_Sohrabizadeh2022_AutoDSE_TODAES.pdf` | 6e32d9176c76 | full text | PRIOR ART | S71 S72 |
| RW0018 | Chimera | 2022 | arXiv (extended version of … | SUPPORTING | hls_dse | `hls_dse/RW0018_Yu2022_Chimera_arXiv.pdf` | 9be54035dfb9 | full text | PARTIAL OVERLAP | S05 S72 |
| RW0019 | GNNDSE | 2022 | DAC | SUPPORTING | hls_dse | `hls_dse/RW0019_Sohrabizadeh2022_GNNDSE_DAC.pdf` | d6410662a86c | full text | PRIOR ART | S71 S89 S10 |
| RW0020 | AutoHLS | 2023 | IEEE MWSCAS | SUPPORTING | hls_dse | `hls_dse/RW0020_Ahmed2023_AutoHLS_MWSCAS_arxiv.pdf` | 252730fe15bf | full text | PRIOR ART | S71 S88 |
| RW0021 | HARP | 2023 | ICCAD | SUPPORTING | hls_dse | `hls_dse/RW0021_Sohrabizadeh2023_HARP_ICCAD.pdf` | 7471b30ba41a | full text | METHOD FOUNDATIONAL | S89 S10 |
| RW0023 | HLSyn | 2023 | NeurIPS (Datasets and Bench… | SUPPORTING | hls_dse | `hls_dse/RW0023_Bai2023_HLSyn_NeurIPS.pdf` | 9797c1e70e9e | full text | METHOD FOUNDATIONAL | S71 S90 S02 |
| RW0026 | TaskTransfer | 2024 | ICCAD | SUPPORTING | hls_dse | `hls_dse/RW0026_Ding2024_TaskTransfer_ICCAD.pdf` | 16ccd89b86d0 | full text | PARTIAL OVERLAP | S10 S11 S87 |
| RW0030 | NLPDSE | 2025 | ACM TODAES | SUPPORTING | hls_dse | `hls_dse/RW0030_Pouget2025_NLPDSE_TODAES.pdf` | 34b85a725f66 | full text | PRIOR ART | S71 S72 |
| RW0032 | Sisyphus | 2025 | FPGA | SUPPORTING | hls_dse | `hls_dse/RW0032_Pouget2025_Sisyphus_FPGA_arxiv.pdf` | ff9f6545572f | full text | PRIOR ART | S71 S75 |
| RW0035 | PatternDSE | 2026 | ICECCME (arXiv preprint) | SUPPORTING | hls_dse | `hls_dse/RW0035_Zhang2026_PatternDSE_ICECCME_arxiv.pdf` | bacd9ce5f87e | full text | PARTIAL OVERLAP | S57 S88 |
| RW0036 | QoRML | 2018 | FCCM | SUPPORTING | multifidelity | `multifidelity/RW0036_Dai2018_QoRML_FCCM_accepted.pdf` | a51995b15e30 | full text | METHOD FOUNDATIONAL | S04 S21 S89 |
| RW0042 | HLPSDSE | 2025 | ICCAD | SUPPORTING | physical | `physical/RW0042_Du2025_HLPSDSE_ICCAD.pdf` | d0bcec56bd13 | full text | RELEVANT BUT DIFFERENT | S78 S61 |
| RW0043 | DPRSurvey | 2018 | ACM Computing Surveys | SUPPORTING | lifecycle_dfx | `lifecycle_dfx/RW0043_Vipin2018_DPRSurvey_CSUR_accepted.pdf` | 1c448e055d98 | full text | METHOD FOUNDATIONAL | S85 S86 |
| RW0044 | FOS | 2020 | ACM TRETS | SUPPORTING | lifecycle_dfx | `lifecycle_dfx/RW0044_Vaishnav2020_FOS_TRETS_arxiv.pdf` | ba7485013bf6 | full text | RELEVANT BUT DIFFERENT | S85 S86 S84 |
| RW0045 | PLD | 2022 | ASPLOS | SUPPORTING | lifecycle_dfx | `lifecycle_dfx/RW0045_Xiao2022_PLD_ASPLOS.pdf` | 17a42a757d21 | full text | RELEVANT BUT DIFFERENT | S85 S94 |
| RW0046 | Bonamy12DPR | 2012 | ReConFig | SUPPORTING | energy_sustainability | `energy_sustainability/RW0046_Bonamy2012_Bonamy12DPR_ReConFig.pdf` | e29c6b640f4d | full text | METHOD FOUNDATIONAL | S86 S19 |
| RW0047 | Nafkha17DPR | 2016 | ISWCS | SUPPORTING | energy_sustainability | `energy_sustainability/RW0047_Nafkha2016_Nafkha17DPR_ISWCS_arxiv.pdf` | 9dfeed771286 | full text | METHOD FOUNDATIONAL | S86 S19 |
| RW0048 | HLPow | 2020 | ASP-DAC | SUPPORTING | energy_sustainability | `energy_sustainability/RW0048_Lin2020_HLPow_ASPDAC_arxiv.pdf` | c6b1774761ca | full text | PARTIAL OVERLAP | S19 |
| RW0052 | GreenFPGA | 2024 | DAC | SUPPORTING | energy_sustainability | `energy_sustainability/RW0052_ChoppaliSudarshan2024_GreenFPGA_DAC_arxiv.pdf` | 4eecc1572a26 | full text | RELEVANT BUT DIFFERENT | S20 S94 |
| RW0053 | IdleSleep | 2024 | ARCS (LNCS 14842) | SUPPORTING | energy_sustainability | `energy_sustainability/RW0053_Qian2024_IdleSleep_ARCS_arxiv.pdf` | 53963a987e44 | full text | RELEVANT BUT DIFFERENT | S85 S86 |
| RW0057 | CORDOBA | 2025 | HPCA | SUPPORTING | energy_sustainability | `energy_sustainability/RW0057_Elgamal2025_CORDOBA_HPCA.pdf` | 4e44ebf0b94e | full text | METHOD FOUNDATIONAL | S20 S92 S43 |
| RW0002 | MVSym | 2023 | Integration, the VLSI Journ… | HOLD | concurrent_multikernel | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S84 S93 |
| RW0005 | DML | 2022 | IEEE Transactions on Comput… | HOLD | lifecycle_dfx | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S85 S93 |
| RW0007 | IronManPro | 2023 | IEEE TCAD | HOLD | hls_dse | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S71 S72 |
| RW0015 | VOISetBased | 2021 | Systems Engineering (Wiley/… | HOLD | bo_mobo | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S33 S03 |
| RW0016 | VOISystemDesign | 1986 | Information Processing & Ma… | HOLD | bo_mobo | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S33 |
| RW0022 | HGBODSE | 2023 | ICFPT | HOLD | hls_dse | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | UNRESOLVED | S72 S05 |
| RW0063 | COSMOS | 2017 | ACM TECS 16(5s) Art. 150 (CO… | HOLD | concurrent_multikernel | — (OPEN_COPY_AVAILABLE) | — | abstract | POTENTIAL OVERLAP | S97 S15 S66 |
| RW0064 | CompSLD12 | 2012 | DATE 2012, pp. 641-646 (Best… | HOLD | concurrent_multikernel | — (OPEN_COPY_AVAILABLE) | — | abstract | POTENTIAL OVERLAP | S97 S15 |
| RW0065 | PGDSE | 2023 | ASP-DAC 2023 | HOLD | concurrent_multikernel | — (NOT_CHECKED) | — | abstract | POTENTIAL OVERLAP | S97 S15 |
| RW0066 | MISO | 2017 | NeurIPS 2017 | HOLD | bo_mobo | — (OPEN_COPY_AVAILABLE) | — | abstract | METHOD FOUNDATIONAL | S99 S05 S16 S33 |
| RW0067 | MISCBO | 2019 | Structural and Multidiscipli… | HOLD | bo_mobo | — (NOT_CHECKED) | — | abstract | UNRESOLVED | S99 S14 |
| RW0068 | CBOMIS | 2026 | arXiv 2607.00865 | HOLD | bo_mobo | — (OPEN_COPY_AVAILABLE) | — | abstract | METHOD FOUNDATIONAL | S99 S14 |
| RW0069 | CMFBO | 2025 | arXiv 2503.01126 | HOLD | bo_mobo | — (OPEN_COPY_AVAILABLE) | — | abstract | METHOD FOUNDATIONAL | S99 S32 |
| RW0070 | Fovea | 2026 | arXiv 2608.03285 | HOLD | multifidelity | — (OPEN_COPY_AVAILABLE) | — | abstract | PARTIAL OVERLAP | S99 S16 S97 |
| RW0071 | SoberDSE | 2026 | arXiv 2603.00986 | HOLD | hls_dse | — (OPEN_COPY_AVAILABLE) | — | abstract | PARTIAL OVERLAP | S72 |
| RW0072 | Prospector | 2020 | ACM journal (DOI 10.1145/342… | HOLD | hls_dse | — (NOT_CHECKED) | — | abstract | PRIOR ART | S72 S71 |
| RW0073 | KuangMOBO | 2023 | ISEDA 2023 | HOLD | hls_dse | — (NOT_CHECKED) | — | abstract | PRIOR ART | S72 |
| RW0074 | Omega | 2026 | IEEE Transactions on Compute… | HOLD | lifecycle_dfx | — (NOT_CHECKED) | — | abstract | PARTIAL OVERLAP | S04 S97 S85 |
| RW0075 | MemIntfHost | 2021 | DATE 2021, pp. 1152-1155 | HOLD | concurrent_multikernel | — (NOT_CHECKED) | — | abstract | PARTIAL OVERLAP | S100 S73 |
| RW0076 | MemIntfHeSoC | 2022 | DATE 2022, pp. 1335-1340 | HOLD | concurrent_multikernel | — (NOT_CHECKED) | — | abstract | PARTIAL OVERLAP | S100 S73 |
| RW0077 | AXIBound | 2023 | IEEE Transactions on Compute… | HOLD | concurrent_multikernel | — (NOT_CHECKED) | — | abstract | PARTIAL OVERLAP | S100 S73 S49 |
| RW0078 | ZynqACP | 2013 | FPGAworld 2013 | HOLD | concurrent_multikernel | — (NOT_CHECKED) | — | abstract | RELEVANT BUT DIFFERENT | S100 S73 S84 |
| RW0079 | ZyCAP | 2014 | IEEE Embedded Systems Letter… | HOLD | lifecycle_dfx | — (OPEN_COPY_AVAILABLE) | — | abstract | RELEVANT BUT DIFFERENT | S85 S86 S12 |
| RW0080 | FADO2 | 2024 | ACM TRETS | HOLD | physical | — (OPEN_COPY_AVAILABLE) | — | abstract | PARTIAL OVERLAP | S98 S59 S15 |
| RW0081 | CMMFOJ | 2022 | ACM TODAES 27(4) Art. 31 | HOLD | multifidelity | — (OPEN_COPY_AVAILABLE) | — | abstract | PRIOR ART | S99 S21 S23 |
| RW0082 | MFHLS18 | 2018 | FPL 2018, pp. 272-279 | HOLD | multifidelity | — (NOT_CHECKED) | — | abstract | PRIOR ART | S99 S21 |
| RW0083 | MLDSEReview | 2025 | Integration, the VLSI Journa… | HOLD | hls_dse | — (LEGITIMATE_OPEN_COPY_NOT_FOUND) | — | abstract | METHOD FOUNDATIONAL | S71 S72 |
| RW0084 | SeedTiming | 2025 | arXiv 2512.13866 | HOLD | physical | — (OPEN_COPY_AVAILABLE) | — | abstract | RELEVANT BUT DIFFERENT | S81 S98 S04 |
| RW0085 | ASPO | 2025 | arXiv 2506.06817 | HOLD | bo_mobo | — (OPEN_COPY_AVAILABLE) | — | abstract | PARTIAL OVERLAP | S99 S87 |

Non-canonical papers (ADJACENT/EXCLUDE), with reasons and provenance, are in `EXCLUSION_REGISTER.csv`. Their full earlier
reviews remain in git history (commit 6a08f53).

## Duplicate handling

- HLSyn (RW0023): the local-library and NeurIPS open-access copies were byte-identical; one canonical copy is kept.
- AutoDSE (RW0017): an 11-page 2020 preprint (sha256 `25d253c6d114…`) is a different version. It is noted, not imported.
