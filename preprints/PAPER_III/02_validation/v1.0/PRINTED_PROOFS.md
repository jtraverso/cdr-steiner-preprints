# Printed proofs · preprint 1.0

Status: **PASS_TARGETED_WRITTEN_REVIEW**. The separate clean reconstruction passed; final artifact evidence is recorded alongside this report.

The two languages give the same mathematical arguments. T and the triangle-
statistics form of T+ are external inputs stated in Appendix E. The two cap
approximation theorems are external mathematical inputs stated in Appendix D.
This report reviews their use; it does not claim a new independent proof of
those external theorems or a specialist review of every analytic provider.

| Result | Written proof | Steps reviewed |
|---|---|---|
| Theorem 1.1 | Sections 2–4, Appendices A–B | Pair/row identities; hub-cycle coordinates; constant-by-type seed; bounded inverse and residual contraction; actual residual integer certificate; disjoint affine exchange footprints; one simultaneous application of T+ and integer switches. |
| Theorem 1.2 | Section 5, Appendix C | Integer outline splitting and zero support; Hilton refinement; permanent product; common residual graph independent of the Latin fillings; exact quota repair; leading coefficient tending to 1/6. No second entropy term is claimed. |
| Theorem 1.3 | Section 7 | Sparse Latin planting; exclusion of exactly three Latin blocks in a Pasch; the one- and two-block frequencies; averaging over permutations; dyadic groups with different two-torsion counts; cubic gap versus quadratic mixed error. The same matrix is retained. |
| Theorem 1.4 | Section 6, Appendix D | Positive real profile and strict cuts; even rounding; congruence of the three-square target; four-coordinate reconstruction; stated cap inputs; ineffectivity of the order threshold. The order1000 calculation is conditional on a representation, not an effective universal existence threshold. |
| Lemma B.1 | Appendix B.1 | Balanced domain of incidence; local transfers and type loads; three-class bound400R^5/n; balanced splitting into hub restrictions and general bound |Trip(o)|400R^6(1+4R^2)/n. The printed inverse is distinguished from formal finite averaging. |
| Lemma B.2 | Appendix B.2 | The bad-triangle operator preserves balanced vectors vanishing on deleted edges; its norm is below1/2 under the stated cutoff. The geometric series restores exact loads, keeps weights positive, and gives the stated test-mass error. |
| Lemma B.3 | Appendix B.3 | Order-two vertex potentials, base-edge values, the additional auxiliary neighbor in the missing-edge bridge, and telescoping. The class coefficient equals (n^2−3 sum(c_i^2)+2n)/4=0. Deleted allowed triangles have zero extended value; the resulting certificate uses surviving triangles. |
| H3 and H4 | Appendix B.4 | Counts use actual surviving neighbors. The six-vertex hinge has four fixed roots; its free choices give the n^(6−4) scale. |
| Integer splitting and flow | Appendix A, Appendix D.1 | Alternating cycles preserve integer row/column sums and zero support. Gale supplies feasibility; Ford–Fulkerson supplies integrality. |

## Corrections checked in this revision

- Appendix E now states only the imported triangle-monitor conclusion. The
  unused Pasch target and inequality were removed; no principal theorem was
  weakened or strengthened.
- High/low names agree with the exchange table and the direction of the unit
  circulation. Prescribed packing counts use pi_i rather than the prime p.
- The bridge in B.3 prints the extra point w adjacent to u,z,o_i. Its three
  adjacency requirements and the four for z, with named-point exclusions,
  lie within the original k+4 neighbor hypothesis.
- The proof of the seed's existing lower bound2*zeta/n now uses the precise
  denominator estimate binom(c_i,2)c_j ≤ c_i^2*n/2, which cancels the c_i^2 in
  the prescribed margin. The previous n^3/2 estimate alone did not explain
  that cancellation. The claimed lower bound and hypotheses are unchanged.
- The figure's cube radius is r_cube, distinct from rho in Appendix C.

The exact finite construction checks supplement these universal arguments;
they are not substituted for them. The Lean reconstruction has its own raw
logs, source/configuration manifests and axiom gate.
