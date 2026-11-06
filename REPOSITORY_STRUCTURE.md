# Repository structure

Each paper uses the same five-part publication layout:

- `01_manuscript/`: bilingual semantic Markdown, generated TeX, compiled PDF, and figure sources.
- `02_validation/`: internal audit, semantic and bilingual checks, compiler logs, rendered-page records and review response.
- `03_reproducibility/`: build script and the series layout templates.
- `04_integrity/`: hashes of the paper and its evidence.
- `05_formalization/`: the shared bilingual formal companion and source-snapshot notes.

`archives/` holds the unchanged, portable shared Lean source snapshot with its source manifest and dependency/provenance records. `publication/` holds the joint audit, editorial records, public dependency registrations and publication receipts. `scripts/` contains executable verifiers. The private/public visibility setting is operational and does not change the mathematical content of preprint 1.0.
