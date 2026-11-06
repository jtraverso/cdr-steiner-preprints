# Plantholt 2004 y Dinitz–Stinson: procedencia en Palomar

## Plantholt 2004, Teorema 1.2

- Entrada Palomar: **PALOMAR-2026-11-04-000016**, versión 1 (publicada 2026-11-04T18:14:34Z).
  Fuente: `jtraverso/plantholt-overfull-criterion`, commit `28ff33dd73fc858056ff0db75d5a6d6cef15c8b5`.
- **Desde el 05-11-2026 la ruta usa el commit `f890094`** (rama `main`, «v2: Chetwynd–Hilton 1985
  (6/7)»), en `C:/cdr-deps/plantholt-overfull-criterion`. Es la **versión 2 registrada** de la
  entrada (ver abajo). Ver la sección «Chetwynd–Hilton 6/7».
  Teoremas: `Plantholt.theorem_1_2`, `OneFactor.lineGraph_colorable_of_isRegular`,
  `OneFactor.overfull_criterion`.
- Dependencia local `plantholt_overfull` = `C:/cdr-deps/plantholt-overfull-criterion` en ese commit
  exacto. Su `ccjs_overfull` es el mismo commit `b85da9a` ya enlazado, y su `vizing` lo sirve el
  `LeanPool.Vizing` vendorizado, a través del shim vacío.
- **Uso.** `Plantholt.theorem_1_2` es paramétrico: vale para todo c ≥ 3/4 tal que los grafos regulares
  de orden par y grado ≥ c·n son 1-factorizables. Chetwynd–Hilton 1985 da ese c = 6/7, y ya era
  hipótesis de la ruta (`Master.ChetwyndHilton_1985`; `CH1985_OneFactor` tiene el mismo enunciado,
  igual por definición). `CDRBicolour/EdgeColouring/PlantholtBridge.lean` (`plantholt_of_CH`):
  orden par, 12n + 7Δ ≤ 21δ y no Δ-coloreable ⇒ un conjunto impar `|S| ≥ 3` induce un subgrafo
  Δ-overfull.
- **Cambio en L183.** La hipótesis numérica 7(|W|−1)² ≤ 9(a−2)² del Corolario 1.7 se reemplaza por
  12(|W|−1) + 63 ≤ 14a, que es 3δ − Δ ≥ 12N/7 con δ ≥ a−3. En la familia P2 equivale a
  24k² − 44k − 103 ≥ 0, cierto para k ≥ 4. La ruta usa k ≥ 5.
- **Por qué no basta la constante 11/12 sola.** `OneFactor.overfull_criterion` (c = 11/12) cubre
  P2(k) sólo para k ≥ 6: con k = 5 (perfil (374, 376, 409)) se necesita 12k² − 52k − 94 ≥ 0, que
  falla por 54. Con c = 6/7 de CH1985 la familia queda cubierta completa.
- **Resultado.** `Plantholt_Corollary_1_7` deja de ser hipótesis de la ruta. El teorema final queda
  `cdr_conjecture_of_branches : ChetwyndHilton_1985 → BKLS_Corollary_12 → RS_Theorem_3_1 →
  CDRConjecture`.

## Colbourn–Dinitz–Rosa / Dinitz–Stinson

- Entrada Palomar: **PALOMAR-2026-11-04-000014**, versión 1 (publicada 2026-11-04T16:31:34Z).
  Fuente: `jtraverso/cdr-bicolouring-sts`, commit `a768a98a648e94ad38d0d84501867c999927c546`.
  Teoremas: `CDR.bicolourable3_mul` (CDR 1999, Teorema 2.4), `CDR.IsSTS.three_mul_sum`,
  `CDR.not_two_classes_of_size_two`, `CDR.Bicolourable3.not_two_odd` (Dinitz–Stinson,
  Proposición 1.2).
- Dependencia local `cdr_bicolouring` = `C:/cdr-deps/cdr-bicolouring-sts` en ese commit. Sólo se
  importa `CDR.Necessary` (y `CDR.Basic`). El producto de esta ruta sigue siendo el propio
  (`CDRBicolour/Product.lean`, puerta E4).
- **Uso.** `CDRBicolour/Palomar/DinitzStinson.lean`:
  - `realises_iff_bicolourable3`: nuestro `Realises a b c` es exactamente
    `CDR.Bicolourable3 (a+b+c) a b c`. Es un cotejo independiente de la capa de enunciados.
  - `STS.even_card_sub_one`: el orden de un STS es impar.
  - `admissible_of_realises`: **necesidad**. Todo perfil realizado con tres clases no vacías es
    admisible: identidad de pares, n ≡ 1, 3 (mod 6) y ningún par de clases de tamaño 2.
- `CDRBicolour/Characterization.lean`: `cdr_characterization`. Con tres clases no vacías,
  realizado ⇔ admisible, condicional sólo a CH1985, BKLS y RS (y la versión
  `cdr_characterization_bicolourable3` con las definiciones de Palomar).

## Chetwynd–Hilton 6/7 (05-11-2026)

- Commit `f890094` de `jtraverso/plantholt-overfull-criterion` (`main`). Agrega
  `OneFactor/{Stair,Label67,Label67b,Pair67,Core67,CoreRank,Factors2,Steps67,Main67,Plantholt67}` y
  conserva los enunciados 11/12. Comparador: cinco teoremas (`comparator.json`).
- **Enunciados usados:** `OneFactor.lineGraph_colorable_of_isRegular67` (d-regular de orden 2n con
  `12n ≤ 7d` ⇒ 1-factorizable) y `OneFactor.overfull_criterion67` (orden par y
  `12·|V| ≤ 7(3δ − Δ)` ⇒ clase 1 ⇔ sin subgrafo Δ-overfull).
- **Efecto en CDR.** `EqMasterHyp`: `11C ≤ 12A` → `6C ≤ 7A` (`Master.oneFactor_67`). L183:
  `hpl : 12(|W|−1) + 63 ≤ 14a` (`plantholt_67`), que en P2 vale desde `k = 4`. La condición de CCJS,
  `12k² − 46k − 8 ≥ 0`, también vale desde `k = 4` (con igualdad), y `stageB` funciona con `k ≥ 4`.
  La rama P2 de la base pasa de `c − b ≥ 39` a `c − b ≥ 27`.
- **Base:** de 88 a **49 testigos** (orden máximo de 1453 a **487**). Los teoremas para todo n quedan
  con 49 `native_decide`, todos de las tablas de testigos.
- **Descartado:** una versión 7/8 con clases de round robin apareadas (rama `seven-eighths`, borrada
  del repo público el 05-11-2026). 6/7 ya estaba en `main` y es más fuerte.

### Registro Palomar de la versión 2 (verificado en el registro el 05-11-2026)

- **PALOMAR-2026-11-04-000016 v2** (actual; la v1 queda «superseded»), registrada el 5 de noviembre
  de 2026: https://palomar-registry.org/entry?id=PALOMAR-2026-11-04-000016&version=2
- Commit fijado: `f8900944da7743b1facd771139c9ebdbfd8aaa28` (= `f890094`), el mismo que usa CDR.
- Título: «Plantholt's overfull criterion for graphs of high minimum degree, with 1-factorization
  theorems for dense regular graphs (6/7 and 11/12)». Cinco enunciados, entre ellos
  `lineGraph_colorable_of_isRegular67` y `overfull_criterion67`.
- Verificación: Comparator (Solution prueba Challenge), kernel de Lean y kernels independientes
  nanoda y con-ron; revisión automática «no problems identified» (no es revisión humana).
- Evidencia archivada: `data.palomar-registry.org/evidence/PALOMAR-2026-11-04-000016-v2/15f0581e…/`
  (`mechanical-report.json`, `review.json`, `source-archive.json`); Actions run 41942564203.
