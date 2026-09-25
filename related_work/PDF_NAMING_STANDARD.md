# PDF Naming Standard

Format: `RW<4-digit>_<FirstAuthor><Year>_<ShortKey>_<Venue>.pdf`

Rules: immutable RW ID; ASCII only; no spaces; stable short key; concise venue; optional `_preprint`, `_accepted`, `_published`, `_arxiv` suffix.

## Clarifications (2026-09-25)

These make the rules above deterministic. They do not change the format.

- **FirstAuthor**: the first author's family name, transliterated to ASCII (diacritics removed; for example, Grün → Grun),
  with all non-alphanumeric characters dropped (Choppali Sudarshan → ChoppaliSudarshan).
- **ShortKey**: the paper's registry `key`, alphanumeric only (for example, `StreamHLS`, `CMMFO`).
- **Venue**: a fixed token such as `DATE`, `DAC`, `ICCAD`, `FPGA`, `FCCM`, `ASPDAC`, `TCAD`, `TRETS`, `TODAES`,
  `NeurIPS`, `AISTATS`, `ASPLOS`, `HPCA`, `CSUR`, `CACM`, `CAL` or `arXiv`.
- **Suffix**: describes the PDF actually held, not the paper:
  - `_arxiv` for an arXiv copy of a published paper;
  - `_preprint` for a pre-publication copy;
  - `_accepted` for an author-accepted manuscript;
  - no suffix for the publisher version.

  When the venue itself is `arXiv`, no suffix is added.
- The filename is a convenience. Identity is the RW ID plus the SHA-256 in `RELATED_WORK_REGISTRY.csv`.
