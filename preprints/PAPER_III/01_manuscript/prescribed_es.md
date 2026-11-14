# Tipos de bloque prescritos y abundancia en sistemas triples de Steiner bicoloreados

**Juan Pablo Traverso Gianini**  
Investigador independiente, Santiago, Chile  
[jtraverso@gmail.com](mailto:jtraverso@gmail.com)  
[ORCID: 0009-0003-6068-4096](https://orcid.org/0009-0003-6068-4096)

**Paper III. Bicoloraciones de sistemas triples de Steiner.**  
**Preprint 1.0 — 14 de noviembre de 2026.**

**DOI:** 10.5281/zenodo.24201563.  
**Repositorio de la serie:** <https://github.com/jtraverso/cdr-steiner-preprints>.

## Resumen

Un sistema triple de Steiner cubre cada par de puntos con un único bloque de tres puntos. En una bicoloración, cada bloque usa exactamente dos colores. El Paper I de esta serie determina el espectro de tipos de bloque para tres colores y órdenes grandes [2]; el Paper II demuestra la conjetura de existencia de Colbourn, Dinitz y Rosa para tres colores [3]. En este paper prescribimos los conteos por tipo de bloque, en el régimen interior, para cualquier número fijo de colores. Nuestra prueba se apoya en T y T+ de *Triangle decompositions III* [4]: T produce una descomposición en triángulos a partir de cuatro condiciones sobre el grafo concreto, mientras que T+ controla simultáneamente estadísticas de triángulos prescritas.

Para $k\ge3$, mostramos que las identidades de pares bastan en órdenes suficientemente grandes si cada clase tiene tamaño lineal y cada tipo prescrito tiene un margen cuadrático positivo. Se puede conservar un sistema parcial prescrito suficientemente disperso y, uniformemente sobre las matrices compatibles con márgenes fijos, el logaritmo del número de realizaciones etiquetadas es $(1/6+o(1))n^2\log n$. Los intercambios reservados hacen exactos los conteos. También extendemos el resultado de diversidad de Pasch del Paper I [2, §6.3]: una misma matriz exacta admite ahora cualquier cantidad fija de realizaciones con distintos conteos de Pasch, para cualquier número fijo de colores. Estos sistemas no son isomorfos incluso al olvidar los colores.

Por último, para cada $k\ge4$ fijo, construimos un sistema estrictamente $k$-bicoloreado en todo orden admisible suficientemente grande. Como esta prueba de existencia se apoya en la aproximación mediante sumas de tres cuadrados, el umbral de orden resultante es inefectivo, aunque el caso de cuatro colores tenga márgenes explícitos.

## 1. ¿Qué podemos prescribir?

Un sistema triple de Steiner de orden $n=|V|$ sobre un conjunto $V$ es una familia de subconjuntos de tres elementos, llamados bloques, tal que cada par no ordenado de puntos distintos pertenece a un único bloque. Sin restricciones de color, la condición necesaria y suficiente para la existencia es $n\equiv1,3\pmod6$. Llamaremos admisibles a estos órdenes.

Fijamos una partición $V=V_1\sqcup\cdots\sqcup V_k$ en clases no vacías. Llamamos permitida a una terna si contiene dos puntos de una clase y un punto de otra, y pedimos que todo bloque sea una terna permitida. Como se usan los $k$ colores, esto se llama una $k$-bicoloración estricta: cada bloque contiene exactamente dos de ellos (aunque esto no excluye que el sistema admita una bicoloración con menos colores).

Colbourn, Dinitz y Rosa estudiaron este problema en 1999 [1]. Su pregunta para tres colores trata de los tamaños de clase que pueden realizarse. Sus Conjeturas 3.5 y 3.6 se refieren a la existencia con cuatro y cinco colores. Aquí el número de colores es fijo, pero arbitrario, y los datos que prescribimos incluyen una matriz completa de conteos por tipo. También preguntamos cuántas realizaciones tiene una matriz y si permite estructuras locales distintas.

Escribimos $c_i=|V_i|$. Para $i\ne j$, sea $t_{ij}$ el número de bloques de tipo $iij$: dos puntos en $V_i$ y uno en $V_j$. Ponemos $t_{ii}=0$. El orden de los índices importa: $t_{ij}$ y $t_{ji}$ cuentan tipos distintos.

En los teoremas sobre matrices suponemos que la partición cumple

$$
n\text{ es impar},\qquad c_ic_j\text{ es par para }i\ne j,
\qquad 3\sum_i c_i(c_i-1)=n(n-1).
\tag{1.1}
$$

Diremos que una matriz entera $t$ es compatible con esta partición si sus entradas fuera de la diagonal son no negativas y

$$
2(t_{ij}+t_{ji})=c_ic_j\quad(i\ne j),\qquad
2\sum_{j\ne i}t_{ij}=c_i(c_i-1)\quad(i=1,\ldots,k).
\tag{1.2}
$$

La sección 2 obtiene estas condiciones contando pares. Para un $\zeta>0$ fijo, la condición de interior exige

$$t_{ij}\ge\zeta n^2\quad(i\ne j).\tag{1.3}$$

Así, una misma constante positiva sirve para todas las entradas y todos los órdenes considerados; no basta con que las entradas sean distintas de cero. La escala $n^2$ proviene del número de pares: un sistema tiene $n(n-1)/6$ bloques.

**Teorema 1.1.** Sean $k\ge3$, $0<\delta\le1$ y $\zeta>0$. Existen $\gamma>0$ y $n_0$ con la siguiente propiedad. Sea $n\ge n_0$, supongamos que la partición satisface (1.1) y $c_i\ge\delta n$, y que $t$ satisface (1.2)–(1.3). Toda familia $Q$ de bloques permitidos que no repita ningún par se puede completar a un sistema triple de Steiner bicoloreado con exactamente $t_{ij}$ bloques de tipo $iij$, siempre que el grafo de los pares cubiertos por $Q$ tenga grado máximo a lo sumo $\gamma n$.

Con $Q$ vacío se realiza toda matriz interior compatible. Las constantes se eligen antes de conocer la partición, la matriz y el sistema parcial; en particular, la matriz no se elige después de haber encontrado un sistema.

Sea $N(V_1,\ldots,V_k;t)$ el número de sistemas sobre esta partición etiquetada fija y con exactamente esta matriz. Contamos familias de bloques distintas sobre $V$, no clases de isomorfismo.

**Teorema 1.2.** Sean $k\ge3$ y $\delta,\zeta,\varepsilon>0$. Existe $n_0$ tal que toda partición y toda matriz que satisfagan (1.1)–(1.3), con $c_i\ge\delta n$ y $n\ge n_0$, cumplen

$$
N(V_1,\ldots,V_k;t)>0,
\qquad
\left(\frac16-\varepsilon\right)n^2\log n
\le\log N(V_1,\ldots,V_k;t)
\le\left(\frac16+\varepsilon\right)n^2\log n.
\tag{1.4}
$$

El error es uniforme sobre las particiones y matrices compatibles con los márgenes fijados. La fórmula (1.4) identifica el coeficiente principal en la escala $n^2\log n$, pero no determina el siguiente término, de orden $n^2$.

Una configuración de Pasch consta de cuatro bloques sobre seis puntos, cada uno de los cuales aparece dos veces. Equivalentemente, tiene la forma $\{abc,ade,fbd,fce\}$ con seis puntos distintos. Contamos estas subfamilias sin orientarlas. Escribimos $P(D)$ para su número en un sistema $D$.

**Teorema 1.3.** Sean $k\ge3$, un entero no negativo $K$, $0<\delta\le1$ y $\zeta>0$. Para todo orden suficientemente grande, cada partición y cada matriz del Teorema 1.1 admiten $K$ realizaciones con valores de $P(D)$ distintos dos a dos. Todas tienen exactamente la misma matriz $t$.

Conteos de Pasch distintos implican que los sistemas no son isomorfos, incluso si se olvidan los colores. Obtenemos esta conclusión sustituyendo cuadrados latinos después de una completación exacta; no afirmamos que se pueda prescribir cualquier número de Pasch.

Los teoremas sobre matrices parten de una partición y de una matriz interior compatible. Construir esos datos para cada orden admisible es un problema aritmético separado.

**Teorema 1.4.** Para cada $k\ge4$ fijo, existe $n_0(k)$ tal que todo $n\ge n_0(k)$ con $n\equiv1,3\pmod6$ admite un sistema triple de Steiner estrictamente $k$-bicoloreado.

Para $k=4,5$, esto da las afirmaciones para órdenes grandes de las Conjeturas 3.5 y 3.6 de [1], pero no resuelve sus órdenes excepcionales pequeños. El umbral del Teorema 1.4 hereda una constante aritmética inefectiva. Si se fija un máximo finito para $k$, podemos tomar el máximo de los finitísimos umbrales correspondientes.

| Resultado | Datos fijados de antemano | Conclusión |
|---|---|---|
| Teorema 1.1 | Partición, matriz interior y sistema parcial disperso | Completación exacta |
| Teorema 1.2 | Partición y matriz interior | Coeficiente principal de conteo $1/6$ |
| Teorema 1.3 | La misma partición y matriz, y $K$ | $K$ conteos de Pasch distintos |
| Teorema 1.4 | Un $k\ge4$ fijo y un orden admisible grande | Realización de algún perfil de $k$ clases no vacías |

**Constantes.** Los Teoremas 1.1–1.3 son uniformes para márgenes fijos, pero aquí no se extrae un umbral numérico de orden. La constante del sistema parcial puede hacerse pequeña al disminuir cualquiera de los márgenes. El Teorema 1.4 tiene además un umbral aritmético explícitamente inefectivo. La estimación $n\ge1000$ del Apéndice D.4 supone que ya se dispone de una representación en el casquete; no elimina esa dificultad.

Los Teoremas 1.1–1.3 usan T y la parte de T+ que controla estadísticas de triángulos en [4]. Primero obtenemos conteos aproximados; después cambiamos bloques reservados sin cambiar los pares que cubren. El Teorema 1.2 deja libres muchas tablas latinas, mientras que el Teorema 1.3 sustituye una de esas tablas y mide los conteos de Pasch resultantes. El resultado aritmético solo se necesita para producir los perfiles del Teorema 1.4. En particular, el argumento de Pasch de la sección 7 usa completación exacta y sustitución, en lugar de la conclusión sobre Pasch de T+.

Las secciones 2–4 establecen las restricciones de pares, construyen la semilla residual y desarrollan los intercambios exactos. La sección 5 cuenta realizaciones dentro de una matriz fija; las secciones 6–7 prueban la existencia aritmética y la diversidad de Pasch. Los Apéndices A–D desarrollan el reparto entero, las inversas acotadas, el cálculo del retículo residual, el grafo usado para contar y las reducciones aritméticas; el Apéndice E reproduce los enunciados de T y T+. Los resultados externos se enuncian donde se usan; el companion separado identifica las declaraciones formales y la evidencia de verificación.

Nuestra construcción de conteo sigue el uso de tablas latinas de Wilson [11], restringidas mediante tablas agregadas de Hilton [8]. El teorema del permanente [9,10] conserva el término principal del conteo; la cota superior es de Linial–Luria [6], y Keevash [12] ofrece el contexto general del conteo de diseños. Para la existencia, el Teorema 5.15 de Keevash [14] obtiene descomposiciones partitas bajo condiciones de divisibilidad, regularidad y extensibilidad con raíces. Ofrece un marco general para la parte de existencia de nuestro problema. Su enunciado no especifica por sí solo la familia de realizaciones de una matriz exacta que contamos aquí, ni compara sus conteos de Pasch. Nos apoyamos en [4] y demostramos explícitamente los pasos sobre matrices exactas y sustituciones (no afirmamos que la mera existencia quede fuera del marco de Keevash).

Las restricciones de Pasch tienen su propia historia. Grannell, Griggs y Whitehead resolvieron el problema de existencia de sistemas anti-Pasch [19], y los conteos extremos de Pasch se estudian, por ejemplo, en Grannell y Lovegrove [20]. Esas preguntas no fijan la matriz de tipos de color que usamos aquí. El Paper I [2, §6.3] ya obtuvo distintos conteos de Pasch para un mismo perfil de tres colores, perturbando semillas y aplicando la conclusión sobre Pasch de T+. La sección 7, en cambio, conserva una matriz exacta para cualquier número fijo de colores sustituyendo un empaquetamiento latino después de completar el sistema y acotando las configuraciones mixtas.

## 2. Las identidades de pares y las coordenadas libres

### 2.1. De dónde salen los factores

Un bloque de tipo $iij$ cubre un par interno de $V_i$ y dos pares entre $V_i$ y $V_j$. Al contar los $\binom{c_i}{2}$ pares internos obtenemos

$$\sum_{j\ne i}t_{ij}=\binom{c_i}{2}.$$

Los $c_ic_j$ pares entre clases dan $2t_{ij}+2t_{ji}=c_ic_j$. Esto demuestra (1.2), incluido el factor dos de la primera ecuación. Sumar las ecuaciones de pares internos cuenta todos los bloques. Como cada bloque cubre tres pares,

$$\sum_i\binom{c_i}{2}=\frac13\binom n2.$$

Multiplicar por seis da $3\sum_i c_i(c_i-1)=n(n-1)$, la última ecuación de (1.1). Para obtener la paridad de $n$, fijemos un punto. Cada bloque que pasa por él cubre dos de sus $n-1$ pares incidentes, de modo que $n-1$ es par. Por último, la ecuación $c_ic_j=2(t_{ij}+t_{ji})$ obliga a que cada producto entre clases sea par.

Estas condiciones también restringen la propia partición. Por ejemplo, al dividir la identidad cuadrática por $n^2$ obtenemos

$$3\sum_i(c_i/n)^2=1+2/n.\tag{2.1}$$

Por tanto, para $k>3$ las clases del mismo tamaño no describen los perfiles límite de estos teoremas.

### 2.2. La diferencia entre matrices es una circulación

Supongamos que dos matrices reales tienen las mismas sumas por pares y por filas. Su diferencia $d$ satisface

$$d_{ij}=-d_{ji},\qquad \sum_{j\ne i}d_{ij}=0.\tag{2.2}$$

Sea $o$ un color central elegido. Las entradas $d_{ij}$ con $i<j$ e $i,j\ne o$ determinan todas las demás. La antisimetría da las entradas en sentido inverso y la ecuación de la fila $i\ne o$ da $d_{io}$. La ecuación de la fila $o$ se deduce entonces de que la suma de todas las filas de una matriz antisimétrica es cero. Hay

$$J=\binom{k-1}{2}$$

coordenadas independientes. En particular, $J=1$ para tres colores.

Para cada coordenada $(i,j)$, asignemos $+1$ a las flechas del ciclo $i\to j\to o\to i$, $-1$ a las flechas inversas y cero al resto. En cada uno de los tres colores entra una flecha y sale otra, por lo que todas las sumas por fila son cero. Esta circulación vale uno en su propia coordenada independiente y cero en las otras. Estos ciclos forman la base que usamos tanto para modificar las masas reales de la semilla como para corregir los conteos enteros. Por ello, coincidir en las $J$ coordenadas y satisfacer (1.2) basta para coincidir en toda la matriz.

## 3. La absorción en el grafo residual concreto

### 3.1. Qué proporcionan T y T+

Si vemos los pares como aristas, un sistema triple de Steiner bicoloreado se identifica con una descomposición del grafo completo en triángulos de tipos $iij$ ($i\ne j$). Durante la prueba eliminamos algunos pares, por lo que la absorción también debe funcionar en el grafo que queda.

Para un grafo $G$, una semilla fraccionaria exacta y difusa asigna pesos positivos de orden $1/n$ a todos sus triángulos permitidos. En cada arista, los pesos de los triángulos que la contienen suman uno. La masa de un tipo es la suma de los pesos de todos los triángulos de ese tipo. Un certificado del retículo físico expresa el indicador de las aristas como una combinación entera de triángulos permitidos que existen en $G$; los coeficientes pueden tener cualquier signo. La semilla proporciona una solución real positiva y el certificado del retículo recoge la compatibilidad entera; T necesita ambas.

El Teorema T de [4] produce una descomposición en triángulos permitidos siempre que se cumplan las cuatro condiciones físicas de la tabla. Su extensión estadística T+ también controla una lista prescrita de funciones acotadas sobre los triángulos permitidos. Las funciones se fijan antes de elegir la descomposición. Una misma descomposición aproxima todas sus sumas ponderadas por la semilla, con error a lo sumo $\eta n^2$ para cada función. Tomamos como función el indicador de cada coordenada de tipo independiente: su suma sobre la descomposición es precisamente el conteo de esos bloques. El número $J$ de pruebas es fijo, por lo que cabe en la cota polinómica que permite T+ cuando $n$ es grande.

| Condición de [4] | Significado aquí | Cómo se verifica |
|---|---|---|
| H1 | Pesos positivos exactos en cada triángulo permitido | La matriz interior y una corrección acotada después de borrar pares |
| H2 | Certificado entero en triángulos que existen en el grafo | Cálculo del retículo en el grafo completo y su versión tras un borrado disperso |
| H3 | Una cantidad lineal de vecinos comunes en cada tercera clase permitida | Tamaños de clase menos los vecinos eliminados en las dos raíces |
| H4 | Para cada par de triángulos permitidos que comparten una arista, al menos $\alpha n^{i-4}$ bisagras con exactamente $i$ vértices, para algún $6\le i\le h$ | Bisagras octaédricas de seis vértices, con dos puntos de libre elección |

Las cuatro condiciones se verifican directamente en el grafo al que se aplica T o T+. En H3 no se exige que las dos raíces formen una arista. Una bisagra de H4 es un conjunto pequeño de aristas que permite completar cualquiera de dos triángulos después de quitarles su arista común; hace posible la sustitución local que utiliza la absorción. Estas condiciones no suponen una descomposición residual ni un absorbedor proporcionado por separado.

El Apéndice E enuncia T y T+ con sus cuantificadores y definiciones completos en la notación de [4]. En particular, la constante de difusión y el exponente que acota el número de pruebas se fijan antes del grafo, de su semilla y de las funciones de prueba. Este paper solo usa la conclusión de T+ sobre estadísticas de triángulos.

### 3.2. La matriz determina la semilla del grafo completo

Definimos

$$a_{ij}=\frac{2t_{ij}}{c_ic_j}\quad(i\ne j).$$

Dividir la ecuación de pares de (1.2) por $c_ic_j$ da $a_{ij}+a_{ji}=1$. Para la ecuación por filas, multiplicamos la definición de $a_{ij}$ por $c_j$ y sumamos sobre $j\ne i$. El resultado es $2\sum_{j\ne i}t_{ij}/c_i=c_i-1$. Así, $\sum_{j\ne i}c_j a_{ij}=c_i-1$. Asignamos a cada triángulo de tipo $iij$ el peso

$$\mu(T)=\frac{a_{ij}}{c_i-1}
=\frac{t_{ij}}{\binom{c_i}{2}c_j}.\tag{3.1}$$

Para un par interno de $V_i$, hay $c_j$ maneras de completarlo con tipo $iij$ para cada $j$. Su carga es $\sum_jc_ja_{ij}/(c_i-1)=1$. Para un par entre $V_i$ y $V_j$, podemos elegir el tercer punto entre los otros $c_i-1$ puntos de $V_i$ o entre los otros $c_j-1$ puntos de $V_j$. El peso total es $a_{ij}+a_{ji}=1$. Por último, hay $\binom{c_i}{2}c_j$ triángulos de tipo $iij$, por lo que su masa total es exactamente $t_{ij}$.

El margen de (1.3) da $\mu(T)\ge2\zeta/n$, al usar $t_{ij}\ge\zeta c_i^2$ y $\binom{c_i}{2}c_j\le c_i^2n/2$. La ecuación de pares da $a_{ij}\le1$ y, como $c_i\ge\delta n$, tenemos $\mu(T)\le2/(\delta n)$ para $n$ grande. La semilla es, por tanto, positiva en todo triángulo permitido, con constantes que solo dependen de los márgenes.

### 3.3. Borrado, corrección y masas reales exactas

Al borrar un empaquetamiento también desaparece todo triángulo que use alguno de sus pares cubiertos. Si restringimos la semilla original a los triángulos restantes, algunas aristas supervivientes quedan con carga menor que uno. Antes de aplicar T debemos corregir esas cargas.

La aplicación de incidencia entre aristas y triángulos transforma pesos de triángulos en cargas de aristas. Su dominio compatible consiste en los vectores cuya carga total entre clases es dos veces la carga total interna. El Lema B.1 construye una inversa por la derecha acotada en ese dominio. El Lema B.2 corrige la restricción de la semilla mediante una serie convergente, y el Lema B.3 proporciona un certificado entero que solo usa triángulos supervivientes. Esta última afirmación es más fuerte que la existencia de una solución real; ninguna de las dos se deduce simplemente de restringir un certificado anterior.

Para usar este paso necesitamos una versión cuantitativa. Fijamos el margen de clase $\delta$, un margen de semilla $\eta>0$ con $\mu(T)\ge\eta/n$ en todo triángulo permitido (por la sección 3.2 sirve $\eta=2\zeta$) y $R\ge1$ con $n\le R\min_ic_i$ (sirve $R=1/\delta$). Ponemos

$$K_c=|\operatorname{Trip}(o)|\,400R^6(1+4R^2),\qquad C_0=1/\eta+2/\delta.$$

Aquí $\operatorname{Trip}(o)$ es la colección finita de restricciones a tres colores que contienen al color central, sobre las que se ensambla la inversa local. El factor $400R^6(1+4R^2)$ acota una corrección local; multiplicarlo por el número de restricciones acota la suma. El lema de semilla residual da un error de masa por tipo a lo sumo

$$E=(4K_c+1)C_0\Delta n\tag{3.2}$$

después de borrar un empaquetamiento cuyo grafo de pares cubiertos tiene grado máximo a lo sumo $\Delta$, siempre que $8K_cC_0^2\Delta\le n$ y se cumplan las cotas inferiores fijadas para los tamaños de clase. La semilla corregida tiene constante de difusión $2C_0$.

Para obtener masas reales exactas en las coordenadas elegidas, tomamos un cubo de objetivos alrededor del vector deseado de $J$ coordenadas. En cada vértice del cubo, la corrección produce una semilla cuyo vector de masas dista a lo sumo $E$ de ese vértice en cada coordenada. Si el radio del cubo es mayor que $E$, el vector deseado está en la envolvente convexa de esos vectores de salida. En efecto, supongamos que un funcional lineal lo separa de esa envolvente. Elegimos el vértice de entrada cuyos signos coinciden con los de los coeficientes del funcional. Su contribución hacia fuera es el radio multiplicado por la suma de los valores absolutos de esos coeficientes; el error posible es a lo sumo $E$ multiplicado por la misma suma. Esto contradice la separación. Una combinación convexa de las semillas correspondientes sigue siendo una semilla exacta positiva y tiene precisamente las masas deseadas.

Las estimaciones y sus dominios se demuestran en el Apéndice B. Para aplicar el argumento del cubo, extendemos los cambios de las coordenadas independientes mediante la base de ciclos de la sección 2.2. Elegimos un radio mayor que (3.2), pero suficientemente pequeño para conservar el margen interior original. Como el grado del borrado es un múltiplo suficientemente pequeño de $n$, ambas exigencias son compatibles. No se impone ninguna hipótesis nueva a la matriz de entrada.

Aquí hay dos escalas de error diferentes. El error $E=O(\lambda n^2)$ que produce el borrado de las huellas de los intercambios se absorbe en este paso real de convexidad. No se descuenta de la reserva entera, cuyo tamaño es del orden de $\lambda^2n^2$. Una vez exactas las masas reales, solo el error menor de T+ debe caber en esa reserva. La Figura 2 separa los dos pasos.

## 4. Completación dispersa con tipos exactos

Demostramos el Teorema 1.1 haciendo que el error estadístico sea menor que una reserva de intercambios independientes de una unidad.

### 4.1. Reservar los intercambios antes de aplicar absorción

El intercambio que aparece en el Paper I [2, §4, antes del Lema 4.1] tiene dos mitades sobre nueve puntos, cada una con nueve bloques. Ponemos los puntos $0,1,2$ en el color $i$, los puntos $3,4,5$ en el color central $o$ y los puntos $6,7,8$ en el color $j$. Cada cadena de tres dígitos de la tabla representa un bloque.

| Mitad | Bloques | Conteo del tipo $iij$ |
|---|---|---|
| Baja | 015, 023, 067; 127, 134, 168; 356, 378, 458 | 1 |
| Alta | 016, 027, 035; 123, 145, 178; 348, 367, 568 | 2 |

Ambas mitades cubren exactamente los mismos 27 pares. Por ejemplo, los pares 01, 05 y 15 del bloque bajo 015 aparecen en los bloques altos 016, 035 y 145. Comprobar los demás bloques da el mismo conjunto de pares, sin repeticiones en ninguna mitad. Cambiar de alta a baja disminuye en uno la coordenada $(i,j)$. Las otras coordenadas independientes no cambian, pues todos los demás tipos que se modifican contienen al color central. Sus cambios son el negativo de la circulación de la base de la sección 2.2, como muestra la Figura 1. Colocamos copias en tres clases de color como en la construcción del espectro exacto de [2].

\begin{figure}[H]
\centering
\includegraphics[width=\linewidth]{figures/circulation_es.pdf}
\caption{Cambio de los conteos de tipos al sustituir la mitad alta por la mitad baja de una copia reservada. Una entrada dirigida cuenta bloques cuyo color repetido está en el origen de la flecha. Las flechas continuas añaden un bloque y las discontinuas quitan uno. El cambio es antisimétrico y tiene sumas por fila nulas, de modo que conserva todas las ecuaciones de pares y filas. El diagrama representa conteos, no el sistema de bloques de nueve puntos.}
\label{fig:circulation}
\end{figure}

Elegimos una constante $\lambda>0$ suficientemente pequeña, que solo depende de $k,\delta,\zeta$. Para $n$ grande, elegimos un primo $p>8$ con $\lambda n/4\le p\le\lambda n$. La colocación proporciona $p^2$ copias por coordenada, con conjuntos de pares cubiertos disjuntos dos a dos. Llamaremos conjunto de pares de una copia a ese conjunto común a sus dos mitades. La colocación de varios colores usada aquí acota el grado de la unión por $9p$; el Paper I registra una cota menos ajustada para su colocación. Los vértices caben en las clases si exigimos $18(J+1)\lambda\le\delta$.

Una colocación explícita es la siguiente. Damos a cada una de las nueve posiciones su propio conjunto de puntos, indexado por el cuerpo de $p$ elementos. Para $(u,v)$ en el cuadrado de ese cuerpo, colocamos la posición $\ell$ en la coordenada $u+\ell v$, para $\ell=0,\ldots,8$. Dos extremos en conjuntos distintos determinan $(u,v)$ de manera única, porque sus pendientes distintas difieren en un elemento no nulo del cuerpo. Por tanto, los conjuntos de pares ocupados son disjuntos. Cada punto pertenece a $p$ copias y tiene a lo sumo ocho vecinos por copia, lo que da grado a lo sumo $8p\le9p$. Usamos conjuntos separados para las coordenadas independientes. Así, el costo en vértices es lineal en $p$, mientras que la cantidad de intercambios es cuadrática.

Sea $L_Q$ el conjunto de pares cubiertos por el empaquetamiento prescrito y sea $\Delta_Q$ el grado máximo del grafo que forman; el Teorema 1.1 supone $\Delta_Q\le\gamma n$. Descartamos todo intercambio cuyo conjunto de pares corte a $L_Q$. Elegimos un par de $L_Q$ en cada copia descartada. Como los conjuntos de pares de las copias son disjuntos, los pares elegidos son distintos. Se descartan a lo sumo $|L_Q|$ copias. Si $\gamma=\lambda^2/256$, entonces

$$|L_Q|\le n\Delta_Q\le\gamma n^2\le p^2/16.$$

Por tanto, el número $s_i$ de copias utilizables en cada coordenada satisface $p^2/2\le s_i\le p^2$. La reserva retenida evita $Q$.

### 4.2. Centrar correctamente el objetivo residual

Ponemos cada intercambio retenido en su mitad alta y llamamos $B_i$ al conteo que resulta en la coordenada $i$. Sea $\pi_i$ el conteo en $Q$. La masa que queremos para la semilla en el grafo fuera de ambos empaquetamientos es

$$r_i=t_i-\pi_i-B_i+s_i/2.\tag{4.1}$$

Para entender este centro, supongamos por un momento que el conteo residual fuese exactamente $r_i$. Adjuntar $Q$ y todas las mitades altas daría $r_i+\pi_i+B_i=t_i+s_i/2$. Alcanzaríamos el objetivo cambiando la mitad de las copias. El término $s_i/2$ centra, por tanto, las correcciones enteras disponibles, mientras que $-\pi_i$ descuenta los bloques ya prescritos en $Q$.

La base de circulaciones extiende el desplazamiento a toda la matriz sin cambiar las sumas por pares ni por filas. Como $B_i\le9p^2$ y $\pi_i\le|Q|\le|L_Q|$, el desplazamiento de cada coordenada es a lo sumo $10\lambda^2n^2$. El grado del grafo de pares cubiertos por $Q$ y por la reserva inicial es a lo sumo

$$\Delta_Q+9p\le(\gamma+9\lambda)n\le18\lambda n.$$

Elegimos $\lambda$ de modo que ambos costes quepan en las estimaciones de corrección de la semilla y del margen interior de la sección 3. La construcción de masas reales exactas da una semilla difusa de este grafo residual concreto con masas $r_i$. Los lemas del retículo, de vecinos comunes y de bisagras verifican las otras tres condiciones en el mismo grafo.

### 4.3. Una completación aproximada y después la corrección entera

Aplicamos T+ con tolerancia $\lambda^2/512$ y los $J$ indicadores de coordenadas. Obtenemos una misma descomposición residual $D_0$ con

$$|N_i(D_0)-r_i|\le\lambda^2n^2/512\le s_i/4$$

para todas las coordenadas a la vez. Adjuntamos $Q$ y obtenemos una descomposición $D_{\rm ext}$ fuera de los conjuntos de pares reservados. Sustituir (4.1) da

$$\left|N_i(D_{\rm ext})-(t_i-B_i+s_i/2)\right|\le s_i/4.$$

Restamos $t_i-B_i$ en la última desigualdad. Así, el entero $z_i=N_i(D_{\rm ext})+B_i-t_i$ queda entre $s_i/4$ y $3s_i/4$, y por tanto entre cero y las $s_i$ copias disponibles. Cambiamos exactamente $z_i$ copias de la coordenada $i$ a su otra mitad. Sus pares cubiertos no cambian, de modo que los intercambios no alteran $D_{\rm ext}$ ni se interfieren entre sí. El conteo final de esa coordenada es

$$N_i(D_{\rm ext})+B_i-z_i=t_i.$$

Las identidades por pares y por filas determinan ahora todas las otras entradas, por la sección 2.2. Esto demuestra la completación exacta conservando todos los bloques de $Q$.

\begin{figure}[H]
\centering
\includegraphics[width=\linewidth]{figures/two_scales_es.pdf}
\caption{Las dos correcciones actúan en escalas diferentes. Izquierda: en un ejemplo esquemático con dos coordenadas, un cubo de radio mayor que el error de corrección conserva el objetivo dentro de la envolvente convexa de sus vértices corregidos. Así se obtienen masas reales exactas. Derecha: T+ deja una discrepancia entera menor, de modo que el número de intercambios necesarios queda entre un cuarto y tres cuartos de las copias disponibles. Los paneles no usan una misma escala numérica.}
\label{fig:two-scales}
\end{figure}

Las constantes se eligen en el orden siguiente. Fijamos $k,\delta,\zeta$, elegimos $\lambda$ suficientemente pequeña para las estimaciones de semilla y colocación, ponemos $\gamma=\lambda^2/256$ y fijamos la tolerancia de T+. Después tomamos el máximo de los umbrales de orden necesarios. La partición, la matriz y el empaquetamiento se reciben al final. No afirmamos un valor numérico de $n_0$.

No afirmamos que esta dependencia sea leve. Al disminuir $\delta$, pueden crecer la razón $R$ y la constante de la inversa $K_c$; al disminuir el margen de la semilla, crece $C_0$. Por ello, la condición $8K_cC_0^2\Delta\le n$ exige un presupuesto de borrado menor. La elección posterior $\gamma\le\lambda^2/256$ permite además que el empaquetamiento prescrito quepa en la reserva de intercambios. Son elecciones suficientes para márgenes positivos fijos, no una cota optimizada que sea uniforme hasta margen cero.

## 5. Conteo para cada matriz prescrita

La construcción mediante grupos y tablas latinas que sigue usa el esquema de conteo de Wilson [11]. Para conteos de diseños sin estas restricciones, véase Keevash [12]. Aquí mantenemos fija la matriz objetivo durante todo el argumento. La cota superior del Teorema 1.2 se deduce de Linial–Luria [6]: olvidar los colores y los conteos por tipo inyecta nuestra familia en la de todos los sistemas triples de Steiner etiquetados. Queda obtener el coeficiente $1/6$ para cada matriz fijada, no para una matriz elegida después mediante el principio del palomar.

### 5.1. Una tabla agregada prescrita conserva muchas realizaciones latinas

Dividimos las filas, columnas y símbolos de un cuadrado latino de orden $B$ en clases de tamaños $b_i$. Una tabla agregada especifica el número $M_{ijs}$ de entradas que tienen fila en la clase $i$, columna en la clase $j$ y símbolo en la clase $s$. Sus tres familias de sumas marginales deben ser $b_ib_j$, $b_ib_s$ y $b_jb_s$. La construcción de Hilton [8] realiza toda tabla agregada entera no negativa con esas marginales mediante un cuadrado latino. Imponemos entradas cero para las ternas de colores prohibidas.

Elegimos una realización y recordamos solo la clase del símbolo en cada casilla. Para una clase de símbolos de tamaño $b_s$, las casillas de esa clase forman un grafo bipartito $b_s$-regular sobre las $B$ filas y las $B$ columnas. Asignar los símbolos individuales equivale a descomponerlo, de forma ordenada, en $b_s$ emparejamientos perfectos. Las distintas clases de símbolos se pueden realizar de manera independiente.

La cota del permanente de Egorychev y Falikman [9,10], aplicada después de retirar cada emparejamiento, da al menos

$$(d!)^B\left(\frac{B!}{B^B}\right)^d$$

factorizaciones ordenadas de un grafo bipartito $d$-regular fijo. En efecto, cuando el grado restante es $d-r$, dividir su matriz de adyacencia por $d-r$ produce una matriz doblemente estocástica. Su permanente es al menos $B!/B^B$, por lo que hay al menos $(d-r)^B B!/B^B$ opciones para el siguiente emparejamiento. Multiplicar para $r=0,\ldots,d-1$ da el producto mostrado.

El logaritmo de ese producto es $B\log(d!)+d\log(B!)-Bd\log B$. Aplicar $\log(s!)\ge s\log s-s$ por separado en $s=d$ y $s=B$ deja $Bd(\log d-2)$. Para una clase de símbolos, $d=b_s$. Al sumar sobre las clases usamos $\sum_s b_s=B$. Denotamos por $\ell$ una cota inferior común para los tamaños de las clases de símbolos, distinta de la matriz objetivo $t$. Si cada $b_s\ge\ell$, obtenemos

$$\log\#\{\text{realizaciones de esta tabla agregada}\}
\ge B^2(\log\ell-2).\tag{5.1}$$

Asignar los símbolos individuales no cambia la tabla agregada: conserva la clase de símbolo de cada casilla. Por eso el número de opciones sigue siendo grande aunque la matriz de tipos esté prescrita.

### 5.2. Una sola completación residual para todas las tablas

Sea $g\ge15$ un orden admisible de grupos con $2/g\le\zeta$, pongamos $\theta=2/g$ y elijamos un sistema triple de Steiner sobre sus $g$ índices. Una colocación de Wilson proporciona $g$ grupos del mismo tamaño $B$, con las mismas cantidades $b_i\ge\ell$ de cada color, y una reserva. Los grupos cubren casi todos los vértices. Sobre cada bloque del sistema de índices colocamos una tabla latina entre sus tres grupos.

Todas las tablas latinas cubren los mismos pares entre grupos. Por eso podemos completar una vez el grafo restante común y conservar esa completación para todas las elecciones posteriores. Si $O=g(g-1)/6$ es el número de bloques de índices, las elecciones de las $O$ tablas son independientes. Cada sistema final permite recuperar sus tablas: el bloque que contiene un par dado de los dos primeros grupos identifica su entrada en el tercero. Por tanto, las elecciones de tablas se aplican de manera inyectiva en sistemas.

Los tipos exactos imponen una condición más. Sea $\mathcal D_{\rm res}$ la completación fija y sean $r_{ij}$ sus conteos por tipo. Construiremos la parte latina a partir de tablas agregadas simétricas, cuya contribución a cada tipo dirigido es un múltiplo de tres. Por tanto, necesitamos

$$t_{ij}-r_{ij}\ge0,\qquad 3\mid(t_{ij}-r_{ij}).\tag{5.2}$$

Antes de completar, reservamos una cantidad acotada de intercambios dentro de la reserva de vértices. La elección de sus mitades corrige los residuos módulo tres de las coordenadas de ciclo independientes, sin cambiar los pares entre grupos. Las ecuaciones de pares y filas dan entonces los residuos de todas las otras entradas. El grafo restante es suficientemente pequeño para que su número de bloques sea a lo sumo $\theta n^2$, mientras que $t_{ij}\ge\zeta n^2$. Elegir $\theta\le\zeta$ da la primera desigualdad de (5.2).

Ponemos $q_{ij}=(t_{ij}-r_{ij})/3$. Restar las identidades del sistema completado de (1.2) muestra que

$$q_{ij}+q_{ji}=O b_ib_j,\qquad \sum_jq_{ij}=O b_i^2.$$

El lema de reparto entero divide $q$ en $O$ matrices no negativas $y^{(a)}$ que satisfacen las mismas ecuaciones sin el factor $O$. La normalización por tres corresponde a las tres posiciones posibles del color que aparece una sola vez entre las clases de fila, columna y símbolo de un bloque latino. Cada $y^{(a)}$ produce una tabla agregada compatible cuya contribución por tipos es $3y^{(a)}$. Las tablas pueden variar independientemente, con contribución total $3\sum_a y^{(a)}=t-r$.

El Apéndice A demuestra el reparto. El Apéndice C construye el patrón balanceado, lo coloca en la partición dada, prueba las condiciones de semilla y retículo residuales y corrige los residuos módulo tres antes de contar las tablas latinas. El Lema C.2 demuestra la realización de las tablas agregadas conservando sus restricciones de soporte. Estas construcciones solo dependen de las hipótesis ya enunciadas.

### 5.3. Obtener el coeficiente principal

Con esta elección de $\theta$, la construcción proporciona

$$gB\ge(1-\theta)n,\qquad \ell\ge n/C,$$

donde $C$ depende de $g,k$ y de los márgenes fijados, pero no de la partición ni del objetivo. Por (5.1) y la inyección,

$$\log N(V_1,\ldots,V_k;t)\ge\frac{g(g-1)}6 B^2(\log\ell-2).\tag{5.3}$$

Dividimos por $n^2\log n$. La cota $\ell\ge n/C$ da $(\log\ell-2)/\log n\ge1-(\log C+2)/\log n$. La cota sobre $gB$ da

$$\frac{g(g-1)B^2}{6n^2}\ge\frac16(1-1/g)(1-2/g)^2.$$

Primero elegimos un $g$ admisible fijo suficientemente grande para que el miembro derecho quede tan cerca de $1/6$ como necesitemos. Después aumentamos $n$ para hacer pequeño el error logarítmico. Junto con la cota superior, esto demuestra (1.4). El caso de tres colores usa un patrón equilibrado de tres clases en la colocación; cumple las mismas condiciones de completación residual y conteo. No se necesita un resultado para todos los órdenes finitos.

## 6. Un perfil para cada orden admisible grande

Los Teoremas 1.1–1.3 se aplican a datos de entrada con márgenes. Ahora explicamos la construcción separada de perfiles que requiere el Teorema 1.4.

### 6.1. Tamaños enteros próximos a un perfil real

Dividir las identidades exactas de tamaños de clase por $n$ y por $n^2$ sugiere las condiciones límite reales

$$p_i>0,\qquad \sum_i p_i=1,\qquad \sum_i p_i^2=1/3.$$

Para obtener una semilla factible elegimos las desigualdades estrictas de corte

$$\left(\sum_{i\in S}p_i\right)^2<3\sum_{i\in S}p_i^2
\quad(\varnothing\ne S\subsetneq\{1,\ldots,k\}).\tag{6.1}$$

Para $k$ fijo solo hay finitísimos subconjuntos propios no vacíos, así que las desigualdades estrictas tienen un margen común positivo. Usamos ese margen en las condiciones de corte del teorema de factibilidad entera de Gale [5]. Después de descontar una pequeña cantidad positiva de base de las asignaciones dirigidas deseadas, el teorema de Gale proporciona las asignaciones restantes para perfiles enteros suficientemente cercanos que satisfagan (1.1). La sección 3 verifica entonces las hipótesis del grafo completo y aplica T. El Lema D.1 presenta explícitamente la red, sus capacidades y todas las desigualdades de corte.

Para $k=d+2\ge5$, el perfil usado es

$$p=(A,A+r/2,r,r/2,\ldots,r/2^{d-1}).$$

Ponemos $s=\sum_{j<d}2^{-j}$, $s_2=\sum_{j<d}4^{-j}$ y $A=(1-rs-r/2)/2$. La suma de las coordenadas es uno. La suma de sus cuadrados es $1/3$ precisamente cuando

$$F(r)=\frac{(1-rs)^2}{2}+\frac{r^2}{8}+r^2s_2-\frac13=0.$$

Para $d\ge3$, se cumple $7/4\le s<2$ y $21/16\le s_2<4/3$. Sustituir da $F(9/100)\ge0$ y $F(13/100)\le0$. La continuidad proporciona una raíz en ese intervalo. También se obtiene $A>2r>0$.

Para verificar los cortes, separamos los subconjuntos que contienen cero, una o las dos coordenadas grandes. En un subconjunto de la cola geométrica, los términos posteriores al mayor suman menos que ese término mayor. Una inducción en el número de términos da $(\sum 2^{-j})^2<3\sum4^{-j}$. Si aparece exactamente una coordenada grande, es mayor que toda la cola seleccionada, pues supera $2r$; al desarrollar el cuadrado, la diferencia sigue siendo positiva. Si aparecen ambas, sea $D$ la parte no vacía de la cola que se omite. Restar de la identidad global la suma de cuadrados seleccionada permite escribir la diferencia de (6.1) como

$$rP_D(2-rP_D)-3r^2Q_D,$$

donde $P_D=\sum_{j\in D}2^{-j}$ y $Q_D=\sum_{j\in D}4^{-j}\le P_D$. Como $P_D<2$ y $5r<2$, la expresión es positiva. La comprobación finita de los cortes proporciona el margen requerido.

### 6.2. Por qué no basta con redondear

Redondear todas las coordenadas por separado solo conserva su suma de forma aproximada y destruye la ecuación cuadrática exacta (2.1). Para satisfacer ambas ecuaciones, primero redondeamos a enteros pares las clases cuyos índices son al menos cuatro. Los objetivos que quedan para la suma y la suma de cuadrados son

$$w=n-\sum_{i\ge4}c_i,\qquad S_4=n(n+2)/3-\sum_{i\ge4}c_i^2.$$

Necesitamos cuatro enteros con suma $w$ y suma de cuadrados $S_4$. Ponemos $M=4S_4-w^2$. En los órdenes admisibles, las paridades elegidas dan $M\equiv3\pmod8$. El teorema de aproximación aritmética proporciona

$$a^2+b^2+c^2=M$$

cerca de la dirección determinada por las cuatro primeras coordenadas reales. Definimos

$$
(c_0,c_1,c_2,c_3)=\frac14
(w+a+b+c,\ w+a-b-c,\ w-a+b-c,\ w-a-b+c).
\tag{6.2}
$$

Las tres coordenadas de la representación son impares. El perfil cumple $p_0+p_2=p_1+p_3$, de modo que el objetivo de la coordenada intermedia $b$ es cero. Cambiar solo el signo de $b$, si hace falta, hace que $w+a+b+c$ sea divisible por cuatro sin alterar la aproximación. El Lema D.3 desarrolla el argumento de redondeo y signo. Los otros tres numeradores tienen entonces la misma divisibilidad. Sumar las cuatro ecuaciones de (6.2) da la suma $w$. Elevar al cuadrado y sumar da $4\sum_{i<4}c_i^2=w^2+M=4S_4$. Su suma de cuadrados es $1$ módulo cuatro, por lo que exactamente uno de esos cuatro enteros es impar. Las clases ya redondeadas son pares. Todos los productos entre clases son, por tanto, pares.

La aproximación hace que $c_i/n$ quede tan cerca de $p_i$ como se necesite. La positividad y los márgenes estrictos de corte se conservan. Así pasamos del perfil real a datos enteros admisibles para cada orden admisible suficientemente grande.

### 6.3. El resultado aritmético y el caso de cuatro colores

El resultado exacto demostrado en el desarrollo aritmético es el siguiente: para todo vector unitario $u\in\mathbb R^3$ y todo $\epsilon>0$, cada entero suficientemente grande $M\equiv3\pmod8$ tiene una representación entera $x_1^2+x_2^2+x_3^2=M$ con

$$|x_i-\sqrt M\,u_i|\le\epsilon\sqrt M\quad(i=1,2,3).\tag{6.3}$$

El resultado para enteros libres de cuadrados es el teorema de equidistribución esférica de Duke [17]; [7] lo sitúa en la teoría más general de formas ternarias positivas. El desarrollo formal [15] combina su versión para enteros libres de cuadrados con rotaciones por cuaterniones para tratar los factores cuadrados. Así, (6.3) recoge el resultado ensamblado para todos los radios, no un nuevo teorema clásico de equidistribución. El Lema D.2 da los resultados precisos y la reducción. El resultado de cuatro cuadrados para radios impares procede de [16]; su prueba sigue la vía del método del círculo descrita allí, con el marco de Heath-Brown [18].

Para cuatro colores, usamos el radio prescrito $M=n(n+8)/3$, que es entero y congruente con tres módulo ocho. Aplicamos (6.3) en $u=(1,0,0)$ con $\epsilon=1/8$. Obtenemos $a\ge7\sqrt M/8$ y $|b|,|c|\le\sqrt M/8$, y por tanto

$$3(a^2+b^2+c^2)=n(n+8),\qquad 7|b|\le a,\quad7|c|\le a.$$

El Apéndice D.4 transforma estas desigualdades en clases enteras de tamaño al menos $n/16$, con las identidades exactas de pares. La asignación explícita que allí se construye está entre $1/400$ y $1-1/400$ y satisface todas las ecuaciones de la semilla. Aplicar T da el caso de cuatro colores.

Para $k\ge5$, las secciones 6.1–6.2 proporcionan los datos requeridos por T. Tomar el máximo de los umbrales aritmético y combinatorio demuestra el Teorema 1.4. El umbral aritmético es inefectivo porque su prueba usa el teorema de Siegel, y mejorar las constantes explícitas del absorbedor no elimina esa dependencia.

## 7. Distintos conteos de Pasch con la misma matriz exacta

### 7.1. Completar un empaquetamiento latino

Tomamos la constante de completación $\gamma$ del Teorema 1.1 y ponemos

$$a=\min\{1,\delta/4,\gamma/18\}.$$

Para $n$ grande, elegimos $m=2^r$ con $an/2<m\le an$ y $r\ge2K+2$. Elegimos conjuntos disjuntos $U,V$ de tamaño $m$ en una clase de color, y $W$ de tamaño $m$ en otra. Es posible porque $2m\le\delta n$.

Un cuadrado latino $L$ sobre esos conjuntos da el empaquetamiento

$$Q_L=\{\{u_i,v_j,w_{L(i,j)}\}:1\le i,j\le m\}.$$

Cubre una vez cada par entre dos de $U,V,W$ y ningún otro par. Todos sus $m^2$ bloques son del mismo tipo. El grafo de pares cubiertos tiene grado $2m$. Como $m\le an$ y $a\le\gamma/18$, se cumple $2m\le\gamma n$, tal como exige el Teorema 1.1. Completamos uno de estos empaquetamientos, $Q_0$, a una realización exacta $D_0$ y ponemos $\mathcal R=D_0\setminus Q_0$. Para cualquier otro cuadrado latino, $D_L=\mathcal R\cup Q_L$ vuelve a ser un sistema triple de Steiner con exactamente la misma matriz $t$.

### 7.2. Contar los dos términos mixtos

Clasificamos cada Pasch por el número de sus bloques que pertenecen a $Q_L$. Las únicas posibilidades son cero, uno, dos y cuatro. Tres es imposible: los tres bloques latinos aportan tres incidencias en cada parte reservada, mientras que cada vértice de un Pasch tiene incidencia total par. Su cuarto bloque debe, por tanto, cortar cada parte en una cantidad impar de puntos y, como tiene tres puntos, una vez en cada parte. Ese bloque no puede pertenecer a $\mathcal R$, pues sus pares entre partes reservadas ya estaban cubiertos por $Q_0$.

En consecuencia,

$$P(D_L)=P(\mathcal R)+I(L)+C_1(L,\mathcal R)+C_2(L,\mathcal R),\tag{7.1}$$

donde $I(L)$ cuenta los intercalados: dos filas y dos columnas cuyas cuatro entradas tienen el patrón $x,y$ en una fila y $y,x$ en la otra. Sus cuatro bloques asociados forman precisamente los Pasch contenidos en $Q_L$. El término $C_s$ cuenta las configuraciones con exactamente $s$ bloques latinos. El término de dos bloques puede aparecer, por lo que se conserva junto al de un bloque.

Si fijamos la tabla y variamos de forma independiente sus permutaciones de filas y símbolos, cualquier bloque latino potencial especificado aparece con frecuencia $1/m$. Dos bloques compatibles especificados que se cortan aparecen conjuntamente con frecuencia $1/[m(m-1)]$. Si comparten fila o columna, dos entradas distintas tienen dos imágenes de símbolo distintas. Si comparten símbolo, la preimagen de ese símbolo determina una fila en cada una de dos columnas, y esas filas son distintas; la permutación uniforme de filas tiene la misma frecuencia para dos puntos. Así quedan cubiertas las tres partes posibles de intersección.

Las cotas de candidatos se obtienen directamente de la unicidad de los pares. Para una configuración con un bloque latino, llamemos $\mathcal R_1,\mathcal R_2,\mathcal R_3$ a los otros tres bloques. Sus intersecciones dos a dos son tres puntos distintos $x,y,z$. Los bloques de $\mathcal R$ que cubren $xy,xz,yz$, si existen, son únicos; sus terceros puntos recuperan el posible bloque latino. Cada configuración tiene una codificación por una terna ordenada $(x,y,z)$ y cada codificación recupera a lo sumo una configuración. Así, $n^3$ acota estos candidatos. Más adelante usamos la cota menos ajustada $27n^3$ para simplificar las estimaciones.

Para una configuración con dos bloques latinos, los dos bloques exteriores comparten un punto $x$, mientras que los dos bloques latinos comparten otro punto $u$. Hay a lo sumo $n$ bloques de $\mathcal R$ por un $x$ fijo: sus otros puntos forman pares disjuntos, pues $\mathcal R$ es un empaquetamiento. Elegimos $x$, un par ordenado de bloques exteriores que pasan por él, y $u$. Hay a lo sumo $n^4$ opciones. Sus otros cuatro puntos deben repartirse entre los dos bloques latinos. Cada bloque latino debe cortar a ambos bloques exteriores, de modo que hay a lo sumo dos emparejamientos cruzados. Por tanto, $2n^4$, y también la cota menos ajustada $6n^4$, acota estos candidatos. Exigir las partes reservadas correctas solo reduce su número. Promediar sobre las dos permutaciones da ahora una reetiquetación con

$$0\le C_1+C_2\le E_{\rm mix}(n,m),\qquad
E_{\rm mix}(n,m)=\frac{27n^3}{m}+\frac{6n^4}{m(m-1)}.\tag{7.2}$$

Los dos términos mixtos se promedian juntos, así que una misma reetiquetación satisface (7.2). No se supone independencia entre sus apariciones.

### 7.3. Separar los conteos internos más que el error mixto

Para $0\le i<K$, tomamos la tabla de suma de

$$G_i=(\mathbb Z/4\mathbb Z)^i\times(\mathbb Z/2\mathbb Z)^{r-2i}.$$

Todos los grupos tienen orden $m$. Un intercalado de una tabla de suma abeliana queda determinado por su fila inicial, su columna inicial y un elemento no nulo $h$ con $2h=0$. Recíprocamente, las dos ecuaciones de símbolos repetidos obligan a esa forma. Cada intercalado sin orientar tiene cuatro orientaciones, por lo que

$$4I_i=m^2\bigl(|G_i[2]|-1\bigr)=m^2(2^{r-i}-1).\tag{7.3}$$

Para $i<j<K$, se deduce $I_i-I_j\ge m^3/(4\cdot2^K)$. Permutar filas y símbolos conserva $I_i$. Elegimos para cada tabla una reetiquetación adecuada mediante (7.2). El sistema completado tiene su conteo de Pasch en

$$[P(\mathcal R)+I_i,\ P(\mathcal R)+I_i+E_{\rm mix}(n,m)].$$

Para comparar el error con la separación, usamos $m\ge an/2$ en el primer término de (7.2). En el segundo, $m\ge2$ da $m-1\ge m/2$, y por tanto $m(m-1)\ge m^2/2\ge a^2n^2/8$. Las dos estimaciones dan

$$E_{\rm mix}(n,m)\le54n^2/a+48n^2/a^2\le102n^2/a^2.$$

La separación es al menos $a^3n^3/(32\cdot2^K)$. Para que supere el error basta $3264\cdot2^K<a^5n$; la construcción utiliza la condición suficiente más cómoda $4096\cdot2^K<a^5n$. Los intervalos son entonces disjuntos, lo que demuestra el Teorema 1.3. Comparamos una separación cúbica con un error cuadrático, con $a$ y $K$ fijados antes de $n$. Los casos $K=0,1$ no necesitan un argumento de separación.

## 8. Preguntas más allá del régimen interior

El margen positivo en cada tipo dirigido se usa tanto para corregir la semilla como para realizar los intercambios exactos. Eliminarlo plantea cuatro preguntas distintas.

| Pregunta | Resultado disponible aquí | Qué debe aportar una extensión |
|---|---|---|
| Espectro general de frontera para $k\ge4$ | Toda matriz compatible con un margen cuadrático positivo fijo | Un sustituto de la semilla interior y de las rutas de intercambio cuando algunos tipos desaparecen o son escasos |
| Espectro de tres colores en todo orden admisible | El resultado interior para órdenes grandes; el Paper I da el espectro para orden grande [2] | Una construcción uniforme que cubra la brecha de órdenes finitos, en vez de una sucesión de testigos aislados |
| Conteo y diversidad de Pasch en la frontera | Conteo principal óptimo y distintos conteos de Pasch con la misma matriz interior exacta | Suficientes elecciones independientes y sustituciones locales que conserven todas las cuotas de frontera |
| Un umbral de orden universal efectivo | Existencia para cada $k\ge4$ fijo | Un sustituto efectivo del paso aritmético que usa el teorema de Siegel |

Los obstáculos son distintos. Un tipo nulo puede eliminar una ruta necesaria para un intercambio, aunque exista una realización entera. Contar exige, además, que la completación conserve muchas elecciones. La última pregunta es aritmética: mejorar una inversa combinatoria no vuelve efectivo, por sí solo, el umbral actual.

Un procedimiento de selección aleatoria por rondas (*nibble*) que respete los tipos podría ayudar a producir empaquetamientos parciales con márgenes positivos menores. Para llegar a las conclusiones de frontera seguirían haciendo falta un certificado entero en el grafo restante e intercambios permitidos suficientes para corregir las cuotas exactas. Una estimación de empaquetamiento a menor densidad no proporciona por sí sola estos dos elementos.

## Apéndice A. Reparto de las cuotas enteras

**Lema A.1.** Sea $M$ una matriz entera no negativa sobre dos conjuntos finitos de índices, con sumas por fila $h a_i$ y por columna $h b_j$, donde $h$ es un entero no negativo. Entonces $M$ es la suma de $h$ matrices enteras no negativas, cada una con sumas por fila $a_i$ y por columna $b_j$. Cada sumando vale cero donde $M$ vale cero.

*Demostración.* Supongamos primero $h>0$. La matriz real $M/h$ tiene las sumas enteras por fila y columna requeridas. Podemos redondearla a una matriz entera conservando esas sumas y dejando cada entrada entre su parte entera inferior y su parte entera superior. Llamaremos suelo y techo a estas dos cotas. Procedemos así. Formamos el grafo bipartito de sus entradas no enteras. Todo vértice no aislado tiene grado al menos dos: si una fila o columna tuviera exactamente una entrada no entera, su suma no podría ser entera. Un grafo finito sin vértices de grado uno y con alguna arista contiene un ciclo. En ese ciclo, que tiene longitud par, aumentamos entradas alternadas y disminuimos las otras en la mayor cantidad positiva que respete los límites originales de suelo y techo. Cada fila y columna del ciclo tiene un aumento y una disminución, así que su suma no cambia. Al menos una entrada se vuelve entera y las entradas ya enteras fuera del ciclo siguen fijas. Repetimos. El número de entradas no enteras disminuye estrictamente, por lo que el proceso termina.

Llamemos $X$ a la matriz entera obtenida. Sus entradas son no negativas y no superan las de $M$: para un entero $M_{ij}\ge0$, el techo de $M_{ij}/h$ es a lo sumo $M_{ij}$. Así, $M-X$ es no negativa, tiene sumas por fila $(h-1)a_i$ y por columna $(h-1)b_j$, y aplicamos inducción. Si $h=0$, cada fila suma cero; por tanto, toda entrada es cero y la familia vacía da la descomposición requerida. Una entrada cero de $M$ no puede recibir una contribución positiva en una suma de matrices no negativas. Esto demuestra también la afirmación sobre los ceros.

**Lema A.2.** Supongamos que $x_{ii}=0$ y que los $x_{ij}\ge0$ son enteros con

$$x_{ij}+x_{ji}=h b_ib_j,\qquad \sum_j x_{ij}=h b_i^2.$$

Entonces $x$ es la suma de $h$ matrices enteras no negativas $y^{(a)}$ con diagonal cero, sumas por pares $b_ib_j$ y sumas por fila $b_i^2$.

*Demostración.* Construimos una matriz de asignación cuyas filas corresponden a pares no ordenados de colores $e=\{i,j\}$ y cuyas columnas corresponden a colores. En la fila $e$, ponemos $x_{ij}$ en la columna $i$, $x_{ji}$ en la columna $j$ y cero en las demás. Su suma por fila es $h b_ib_j$. Su suma en la columna $i$ es $h b_i^2$. Aplicamos el Lema A.1. Cada sumando sigue estando apoyado solo en los dos extremos de su fila, porque los ceros se conservan. Leemos su entrada en $(\{i,j\},i)$ como $y^{(a)}_{ij}$. Las sumas por fila de la matriz de asignación dan las sumas por pares de $y^{(a)}$; sus sumas por columna dan las sumas por fila de $y^{(a)}$. Sumar sobre $a$ recupera $x$.

Para aplicar este resultado a la sección 5.2, dividimos primero por tres las cuotas residuales no negativas $t-r$. La congruencia de (5.2) hace que el cociente sea entero. Sus sumas por pares y por filas tienen la forma del Lema A.2 con $h=O$. Así obtenemos todas las matrices $y^{(a)}$ usadas allí, sin ninguna hipótesis adicional de divisibilidad sobre los sumandos individuales.

## Apéndice B. Corrección en el grafo residual

Este apéndice demuestra los dos hechos usados en la sección 3: los errores pequeños en las cargas de las aristas se pueden corregir con pesos acotados, y borrar un empaquetamiento permitido disperso conserva la condición del retículo físico. La existencia de una solución real y la de una solución entera son afirmaciones distintas.

### B.1. Una inversa por la derecha con dominio explícito

Para un vector de aristas $r$, ponemos

$$\ell(r)=\sum_{e\text{ entre clases}}r_e-2\sum_{e\text{ interna}}r_e.$$

Cada triángulo permitido tiene una arista interna y dos entre clases, por lo que su vector de incidencia cumple $\ell=0$. Todas las normas que siguen son normas del máximo. Sea $A$ la aplicación de incidencia entre aristas y triángulos.

**Lema B.1.** Supongamos que cada clase tiene al menos $c_\ast\ge4$ puntos y que $n\le R c_\ast$, con $R\ge1$. Para tres clases existe una aplicación lineal $\Phi$ sobre $\ker\ell$ tal que $A\Phi r=r$ y $\|\Phi r\|\le400R^5\|r\|/n$. Para $k\ge3$ clases vale la misma conclusión con la constante $K_c=|\operatorname{Trip}(o)|400R^6(1+4R^2)$ en lugar de $400R^5$.

*Demostración para tres clases.* Sean $a,b,c$ sus tamaños y sea $D=\|r\|$. Primero cubrimos las aristas internas. Para cada clase $i$, elegimos otra clase $j$ y asignamos el peso $r_{uv}/c_j$ a cada triángulo $uvw$ con $u,v\in V_i$ y $w\in V_j$. La carga de su arista interna es exactamente $r_{uv}$. Cada peso tiene valor absoluto a lo sumo $D/c_\ast$. Una arista entre clases recibe contribuciones de, a lo sumo, las dos clases de sus extremos, con valor absoluto total a lo sumo $2RD$. El vector restante está soportado en las aristas entre clases, cumple $\ell=0$ y tiene norma a lo sumo $D'=(1+2R)D$.

Para una matriz de cargas $h$ entre las clases $i,j$, separamos la media, las desviaciones por fila y columna, y el resto:

$$h_{uw}=C+f(u)+g(w)+h^0_{uw}.$$

Aquí $C$ es la media de todas las entradas, $f$ es la media de la fila menos $C$, y $g$ es la media de la columna menos $C$. Por tanto, $f,g$ tienen suma cero y todas las sumas por fila y columna de $h^0$ son cero. Sus cotas absolutas son, respectivamente, $D',2D',2D',4D'$. Los pesos siguientes realizan los tres términos no constantes sin añadir carga a ninguna arista interna:

$$
\begin{aligned}
 h^0:&\quad \psi_{uv,w}=\frac{h^0_{uw}+h^0_{vw}}{c_i-2},\quad u,v\in V_i,\ w\in V_j;\\
 f:&\quad \psi_{wz,u}=\frac{f(u)}{c_j-1},\quad w,z\in V_j,\ u\in V_i;\\
 g:&\quad \psi_{uv,w}=\frac{g(w)}{c_i-1},\quad u,v\in V_i,\ w\in V_j.
\end{aligned}
\tag{B.1}
$$

Por ejemplo, sumar la primera expresión sobre $v\ne u$ da $h^0_{uw}$, pues la suma de esa columna de $h^0$ es cero. Sumar sobre $w$ da cero porque sus sumas por fila se anulan. Las otras dos comprobaciones usan las sumas nulas de $f$ y $g$. Como $c_\ast\ge4$, la corrección total sobre un triángulo tiene valor absoluto a lo sumo $24D'/c_\ast$.

Solo quedan tres cargas constantes entre clases, que denotamos por $C_{AB},C_{AC},C_{BC}$. Su compatibilidad es $abC_{AB}+acC_{AC}+bcC_{BC}=0$. Usamos los siguientes pesos constantes por tipo:

$$
\begin{gathered}
x_{AAB}=x_{AAC}=0,\qquad
x_{ABB}=\frac{C_{AB}}{b-1},\qquad x_{ACC}=\frac{C_{AC}}{c-1},\\
x_{BBC}=-\frac{a}{c}x_{ABB},\qquad
x_{BCC}=-\frac{a}{b}x_{ACC}.
\end{gathered}
\tag{B.2}
$$

Las cargas internas se anulan. Las cargas en $AB$ y $AC$ son las constantes requeridas, y la carga en $BC$ es $-aC_{AB}/c-aC_{AC}/b=C_{BC}$. Estos pesos tienen norma a lo sumo $2RD'/c_\ast$. Al sumar las tres etapas obtenemos

$$\|\Phi r\|\le[1+(24+2R)(1+2R)]D/c_\ast\le79R^3D/n\le400R^5D/n.$$

La clase sucesora de cada clase se elige una sola vez, de modo que la construcción es lineal en $r$.

Esta es una construcción explícita de la inversa, con la cota intermedia más ajustada que acabamos de obtener. La fuente formal usa un promedio finito para probar la cota $400R^5/n$ en el mismo dominio compatible. La prueba escrita es una demostración alternativa de la estimación que usamos aquí, no una transcripción de la construcción formal.

*Ensamblaje para más clases.* Sea $\operatorname{Trip}(o)$ la familia de todos los subconjuntos de tres colores que contienen un color central elegido $o$. Repartimos cada coordenada de arista por igual entre las restricciones que contienen los colores de sus extremos. Sean $G^0_\tau r$ los vectores obtenidos; su suma es $r$ y cada uno tiene norma a lo sumo $\|r\|$. No necesariamente cumplen la ecuación de balance por separado. Sea $z_0$ el vector de peso total uno distribuido uniformemente sobre las aristas internas de la clase central. Como $\ell(z_0)=-2$, ponemos

$$G_\tau r=G^0_\tau r+\tfrac12\ell(G^0_\tau r)z_0.$$

Cada $G_\tau r$ tiene balance cero y la suma sigue siendo $r$, porque $\ell(r)=0$. Las desigualdades $\|z_0\|\le4/c_\ast^2$ y $|\ell(G^0_\tau r)|\le2n^2\|r\|$ dan $\|G_\tau r\|\le(1+4R^2)\|r\|$. El orden de cada restricción es al menos $c_\ast$, por lo que sustituir ese orden por $n$ cuesta, a lo sumo, otro factor $R$. Aplicamos la inversa de tres clases a cada restricción y sumamos. Así se obtiene exactamente $K_c$.

### B.2. Borrar pares sin perder la positividad

**Lema B.2.** Sea $L$ el conjunto de pares ocupado por un empaquetamiento permitido, de grado máximo $\Delta$. Supongamos que el grafo completo tiene una semilla exacta $\mu_0$ con $1/(C_0n)\le\mu_0(T)\le C_0/n$, donde $C_0\ge1$. Si $8K_cC_0^2\Delta\le n$, el grafo residual tiene una semilla exacta entre $1/(2C_0n)$ y $2C_0/n$. Para toda función de prueba $0\le w\le1$, su masa ponderada difiere de la de $\mu_0$ en a lo sumo $(4K_c+1)C_0\Delta n$.

*Demostración.* Llamamos malo a un triángulo que contiene una arista de $L$, y bueno a cualquier otro. Sean $b$ y $g$ las restricciones a triángulos malos y buenos. Extendemos por cero en $L$ el indicador de las aristas residuales y ponemos $d_0=1_{E\setminus L}-Ag\mu_0$. El vector $d_0$ se anula en $L$. Su balance es cero, pues $L$ es unión de triángulos permitidos y cada columna de $A$ tiene balance cero. Una arista superviviente pertenece a lo sumo a $2\Delta$ triángulos malos: el tercer punto debe ser vecino en $L$ de uno de sus extremos. Por ello, $\|d_0\|\le2\Delta C_0/n$.

En el espacio de vectores de balance cero que se anulan en $L$, definimos $R_0=Ab\Phi$. Este operador conserva el espacio. En efecto, todos los triángulos que contienen una arista de $L$ son malos, de modo que allí $Ab\Phi x=A\Phi x=x=0$. Una arista superviviente tiene a lo sumo $2\Delta$ extensiones malas, por lo que $\|R_0x\|\le2\Delta K_c\|x\|/n\le\|x\|/2$. La serie geométrica convergente

$$x=\sum_{s\ge0}R_0^s d_0$$

satisface $(I-R_0)x=d_0$ y $\|x\|\le2\|d_0\|$. Sea $\psi=\Phi x$. Entonces $Ag\psi=d_0$ y $\|\psi\|\le4K_cC_0\Delta/n^2\le1/(2C_0n)$. Por tanto, $g(\mu_0+\psi)$ es la semilla positiva requerida. Cambian a lo sumo $n^3$ pesos de triángulos y se eliminan a lo sumo $n^2\Delta$ triángulos. Multiplicar estas cantidades por las cotas respectivas de $\psi$ y $\mu_0$ da $(4K_c+1)C_0\Delta n$. La misma estimación vale para toda función de prueba entre cero y uno. Esto demuestra (3.2).

### B.3. Un certificado entero con triángulos supervivientes

**Lema B.3.** Sea una partición que satisface (1.1), y sea $H$ el grafo completo después de borrar los pares de un empaquetamiento permitido. Supongamos que, en cada clase, todo conjunto de a lo sumo $k+4$ puntos tiene un vecino común en $H$ distinto de esos puntos. Entonces $1_{E(H)}$ es una combinación entera de triángulos permitidos de $H$.

Si el borrado tiene grado máximo $\Delta$, la condición de vecinos se deduce de $c_i>(k+4)(\Delta+1)$. También se cumple cuando cada clase contiene más de $k+4$ puntos adyacentes a todos los demás puntos.

*Demostración.* Trabajamos en el cociente del grupo abeliano libre sobre $E(H)$ por el subgrupo generado por sus triángulos permitidos. Escribimos $\chi(uv)$ para la imagen de una arista superviviente. Un triángulo permitido da la relación $\chi(uv)+\chi(uw)+\chi(vw)=0$. Probaremos que la suma de las imágenes de todas las aristas es cero.

Consideremos primero $x,x',x''$ de una misma clase, con sus tres aristas internas presentes, y dos puntos $w,w'$ exteriores a esa clase y adyacentes a los tres. Al restar las relaciones de los triángulos obtenemos $D(x)+D(x')=D(x)+D(x'')=D(x')+D(x'')=0$, donde $D(x)=\chi(xw)-\chi(xw')$. Por tanto, $D(x)=D(x')=D(x'')$ y $2D(x)=0$. La misma conclusión vale para cualesquiera dos puntos $x,x'$ adyacentes a $w,w'$, aunque falte $xx'$. Elegimos un vecino común $y$ en su clase y después puntos auxiliares que completen las ternas $x,y,z$ y $x',y,z'$, todos adyacentes a $w,w'$. Cada elección exige adyacencia a lo sumo a cuatro puntos prescritos. El cálculo anterior transfiere la igualdad a través de $y$.

Elegimos puntos base $o_i\in V_i$ adyacentes dos a dos, usando sucesivamente la condición de vecinos. Para $v\in V_i$, elegimos $w$ fuera de $V_i$, adyacente a $v,o_i$, y ponemos $\epsilon(v)=\chi(vw)-\chi(o_iw)$. El cálculo de diferencias anterior demuestra que esto no depende de $w$. Aplicándolo con los papeles de las dos clases intercambiados obtenemos $2\epsilon(v)=0$; además, $\epsilon(o_i)=0$. Así, cambiar un extremo dentro de su clase modifica la imagen de una arista en la diferencia de sus dos valores de $\epsilon$. El paso que evita una arista base ausente es el siguiente. Para una arista superviviente $uv$ con $u\in V_i$, $v\in V_j$, elegimos $z\in V_i$ adyacente a $u,o_i,v,o_j$ y distinto de ellos. Para justificar la primera identidad incluso si falta la arista $o_iv$, elegimos un punto auxiliar $w\in V_j$, distinto de $v,o_j$, adyacente a $u,z,o_i$. El cálculo anterior de diferencias, aplicado a los puntos exteriores $v,w$ y a los interiores $u,z$, da $\chi(uv)-\chi(zv)=\chi(uw)-\chi(zw)$. La definición de $\epsilon$ usando $w$ convierte el segundo miembro en $\epsilon(u)-\epsilon(z)$. Las otras dos identidades usan las aristas base presentes. Por tanto,

$$\chi(uv)-\chi(zv)=\epsilon(u)-\epsilon(z),\qquad
\chi(zv)-\chi(zo_j)=\epsilon(v),\qquad
\chi(zo_j)-\chi(o_io_j)=\epsilon(z).$$

Al sumarlas obtenemos la expresión buscada mediante la arista base, sin usar $o_iv$ ni $uo_j$. Si un extremo ya es un punto base, la identidad correspondiente es inmediata. La elección de $z$ exige cuatro adyacencias y la elección auxiliar de $w$ exige tres. Para excluir los puntos nombrados se prescriben a lo sumo $k+4$ puntos en cada elección, como permite la hipótesis del lema.

Sea $\beta_{ij}=\chi(o_io_j)$. Para una arista superviviente entre clases obtenemos $\chi(uv)=\beta_{ij}+\epsilon(u)+\epsilon(v)$. Para una arista interna superviviente $uv\subset V_i$, completarla con un punto de otra clase da $\chi(uv)=-2\beta_{ij}+\epsilon(u)+\epsilon(v)$. El cálculo de diferencias en $o_i$ muestra que $2\beta_{ij}$ no depende de $j$; la simetría lo convierte en un único elemento $\gamma$ para todos los pares de clases. Ponemos $\kappa_{ii}=-\gamma$ y $\kappa_{ij}=\beta_{ij}$ si $i\ne j$.

Definimos sobre *todos* los pares, incluidos los ausentes, el valor $f(uv)=\kappa_{ij}+\epsilon(u)+\epsilon(v)$. En los pares supervivientes coincide con $\chi(uv)$. Al sumar sobre todos los pares, la contribución de $\epsilon$ es $(n-1)\sum_v\epsilon(v)=0$, porque $n$ es impar. Como cada $c_ic_j$ es par, la contribución de las clases es

$$\left(\tfrac12\sum_{i<j}c_ic_j-\sum_i\binom{c_i}{2}\right)\gamma=0,$$

donde la última igualdad es (1.1). En cualquier triángulo permitido, sobrevivan o no sus pares, la suma de sus tres valores de $f$ es $-\gamma+2\kappa_{ij}+2(\epsilon(u)+\epsilon(v)+\epsilon(w))=0$. Los pares borrados se reparten en triángulos de ese tipo. Al restar su contribución nula de la suma sobre todos los pares queda $\sum_{E(H)}\chi=0$, como queríamos. Esta resta se hace en el cociente residual; no supone que sobreviva un certificado del grafo original.

### B.4. Las dos condiciones de vecinos

Para H3, una clase prescrita para el tercer punto contiene al menos $c_i-2(\Delta+1)$ vecinos comunes de dos raíces. Cada raíz puede excluirse a sí misma y sus vecinos ausentes excluyen a lo sumo otros $\Delta$ puntos.

Para H4, sean $uva$ y $uvb$ dos triángulos permitidos que comparten exactamente $uv$. Elegimos $p$ del color de $u$ y $q$ del color de $v$, distintos de las cuatro raíces y entre sí. Pedimos que estén presentes las siete aristas

$$uq,\ pv,\ pq,\ pa,\ pb,\ qa,\ qb$$

Su unión $J$ tiene dos completaciones: $J\cup\{ua,va\}$ se descompone como $\{uqa,pva,pqb\}$, mientras que $J\cup\{ub,vb\}$ se descompone como $\{uqb,pvb,pqa\}$. Cada triángulo tiene el tipo de uno de los triángulos originales. Elegir primero $p$ y luego $q$ deja al menos $(\delta n-4\Delta-5)^2$ posibilidades. El conjunto de aristas permite recuperar $p$ y $q$ como los únicos vecinos de $v$ y de $u$ en $J$, de modo que las elecciones dan bisagras distintas. Para $\Delta/n$ suficientemente pequeño y $n$ grande, hay al menos $\delta^2n^2/4$ bisagras con exactamente seis vértices. Esta es la potencia requerida $n^{6-4}$.

## Apéndice C. La construcción de conteo completa

Este apéndice construye la completación residual común usada en la sección 5. Las tablas latinas solo variarán después de elegir esa completación.

### C.1. Un patrón balanceado que cabe en cada perfil grande

**Lema C.1.** Para márgenes fijos de interior y de tamaño de clase, y cualquier precisión fija suficientemente pequeña, todos los perfiles de entrada suficientemente grandes se pueden aproximar mediante vectores enteros positivos normalizados $v$ que satisfacen $3\sum v_i^2=(\sum v_i)^2$. Basta una colección finita de esos vectores. Para tres colores se puede usar $v=(1,1,1)$.

*Demostración.* Un límite $p$ de los perfiles normalizados tiene coordenadas positivas, suma uno y cumple $3\sum p_i^2=1$. Las asignaciones de la sección 3 tienen límites subsecuenciales $a_{ij}$ separados de cero y de uno, con sumas por par iguales a uno y $\sum_jp_ja_{ij}=p_i$. Por tanto, todo subconjunto propio no vacío satisface

$$3\sum_{i\in S}p_i^2-p(S)^2=2\sum_{i\in S,j\notin S}p_ip_ja_{ij}>0.$$

Para $k\ge4$, sea $e$ el indicador de tres colores cualesquiera, pongamos $Q(z)=3\sum z_i^2-(\sum z_i)^2$ y sea $\sigma(z)=\sum_{i\notin\operatorname{supp}(e)}z_i$. Para un vector racional $z$ cercano a $p$, el vector racional

$$y=Q(z)e+6\sigma(z)z$$

satisface $Q(y)=0$. En efecto, $Q(e)=0$ y la forma polar en $(e,z)$ es $-3\sigma(z)$, por lo que los dos términos restantes se cancelan. En $z=p$, el vector es el múltiplo positivo $6\sigma(p)p$. Así, $y/\sum y_i$ aproxima a $p$, sigue siendo positivo y conserva los cortes estrictos. Eliminar denominadores da $v$. Los límites posibles forman un conjunto compacto con los márgenes fijos. Un número finito de entornos de aproximación lo cubre. Todos los perfiles de entrada suficientemente grandes están en su unión; de lo contrario, una subsucesión convergente exterior tendría un límite interior. Esto prueba la uniformidad. Para $k=3$, la identidad $\sum_i(3c_i-n)^2=6n$ da directamente $c_i/n\to1/3$.

Los cortes estrictos también proporcionan una asignación entera con sumas por par $v_iv_j$ y sumas por fila $v_i^2$: enviamos la capacidad $v_iv_j$ de cada par a sus dos extremos. La condición de corte es $\sum_{i\in S}v_i^2\ge\sum_{i<j\in S}v_iv_j$, que equivale a $Q(v|_S)\ge0$. La oferta total coincide con la demanda total. El criterio de cortes de Gale [5] da la factibilidad. Con capacidades enteras, el argumento de caminos aumentantes de Ford–Fulkerson [21] da un flujo entero y, por tanto, la asignación. Para tres colores basta la asignación cíclica sobre $(1,1,1)$.

Sea $g\ge15$ fijo y admisible, y pongamos $\rho=1/(2g)$. Elegimos la precisión $\xi<\rho\delta/4$. Para uno de los patrones de la colección finita, sean $M=\sum v_i$ y

$$\ell=\left\lfloor\frac{(1-\rho/2)n}{gM}\right\rfloor,\qquad b_i=\ell v_i,\qquad B=\ell M.$$

Para $n$ grande, colocamos $g$ grupos disjuntos con $b_i$ puntos del color $i$ en cada uno. La aproximación garantiza $c_i-gb_i\ge\rho\delta n/4$, de modo que todos los colores conservan suficientes puntos en la reserva. Además, $(1-\rho)n\le gB\le(1-\rho/2)n$ y $\ell\ge n/(4g\max M)$. Estas desigualdades justifican la colocación y la constante uniforme de la sección 5.3.

### C.2. Realización de una tabla agregada

**Lema C.2.** Todo arreglo entero no negativo $M_{ijs}$ con las tres familias de marginales $b_ib_j,b_ib_s,b_jb_s$ es la tabla agregada de un cuadrado latino. Si $y_{ij}+y_{ji}=b_ib_j$ y $\sum_jy_{ij}=b_i^2$, asignar a cada una de $M_{iij},M_{iji},M_{jii}$ el valor $y_{ij}$ y poner cero en las demás entradas da una tabla agregada cuyos conteos de bloques son $3y_{ij}$.

*Demostración.* Es la realización de Hilton [8]; la siguiente prueba por repartos incluye la conservación de los ceros. Para cada clase de filas $i$, aplicamos el Lema A.1 a su matriz sobre clases de columnas y símbolos, repartiéndola en $b_i$ matrices con sumas por fila $b_j$ y por columna $b_s$. Estas corresponden a las filas individuales. Ahora, para una clase de columnas $j$, formamos la matriz sobre filas individuales y clases de símbolos. Sus sumas por fila son $b_j$ y sus sumas por columna son $b_jb_s$. La repartimos en $b_j$ matrices con sumas por fila uno y por columna $b_s$. Cada casilla tiene ahora exactamente una clase de símbolo, y cada fila y columna individual tiene exactamente $b_s$ casillas de esa clase. Esas casillas forman un grafo bipartito $b_s$-regular. Contar sus aristas desde cualquier conjunto de filas prueba la condición de Hall y, por tanto, la existencia de un emparejamiento perfecto. Retiramos sucesivamente esos emparejamientos y asignamos los símbolos distintos. Así obtenemos un cuadrado latino sin cambiar los conteos por clase ni los ceros. Para la tabla agregada simétrica del enunciado, las marginales diagonales son $\sum_jy_{ij}=b_i^2$ y las demás son $y_{ij}+y_{ji}=b_ib_j$. Sumar las tres posiciones de la clase simple da $3y_{ij}$.

### C.3. Una semilla exacta en el grafo residual común

Sean $W_1,\ldots,W_g$ los grupos y $W_\ast$ la reserva de vértices. Borramos todas las aristas entre grupos distintos. El grafo restante $H$ es la unión de los grafos completos sobre $W_a\cup W_\ast$. Escribimos $x=B/n$ e $y=|W_\ast|/n=1-gx$; para $n$ grande, $0<y\le x$. Los pesos siguientes distinguen solo cuántos puntos del triángulo están en la reserva:

$$w_2=w_3=\frac1{g(x+y)},\qquad w_1=\frac{1-yw_2}{x},\qquad w_0=\frac{1-yw_1}{x}.\tag{C.1}$$

Satisfacen $xw_0+yw_1=xw_1+yw_2=1$ y $xw_2+yw_3=1/g$. Además, $w_1-w_2=(1-1/g)/x\ge0$ y $w_0-w_2=(x-y)(w_1-w_2)/x\ge0$. Por tanto, $w_2\le w_j\le1/x$.

En el grafo completo sobre $W_a\cup W_\ast$, multiplicamos el peso original por tipo (3.1) por $w_s$ cuando el triángulo tiene $s$ puntos de la reserva. La carga local deseada es uno en las aristas que tocan $W_a$ y $1/g$ en las aristas de la reserva. Si las proporciones de colores en ambas partes fueran exactamente las del conjunto completo, (C.1) daría esas cargas, salvo por la exclusión de las dos raíces. La diferencia entre el número de puntos de un color en el grupo y $xc_i$ es a lo sumo $xn\xi$, y la diferencia correspondiente en la reserva respecto de $yc_i$ es a lo sumo $gxn\xi$. Como el peso original por tipo es a lo sumo $2/(\delta n)$, sumar sobre los colores y excluir las raíces acota el error de carga local por

$$\epsilon\le\frac{2k(g+1)\xi}{\delta}+\frac{8k}{\delta nx}.\tag{C.2}$$

La carga objetivo tiene balance exacto, no aproximado. Para comprobarlo, sean $b=(b_i)$, $r=(c_i-gb_i)$ y $d(z)=3\sum z_i^2-(\sum z_i)^2-2\sum z_i$. Al desarrollar obtenemos

$$g\,d(b+r)-(g-1)d(r)=d(gb+r)-g(g-1)Q(b)=0.$$

La última igualdad usa (1.1) y $Q(b)=0$. Expresa precisamente que el objetivo local, con carga $1/g$ en las aristas de la reserva, tiene $\ell=0$. La incidencia de la semilla preliminar también tiene balance cero. Por tanto, el Lema B.1 corrige su error. El orden local es $(x+y)n$ y cada clase local ocupa una fracción positiva fija de él. Los pesos preliminares son al menos $(\eta/g)/((x+y)n)$ y a lo sumo $(4/\delta)/((x+y)n)$ para cierto $\eta$ positivo fijo que proviene del margen interior. Elegimos primero $\xi$ suficientemente pequeño y después $n$ suficientemente grande para que la corrección de la inversa sea a lo sumo la mitad de esa cota inferior. La semilla local corregida es positiva en todos los triángulos permitidos. Sumar las $g$ semillas da carga uno en cada arista de $H$: una arista de grupo aparece en una pieza y una arista de la reserva aparece en las $g$ piezas, con carga $1/g$ en cada una.

Para el certificado del retículo, usamos la asignación del Lema C.1 y la tabla agregada del Lema C.2 para colocar un empaquetamiento latino permitido sobre cada bloque del sistema de índices. Esto cubre exactamente las aristas borradas entre grupos. La reserva proporciona los vecinos comunes exigidos por el Lema B.3. También proporciona todos los puntos libres de la construcción de bisagras del Apéndice B.4. Así, H2–H4 se cumplen en $H$, con constantes que solo dependen de los parámetros fijos.

Antes de aplicar T borraremos una cantidad acotada de conjuntos de pares ocupados por intercambios. La semilla sobrevive de la siguiente manera. Una inversa acotada sobre $H$ se obtiene repartiendo los vectores de aristas entre sus $g$ piezas completas y asignando a cada arista de la reserva la fracción $1/g$. Corregimos el balance de cada parte con el vector uniforme sobre las aristas internas de un color de la reserva, tal como en el Lema B.1. Cada pieza tiene clases de tamaño lineal, de modo que la inversa resultante tiene norma a lo sumo $K_H/n$ para un $K_H$ fijo. El Lema B.2 se aplica ahora con esa inversa: su prueba solo usa la ecuación de balance, una inversa acotada y la cota $2\Delta$ sobre las extensiones malas de una arista superviviente. Un borrado acotado tiene $\Delta=O(1)$, así que la positividad vale para $n$ grande. La reserva restante también prueba H2–H4. Por tanto, T completa el grafo después de separar esos intercambios.

### C.4. Corregir los residuos antes de contar

Reservamos dos copias del intercambio de nueve puntos por cada una de las $J$ coordenadas independientes, todas disjuntas en vértices y contenidas en $W_\ast$. Completamos el resto mediante C.3, añadimos todas las mitades altas y llamamos $r^0$ al vector de tipos obtenido. Para la coordenada $i$, cambiamos el número $z_i\in\{0,1,2\}$ de copias que sea congruente con $r^0_i-t_i$ módulo tres. Cada cambio disminuye esa coordenada en uno y no modifica las otras. La completación resultante tiene $r_i\equiv t_i\pmod3$ en las coordenadas independientes.

El grafo omitido entre grupos tiene $6O b_ib_j$ aristas entre los colores $i,j$ y $3O b_i^2$ aristas internas del color $i$. Por tanto, $t-r$ tiene sumas por par $3O b_ib_j$ y sumas por fila $3O b_i^2$. Reducir estas ecuaciones módulo tres y usar las coordenadas de ciclos de la sección 2.2 da la divisibilidad de todas las entradas. Además,

$$|E(H)|\le gB^2/2+|W_\ast|n\le n^2/(2g)+\rho n^2=n^2/g.$$

Cada bloque residual usa tres de esas aristas, de modo que $r_{ij}\le n^2/(3g)\le(2/g)n^2$. Elegir $2/g\le\zeta$ prueba $t-r\ge0$. El Lema A.2 reparte entonces $(t-r)/3$ y el Lema C.2 realiza cada sumando. Esto completa todas las construcciones usadas en la sección 5.

## Apéndice D. El paso aritmético a perfiles enteros

### D.1. De los cortes estrictos a una asignación positiva

**Lema D.1.** Sea $p$ un vector con coordenadas positivas, suma uno, suma de cuadrados $1/3$ y los cortes estrictos (6.1). Todo perfil entero normalizado suficientemente cercano que satisfaga (1.1), de orden suficientemente grande, tiene una asignación $a_{ij}$ separada de cero y de uno, con $a_{ij}+a_{ji}=1$ y $\sum_{j\ne i}c_ja_{ij}=c_i-1$.

*Demostración.* Elegimos $\delta_0,\sigma>0$ de modo que todo perfil cercano tenga $c_i\ge\delta_0n$ y que cada corte propio no vacío cumpla $3\sum_{i\in S}c_i^2-c(S)^2\ge\sigma n^2$. Elegimos un $\eta_{\rm flow}>0$ fijo pequeño y ponemos $B_0=\lceil\eta_{\rm flow} n^2\rceil$. Buscamos asignaciones enteras dirigidas $x_{ij}$ con sumas por par $c_ic_j$, sumas por fila $c_i(c_i-1)$ y $x_{ij}\ge B_0$. Después de reservar $B_0$ en cada dirección, el par $ij$ tiene capacidad $e_{ij}=c_ic_j-2B_0$ y el color $i$ tiene demanda $d_i=c_i(c_i-1)-(k-1)B_0$.

Enviamos la capacidad de cada par a sus dos colores extremos. La capacidad total coincide con la demanda total por (1.1). El criterio de factibilidad de Gale [5], junto con la integralidad de Ford–Fulkerson [21], pide que la demanda de cada subconjunto sea al menos la capacidad atrapada en su interior. La diferencia es

$$\sum_{i\in S}d_i-\sum_{i<j\in S}e_{ij}=\tfrac12\bigl(3\sum_{i\in S}c_i^2-c(S)^2-2c(S)\bigr)-|S|(k-|S|)B_0.\tag{D.1}$$

Elegimos $\eta_{\rm flow}\le\min\{\delta_0^2/8,\sigma/(16k^2)\}$. Para $n$ grande, las capacidades son no negativas y (D.1) es positiva en cada subconjunto propio no vacío. Para el conjunto vacío y el total vale cero. Existe, por tanto, un flujo entero. Restituimos la cantidad reservada y ponemos $a_{ij}=x_{ij}/(c_ic_j)$. Como ambas direcciones reciben al menos $B_0$, estas razones pertenecen a $[\eta_{\rm flow},1-\eta_{\rm flow}]$. Dividir la ecuación de fila por $c_i$ da la ecuación requerida de la semilla.

### D.2. Todos los radios, incluidos los factores cuadrados

Usamos dos teoremas analíticos externos en las siguientes formas para casquetes fijos. Primero, el teorema de Duke [17] afirma que, para todo vector unitario $u\in\mathbb R^3$ y toda precisión positiva, cada entero libre de cuadrados $d\equiv3\pmod8$ suficientemente grande tiene un punto entero de norma al cuadrado $d$ que aproxima a $u$ con esa precisión después de dividirlo por $\sqrt d$. El contrato formal preciso está registrado en [15]. Segundo, el teorema [16] afirma que, para todo cuaternión unitario $q\in\mathbb R^4$ y toda precisión positiva, cada entero impar $s$ suficientemente grande tiene un cuaternión entero $\beta$ con $\sum\beta_i^2=s$ tal que $\beta/\sqrt s$ aproxima a $q$ con esa precisión. La distribución de puntos reticulares en esferas y elipsoides tiene una literatura clásica, que incluye a Pommerenke [22]. El enunciado para radios impares que usamos es el demostrado en [16], mediante el método del círculo y la fórmula de Jacobi; la referencia histórica no lo sustituye.

Aunque sus pruebas analíticas quedan fuera de este paper, el resultado final en Lean sigue siendo incondicional, porque el árbol de fuentes seleccionado importa pruebas formales de ambos resultados en vez de dejarlos como hipótesis del teorema. En particular, el desarrollo para enteros libres de cuadrados combina cotas de Weyl por grado con una cota inferior de representaciones que usa el teorema de Siegel. El desarrollo para cuatro cuadrados combina una estimación en casquetes fijos con la fórmula de Jacobi. El companion adjunto identifica esos módulos. Estos módulos se compilaron en la reconstrucción limpia descrita en la verificación formal. Que sus enunciados formales expresen fielmente los teoremas analíticos citados sigue requiriendo una lectura especializada; una importación compilada y un informe de axiomas no la sustituyen.

**Lema D.2.** Estos resultados y el teorema de tres cuadrados de Gauss–Legendre implican (6.3) para todo $M\equiv3\pmod8$ suficientemente grande.

*Demostración.* Escribimos $M=ds^2$ con $d$ libre de cuadrados. Entonces $s$ es impar y $d\equiv3\pmod8$. Para todo $d$ que supere el umbral del primer resultado, multiplicamos la representación de $d$ en la región esférica por $s$.

Solo hay un número finito de valores menores de $d$. Para cada uno, Gauss–Legendre da un vector entero $v$ de norma al cuadrado $d$. Sea $y=v/\sqrt d$. Elegimos un cuaternión unitario cuya rotación lleve $y$ a $u$. Si $y\ne-u$, basta normalizar el cuaternión $(1+y\cdot u,y\times u)$; si $y=-u$, usamos media vuelta alrededor de un eje perpendicular a $y$. La conjugación por cuaterniones depende continuamente del cuaternión, de modo que el segundo resultado da, para todo impar $s$ suficientemente grande, un $\beta$ entero de norma al cuadrado $s$ cuya rotación normalizada lleva $y$ tan cerca de $u$ como se necesite. Interpretamos $v$ como cuaternión puramente imaginario y ponemos $x=\beta v\overline\beta$. Sus coordenadas son enteras, su parte real es cero y la multiplicatividad de la norma da $|x|^2=d s^2=M$. Su dirección normalizada es la requerida. Tomamos el máximo $S$ de los umbrales de rotación para los finitísimos valores pequeños de $d$. Si $D$ es el umbral del primer resultado, $M>D(S+1)^2$ garantiza $s>S$ cuando $d<D$. Así obtenemos un solo umbral para todos los $M$, lo que demuestra el lema.

### D.3. La elección de signo en las cuatro coordenadas restantes

Para el perfil de la sección 6.1, sea $q=(p_0,p_1,p_2,p_3)$. Cumple $q_0+q_2=q_1+q_3$. Las coordenadas de Hadamard de $q$ son, por tanto,

$$u_0=2(q_0-q_3),\qquad u_1=0,\qquad u_2=2(q_3-q_2).$$

Redondeamos las otras coordenadas a $c_i=2\lfloor np_i/2\rfloor$. Cada error de redondeo está entre $-2$ y cero. Con $w,S_4,M$ como en la sección 6.2, sea $\nu=u_0^2+u_2^2>0$. Al desarrollar las sumas obtenemos $w=n\sum_{i<4}q_i+O_k(1)$ y $M=\nu n^2+O_k(n)$. Así, $\sqrt M/n\to\sqrt \nu$. Aplicamos el Lema D.2 en la dirección $(u_0,0,u_2)/\sqrt \nu$ con una precisión fija suficientemente pequeña. Entonces $(a,b,c)/n$ está tan cerca de $(u_0,0,u_2)$ como se requiera.

Para $n$ admisible, el entero $n(n+2)/3$ es $1$ módulo cuatro. La cola redondeada tiene entradas pares, de modo que $S_4\equiv1\pmod4$ y $w$ es impar. Por tanto, $M=4S_4-w^2\equiv3\pmod8$, y $a,b,c$ son todos impares. Si hace falta, sustituimos solo $b$ por $-b$ para que $w+a+b+c$ sea divisible por cuatro. Esto cambia la suma en dos módulo cuatro y conserva la aproximación, porque la coordenada objetivo de $b$ es cero. Los otros tres numeradores de (6.2) difieren en dos veces la suma de dos impares, así que también son divisibles por cuatro. La fórmula (6.2) proporciona ahora enteros cercanos a las proporciones positivas requeridas. Sus identidades de suma y suma de cuadrados se comprobaron en la sección 6.2. Como la suma de sus cuadrados es $1$ módulo cuatro, exactamente uno de estos cuatro enteros es impar. Esto prueba todas las condiciones de paridad, y el Lema D.1 proporciona la semilla.

### D.4. El caso de cuatro colores da márgenes explícitos

Sea $n\ge1000$ admisible y tomemos la representación de la sección 6.3, con $a\ge0$ y $7|b|,7|c|\le a$. Definimos

$$f=(a+b+c,\ a-b-c,\ -a+b-c,\ -a-b+c).$$

Sus entradas son impares y congruentes entre sí módulo cuatro. Elegimos $s\in\{-1,1\}$ de modo que $n+sf_0$ sea divisible por cuatro, y ponemos $c_i=(n+sf_i)/4$. Son enteros y suman $n$. Además, $\sum f_i^2=4(a^2+b^2+c^2)$, de donde $3\sum c_i^2=n^2+2n$. El argumento de congruencias de D.3 vuelve a dar exactamente una clase impar.

De $3a^2\le n(n+8)$ y $n\ge1000$, elevar al cuadrado las cotas positivas permite comprobar $12a\le7n$ y $2400a\le1393n$. Por tanto,

$$|f_i|\le9a/7\le3n/4,\qquad c_i\ge n/16,\qquad |c_i-c_j|\le4a/7\le199n/600.$$

Ponemos $a_{ij}=1/2+3(c_i-c_j)/(2n)$. Sus valores están en $[1/400,1-1/400]$ y sus sumas por par son uno. Finalmente,

$$\sum_{j\ne i}c_ja_{ij}=\frac{n-c_i}{2}+\frac{3}{2n}\left(c_in-\sum_jc_j^2\right)=c_i-1.$$

Así, (3.1) da una semilla exacta y difusa con márgenes fijos, y el Apéndice B da H2–H4 en el grafo completo. Aplicar T demuestra el caso de cuatro colores sin ninguna hipótesis adicional sobre el perfil.

## Apéndice E. Los teoremas de absorción utilizados

Este apéndice reproduce T y T+ de [4, §§1–2]. Precisa todos sus datos de entrada; sus pruebas permanecen en [4]. La notación de este apéndice es local. En particular, $I$ es un conjunto de etiquetas y $q$ es un exponente para el número de pruebas.

Sea $G$ un grafo simple finito sobre $V$, con $n=|V|$, una asignación de etiquetas $\lambda:V\to I$ y un conjunto $\mathcal F$ de multiconjuntos de etiquetas. No se necesita suponer que $I$ sea finito. Sea $\mathcal T$ su familia de triángulos permitidos: los conjuntos de tres vértices cuyos tres pares son aristas y cuyo multiconjunto de etiquetas pertenece a $\mathcal F$. Una descomposición de un conjunto de aristas es una familia de triángulos permitidos cuyos conjuntos de aristas son disjuntos dos a dos y cuya unión es ese conjunto de aristas.

Sean $\alpha>0$, $C\ge1$ y un entero $h\ge6$. Las cuatro condiciones son las siguientes.

**H1 (semilla exacta y difusa).** Existe $\mu:\mathcal T\to\mathbb R$ tal que

$$\frac1{Cn}\le\mu(Q)\le\frac Cn\quad(Q\in\mathcal T),\qquad
\sum_{Q\in\mathcal T:\ e\in E(Q)}\mu(Q)=1\quad(e\in E(G)).$$

La cota inferior se aplica a cada triángulo permitido y la ecuación de carga a cada arista presente.

**H2 (retículo físico).** En las coordenadas enteras de pares,

$$\mathbf1_{E(G)}\in\operatorname{span}_{\mathbb Z}
\{\mathbf1_{E(Q)}:Q\in\mathcal T\}.$$

Los coeficientes pueden ser negativos. Solo se pueden usar triángulos presentes en el grafo.

**H3 (vecinos comunes tipados).** Para todo par de vértices distintos $u,v\in V$ y toda etiqueta $\ell\in I$ con $\{\lambda(u),\lambda(v),\ell\}\in\mathcal F$ como multiconjunto,

$$|\{w\in V:uw,vw\in E(G),\ \lambda(w)=\ell\}|\ge\alpha n.$$

No se supone que $uv$ sea una arista.

**H4 (bisagras físicas).** Sean $T_a=\{u,v,a\}$ y $T_b=\{u,v,b\}$ dos triángulos permitidos cualesquiera que comparten exactamente la arista $uv$. Una bisagra es un conjunto de aristas $J\subseteq E(G)$ disjunto de $E(T_a)\cup E(T_b)$ tal que tanto $J\cup\{ua,va\}$ como $J\cup\{ub,vb\}$ admiten descomposiciones en triángulos permitidos. Su orden es el número de vértices incidentes con $J$. Para cada uno de estos pares de triángulos raíz existe un entero $i$, $6\le i\le h$, para el cual al menos $\alpha n^{i-4}$ bisagras distintas tienen orden exactamente $i$. Las cuatro raíces están fijadas; las bisagras se cuentan como conjuntos de aristas, no como enumeraciones de sus vértices.

**Teorema T ([4]).** Fijemos $I,\mathcal F,\alpha,C,h$ con $\alpha>0$, $C\geq1$ y $h\geq6$. Existe un entero $n_0$ tal que todo grafo etiquetado G de orden $n\geq n_0$ que satisface H1–H4 admite una descomposición en triángulos permitidos.

Para el siguiente enunciado, definimos el objetivo fraccionario de una función sobre triángulos por

$$M_\mu(w)=\sum_{Q\in\mathcal T}\mu(Q)w(Q).$$

**Teorema T+ (versión de estadísticas de triángulos, [4]).** Fijemos $I,\mathcal F,\alpha,C,h$ como en el Teorema T, junto con $\eta>0$ y un entero $q\geq0$. Existe un entero $n_0$ tal que lo siguiente vale para todo grafo etiquetado G de orden $n\geq n_0$ y toda semilla especificada $\mu$ que satisface H1, siempre que se cumplan H2–H4. Para toda familia finita $(w_j)_{j\in\mathcal J}$ con

$$|\mathcal J|\leq n^q,\qquad |w_j(Q)|\leq1\quad(j\in\mathcal J,\ Q\in\mathcal T),$$

existe una misma descomposición en triángulos permitidos $\mathcal D$ tal que

$$\left|\sum_{Q\in\mathcal D}w_j(Q)-M_\mu(w_j)\right|\leq\eta n^2
\quad(j\in\mathcal J).$$

El umbral se elige antes del grafo, de la semilla especificada y de toda la familia de pruebas. Una misma descomposición satisface todas las desigualdades. En la sección 4 usamos como pruebas los indicadores de los tipos independientes; como su número solo depende de $k$, podemos tomar $q=1$ y aumentar el umbral de orden. La tolerancia se elige antes de aplicar el teorema. Esta es la conclusión de `main_theorem_T_with_triangle_monitors`, la declaración importada en este paper. El Teorema 1.3 usa la prueba por sustitución latina de la sección 7.


## Verificación formal

La selección de fuentes adjunta expone nuestros cuatro resultados principales mediante el módulo común `CDRIII`. Partiendo sin objetos compilados del proyecto, los 1305 módulos seleccionados de dependencias ajenas a Mathlib y el módulo común compilaron en una reconstrucción aislada. Solo se reutilizó la caché externa de Mathlib y sus dependencias con las revisiones fijadas; no se recompiló Mathlib desde sus fuentes.

Las cuatro consultas de axiomas de los teoremas finales muestran solo `propext`, `Classical.choice` y `Quot.sound`. Los hashes de las fuentes coinciden antes y después de la compilación, y la auditoría terminada vincula los objetos compilados con las fuentes seleccionadas y la configuración final. No se cambió ninguna prueba Lean ni ninguna hipótesis matemática. El companion adjunto registra el SHA-256 del archivo, las declaraciones exactas, los comandos y la evidencia de verificación.

El companion documenta la formalización y no sustituye las demostraciones del paper, cuyos argumentos técnicos se desarrollan en los Apéndices A–D. Los teoremas externos citados se invocan con sus hipótesis declaradas, sin reproducir sus demostraciones.

## Agradecimientos

El autor agradece profundamente a su esposa María Paz y a sus hijos Lucas, Juan Cristóbal, Francisca, Raimundo y Benjamín su amor, paciencia y apoyo.

## Uso de inteligencia artificial y herramientas computacionales

Claude, de Anthropic, y ChatGPT/Codex, de OpenAI, se utilizaron para explorar y comprobar argumentos y para preparar el manuscrito.

Certo [13] se utilizó para explorar casos finitos, comprobar identidades y evaluar construcciones candidatas. Estos cálculos orientaron el desarrollo de los argumentos; las comprobaciones finitas no se trataron como pruebas de enunciados universales.

El autor es responsable de los argumentos, las citas, el código y la exposición. Ningún sistema de IA figura como autor.

## Referencias

1. C. J. Colbourn, J. H. Dinitz y A. Rosa. Bicoloring Steiner triple systems. *Electronic Journal of Combinatorics* 6 (1999), R25. <https://doi.org/10.37236/1457>.
2. J. P. Traverso Gianini. The exact block-type spectrum in the Colbourn–Dinitz–Rosa problem. Paper I, 2026. <https://doi.org/10.5281/zenodo.23987251>.
3. J. P. Traverso Gianini. A proof of the Colbourn–Dinitz–Rosa conjecture. Paper II, 2026. <https://doi.org/10.5281/zenodo.23987256>.
4. J. P. Traverso Gianini. Triangle decompositions III: Physical typed absorption and prescribed statistics. 2026. <https://doi.org/10.5281/zenodo.23867836>.
5. D. Gale. A theorem on flows in networks. *Pacific Journal of Mathematics* 7 (1957), 1073–1082. <https://msp.org/pjm/1957/7-2/pjm-v7-n2-p04-s.pdf>.
6. N. Linial y Z. Luria. An upper bound on the number of Steiner triple systems. *Random Structures & Algorithms* 43 (2013), 399–406. <https://doi.org/10.1002/rsa.20487>; preprint de los autores <https://arxiv.org/abs/1108.5042>.
7. W. Duke y R. Schulze-Pillot. Representation of integers by positive ternary quadratic forms and equidistribution of lattice points on ellipsoids. *Inventiones Mathematicae* 99 (1990), 49–57. <https://www.math.ucla.edu/~wdduke/preprints/lattice2.pdf>.
8. A. J. W. Hilton. Outlines of Latin squares. En *Combinatorial Design Theory*, North-Holland Mathematics Studies 149 (1987), 225–241. <https://www.sciencedirect.com/science/chapter/bookseries/pii/S0304020808728895>.
9. G. P. Egorychev. The solution of van der Waerden's problem for permanents. *Advances in Mathematics* 42 (1981), 299–305. <https://doi.org/10.1016/0001-8708(81)90044-X>.
10. D. I. Falikman. Proof of the van der Waerden conjecture regarding the permanent of a doubly stochastic matrix. *Mathematical Notes* 29 (1981), 475–479. <https://doi.org/10.1007/BF01139954>.
11. R. M. Wilson. Nonisomorphic Steiner triple systems. *Mathematische Zeitschrift* 135 (1974), 303–313. <https://doi.org/10.1007/BF01215371>.
12. P. Keevash. Counting designs. *Journal of the European Mathematical Society* 20 (2018), 903–927. <https://doi.org/10.4171/JEMS/779>.
13. J. P. Traverso Gianini. Certo. Software. <https://github.com/jtraverso/certo-math>.
14. P. Keevash. Coloured and directed designs. En *Building Bridges II*, Bolyai Society Mathematical Studies 28 (2020), 279–315. <https://arxiv.org/abs/1807.05770>.
15. J. P. Traverso Gianini. Formalization of Duke–Schulze-Pillot bounds and squarefree three squares in fixed caps. Palomar, versión 2. <https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-07-000007&version=2>.
16. J. P. Traverso Gianini. Four squares in caps, and Jacobi’s four-square theorem for odd integers. Paquete de teoremas formales. <https://github.com/jtraverso/four-squares-in-caps>; <https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-08-000002&version=1>.
17. W. Duke. Hyperbolic distribution problems and half-integral weight Maass forms. *Inventiones Mathematicae* 92 (1988), 73–90. <https://doi.org/10.1007/BF01393993>.
18. D. R. Heath-Brown. A new form of the circle method, and its application to quadratic forms. *Journal für die reine und angewandte Mathematik* 481 (1996), 149–206. <https://doi.org/10.1515/crll.1996.481.149>.
19. M. J. Grannell, T. S. Griggs and C. A. Whitehead. The resolution of the anti-Pasch conjecture. *Journal of Combinatorial Designs* 8 (2000), 300–309. <https://doi.org/10.1002/1520-6610(2000)8:4%3C300::AID-JCD7%3E3.0.CO;2-R>.
20. M. J. Grannell and A. D. S. Lovegrove. Maximizing the number of Pasch configurations in a Steiner triple system. *Bulletin of the Institute of Combinatorics and its Applications* 69 (2013), 25–35. <https://grannell.net/Papers/maxpasch.pdf>.
21. L. R. Ford, Jr. and D. R. Fulkerson. Maximal flow through a network. *Canadian Journal of Mathematics* 8 (1956), 399–404. <https://doi.org/10.4153/CJM-1956-045-5>.
22. Ch. Pommerenke. Über die Gleichverteilung von Gitterpunkten auf m-dimensionalen Ellipsoiden. *Acta Arithmetica* 5 (1959), 227–257. <https://doi.org/10.4064/aa-5-2-227-257>.


### Material suplementario

**[S1]** Companion de formalización y archivo de fuentes Lean, depositados con este preprint bajo el DOI **10.5281/zenodo.24201563**. La ubicación oficial del paquete es `preprints/PAPER_III` en <https://github.com/jtraverso/cdr-steiner-preprints>. El companion se ofrece en inglés y español junto a los manuscritos.
