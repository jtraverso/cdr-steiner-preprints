# Formalization companion: prescribed block types and abundance

**Juan Pablo Traverso Gianini**  
Independent researcher, Santiago, Chile  
[jtraverso@gmail.com](mailto:jtraverso@gmail.com)  
[ORCID: 0009-0003-6068-4096](https://orcid.org/0009-0003-6068-4096)

**Paper III. Bicolorings of Steiner triple systems.**  
**Preprint 1.0 — 14 November 2026.**  
DOI: **10.5281/zenodo.24201563**.

## 1. Scope and statements

This companion documents the selected proof tree for CDR Paper III. It is not the whole research checkout. The manuscript contains the mathematical arguments, including the technical proofs in Appendices A–D. The present document explains their formal interfaces, source provenance and verification evidence.

The aggregate `CDRIII.lean` publicly imports the four defining modules below. Thus importing that aggregate exposes all four declarations. Their literal statements are supplied in `THEOREM_STATEMENTS.md` in this same directory and can also be read in the source files.

| Manuscript theorem | Exact declaration | Defining module |
|---|---|---|
| 1.1 | `CDRBicolour.KBicolor.kbicolour_completion_types_exact` | `CDRBicolour.KBicolor.CompletionExact` |
| 1.2 | `CDRBicolour.KBicolor.optimal_prescribed_type_count_of_three_le` | `CDRBicolour.KBicolor.PrescribedCounting.OptimalPrescribed` |
| 1.3 | `CDRBicolour.KBicolor.kbicolour_types_exact_many_pasch_counts` | `CDRBicolour.KBicolor.ExactTypesPasch` |
| 1.4 | `CDRBicolour.PaperIII.bicolourable_eventually_unconditional` | `CDRBicolour.PaperIII.Unconditional` |

The theorem statements and all copied Lean proof files are those of the frozen source selection. The exact completion theorem permits any sparse prescribed allowed packing, not just an empty one. The counting theorem fixes each compatible interior matrix before counting labeled systems. The Pasch theorem keeps that exact matrix while giving any fixed finite number of distinct counts. The arithmetic endpoint proves eventual existence at every admissible order for each fixed number of at least four colors; its order threshold is ineffective.

The Pasch declaration uses a relative type margin. The manuscript's absolute margin implies it: from `t_ij >= zeta*n^2` and `c_i*c_j <= n^2`, one obtains `2*t_ij >= (2*zeta)*c_i*c_j`. This is an application of the existing endpoint, not a change to its hypotheses. Diagonal matrix entries have no mathematical role and are set to zero in the manuscript.

## 2. What the formal objects mean

`ksz lab i` counts vertices of color `i`. `bicF k` permits precisely multisets with two equal labels and one different label. `kHost lab` has the complete graph underneath. `IsDecomposition` requires allowed triples, pairwise disjoint edge sets, and coverage of every host edge. On the complete host this is exactly a bicolored Steiner triple system.

`kTypeCount lab D i j` counts blocks with repeated color `i` and singleton color `j`. `exactTypeCount lab tv` counts distinct block families on the fixed finite vertex set, rather than isomorphism classes. `Pasch.count D` counts unoriented four-block Pasch subfamilies. Injectivity of this statistic over `Fin K` distinguishes the systems even when their colors are forgotten.

`Bicolourable v k` includes an actual system on `Fin v` and a surjective labeling by `Fin k`, with exactly two labels per block. `Admissible v` means residue one or three modulo six. The endpoint `bicolourable_eventually_unconditional` does not assume `ThreeSquaresDense` or `GaleInt`: it imports and applies their providers.

## 3. From the written proofs to the source tree

### Seed correction and exact completion

`BRIRatio` proves a bounded three-color inverse; `BRIkGlue` combines the restrictions containing a hub. The written Lemma B.1 gives an explicit alternative construction of the same bounded inverse by separating matrix means and row and column deviations. The formal proof uses finite averaging. The two arguments have the same compatible domain and the written bound is no larger than the formal constant. No claim is made that the new prose is a line-by-line transcription of that implementation.

`GenSeed` and `ResidualSeedK` provide the contraction correction after pair deletion. Their smallness condition and mass bound appear in Lemma B.2 and (3.2). `ResidualLattice` supplies the surviving-triangle quotient calculation of Lemma B.3. `Hinge` supplies the six-vertex construction in Appendix B.4. `ExactSeedK` uses cycle coordinates and convexity to recover exact real masses. `ReservedCopies` rejects collisions with the prescribed packing and bounds their number. `ReservedSpectrum` switches the required integer number of copies. `CompletionExact` assembles these facts with the triangle-monitor part of T+.

### Counting at each prescribed matrix

`TargetSeedData` obtains robust seed data from the theorem's own input. The `Pattern` and `Wilson` modules construct balanced patterns, fit equal groups into the partition, and correct the actual residual seed. Appendix C gives this construction, including a compactness argument for the finite choice of rational patterns; it makes no effective numerical claim about that choice.

`ReservedCore` and `ModularResidual` prepare a bounded reserve and repair the type residues modulo three. `ResidualQuotas` subtracts the actual residual counts. `HiltonExact` preserves the three outline marginals through the splitting stages of Lemma C.2. `RegularFactorizations` and `RegularEntropy` use the permanent lower bound. `GroupEntropyAssembly` injects the independent table choices into the exact matrix fiber. `SharpPrescribed` chooses the fixed group order, and `OptimalPrescribed` adds the general upper bound. The final endpoint includes three colors through the balanced three-class pattern.

### Pasch diversity

`LatinCompletionReplacement` and `LatinReplacement` preserve both the pair footprint and the type vector. `PaschPartiteParity` excludes the case of three Latin blocks. `LatinPaschConfigurationSplit` retains the one- and two-block mixed terms. `LatinPackingFrequencies` and `LatinMixedAverage` control both terms with one average. `TwoTorsionProducts`, `LatinIntercalateCounting` and `DyadicLatinFamily` construct tables with separated internal counts. `LatinMixedBudget` makes their cubic gap exceed the quadratic mixed error. These steps correspond to Section 7, including both candidate encodings and the explicit error comparison.

### Arithmetic existence

`PaperIII.Geom` proves the positive limiting profile and its strict cuts. `Arith` and `ArithMain` perform the even rounding and the four-coordinate reconstruction. `KBicolor.Four` proves the explicit four-color margins. `UnconditionalArithmetic` uses `ThreeSquaresLib.ThreeSquaresDenseProof`, which combines squarefree three-squares approximation with four-squares quaternion rotations. `Unconditional` discharges the contracts. Appendix D prints the cut-to-flow argument and the reduction for square factors; the two analytic input theorems are explicitly stated and cited there. Siegel's ineffective constant remains part of this dependency.

### Analytic providers and their verification boundary

The arithmetic result is unconditional as a Lean theorem statement. This means the endpoint has no remaining cap-density hypothesis; it does not mean that this editorial review independently reconstructed the analytic proofs. The distinction is between a mathematical dependency, a proved declaration imported into an environment, and the provenance of that environment.

| Input | Provider in the selected tree | Role |
|---|---|---|
| Squarefree three-squares caps | `ThreeSquaresLib.DukeSquarefreeProof` | Combines degreewise Weyl bounds from `IsoDegreewiseWeyl` with the Siegel-based lower bound in `B3_RepresentationLower` |
| Four-squares caps at odd radii | `ThreeSquaresLib.FourSquaresDenseProof` | Combines `FinalH2` with the representation count from `JacobiCount` |
| All radii congruent to three modulo eight | `ThreeSquaresLib.ThreeSquaresDenseProof` | Applies the squarefree input and quaternion rotations to absorb square factors |

The manuscript cites Duke (1988), Duke–Schulze-Pillot (1990), Heath-Brown (1996) and the relevant formal packages. Pommerenke is included as historical context for sphere and ellipsoid distribution, not as an unchecked replacement for the exact odd-radius input. Appendix D states the inputs actually used. The present review did not independently audit every analytic lemma in these providers. The docstring of `ThreeSquaresDense` credits Duke–Schulze-Pillot (1990), whereas the manuscript attributes the squarefree input to Duke (1988) [17], with Duke–Schulze-Pillot as context, and the all-radii assembly to [15]. The Lean source is left unchanged so that the frozen hashes remain valid.

Appendix E supplies the full definitions and quantifiers of T and the triangle-statistics form of T+, matching `main_theorem_T_with_triangle_monitors`. Their proofs are external mathematical dependencies, even though the selected Lean closure imports their providers. The Pasch argument in this paper uses the triangle-statistics part of T+ followed by Latin replacement; it does not apply the Pasch conclusion of T+.

### Local notation

The prime used for exchange placement is denoted by $p$, the number of usable copies by $s_i$, their prescribed-packing counts by $\pi_i$, and the tail length in the geometric profile by $d$. Appendix B uses $c_\ast$ for its minimum class size and $\chi$ for the edge image in the residual quotient. The rational pattern in Appendix C is $v$, its vertex reserve is $W_\ast$, and the squared directional norm in D.3 is $\nu$. Section 7 retains $m$ for the Latin order, uses $\mathcal R$ for the exterior packing and $E_{\rm mix}$ for the mixed-error envelope. The completed exterior packing in Section 4 is $D_{\rm ext}$, distinct from the real correction error $E$. These names are local to the written proofs; the Lean sources use their own identifiers, with the same constants and hypotheses.

## 4. Contents and identity of the source freeze

The selection contains 1,305 non-Mathlib dependency modules, the `CDRIII` aggregate and its axiom-query file. Mathlib is pinned at `c55e6e786f49471c72fbddbec5415808896aec1e`; Lean is `v4.35.0-rc3`. Every mathematical source retains its recorded hash. The source selection follows imports and excludes the pending descent and finite-spectrum developments. Upstream licenses are included.

The archive `CDRIII_Lean_v1.0.zip` has SHA-256 `08dcee5b5d67d00d1f561988e8c716c57c92d250ca54270f3d417429fb52e649`. Its entry manifest verifies every included source and evidence file. `02_validation/v1.0/FREEZE.json` records its identity; `CLEAN_REBUILD_AUDIT.json` binds the mathematical source and object hashes to the successful run. The package-wide manifest covers the documents separately.

## 5. Completed reconstruction and verification scope

The isolated run began on 13 November 2026 from source selection commit `16010adb21ac0d755d5940689ce82537399e553d` with no project build objects. All 1,306 project modules compiled successfully on 14 November. Only the pinned external Mathlib ecosystem cache was copied; this is not a reconstruction of Mathlib itself. Resumptions retained only objects produced in that same clean run, with recorded integrity checks.

The final configuration is commit `8756b2ef2dbe56002617a86e97e1b16a790ae069`. It restores the absorption provider's original implicit-binding settings for its two libraries and increases the heartbeat resource budget. CDR keeps its stricter setting. No `.lean` proof file or mathematical hypothesis changed. The final attempt used one runtime thread after `BRIUniform` failed to allocate memory with greater concurrency; that unmodified module subsequently compiled. Failed attempts and adjustment records are retained under `02_validation/v1.0/clean_run`.

Both commands succeeded: `lake --no-cache --fail-fast build CDRIII` and `lake env lean checks/Axioms.lean`. The four exact endpoint queries contain only `propext`, `Classical.choice` and `Quot.sound`. All 1,307 Lean source hashes agree before and after the run, as do the final configuration hashes. The independent package audit verifies the resulting object hashes and exact declaration names. Windows log-decoding failures were corrected by using UTF-8 in the verification scripts; neither required rebuilding Lean.

This closes the source-bound reconstruction gate. It does not constitute an independent specialist review of every analytic proof imported from external work. The written reductions and formal interfaces were reviewed within the stated scope; finite identity checks supplement that review. The bilingual audit compares mathematical formulas and numbering, and the PDF audit checks actual URI destinations and rendered pages.

## 6. Reproduction and distribution

From the repository root, `python scripts/verify_package.py` checks the sealed package without changing it. For a full reconstruction, use the pinned toolchain in `lean/`, obtain the pinned Mathlib dependencies and run `lake build CDRIII`, followed by `lake env lean checks/Axioms.lean`. Detailed instructions are in `preprints/PAPER_III/03_reproducibility/README.md`. The Markdown sources are the semantic sources; the TeX files and PDFs are their publication artifacts.

The official home of this package is `preprints/PAPER_III` in <https://github.com/jtraverso/cdr-steiner-preprints>, beside Papers I–II. The preprint, this companion and the Lean source archive are deposited under DOI **10.5281/zenodo.24201563**. The source archive includes the complete source-bound reconstruction evidence for this preprint.
