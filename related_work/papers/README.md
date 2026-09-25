# Canonical PDF store (local only)

PDFs live in `papers/<category>/RW####_<FirstAuthor><Year>_<Key>_<Venue>[_suffix].pdf` and are **not committed**:
this repository is public and most PDFs are copyrighted. `.gitignore` in this folder excludes `*.pdf`.

To rebuild a local copy, use `pdf_source_url` (downloads) or `original_path` (local library) from
`../RELATED_WORK_REGISTRY.csv` / `../PDF_PROVENANCE.csv`. Then check the file with `sha256sum` against the registry.
A file whose hash differs is a different version and must not replace the registered one silently.

Folders hold only canonical papers (CORE in `core/`, SUPPORTING by topic): core, concurrent_multikernel, hls_dse,
multifidelity, bo_mobo, physical, lifecycle_dfx, energy_sustainability (see `../README.md`). ADJACENT/EXCLUDE papers are
never kept here; see `../EXCLUSION_REGISTER.csv`.
