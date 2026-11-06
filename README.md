# Bicolorings of Steiner triple systems

**Preprint 1.0 — 6 November 2026.** Each paper can be read independently. These manuscripts have not undergone journal peer review.

| Paper | English title | Título en español | Manuscripts |
|---|---|---|---|
| I | The exact block-type spectrum in the Colbourn–Dinitz–Rosa problem | El espectro exacto de tipos de bloque en el problema de Colbourn–Dinitz–Rosa | [EN](preprints/PAPER_I/01_manuscript/spectrum_en.pdf) · [ES](preprints/PAPER_I/01_manuscript/spectrum_es.pdf) |
| II | A proof of the Colbourn–Dinitz–Rosa conjecture | Una demostración de la conjetura de Colbourn–Dinitz–Rosa | [EN](preprints/PAPER_II/01_manuscript/profiles_en.pdf) · [ES](preprints/PAPER_II/01_manuscript/profiles_es.pdf) |

Paper I characterizes prescribed block-type counts at sufficiently large admissible order, using physical typed absorption. Paper II constructs every admissible class-size profile by descent, edge coloring and the published small-order theorem.

[Shared formal companion, EN](preprints/PAPER_I/05_formalization/companion_en.pdf) · [Informe formal, ES](preprints/PAPER_I/05_formalization/companion_es.pdf) · [Source archive](archives/CDR_shared_Lean_source_7643193.zip) · [Internal audit](publication/JOINT_DOCUMENT_AUDIT.json) · [Repository structure](REPOSITORY_STRUCTURE.md) · [Citations](CITATION.md).

Run `python scripts/verify_repository.py` and `python scripts/verify_release.py`. These audits check the delivered bytes, finite certificates, archived axiom records, bilingual consistency and release artifacts. They do not invoke Lean. The companion distinguishes the spectrum endpoint, which uses the three standard Lean axioms, from the all-order endpoints, which also use the 49 recorded native decision certificates.

Theorem 6.2 of Paper I has a symbolic Lean proof, not a finite-enumeration proof. Appendix B prints the residual-intersection criterion and the proof dependencies. `python scripts/verify_intersection_evidence.py` checks the unchanged source and archived axiom report; the commands for an independent Lean rebuild are printed there. Full URLs are written in the PDF bibliographies.

This repository contains the first public preprint edition and its supporting documents. Development drafts and their Git history are not included. The shared Lean archive is unchanged.

| Zenodo record | DOI |
|---|---|
| Paper I, exact spectrum | [10.5281/zenodo.23987251](https://doi.org/10.5281/zenodo.23987251) |
| Paper II, conjecture | [10.5281/zenodo.23987256](https://doi.org/10.5281/zenodo.23987256) |

BKLS is publicly registered as [PALOMAR-2026-11-06-000002 v1](https://palomar-registry.org/entry?id=PALOMAR-2026-11-06-000002&version=1), at the same source revision used by the frozen dependency. See the [public registration record](publication/audit/BKLS_PALOMAR.json).

Supplementary references [S1], [S2], etc. print the resource addresses in each PDF. The bibliography checker also checks actual PDF hyperlink destinations. The [publication checks](publication/RELEASE_CHECKS.json) supplement the retained mathematical audit; no new Lean build was performed.

The articles, companion and original figures are available under [CC BY 4.0](LICENSE.md). The Lean sources retain their upstream licenses.

[Download release v1.0](https://github.com/jtraverso/cdr-steiner-preprints/releases/tag/v1.0) · [Publication receipts and public-access verification](publication/zenodo/). Both Zenodo records are published.
