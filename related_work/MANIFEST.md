# Related Work Manifest — HLS-DSE V23.2

Repository-derived inventory generated 2026-09-25 from `RELATED_WORK_REGISTRY.csv` and `PDF_PROVENANCE.csv`.
PDFs are stored locally under `related_work/papers/<category>/` and are **not committed** (public repository;
see `papers/.gitignore`). Verify a local copy with `sha256sum` against the registry.

## Totals (repository-derived)

| Item | Count |
|---|---|
| Registered papers | 62 |
| PDFs held locally (canonical copies) | 55 |
| — copied from the existing local library | 34 |
| — downloaded from open-access sources | 21 |
| Metadata only (paywalled, no legitimate open copy found) | 6 |
| Open access but PDF not stored (download blocked) | 1 |
| Reviewed from full text | 56 |
| Reviewed from abstract only | 6 |
| Metadata complete (authors, venue, URL and DOI) | 57 |
| Missing DOI (proceedings without DOI, arXiv-only, or unconfirmed) | 5 |

## Per category

| Category | Papers | PDFs |
|---|---|---|
| core | 1 | 1 |
| concurrent_multikernel | 4 | 3 |
| hls_dse | 22 | 19 |
| multifidelity | 3 | 3 |
| bo_mobo | 2 | 2 |
| physical | 6 | 6 |
| lifecycle_dfx | 4 | 3 |
| energy_sustainability | 14 | 14 |
| other | 6 | 4 |

## Inventory

| ID | Key | Year | Venue | Category | Canonical PDF | SHA-256 (prefix) | Review | Overlap | Related studies (direct) |
|---|---|---|---|---|---|---|---|---|---|
| RW0001 | CRYPTONITE | 2025 | IEEE ASAP | hls_dse | `hls_dse/RW0001_Maheswaran2025_CRYPTONITE_ASAP_arxiv.pdf` | 50310049e0a1 | full text | PARTIAL OVERLAP | S32 S34 S88 |
| RW0002 | MVSym | 2023 | Integration, the VLSI Journal | concurrent_multikernel | — (METADATA_ONLY_PAYWALLED) | — | abstract | PARTIAL OVERLAP | S19 S20 S83 S84 |
| RW0003 | MultiFPGAAlloc | 2019 | DAC | concurrent_multikernel | `concurrent_multikernel/RW0003_Shan2019_MultiFPGAAlloc_DAC_accepted.pdf` | 07bce8536ccb | full text | PARTIAL OVERLAP | S07 S15 S65 S73 |
| RW0004 | EnergyOptAlloc | 2022 | IEEE TCAD | concurrent_multikernel | `concurrent_multikernel/RW0004_Shan2022_EnergyOptAlloc_TCAD_accepted.pdf` | e52ff84e7a15 | full text | PARTIAL OVERLAP | S07 S15 S19 S20 S65 S73 |
| RW0005 | DML | 2022 | IEEE Transactions on Computers | lifecycle_dfx | — (METADATA_ONLY_PAYWALLED) | — | abstract | PARTIAL OVERLAP | S85 S86 S94 |
| RW0006 | CMMFO | 2021 | DATE | core | `core/RW0006_Sun2021_CMMFO_DATE_accepted.pdf` | 6de6884b3a23 | full text | PARTIAL OVERLAP | S04 S05 S06 S19 S20 S21 S23 S32 S33 S34 S59 S61 S72 S78 S81 S88 |
| RW0007 | IronManPro | 2023 | IEEE TCAD | hls_dse | — (METADATA_ONLY_PAYWALLED) | — | abstract | POTENTIAL OVERLAP | — |
| RW0008 | HLSFactory | 2024 | MLCAD | other | `other/RW0008_AbiKaram2024_HLSFactory_MLCAD_arxiv.pdf` | d4a8be4b378d | full text | PARTIAL OVERLAP | S59 S61 S78 S81 |
| RW0009 | HierQoR | 2024 | DATE | multifidelity | `multifidelity/RW0009_Gao2024_HierQoR_DATE_arxiv.pdf` | 27f0e3e78596 | full text | PARTIAL OVERLAP | S04 S06 S10 S11 S21 S59 S61 S72 S78 S81 S90 |
| RW0010 | CollectiveHLS | 2024 | ACM TRETS | hls_dse | `hls_dse/RW0010_Ferikoglou2024_CollectiveHLS_TRETS.pdf` | 91a853ae675c | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0011 | StreamHLS | 2025 | FPGA | concurrent_multikernel | `concurrent_multikernel/RW0011_Basalama2025_StreamHLS_FPGA.pdf` | 83570565411d | full text | PARTIAL OVERLAP | S02 S04 S06 S07 S15 S21 S36 S37 S56 S65 S72 |
| RW0012 | MTBO | 2013 | NeurIPS (NIPS 2013) | multifidelity | `multifidelity/RW0012_Swersky2013_MTBO_NeurIPS.pdf` | 294123432b98 | full text | PARTIAL OVERLAP | S04 S05 S06 S10 S11 S20 S21 S23 S33 S72 S90 |
| RW0013 | CMOBOOCE | 2025 | AISTATS 2025 (PMLR 258) | bo_mobo | `bo_mobo/RW0013_Li2025_CMOBOOCE_AISTATS.pdf` | ea366cbae1c5 | full text | POTENTIAL OVERLAP | — |
| RW0014 | CoopBO | 2025 | Structural and Multidisciplin… | bo_mobo | `bo_mobo/RW0014_Pretsch2025_CoopBO_SMO.pdf` | 62192a8fbea6 | full text | PARTIAL OVERLAP | S07 S15 S65 |
| RW0015 | VOISetBased | 2021 | Systems Engineering (Wiley/IN… | other | — (METADATA_ONLY_PAYWALLED) | — | abstract | PARTIAL OVERLAP | S04 S05 S06 S20 S21 S23 S33 S72 |
| RW0016 | VOISystemDesign | 1986 | Information Processing & Mana… | other | — (METADATA_ONLY_PAYWALLED) | — | abstract | POTENTIAL OVERLAP | — |
| RW0017 | AutoDSE | 2022 | ACM TODAES | hls_dse | `hls_dse/RW0017_Sohrabizadeh2022_AutoDSE_TODAES.pdf` | 6e32d9176c76 | full text | POTENTIAL OVERLAP | — |
| RW0018 | Chimera | 2022 | arXiv (extended version of ID… | hls_dse | `hls_dse/RW0018_Yu2022_Chimera_arXiv.pdf` | 9be54035dfb9 | full text | PARTIAL OVERLAP | S05 S20 S23 S33 |
| RW0019 | GNNDSE | 2022 | DAC | hls_dse | `hls_dse/RW0019_Sohrabizadeh2022_GNNDSE_DAC.pdf` | d6410662a86c | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0020 | AutoHLS | 2023 | IEEE MWSCAS | hls_dse | `hls_dse/RW0020_Ahmed2023_AutoHLS_MWSCAS_arxiv.pdf` | 252730fe15bf | full text | PARTIAL OVERLAP | S32 S34 S88 |
| RW0021 | HARP | 2023 | ICCAD | hls_dse | `hls_dse/RW0021_Sohrabizadeh2023_HARP_ICCAD.pdf` | 7471b30ba41a | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0022 | HGBODSE | 2023 | ICFPT | hls_dse | — (METADATA_ONLY_PAYWALLED) | — | abstract | PARTIAL OVERLAP | S19 S20 |
| RW0023 | HLSyn | 2023 | NeurIPS (Datasets and Benchma… | hls_dse | `hls_dse/RW0023_Bai2023_HLSyn_NeurIPS.pdf` | 9797c1e70e9e | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0024 | Balor | 2024 | ICCAD | hls_dse | `hls_dse/RW0024_Murphy2024_Balor_ICCAD.pdf` | 0101982c5232 | full text | POTENTIAL OVERLAP | — |
| RW0025 | HLPerf | 2024 | ACM TRETS | hls_dse | — (NOT_FOUND) | — | full text | PARTIAL OVERLAP | S02 S07 S15 S36 S37 S56 S65 |
| RW0026 | TaskTransfer | 2024 | ICCAD | hls_dse | `hls_dse/RW0026_Ding2024_TaskTransfer_ICCAD.pdf` | 16ccd89b86d0 | full text | PARTIAL OVERLAP | S05 S10 S11 S20 S23 S33 S90 |
| RW0027 | Iceberg | 2025 | ICLAD | hls_dse | `hls_dse/RW0027_Ding2025_Iceberg_ICLAD.pdf` | ae8c9505e905 | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0028 | LIFT | 2025 | arXiv | hls_dse | `hls_dse/RW0028_Prakriya2025_LIFT_arXiv.pdf` | 921d038cefa1 | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0029 | LLMDSE | 2025 | arXiv | hls_dse | `hls_dse/RW0029_Wang2025_LLMDSE_arXiv.pdf` | 5d75eca169c9 | full text | PARTIAL OVERLAP | S05 S20 S23 S33 |
| RW0030 | NLPDSE | 2025 | ACM TODAES | hls_dse | `hls_dse/RW0030_Pouget2025_NLPDSE_TODAES.pdf` | 34b85a725f66 | full text | PARTIAL OVERLAP | S04 S06 S21 S32 S34 S72 S73 S88 |
| RW0031 | Prometheus | 2025 | ACM TODAES | hls_dse | `hls_dse/RW0031_Pouget2025_Prometheus_TODAES.pdf` | 2027336b4b0a | full text | PARTIAL OVERLAP | S04 S06 S07 S15 S21 S59 S61 S65 S72 S73 S78 S81 |
| RW0032 | Sisyphus | 2025 | FPGA | hls_dse | `hls_dse/RW0032_Pouget2025_Sisyphus_FPGA_arxiv.pdf` | ff9f6545572f | full text | PARTIAL OVERLAP | S04 S06 S21 S72 S73 |
| RW0033 | FIFOAdvisor | 2026 | ASP-DAC | hls_dse | `hls_dse/RW0033_AbiKaram2026_FIFOAdvisor_ASPDAC.pdf` | 8f57ad7f0cf5 | full text | PARTIAL OVERLAP | S02 S04 S06 S07 S15 S21 S36 S37 S56 S65 S72 S73 |
| RW0034 | MPMLLM4DSE | 2026 | DATE | hls_dse | `hls_dse/RW0034_Xu2026_MPMLLM4DSE_DATE_arxiv.pdf` | 3fc8c97cb72a | full text | PARTIAL OVERLAP | S10 S11 S90 |
| RW0035 | PatternDSE | 2026 | ICECCME (arXiv preprint) | hls_dse | `hls_dse/RW0035_Zhang2026_PatternDSE_ICECCME_arxiv.pdf` | bacd9ce5f87e | full text | PARTIAL OVERLAP | S32 S34 S88 |
| RW0036 | QoRML | 2018 | FCCM | multifidelity | `multifidelity/RW0036_Dai2018_QoRML_FCCM_accepted.pdf` | a51995b15e30 | full text | PARTIAL OVERLAP | S04 S06 S21 S59 S61 S72 S78 S81 |
| RW0037 | FADO | 2023 | FPGA | physical | `physical/RW0037_Du2023_FADO_FPGA_arxiv.pdf` | 4e63512b5bd8 | full text | PARTIAL OVERLAP | S02 S07 S15 S36 S37 S56 S65 |
| RW0038 | RapidStream2 | 2023 | ACM TRETS | physical | `physical/RW0038_Guo2023_RapidStream2_TRETS.pdf` | 84621e5b380a | full text | PARTIAL OVERLAP | S04 S06 S07 S15 S21 S32 S34 S59 S61 S65 S72 S78 S81 S85 S86 S88 S94 |
| RW0039 | TAPA | 2023 | ACM TRETS | physical | `physical/RW0039_Guo2023_TAPA_TRETS.pdf` | 4c527f953fc0 | full text | PARTIAL OVERLAP | S07 S15 S59 S61 S65 S73 S78 S81 |
| RW0040 | RapidStreamIR | 2024 | ICCAD | physical | `physical/RW0040_Lau2024_RapidStreamIR_ICCAD.pdf` | af17ea282c55 | full text | PARTIAL OVERLAP | S07 S15 S59 S61 S65 S78 S81 |
| RW0041 | TAPACS | 2024 | ASPLOS | physical | `physical/RW0041_Prakriya2024_TAPACS_ASPLOS.pdf` | 63eea3584b15 | full text | PARTIAL OVERLAP | S02 S07 S15 S36 S37 S56 S59 S61 S65 S73 S78 S81 |
| RW0042 | HLPSDSE | 2025 | ICCAD | physical | `physical/RW0042_Du2025_HLPSDSE_ICCAD.pdf` | d0bcec56bd13 | full text | PARTIAL OVERLAP | S02 S05 S07 S15 S20 S23 S32 S33 S34 S36 S37 S56 S59 S61 S65 S78 S81 S88 |
| RW0043 | DPRSurvey | 2018 | ACM Computing Surveys | lifecycle_dfx | `lifecycle_dfx/RW0043_Vipin2018_DPRSurvey_CSUR_accepted.pdf` | 1c448e055d98 | full text | PARTIAL OVERLAP | S59 S61 S78 S81 S85 S86 S94 |
| RW0044 | FOS | 2020 | ACM TRETS | lifecycle_dfx | `lifecycle_dfx/RW0044_Vaishnav2020_FOS_TRETS_arxiv.pdf` | ba7485013bf6 | full text | PARTIAL OVERLAP | S02 S36 S37 S56 S59 S61 S73 S78 S81 S83 S84 S85 S86 S94 |
| RW0045 | PLD | 2022 | ASPLOS | lifecycle_dfx | `lifecycle_dfx/RW0045_Xiao2022_PLD_ASPLOS.pdf` | 17a42a757d21 | full text | PARTIAL OVERLAP | S04 S06 S21 S32 S34 S59 S61 S72 S78 S81 S85 S86 S88 S94 |
| RW0046 | Bonamy12DPR | 2012 | ReConFig | energy_sustainability | `energy_sustainability/RW0046_Bonamy2012_Bonamy12DPR_ReConFig.pdf` | e29c6b640f4d | full text | PARTIAL OVERLAP | S04 S06 S19 S20 S21 S59 S61 S72 S78 S81 S85 S86 S94 |
| RW0047 | Nafkha17DPR | 2016 | ISWCS | energy_sustainability | `energy_sustainability/RW0047_Nafkha2016_Nafkha17DPR_ISWCS_arxiv.pdf` | 9dfeed771286 | full text | PARTIAL OVERLAP | S19 S20 S59 S61 S78 S81 S85 S86 S94 |
| RW0048 | HLPow | 2020 | ASP-DAC | energy_sustainability | `energy_sustainability/RW0048_Lin2020_HLPow_ASPDAC_arxiv.pdf` | c6b1774761ca | full text | PARTIAL OVERLAP | S05 S10 S11 S19 S20 S23 S32 S33 S34 S59 S61 S78 S81 S88 S90 |
| RW0049 | PowerGear | 2022 | DATE | energy_sustainability | `energy_sustainability/RW0049_Lin2022_PowerGear_DATE_preprint.pdf` | 742fb8414912 | full text | PARTIAL OVERLAP | S04 S06 S10 S11 S19 S20 S21 S59 S61 S72 S78 S81 S90 |
| RW0050 | EtoEDSE | 2024 | IEEE TCAD | energy_sustainability | `energy_sustainability/RW0050_Liao2024_EtoEDSE_TCAD_arxiv.pdf` | db1a8c2a44ff | full text | PARTIAL OVERLAP | S07 S15 S19 S20 S65 |
| RW0051 | FOCAL | 2024 | ASPLOS | energy_sustainability | `energy_sustainability/RW0051_Eeckhout2024_FOCAL_ASPLOS.pdf` | 2127c50699ee | full text | PARTIAL OVERLAP | S19 S20 S85 S86 S94 |
| RW0052 | GreenFPGA | 2024 | DAC | energy_sustainability | `energy_sustainability/RW0052_ChoppaliSudarshan2024_GreenFPGA_DAC_arxiv.pdf` | 4eecc1572a26 | full text | PARTIAL OVERLAP | S19 S20 S85 S86 S94 |
| RW0053 | IdleSleep | 2024 | ARCS (LNCS 14842) | energy_sustainability | `energy_sustainability/RW0053_Qian2024_IdleSleep_ARCS_arxiv.pdf` | 53963a987e44 | full text | PARTIAL OVERLAP | S19 S20 S59 S61 S78 S81 S83 S84 S85 S86 S94 |
| RW0054 | SustHWSpec | 2024 | ICCAD | energy_sustainability | `energy_sustainability/RW0054_Dangi2024_SustHWSpec_ICCAD.pdf` | 62ee8d8e756c | full text | PARTIAL OVERLAP | S19 S20 S85 S86 S94 |
| RW0055 | ASI | 2025 | IEEE CAL | energy_sustainability | `energy_sustainability/RW0055_Roelandts2025_ASI_CAL_accepted.pdf` | 167ee80bbf34 | full text | PARTIAL OVERLAP | S19 S20 |
| RW0056 | CATransformers | 2025 | NeurIPS | energy_sustainability | `energy_sustainability/RW0056_Wang2025_CATransformers_NeurIPS_arxiv.pdf` | ad0e83a21cf0 | full text | PARTIAL OVERLAP | S05 S19 S20 S23 S33 S85 S86 S94 |
| RW0057 | CORDOBA | 2025 | HPCA | energy_sustainability | `energy_sustainability/RW0057_Elgamal2025_CORDOBA_HPCA.pdf` | 4e44ebf0b94e | full text | PARTIAL OVERLAP | S19 S20 S43 S45 S85 S86 S92 S94 |
| RW0058 | HIPPO | 2025 | ICCAD | energy_sustainability | `energy_sustainability/RW0058_Lin2025_HIPPO_ICCAD.pdf` | 7a22676cbf69 | full text | PARTIAL OVERLAP | S04 S06 S19 S20 S21 S59 S61 S72 S78 S81 |
| RW0059 | SustGap | 2025 | Communications of the ACM | energy_sustainability | `energy_sustainability/RW0059_Eeckhout2025_SustGap_CACM_preprint.pdf` | c9d6ad1dce43 | full text | POTENTIAL OVERLAP | — |
| RW0060 | HLSToday | 2022 | ACM TRETS | other | `other/RW0060_Cong2022_HLSToday_TRETS.pdf` | f851f669cec2 | full text | POTENTIAL OVERLAP | — |
| RW0061 | TARO | 2023 | IEEE TCAD | other | `other/RW0061_Choi2023_TARO_TCAD.pdf` | 3b87c2d419d1 | full text | PARTIAL OVERLAP | S59 S61 S78 S81 |
| RW0062 | HLSFactoryAgent | 2026 | OSCAR Workshop @ ISCA (arXiv) | other | `other/RW0062_Chandana2026_HLSFactoryAgent_OSCAR_arxiv.pdf` | 4a91ff723c1f | full text | POTENTIAL OVERLAP | — |

## Duplicate handling

- HLSyn (RW0023): the copy in the local library and the NeurIPS open-access download were byte-identical
  (same SHA-256). One canonical copy is kept; both origins are recorded in the registry notes and `PDF_PROVENANCE.csv`.
- AutoDSE (RW0017): an 11-page 2020 preprint (sha256 `25d253c6d114…`) also exists locally. It is a different version,
  so it is recorded in the RW0017 notes, not imported.

Original PDFs in the local library were copied, not moved; they remain at their original paths.
