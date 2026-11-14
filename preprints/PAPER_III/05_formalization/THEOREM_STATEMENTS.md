# Literal theorem statements

CDR Paper III, preprint 1.0. Complete contracts copied from the frozen source files.

## Theorem 1.1

`CDRBicolour.KBicolor.kbicolour_completion_types_exact`

```lean
theorem kbicolour_completion_types_exact (k : ℕ) (hk : 3 ≤ k) {δ ε : ℝ} (hδ : 0 < δ) (hδ1 : δ ≤ 1)
    (hε : 0 < ε) :
    ∃ γ : ℝ, 0 < γ ∧ ∃ n₀ : ℕ, ∀ (n : ℕ) (lab : Fin n → Fin k), n₀ ≤ n → Odd n →
      (∀ X, δ * n ≤ ksz lab X) →
      (∀ X Y, X ≠ Y → Even (ksz lab X * ksz lab Y)) →
      3 * ∑ X, ksz lab X * (ksz lab X - 1) = n * (n - 1) →
      ∀ t : Fin k → Fin k → ℕ,
      (∀ X Y, X ≠ Y → 2 * (t X Y + t Y X) = ksz lab X * ksz lab Y) →
      (∀ X, 2 * ∑ Y ∈ univ.filter (fun Y => Y ≠ X), t X Y = ksz lab X * (ksz lab X - 1)) →
      (∀ X Y, X ≠ Y → ε * (n : ℝ) ^ 2 ≤ t X Y) →
      ∀ (Q : Finset (Finset (Fin n))) (ΔQ : ℕ),
      (∀ T ∈ Q, IsAllowed (kHost lab) (bicF k) T) →
      (Q : Set (Finset (Fin n))).PairwiseDisjoint triEdges →
      (∀ p, degL (Q.biUnion triEdges) p ≤ ΔQ) → (ΔQ : ℝ) ≤ γ * n →
      ∃ D : Finset (Finset (Fin n)), IsDecomposition (kHost lab) (bicF k) (edges (kHost lab)) D ∧
        Q ⊆ D ∧ ∀ X Y, X ≠ Y → kTypeCount lab D X Y = t X Y
```

## Theorem 1.2

`CDRBicolour.KBicolor.optimal_prescribed_type_count_of_three_le`

```lean
theorem optimal_prescribed_type_count_of_three_le (k : ℕ) (hk : 3 ≤ k) {δ ζ ε : ℝ}
    (hδ : 0 < δ) (hζ : 0 < ζ) (hε : 0 < ε) :
    ∃ n₀ : ℕ, ∀ (n : ℕ) (lab : Fin n → Fin k), n₀ ≤ n → Odd n →
      (∀ i, δ*n ≤ ksz lab i) →
      (∀ i j, i ≠ j → Even (ksz lab i*ksz lab j)) →
      3*∑ i,ksz lab i*(ksz lab i-1)=n*(n-1) →
      ∀ target : Fin k → Fin k → ℕ,
      (∀ i j, i ≠ j → 2*(target i j+target j i)=ksz lab i*ksz lab j) →
      (∀ i, 2*∑ j ∈ univ.filter (fun j => j ≠ i), target i j=ksz lab i*(ksz lab i-1)) →
      (∀ i j, i ≠ j → ζ*(n : ℝ)^2 ≤ target i j) →
      let tv : TypeCoord k → ℕ := fun q => target q.1.1 q.1.2
      0 < exactTypeCount lab tv ∧
        (1/6-ε)*(n : ℝ)^2*Real.log n ≤ Real.log (exactTypeCount lab tv) ∧
        Real.log (exactTypeCount lab tv) ≤ (1/6+ε)*(n : ℝ)^2*Real.log n
```

## Theorem 1.3

`CDRBicolour.KBicolor.kbicolour_types_exact_many_pasch_counts`

```lean
theorem kbicolour_types_exact_many_pasch_counts (K k : ℕ) (hk : 3 ≤ k) {δ η : ℝ}
    (hδ : 0 < δ) (hδ1 : δ ≤ 1) (hη : 0 < η) :
    ∃ n₀ : ℕ, ∀ (n : ℕ) (lab : Fin n → Fin k), n₀ ≤ n → Odd n →
      (∀ X, δ*n ≤ ksz lab X) →
      (∀ X Y, X ≠ Y → Even (ksz lab X * ksz lab Y)) →
      3 * ∑ X, ksz lab X * (ksz lab X-1) = n*(n-1) →
      ∀ t : Fin k → Fin k → ℕ,
      (∀ X Y, X ≠ Y → 2*(t X Y+t Y X) = ksz lab X * ksz lab Y) →
      (∀ X, 2*∑ Y ∈ univ.filter (fun Y => Y ≠ X), t X Y = ksz lab X * (ksz lab X-1)) →
      (∀ X Y, X ≠ Y → η*ksz lab X*ksz lab Y ≤ 2*t X Y) →
      ∃ D : Fin K → Finset (Finset (Fin n)),
        (∀ i, IsDecomposition (kHost lab) (bicF k) (edges (kHost lab)) (D i)) ∧
        (∀ i X Y, X ≠ Y → kTypeCount lab (D i) X Y = t X Y) ∧
        Function.Injective (fun i => Pasch.count (D i))
```

## Theorem 1.4

`CDRBicolour.PaperIII.bicolourable_eventually_unconditional`

```lean
theorem bicolourable_eventually_unconditional {k : ℕ} (hk : 4 ≤ k) :
    ∃ v₀ : ℕ, ∀ v, v₀ ≤ v → Admissible v → Bicolourable v k :=
  bicolourable_eventually_with_registered_gale threeSquaresDense_verified hk

/-- CDR Conjecture 3.5 for every sufficiently large admissible order. -/
theorem conj35_large_unconditional :
    ∃ v₀ : ℕ, ∀ v, v₀ ≤ v → Admissible v → Bicolourable v 4 :=
  bicolourable_eventually_unconditional (by norm_num)

/-- CDR Conjecture 3.6 for every sufficiently large admissible order. -/
theorem conj36_large_unconditional :
    ∃ v₀ : ℕ, ∀ v, v₀ ≤ v → Admissible v → Bicolourable v 5 :=
  bicolourable_eventually_unconditional (by norm_num)

theorem capRep_eventually_verified :
    ∃ V₀ : ℕ, ∀ v, V₀ ≤ v → Admissible v → CapRep v :=
  capRep_eventually threeSquaresDense_verified

theorem two_cap_at_verified : ∃ N₀ : ℕ, TwoCapAt N₀ :=
  threeSquaresDense_supplies_two_cap threeSquaresDense_verified

theorem cap_two_eventually_verified :
    ∃ V₀ : ℕ, ∀ v, V₀ ≤ v → Admissible v → CapRepTwo v :=
  cap_two_eventually_of_radius_caps two_cap_at_verified

/-- The same labelled profile satisfies both bounds; no arithmetic input remains. -/
theorem four_colour_sharp_counting_eventually {ε : ℝ} (hε : 0 < ε) :
    ∃ V₀ : ℕ, ∀ v, V₀ ≤ v → Admissible v →
      ∃ lab : Fin v → Fin 4, (∀ X, 0 < ksz lab X) ∧ 0 < kCount lab ∧
        (1/6-ε)*(v : ℝ)^2*Real.log v ≤ Real.log (kCount lab) ∧
        Real.log (kCount lab) ≤ (1/6+ε)*(v : ℝ)^2*Real.log v
```
