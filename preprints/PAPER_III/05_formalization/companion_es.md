# Companion de formalización: tipos de bloque prescritos y abundancia

**Juan Pablo Traverso Gianini**  
Investigador independiente, Santiago, Chile  
[jtraverso@gmail.com](mailto:jtraverso@gmail.com)  
[ORCID: 0009-0003-6068-4096](https://orcid.org/0009-0003-6068-4096)

**Paper III. Bicoloraciones de sistemas triples de Steiner.**  
**Preprint 1.0 — 14 de noviembre de 2026.**  
DOI: **10.5281/zenodo.24201563**.

## 1. Alcance y enunciados

Este companion documenta el árbol de pruebas seleccionado para CDR III. No es todo el árbol de investigación. El manuscrito contiene los argumentos matemáticos, incluidas las pruebas técnicas de los Apéndices A–D. Este documento explica sus interfaces formales, la procedencia de las fuentes y la evidencia de verificación.

El módulo conjunto `CDRIII.lean` importa públicamente los cuatro módulos de la tabla. Por tanto, importarlo permite usar las cuatro declaraciones. Sus enunciados literales están en `THEOREM_STATEMENTS.md`, en este mismo directorio, y también se pueden leer en las fuentes.

| Teorema del manuscrito | Declaración exacta | Módulo que la define |
|---|---|---|
| 1.1 | `CDRBicolour.KBicolor.kbicolour_completion_types_exact` | `CDRBicolour.KBicolor.CompletionExact` |
| 1.2 | `CDRBicolour.KBicolor.optimal_prescribed_type_count_of_three_le` | `CDRBicolour.KBicolor.PrescribedCounting.OptimalPrescribed` |
| 1.3 | `CDRBicolour.KBicolor.kbicolour_types_exact_many_pasch_counts` | `CDRBicolour.KBicolor.ExactTypesPasch` |
| 1.4 | `CDRBicolour.PaperIII.bicolourable_eventually_unconditional` | `CDRBicolour.PaperIII.Unconditional` |

Los enunciados y todos los archivos de pruebas Lean copiados son los de la selección de fuentes congelada. El teorema de completación exacta admite cualquier empaquetamiento permitido disperso prescrito, no solo el vacío. El teorema de conteo fija cada matriz interior compatible antes de contar los sistemas etiquetados. El teorema de Pasch conserva esa matriz exacta y proporciona cualquier cantidad finita fija de conteos distintos. El resultado aritmético prueba existencia en todo orden admisible suficientemente grande para cada cantidad fija de al menos cuatro colores; su umbral es inefectivo.

La declaración de Pasch usa un margen relativo por tipo. El margen absoluto del manuscrito lo implica: de `t_ij >= zeta*n^2` y `c_i*c_j <= n^2` se obtiene `2*t_ij >= (2*zeta)*c_i*c_j`. Es una aplicación del teorema existente, no un cambio de hipótesis. Las entradas diagonales no tienen papel matemático y se toman iguales a cero en el manuscrito.

## 2. Significado de los objetos formales

`ksz lab i` cuenta los vértices de color `i`. `bicF k` permite exactamente los multiconjuntos con dos etiquetas iguales y una distinta. El grafo subyacente de `kHost lab` es completo. `IsDecomposition` exige ternas permitidas, conjuntos de aristas disjuntos dos a dos y cobertura de cada arista del grafo. En el grafo completo esto es exactamente un sistema triple de Steiner bicoloreado.

`kTypeCount lab D i j` cuenta los bloques con color repetido `i` y color simple `j`. `exactTypeCount lab tv` cuenta familias de bloques distintas sobre el conjunto finito fijo de vértices, no clases de isomorfismo. `Pasch.count D` cuenta subfamilias de cuatro bloques de Pasch sin orientación. La inyectividad de esa estadística sobre `Fin K` distingue los sistemas incluso si se olvidan sus colores.

`Bicolourable v k` incluye un sistema concreto sobre `Fin v` y una asignación sobreyectiva de etiquetas en `Fin k`, con exactamente dos etiquetas por bloque. `Admissible v` significa residuo uno o tres módulo seis. El resultado `bicolourable_eventually_unconditional` no supone `ThreeSquaresDense` ni `GaleInt`: importa y aplica sus demostraciones.

## 3. De las pruebas escritas al árbol de fuentes

### Corrección de la semilla y completación exacta

`BRIRatio` demuestra una inversa acotada para tres colores; `BRIkGlue` combina las restricciones que contienen un color central. El Lema B.1 escrito da otra construcción explícita de la misma inversa acotada, separando medias y desviaciones por fila y columna. La prueba formal usa promedios finitos. Los dos argumentos tienen el mismo dominio compatible y la cota escrita no supera la constante formal. No se afirma que la nueva prosa sea una transcripción línea por línea de esa implementación.

`GenSeed` y `ResidualSeedK` proporcionan la corrección por contracción después de borrar pares. Su condición de pequeñez y su cota de masas aparecen en el Lema B.2 y en (3.2). `ResidualLattice` contiene el cálculo del cociente con triángulos supervivientes del Lema B.3. `Hinge` contiene la construcción de seis vértices del Apéndice B.4. `ExactSeedK` usa coordenadas de ciclos y convexidad para recuperar masas reales exactas. `ReservedCopies` rechaza las copias que chocan con el empaquetamiento prescrito y acota cuántas se pierden. `ReservedSpectrum` cambia el número entero requerido de copias. `CompletionExact` ensambla estos hechos con la parte de T+ que controla funciones de prueba de triángulos.

### Conteo para cada matriz prescrita

`TargetSeedData` obtiene los datos de semilla robusta a partir de las propias hipótesis del teorema. Los módulos `Pattern` y `Wilson` construyen patrones balanceados, colocan grupos iguales en la partición y corrigen la semilla residual concreta. El Apéndice C desarrolla esta construcción, incluido un argumento de compacidad para elegir una colección finita de patrones racionales; no afirma una cota numérica efectiva para esa elección.

`ReservedCore` y `ModularResidual` preparan una reserva acotada y corrigen los residuos de tipos módulo tres. `ResidualQuotas` resta los conteos residuales concretos. `HiltonExact` conserva las tres marginales de la tabla agregada en los repartos del Lema C.2. `RegularFactorizations` y `RegularEntropy` usan la cota inferior del permanente. `GroupEntropyAssembly` inyecta las elecciones independientes de tablas en la familia de sistemas con matriz exacta. `SharpPrescribed` elige el orden fijo de grupos y `OptimalPrescribed` añade la cota superior general. El resultado final incluye tres colores mediante el patrón balanceado de tres clases.

### Diversidad de Pasch

`LatinCompletionReplacement` y `LatinReplacement` conservan el conjunto de pares ocupado y el vector de tipos. `PaschPartiteParity` excluye el caso de tres bloques latinos. `LatinPaschConfigurationSplit` conserva los términos mixtos con uno y dos bloques. `LatinPackingFrequencies` y `LatinMixedAverage` controlan ambos con un solo promedio. `TwoTorsionProducts`, `LatinIntercalateCounting` y `DyadicLatinFamily` construyen tablas con conteos internos separados. `LatinMixedBudget` hace que su brecha cúbica supere el error mixto cuadrático. Estos pasos corresponden a la sección 7, incluidas ambas codificaciones de candidatos y la comparación explícita de errores.

### Existencia aritmética

`PaperIII.Geom` prueba el perfil límite positivo y sus cortes estrictos. `Arith` y `ArithMain` realizan el redondeo par y la reconstrucción de cuatro coordenadas. `KBicolor.Four` prueba los márgenes explícitos para cuatro colores. `UnconditionalArithmetic` usa `ThreeSquaresLib.ThreeSquaresDenseProof`, que combina la aproximación por tres cuadrados para enteros libres de cuadrados con rotaciones de cuaterniones obtenidas mediante cuatro cuadrados. `Unconditional` satisface los contratos. El Apéndice D desarrolla el argumento de cortes y flujos y la reducción para factores cuadrados; allí se enuncian y citan explícitamente los dos resultados analíticos usados. La constante inefectiva de Siegel sigue formando parte de esa dependencia.

### Desarrollos analíticos y alcance de su verificación

El resultado aritmético es incondicional en su enunciado Lean. Esto significa que el teorema final no conserva una hipótesis de densidad en casquetes; no significa que esta revisión editorial haya reconstruido de forma independiente las pruebas analíticas. Hay que distinguir una dependencia matemática, una declaración demostrada que se importa a un entorno y la procedencia de ese entorno.

| Resultado de entrada | Desarrollo en el árbol seleccionado | Función |
|---|---|---|
| Tres cuadrados libres de cuadrados en casquetes | `ThreeSquaresLib.DukeSquarefreeProof` | Combina las cotas de Weyl por grado de `IsoDegreewiseWeyl` con la cota inferior basada en Siegel de `B3_RepresentationLower` |
| Cuatro cuadrados en casquetes para radios impares | `ThreeSquaresLib.FourSquaresDenseProof` | Combina `FinalH2` con el conteo de representaciones de `JacobiCount` |
| Todos los radios congruentes con tres módulo ocho | `ThreeSquaresLib.ThreeSquaresDenseProof` | Aplica el resultado para enteros libres de cuadrados y rotaciones por cuaterniones para absorber los factores cuadrados |

El manuscrito cita a Duke (1988), Duke–Schulze-Pillot (1990), Heath-Brown (1996) y los paquetes formales correspondientes. Pommerenke se incluye como contexto histórico de la distribución en esferas y elipsoides, no como sustituto sin verificar del resultado preciso para radios impares. El Apéndice D enuncia los resultados que se usan. Esta revisión no auditó de forma independiente cada lema analítico de esos desarrollos. La documentación de `ThreeSquaresDense` en Lean atribuye el resultado a Duke–Schulze-Pillot (1990), mientras que el manuscrito atribuye el caso libre de cuadrados a Duke (1988) [17], con Duke–Schulze-Pillot como contexto, y el ensamblaje para todos los radios a [15]. La fuente Lean no se modifica, para que los hashes congelados sigan siendo válidos.

El Apéndice E proporciona las definiciones y los cuantificadores completos de T y de la versión de T+ para estadísticas de triángulos, correspondiente a `main_theorem_T_with_triangle_monitors`. Sus pruebas son dependencias matemáticas externas, aunque el cierre Lean seleccionado importe sus desarrollos. El argumento de Pasch de este paper usa la parte de T+ sobre estadísticas de triángulos, seguida de una sustitución latina; no aplica la conclusión sobre Pasch de T+.

### Notación local

El primo de la colocación de intercambios se denota por $p$, el número de copias utilizables por $s_i$ y la longitud de la cola del perfil geométrico por $d$. El Apéndice B usa $c_\ast$ para el tamaño mínimo de clase y $\chi$ para la imagen de una arista en el cociente residual. El patrón racional del Apéndice C es $v$, su reserva de vértices es $W_\ast$ y la norma direccional al cuadrado de D.3 es $\nu$. La sección 7 conserva $m$ para el orden latino, usa $\mathcal R$ para el empaquetamiento exterior y $E_{\rm mix}$ para la cota del error mixto. El empaquetamiento exterior completado de la sección 4 es $D_{\rm ext}$, distinto del error real de corrección $E$. Estos nombres son locales a las pruebas escritas; las fuentes Lean usan sus propios identificadores, con las mismas constantes e hipótesis.

## 4. Contenido e identidad del freeze de fuentes

La selección contiene 1305 módulos de dependencias ajenas a Mathlib, el módulo común `CDRIII` y su archivo de consulta de axiomas. Mathlib está fijado en `c55e6e786f49471c72fbddbec5415808896aec1e`; Lean es `v4.35.0-rc3`. Todas las fuentes matemáticas conservan sus hashes registrados. La selección sigue las importaciones y excluye los desarrollos pendientes de descenso y espectro finito. Se incluyen las licencias de origen.

El archivo `CDRIII_Lean_v1.0.zip` tiene SHA-256 `08dcee5b5d67d00d1f561988e8c716c57c92d250ca54270f3d417429fb52e649`. Su manifiesto verifica cada fuente y cada archivo de evidencia incluidos. `02_validation/v1.0/FREEZE.json` registra su identidad; `CLEAN_REBUILD_AUDIT.json` vincula los hashes de fuentes matemáticas y objetos con la ejecución correcta. El manifiesto general del paquete cubre los documentos por separado.

## 5. Reconstrucción terminada y alcance de la verificación

La ejecución aislada comenzó el 13 de noviembre de 2026 desde la selección del commit `16010adb21ac0d755d5940689ce82537399e553d`, sin objetos compilados iniciales del proyecto. Los 1306 módulos del proyecto compilaron correctamente el 14 de noviembre. Solo se copió la caché externa de Mathlib y sus dependencias con las revisiones fijadas; no se reconstruyó Mathlib desde sus fuentes. Las reanudaciones conservaron únicamente objetos producidos en esa misma reconstrucción, con comprobaciones de integridad registradas.

La configuración final corresponde al commit `8756b2ef2dbe56002617a86e97e1b16a790ae069`. Restablece las opciones originales de variables implícitas de las dos bibliotecas de absorción y aumenta el presupuesto de ejecución por pasos. CDR conserva su opción más estricta. No cambió ninguna fuente de prueba `.lean` ni ninguna hipótesis matemática. La ejecución final usó un hilo después de que `BRIUniform` fallara al asignar memoria con mayor concurrencia; ese mismo módulo, sin modificaciones, compiló después. Los intentos fallidos y los ajustes se conservan en `02_validation/v1.0/clean_run`.

Ambos comandos terminaron correctamente: `lake --no-cache --fail-fast build CDRIII` y `lake env lean checks/Axioms.lean`. Las cuatro consultas exactas solo muestran `propext`, `Classical.choice` y `Quot.sound`. Los hashes de las 1307 fuentes Lean coinciden antes y después de la ejecución, al igual que los hashes de la configuración final. La auditoría independiente del paquete verifica los hashes de objetos y los nombres exactos de las declaraciones. Los fallos de lectura de registros en Windows se corrigieron usando UTF-8 en los verificadores; ninguno requirió recompilar Lean.

Esto cierra la comprobación de reconstrucción vinculada a las fuentes. No constituye una revisión especializada independiente de cada prueba analítica importada de trabajos externos. Las reducciones escritas y las interfaces formales se revisaron dentro del alcance declarado; los cálculos de identidades finitas complementan esa revisión. La auditoría bilingüe compara las fórmulas y la numeración, y la revisión de PDF comprueba los destinos URI reales y las páginas renderizadas.

## 6. Reproducción y distribución

Desde la raíz del repositorio, `python scripts/verify_package.py` comprueba el paquete sellado sin modificarlo. Para una reconstrucción completa, se usa la versión fijada de Lean en `lean/`, se obtienen las dependencias fijadas de Mathlib y se ejecuta `lake build CDRIII`, seguido de `lake env lean checks/Axioms.lean`. Las instrucciones detalladas están en `preprints/PAPER_III/03_reproducibility/README.md`. Los archivos Markdown son las fuentes semánticas; los TeX y PDF son sus documentos de publicación.

La ubicación oficial de este paquete es `preprints/PAPER_III` en <https://github.com/jtraverso/cdr-steiner-preprints>, junto a los Papers I–II. El preprint, este companion y el archivo de fuentes Lean se depositan bajo el DOI **10.5281/zenodo.24201563**. El archivo de fuentes incluye la evidencia completa de reconstrucción vinculada a las fuentes de este preprint.
