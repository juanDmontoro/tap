# Hallazgos en GeostatsGuy/PythonNumericalDemos para los simuladores del mapa TAP

**Repositorio analizado:** clon local `geo/PythonNumericalDemos` (commit `86190bb`, 3-mar-2026). Licencia MIT, © 2018 Michael Pyrcz: se puede reutilizar y adaptar si se conserva el aviso de copyright y de licencia.
**Método:** he leído el JSON de cada cuaderno candidato (celdas markdown y celdas de código con widgets, datos y modelos). **No he ejecutado ningún cuaderno**, así que lo que digo de los gráficos sale del código (`plt.subplot`, títulos, ejes), no de verlos renderizados. Las cifras de sliders (min/max/valor) están copiadas del código.

**Patrón común de los cuadernos interactivos:** `ipywidgets.interactive_output(f, {...})` con sliders `continuous_update=False`. Cada cambio vuelve a generar el conjunto de datos con una semilla fija (`seed = 13014` o `73073`) y redibuja de 1 a 4 paneles de matplotlib. Para pasarlo a JS bastan un PRNG con semilla, unas cuantas funciones numéricas y canvas/SVG.

---

## 0. Resumen: los más prometedores

| # | Cuaderno | Nodo(s) | Duplica | Viabilidad JS | Esfuerzo |
|---|---|---|---|---|---|
| 1 | Interactive_Linear_Solutions | ridge, lasso, (enet), d_train | No | Alta | 1–1,5 días |
| 2 | Interactive_Ridge_Regresion | ridge, d_hiper, d_sesgo, d_part | No | Alta | 1 día |
| 3 | Interactive_LASSO_Regression | lasso, d_hiper, d_prep | No | Alta/Media | 1–1,5 días |
| 4 | Interactive_DecisionMaking | d_deseq, d_mreg (pérdida → estimación óptima) | No | Alta | 0,5–1 día |
| 5 | Interactive_Norms | d_mreg (MAE vs MSE), mco | No | Alta | 0,5–1 día |
| 6 | Interactive_Decision_Tree | arbol_reg, d_hiper | No | Media | 2 días |
| 7 | SubsurfaceDataAnalytics_EnsembleTrees (estático) | bagging, rf, d_cv (OOB) | No | Alta en 1D, Media en 2D | 1,5–2 días |
| 8 | Interactive_Optimization + SubsurfaceDataAnalytics_ANN | d_train, mlp | No | Alta | 1 día cada uno |
| 9 | Interactive_Overfit | poli, d_sesgo, d_part | **Parcial** (slide «Elige el grado») | Alta | 0,5 días |
| 10 | Interactive_Shapley_Values | d_interp | No | Baja tal cual; Media con modelo propio | 2 días |
| 11 | Interactive_Bayesian_Updating | d_mclas, d_deseq (tasa base) | No | Alta | 0,5 días |
| 12 | Interactive_Bootstrap / Interactive_Confidence_Interval | bagging, d_cv (error típico) | No | Alta | 0,5–1 día |

---

## 1. Complejidad, regularización y sesgo-varianza

### 1.1 `Interactive_Overfit.ipynb`: «Machine Learning Overfit/Generalization Demo» (Pyrcz y J. E. McCarthy II)
- **Qué enseña:** ajusta polinomios de grado 1 a 12 a datos de una parábola con ruido. Repite la partición train/test 20 veces (`nreal = 20`) y dibuja el MSE de entrenamiento y de test medios contra el grado, con bandas P10–P90. Así se ve que el error de test se dispara cuando el modelo es demasiado complejo y cómo depende del tamaño de muestra y del ruido.
- **Interactividad (comprobada):** `n` (IntSlider 15–80, valor 30, número de datos), `Test %` (0,05–0,95, proporción de test en `train_test_split`), `Noise StDev` (0–50, desviación típica del ruido gaussiano), `Model Order` (1–12, grado del ejemplo mostrado). Tres paneles: (1) curva del polinomio con los puntos de train en rojo y de test en azul; (2) histogramas del error de train y de test; (3) MSE de train/test contra el grado (escala log) con bandas y una línea vertical en el grado elegido.
- **Datos:** sintéticos, `X ~ U(0,20)`, `y = X² + 50 + N(0, σ)`. Las etiquetas de los ejes dicen «Porosity / Permeability», pero los datos no tienen nada que ver con el subsuelo.
- **Nodos:** `poli`, `d_sesgo`, `d_part`.
- **Duplicación:** **parcial** con la slide «Elige el grado» del tema 1. Lo que aporta de nuevo: la curva de error contra complejidad con la dispersión entre particiones, el slider del % de test y el efecto de `n`.
- **Viabilidad JS:** **Alta**. Un polinomio por mínimos cuadrados (ecuaciones normales con x reescalado a [-1,1] para no tener problemas numéricos en grado 12), 12 grados × 20 particiones: cálculo instantáneo. Unas 0,5 jornadas.
- **Adaptación:** **ampliar** la slide existente en vez de crear otra. «Simular» en `poli` o `d_sesgo` mostraría *ventas semanales en función de la inversión en publicidad*, con sliders n, ruido, % test y grado, y el panel de «MSE test vs grado con banda». El botón de `d_part` podría reutilizar el mismo simulador con el % de test destacado.

### 1.2 `overfit_demonstration.ipynb`: ejercicio de sobreajuste de tendencias
- **Qué enseña:** 8 puntos de entrenamiento escritos a mano y 4 de test. Ajusta polinomios de grado 1, 3, 5 y 7 (el de grado 7 interpola los 8 puntos y el residuo es 0), compara los residuos de train con los de test y dibuja con `seaborn.regplot` los intervalos de confianza, que se abren mucho al subir el grado. Explica con texto el sesgo y la varianza.
- **Interactividad:** **no interactivo**.
- **Datos:** arrays escritos a mano (z, permeabilidad).
- **Nodos:** `poli`, `d_sesgo`.
- **Duplicación:** sí, con «Elige el grado» y con 1.1.
- **Viabilidad JS:** Alta, pero aporta poco.
- **Adaptación:** solo una idea suelta: añadir al simulador 1.1 una opción «mostrar banda de confianza del ajuste» para ver cómo explota la varianza con pocos datos.

### 1.3 `Polynomial_Model_Components.ipynb` (sin título)
- **Qué enseña:** descompone un polinomio de grado 5 que pasa por 5 puntos en sus términos X, X², …, X⁵ (dibujados en tres escalas del eje y). Después perturba los coeficientes con un error relativo del 1 % (`std_err_fraction = 0.01`, `L = 100` realizaciones) y dibuja las 100 curvas resultantes: con coeficientes de grado alto, un error mínimo en ellos cambia mucho la predicción.
- **Interactividad:** **no interactivo** (los parámetros se cambian a mano en el código).
- **Datos:** 5 puntos escritos a mano.
- **Nodos:** `poli` y, de forma indirecta, `d_prep` (por qué conviene estandarizar o usar polinomios ortogonales).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**, menos de media jornada.
- **Adaptación:** una pestaña «componentes» dentro del simulador de `poli`: barras con el peso de cada término y un slider «error relativo en coeficientes» que dibuja el abanico de curvas. Mensaje: con grado alto los coeficientes son inestables y no se pueden interpretar.

### 1.4 `Interactive_Ridge_Regresion.ipynb`: «Interactive Demonstration of Ridge Regression and Introduction to Hyperparameter Tuning»
- **Qué enseña:** recorre λ entre 1e-5 y 1e5 (20 valores en escala log) con 20 particiones train/test y dibuja el MSE de train, de test y **contra la verdad** (la recta real conocida) en función de λ. Muestra que regularizar reduce la varianza cuando hay ruido y pocos datos, y que sin ruido solo mete sesgo.
- **Interactividad (comprobada):**
  - *Demo 1:* `n` (5–200), `Test %` (0,05–0,95), `Noise StDev` (0–200), `Regularization` (FloatLogSlider 10⁻⁵–10⁵, λ). Paneles: recta ridge frente a la recta verdadera (en gris), histogramas de error train/test, curvas de MSE train/test/verdad contra λ con bandas P10–P90 y el λ actual marcado.
  - *Demo 2:* `n`, `Test %`, `Regularization` sobre datos reales: gráfico de dispersión real frente a predicho (train/test), histogramas de error y MSE contra λ.
- **Datos:** demo 1 sintética, `y = 20·X + 50 + N(0,σ)` con `X ~ U(0,20)`. Demo 2 con el CSV externo `unconv_MV.csv` (GeoDataSets, 1000 pozos): 6 predictores (`Por, LogPerm, AI, Brittle, TOC, VR`) → `Production`. **Ojo:** en el código de la demo 2 no hay ningún paso de estandarización antes de `Ridge`.
- **Nodos:** `ridge`, `d_hiper`, `d_sesgo`, `d_part`.
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. Ridge tiene solución cerrada, `(XᵀX + λI)⁻¹Xᵀy` (sin penalizar el intercepto); con 1 a 6 predictores es inmediato. Para la demo multivariante bastaría un conjunto sintético de negocio. 1 jornada.
- **Adaptación:** «Simular» en `ridge`: *demanda en función del precio*, con pocos datos y mucho ruido. Sliders n, ruido, % test y log λ; panel de MSE train/test/verdad contra λ. Se puede añadir la **regla del error típico** (`d_hiper`) marcando el λ mínimo y el λ más grande que queda a 1 ET del mínimo. Eso no está en el cuaderno: es una propuesta.

### 1.5 `Interactive_LASSO_Regression.ipynb`: «Interactive Demonstration of LASSO Regression…»
- **Qué enseña:** lo mismo que 1.4 pero con `Lasso`. La demo multivariante añade la **trayectoria de los coeficientes contra λ**: media de 20 particiones con banda P25–P75 para los 6 predictores, que se ve cómo se anulan uno a uno.
- **Interactividad (comprobada):** demo 1 con `n`, `Test %`, `Noise StDev` y `Regularization` (10⁻⁵–10⁵); demo 2 con `n`, `Test %` y `Regularization`. Paneles de la demo 2: dispersión real frente a predicho, trayectoria de coeficientes y MSE train/test contra λ.
- **Datos:** demo 1 sintética (recta 20x+50, igual que en ridge). Demo 2 con `unconv_MV.csv` **cargado desde un archivo local** (`pd.read_csv("unconv_MV.csv")`), así que el cuaderno no funciona tal cual sin descargarlo.
- **Cuidado pedagógico:** el panel se titula «Standardized Model Coefficients», pero el código **no estandariza** las X antes de ajustar `Lasso(alpha=clam)`. Los coeficientes están en unidades originales, así que el orden en que se anulan depende de la escala de cada variable. Además, en la demo 1 el título del panel pone «Ridge Regression Model» por un error de copia. Las dos cosas sirven de ejemplo para `d_prep`.
- **Nodos:** `lasso`, `d_hiper`, `d_prep` (y `enet` como extensión).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta/Media**. LASSO por descenso por coordenadas con umbral suave es un bucle de unas 20 líneas; 20 λ × 20 particiones × 6 variables es inmediato. 1–1,5 jornadas si se hace junto con 1.4.
- **Adaptación:** «Simular» en `lasso`: *¿qué variables explican las ventas de una tienda?* (precio, promoción, temperatura, tráfico web y 4 variables de ruido). Sliders λ y n, más una casilla **«estandarizar dentro del pipeline»** para enseñar que, sin estandarizar, LASSO elimina antes las variables de escala pequeña. Con un slider de mezcla α se convierte en el simulador de `enet`.

### 1.6 `Interactive_Linear_Solutions.ipynb`: superficies de pérdida de ridge y LASSO
- **Qué enseña:** con 2 predictores y sin intercepto, dibuja en el plano (b₁, b₂) tres mapas de contorno: el RSS, el término de penalización y la pérdida total. Marca la solución MCO, el origen y la solución regularizada, junto con la trayectoria de soluciones al variar λ. El tercer panel compara ridge (encoge de forma suave) con LASSO (va hacia los ejes y anula coeficientes).
- **Interactividad (comprobada):** tres paneles con un solo control cada uno:
  1. Ridge: `λ`, FloatLogSlider con `min=1, max=6`, es decir λ entre 10¹ y 10⁶. Paneles: RSS, penalización L2 y pérdida total con la solución.
  2. LASSO: `λ`, FloatSlider lineal 10–3000 (paso 35). Los mismos tres paneles con L1.
  3. Comparación: `λ level`, IntSlider 1–20. Usa una escala de λ distinta para ridge y para LASSO «because they respond quite differently». Dos paneles con la trayectoria y las coordenadas b₁ y b₂ anotadas.
  - Nota: algunos títulos del panel LASSO siguen diciendo «Ridge … L2» (error de copia).
- **Datos:** sintéticos. n = 50, (X₁, X₂) normal bivariante con medias 10, varianzas 4 y covarianza 2,5, `y = 3·X₁ + 2·X₂ + N(0; 0,5)`.
- **Nodos:** `ridge`, `lasso`, `enet` (extensión natural) y `d_train` (minimizar una pérdida).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. La rejilla de pérdida es de 100×100 evaluaciones de un RSS con 2 parámetros; ridge es cerrado y LASSO en 2D es descenso por coordenadas. Contornos con d3-contour desde CDN, o a mano con marching squares. 1–1,5 jornadas.
- **Adaptación:** creo que es **el mejor candidato para la parte geométrica de `ridge`/`lasso`/`enet`**. Ejemplo: *ventas ~ gasto en TV + gasto en radio*, dos predictores correlacionados. Sliders λ y α (mezcla L1/L2, que no está en el cuaderno y sirve para `enet`) y un slider de la correlación entre X₁ y X₂ (propuesta). Se vería el rombo, el círculo y la mezcla, y el punto donde la solución toca el eje.

### 1.7 `Interactive_Polynomial_Solution.ipynb` (el título interno es de regresión lineal)
- **Qué enseña:** pese al nombre, trata la **regresión lineal simple**. Ajusta con `scipy.stats.linregress`, calcula la raíz del MSE en una rejilla 100×100 de (b₀, b₁) y dibuja el mapa de error con la solución óptima y varios modelos subóptimos coloreados por su error, además de las rectas correspondientes sobre los datos. El markdown dice «In the future I will add general polynomial modeling».
- **Interactividad:** **no interactivo** (ipywidgets no aparece).
- **Datos:** CSV externo `Density_Por_data.csv` (GeoDataSets), del que toma una muestra del 30 %.
- **Nodos:** `mco`, `d_train`.
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**, media jornada.
- **Adaptación:** «Simular» en `mco`: el alumno **arrastra un punto (b₀, b₁) sobre el mapa de error** o mueve dos sliders, ve la recta correspondiente sobre los datos (*coste por pedido ~ tamaño del pedido*) y compara su error con el del óptimo MCO. Se puede combinar con 2.1 (descenso del gradiente sobre ese mismo mapa).

### 1.8 `Interactive_Norms.ipynb`: regresión lineal con norma Lᵖ
- **Qué enseña:** ajusta una recta minimizando Σ|e|ᵖ (con `scipy.optimize.minimize`) para L1, L2, L3 y una p elegida, y muestra cómo cambia el ajuste ante un **valor atípico** que coloca el usuario. La L1 es robusta y las p grandes persiguen al atípico.
- **Interactividad (comprobada):** `Lᵖ` (0,1–10, p de la norma personalizada), `n` (15–80), `Error (σ)` (0–0,95, ruido), `X_{n+1}` e `Y_{n+1}` (0–1, coordenadas del punto añadido). Un panel con los datos, el atípico y las 4 rectas (L1, L2, L3 y la p elegida).
- **Datos:** sintéticos, `X ~ U(0; 0,5)`, `y = X² + N(0,σ)`, más un punto puesto por el usuario.
- **Nodos:** `d_mreg` (MAE frente a RMSE: qué pérdida optimizar y qué métrica informar) y `mco`. También tangencialmente `d_train`.
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. Dos parámetros: L2 cerrado, L1 por IRLS o Nelder-Mead, p general por Nelder-Mead (unas 40 líneas). 0,5–1 jornada.
- **Adaptación:** «Simular» en `d_mreg`: *tiempo de entrega ~ distancia*, con un pedido anómalo que el alumno arrastra. Se muestran a la vez las rectas MSE/MAE y una tabla de RMSE, MAE y R² de cada recta. Mensaje: la métrica que se optimiza decide qué recta sale. Se puede enlazar con la pérdida de Huber (`gb`) como extensión.

---

## 2. Optimización y redes neuronales

### 2.1 `Interactive_Optimization.ipynb`: «Interactive Gradient Descent»
- **Qué enseña:** anima el descenso del gradiente con **momento** y **tasa de aprendizaje que decae exponencialmente** sobre una superficie de pérdida 2D con mínimos locales (un cono con ruido gaussiano suavizado). El gradiente se calcula numéricamente (`delta = 0.001`).
- **Interactividad:** **no tiene sliders** aunque importa ipywidgets. Los parámetros están fijos en el código (`r0 = 10`, `momentum = 0.9`, `k = 0.04`, inicio en (5, 50)) y se visualizan con `matplotlib.animation.FuncAnimation` (dos animaciones).
- **Datos:** superficie sintética de 100×100 normalizada a [0,100].
- **Nodos:** `d_train` (tasa, momento, mínimos locales); sirve de base para `mlp` y para `logit`.
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. Ruido suavizado en una rejilla, interpolación bilineal y bucle del descenso con `requestAnimationFrame`. 1 jornada.
- **Adaptación:** «Simular» en `d_train` con sliders tasa inicial, decaimiento, momento, punto de inicio (clic) y nº de pasos, y un selector de superficie («convexa: pérdida de una logística» o «con mínimos locales: red neuronal»). Opcional: SGD con lotes, añadiendo ruido al gradiente según el tamaño de lote, que no está en el cuaderno.

### 2.2 `Interactive_NeuralNetwork_SingleLayer.ipynb`: «Introduction to Artificial Neural Networks: Single Layer ANN» (J. E. McCarthy II, supervisado por Pyrcz)
- **Qué enseña:** cuatro bloques. (a) Las funciones de activación sigmoide, tanh y ReLU. (b) Una red 1→1→1 con pesos puestos a mano para ajustar unos datos normalizados. (c) Un perceptrón de 3 entradas entrenado con descenso del gradiente programado a mano («¿pelo? ¿patas? ¿más de un ojo?» → probabilidad), con curvas de peso y de coste por época. (d) Sobreajuste con regresión polinómica. (e) Una red Keras con anchura, nº de capas, tasa y épocas.
- **Interactividad (comprobada):**
  - Activaciones: tres sliders `X` (sigmoide −10–10, tanh −10–10, ReLU −1–1), que mueven un punto sobre cada curva.
  - Red a mano: `Act. Funtion` (Sigmoid/Tanh/ReLU), `Weight 1`, `Bias 1`, `Weight 2` (todos −5–5). Paneles: curva de la red sobre los datos y diagrama de la red con los valores escritos encima de una imagen PNG descargada de GitHub.
  - Perceptrón: desplegables `Hair?`, `Number of Legs?` (2/4) y `More than 1 eye?` → probabilidad predicha.
  - Sobreajuste: `Added STD` (0–1), `Degrees` (1–20), `N. Training Samples` (15–80) y la casilla `Show Test Data`. Usa `PolynomialFeatures + LinearRegression` en un `Pipeline`. Nota: el «test score» se calcula con `cross_val_score` **sobre el conjunto de test**, lo que es metodológicamente discutible.
  - Keras: `Width of Hidden Layers` (5–50), `Learning Rate` (log, 0,001–0,01), `Epochs` (500–1100) y `Number of Hidden Layers` (1–3), con optimizador Adam y pérdida MSE.
- **Datos:** CSV externo `Stochastic_1D_por_perm_demo.csv` (GeoDataSets); el perceptrón usa datos de juguete escritos a mano.
- **Nodos:** `mlp` y `d_train`. El bloque de sobreajuste corresponde a `poli`/`d_sesgo`.
- **Duplicación:** el bloque de sobreajuste duplica «Elige el grado». El resto no.
- **Viabilidad JS:** activaciones, red a mano y perceptrón: **Alta** (cálculo trivial). La parte Keras: **Baja** tal cual (TensorFlow), **Media** si se reescribe como un MLP pequeño en JS con retropropagación (1–3 capas, ≤ 50 neuronas, 1D: viable en el navegador). 1 jornada para lo sencillo y 2–3 para un MLP entrenable.
- **Adaptación:** «Simular» en `mlp`, en dos niveles. (1) *Construye la red a mano*: 1 entrada → 2–3 neuronas ocultas → salida, con sliders de pesos y sesgos y un selector de activación, para ajustar la curva de *conversión ~ descuento*. (2) *Entrena la red*: anchura, capas, tasa y épocas, mostrando las curvas de pérdida de train y validación (parada temprana, enlazado con `d_train`).

### 2.3 `SubsurfaceDataAnalytics_ANN.ipynb`: red 3-2-1 programada a mano
- **Qué enseña:** entrena con retropropagación escrita a mano (sigmoide en la capa oculta, salida lineal) una red de 3 entradas, 2 neuronas ocultas y 1 salida, con **un solo ejemplo** de entrenamiento (x = 0,5; 0,2; 0,7 → y = 0,3), `lr = 0.2` y 1000 épocas. Inicializa los pesos con U(±1/√n). Dibuja un diagrama de la red con pesos, sesgos y gradientes en una época (`iepoch = 10`) y la convergencia de la predicción, los pesos y los sesgos a lo largo de las épocas.
- **Interactividad:** **no interactivo** (importa ipywidgets, pero `iepoch` está fijo). Hay un posible error: el panel de sesgos (φ₄, φ₅, φ₆) dibuja las series `w14, w24, w34`, que son pesos.
- **Datos:** un ejemplo sintético escrito a mano.
- **Nodos:** `mlp`, `d_train`.
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. Son 9 pesos y 3 sesgos. 1 jornada, casi todo el diagrama.
- **Adaptación:** complemento de 2.2: un slider «época» que recorre el entrenamiento y muestra en el diagrama los valores y gradientes de cada conexión (forward y backward), con slider de tasa. Muy útil para explicar qué es una época y qué hace la retropropagación.

### 2.4 `SubsurfaceDataAnalytics_ANN_ActivationFunctions.ipynb`
- **Qué enseña:** dibuja las funciones sigmoide, tanh y ReLU con sus derivadas, y además la función escalón. El markdown inicial, por error de copia, habla de «support vector machines».
- **Interactividad:** **no interactivo**. **Datos:** ninguno. **Nodo:** `mlp`. **Duplicación:** se solapa con el bloque (a) de 2.2.
- **Viabilidad:** Alta y trivial. **Adaptación:** una pestaña del simulador de `mlp` con la curva y su derivada (desvanecimiento del gradiente en la sigmoide).

### 2.5 `SubsurfaceDataAnalytics_NeuralNet.ipynb`: «Artificial Neural Networks for Prediction in Python»
- **Qué enseña:** una red Keras 1D (profundidad → porosidad normalizada), primero con un ajuste razonable y después **sobreajustada** (tasa más baja, más épocas), con las curvas de error de train y de test por época.
- **Interactividad:** **no interactivo**. **Datos:** CSV `1D_Porosity.csv` (GeoDataSets).
- **Nodos:** `mlp`, `d_train` (parada temprana).
- **Duplicación:** no.
- **Viabilidad JS:** **Baja** tal cual (TensorFlow). La idea es reimplementable con el MLP en JS de 2.2 (Media).
- **Adaptación:** se integra en el nivel (2) de 2.2, con la curva de validación por época y un marcador de «mejor época».

---

## 3. Árboles y ensembles

### 3.1 `Interactive_Decision_Tree.ipynb`: «Machine Learning Decision Tree Demo»
- **Qué enseña:** un árbol de regresión con 2 predictores. Dibuja las regiones rectangulares (hojas) con la predicción escrita dentro, un gráfico de real frente a predicho con medias y P25–P75 condicionados por hoja, y el MSE de train y de test contra `max_leaf_nodes` (de 2 a 100) con el valor actual marcado.
- **Interactividad (comprobada):** un único slider `n_leaf` (IntSlider 2–150, que es `max_leaf_nodes`). Tres paneles: mapa de regiones con los puntos de train y de test, validación con estadísticos condicionados y curva de ajuste del hiperparámetro.
- **Datos:** CSV `unconv_MV.csv` (muestra del 30 %, unos 300 pozos). Usa `Por` y `Brittle` → `Production`, con ruido N(0, 700) añadido y una partición 75/25.
- **Nodos:** `arbol_reg`, `d_hiper`, `d_sesgo`.
- **Duplicación:** no.
- **Viabilidad JS:** **Media**. Hay que programar un CART de regresión 2D con crecimiento *best-first* hasta `max_leaf_nodes` (que es lo que hace sklearn con ese parámetro): ordenar por cada variable y buscar el mejor corte por SSE. Con n ≈ 300 y 100 hojas va sobrado. La curva de MSE contra hojas sale gratis de un único crecimiento best-first, guardando el árbol tras cada división. 2 jornadas.
- **Adaptación:** «Simular» en `arbol_reg`: *ventas ~ precio + gasto en promoción*, con un «punto dulce» en el precio, como el «sweet spot» de brittleness del original. Slider de nº de hojas, mapa de regiones y curva train/test. Variante para `arbol_clas`: *abandono sí/no* con impureza de Gini.

### 3.2 `Experiential_DecisionTree.ipynb` y `DT_Demo.ipynb`
- **Qué enseñan:** el flujo completo con sklearn sobre `unconv_MV_v4.csv` (Experiential, archivo **local**) y `unconv_MV.csv` (DT_Demo, archivo local). Incluyen la matriz de correlaciones, un árbol con `max_depth` (4 en Experiential; 3 con `min_samples_leaf=5` en DT_Demo), un bucle que hace crecer `max_leaf_nodes`, el MSE de test y de k-fold contra el nº de hojas, la poda a 10–12 hojas, **la conversión del árbol a reglas if/else** (`tree_to_code`), la trayectoria de decisiones de una predicción (`get_lineage`) y la importancia de Gini.
- **Interactividad:** **no interactivos**.
- **Nodos:** `arbol_reg`, `d_hiper`, `d_cv`, `d_interp` (reglas e importancia).
- **Duplicación:** se solapan con 3.1.
- **Viabilidad JS:** la idea de «árbol → reglas» es **Alta** una vez hecho el CART de 3.1.
- **Adaptación:** dentro del simulador de 3.1, un panel con las **reglas legibles** del árbol actual («SI precio ≤ 4,2 € Y promo > 300 € → ventas ≈ 1250»), útil para `d_interp`.

### 3.3 `SubsurfaceDataAnalytics_EnsembleTrees.ipynb`: «Tree Bagging and Random Forest»
- **Qué enseña:** bagging con 6 árboles profundos entrenados sobre remuestreos bootstrap (dibuja cada uno, con los datos repetidos o ausentes) y el promedio progresivo de 1 a 6 árboles, que suaviza la superficie de predicción y reduce la varianza. Pasa después a random forest (`max_features`) mostrando la diversidad de los primeros cortes, y termina con el **error OOB** y la importancia de variables con barras de error entre árboles, y el MSE OOB contra el nº de árboles.
- **Interactividad:** **no interactivo**.
- **Datos:** CSV `unconv_MV.csv` (300 para train y 700 para test, 2 predictores).
- **Nodos:** `bagging`, `rf`, `d_cv` (OOB), `d_interp` (importancia).
- **Duplicación:** no; la asignatura tiene simuladores de boosting, no de bagging ni de RF.
- **Viabilidad JS:** **Alta en 1D** (árboles de un predictor, bootstrap y promedio: muy ligero) y **Media en 2D** (reutiliza el CART de 3.1). 1,5–2 jornadas.
- **Adaptación:** «Simular» en `bagging`/`rf`: *ventas diarias ~ temperatura* (1D). Sliders nº de árboles (1–200), profundidad y `max_features` (en 2D). Paneles: árboles individuales en gris con el promedio encima, MSE de test y **MSE OOB** contra nº de árboles, y en cada árbol qué datos han quedado «fuera de la bolsa».

### 3.4 `SubsurfaceDataAnalytics_Gradient_Boosting_Simple.ipynb` y `SubsurfaceDataAnalytics_Gradient_Boosting.ipynb`
- **Qué enseñan:** *Simple*: un conjunto sintético 1D (componente aditiva + cíclica + aleatoria) y boosting de 1 a 12 árboles visto en el espacio original y en el de los residuos (cada árbol ajusta el residuo del anterior). *Completo*: `unconv_MV.csv` con 2 predictores, stumps frente a árboles más profundos, el patrón «a cuadros» de los stumps, profundidad × nº de árboles × tasa de aprendizaje y su efecto en la varianza explicada en test.
- **Interactividad:** **no interactivos**.
- **Nodos:** `gb`.
- **Duplicación:** **sí**, con `slides/04/simuladores/gbm_boosting.html`.
- **Viabilidad:** Alta/Media, pero no hace falta.
- **Adaptación:** como mucho, comparar con el simulador existente y robar dos ideas si no las tiene: (a) la vista en el espacio de residuos árbol a árbol y (b) el patrón de stumps en 2D.

### 3.5 `SubsurfaceDataAnalytics_MultipleModelsSimple.ipynb` y `SubsurfaceDataAnalytics_MultipleModels.ipynb`
- **Qué enseñan:** sobre `unconv_MV.csv` (Por y Brittle → Production, estandarizados), ajustan uno tras otro kNN, árbol, random forest y gradient boosting (y ridge en la versión completa), y los comparan con mapas de predicción en una figura final. La versión simple dice que no hay ajuste de hiperparámetros ni test.
- **Interactividad:** **no interactivos**.
- **Nodos:** visión general de los estimadores, sin conexión clara con `voting`/`stacking` (no combinan modelos).
- **Duplicación:** no.
- **Viabilidad JS:** Media (requiere varios algoritmos).
- **Adaptación:** idea para un futuro «comparador»: el mismo conjunto 2D de negocio y un selector de modelo que muestra su superficie de predicción. Reutilizaría los motores de 1.4, 3.1 y 3.3. Baja prioridad.

---

## 4. Interpretación

### 4.1 `Interactive_Shapley_Values.ipynb`: «Interactive Shapley Value Demonstration in Python»
- **Qué enseña:** cinco experimentos con `RandomForestRegressor` y `shap.TreeExplainer`. (1) Un predictor lineal: el Shapley es f(X₁) − E[y]. (2) Dos predictores lineales, con las contribuciones marginales de cada coalición. (3) Una relación cuadrática en X₁ y lineal en X₂. (4) Predictores **correlacionados** (ρ). (5) Importancia global (`summary_plot` en barras, enjambre y violín) y el efecto del sobreajuste.
- **Interactividad (comprobada):**
  - Exp. 1: `b_1` (0–1) y `σ_noise` (0,01–1).
  - Exp. 2: `b_1`, `b_2` (0–5), `σ_noise` (0,01–5) y `leaf nodes` (2–100).
  - Exp. 3: lo mismo, con `leaf nodes` hasta 1000.
  - Exp. 4 y 5: `b_1`, `b_2`, `ρ` (−1–1), `σ_noise`, `leaf nodes` (2–100) y `# tree` (1–100).
  - Paneles: los datos con el modelo y los `shap.dependence_plot` de cada variable (o los `summary_plot` en el exp. 5).
- **Datos:** sintéticos (X ~ N(0,1), con n = 50 y 25 de fondo en el exp. 1, y n = 300 y 200 de fondo después).
- **Nodos:** `d_interp` (Shapley y dependencia) y, de rebote, `rf`.
- **Duplicación:** no.
- **Viabilidad JS:** **Baja** tal cual (sklearn + shap). **Media** reimplementado: con 2 variables el Shapley exacto solo tiene 2 órdenes. Con un modelo conocido (la función verdadera o un bosque pequeño propio de 3.3) y la esperanza marginal sobre un conjunto de fondo (Shapley intervencional), en JS es un doble bucle. 2 jornadas, menos si ya existe el motor de árboles.
- **Adaptación:** «Simular» en `d_interp`: *precio de una vivienda ~ superficie + antigüedad*. Sliders b₁, b₂, ρ y ruido; selector «modelo verdadero / bosque con k hojas». Muestra el gráfico de dependencia de Shapley de cada variable y la barra de importancia global, y cómo la correlación reparte el mérito. Se puede añadir el PDP/ICE para comparar (no está en el cuaderno).

### 4.2 `SubsurfaceDataAnalytics_Feature_Ranking.ipynb`: «Feature Selection/Ranking»
- **Qué enseña:** un catálogo de métodos de ordenación de variables sobre `unconv_MV_v4.csv` (200 pozos): covarianza, Pearson, Spearman, correlación parcial y semiparcial, diagramas de violín y de caja condicionados, coeficientes b frente a β (estandarizados), importancia de RF, RFE, información mutua (con mRMR y un «delta MI quotient»), VIF y Shapley (el código llama a `shap` decenas de veces).
- **Interactividad:** **no interactivo**.
- **Nodos:** `d_interp` y, sobre todo, la idea «coeficiente sin estandarizar frente a estandarizado» para `mco`/`d_prep`.
- **Duplicación:** no.
- **Viabilidad JS:** Baja como conjunto (demasiados métodos y dependencias). Partes sueltas (β estandarizados, correlación parcial): Alta.
- **Adaptación:** baja prioridad. Como mucho, una tarjeta en `d_interp` que compare «coeficiente bruto / estandarizado / importancia por permutación» para el mismo modelo lineal.

---

## 5. Decisiones, métricas y probabilidad

### 5.1 `Interactive_DecisionMaking.ipynb`: «Optimum Decision Making in Python»
- **Qué enseña:** dada una distribución de incertidumbre N(μ, σ) y una **función de pérdida asimétrica** (pendiente y potencia distintas para infraestimar y para sobreestimar), calcula la pérdida esperada de cada posible estimación por convolución y marca la **estimación óptima**. Con pérdida lineal asimétrica el óptimo es un cuantil; con pérdida cuadrática simétrica es la media.
- **Interactividad (comprobada):** `μ` (0–1), `σ` (0,001–0,25), `m_under` y `m_over` (0–1, pendiente de la pérdida por infraestimar y por sobreestimar), `p_under` y `p_over` (1–5, exponente), `Step` (log, 10⁻⁴–10⁻¹, resolución). Tres paneles: distribución de incertidumbre con el óptimo marcado, función de pérdida (verde = infraestimar, azul = sobreestimar) y pérdida esperada contra la estimación.
- **Datos:** sintéticos (paramétricos).
- **Nodos:** `d_deseq` (costes asimétricos) y `d_mreg` (por qué MSE lleva a la media y MAE a la mediana, y la pérdida *pinball* a los cuantiles). Por analogía, `d_mclas` (mover el umbral según los costes).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**. Es una suma discreta: para cada estimación, Σ pdf·pérdida. 0,5–1 jornada.
- **Adaptación:** «Simular» en `d_deseq`: **el problema del vendedor de periódicos**. Demanda incierta N(μ,σ), coste de quedarse sin stock frente a coste de sobrante, y la cantidad óptima a pedir (cuantil crítico c_u/(c_u+c_o)). Una segunda pestaña para clasificación: con probabilidades predichas y costes FN/FP, el umbral óptimo. Esa pestaña es una propuesta, no está en el cuaderno.

### 5.2 `Interactive_Bayesian_Updating.ipynb` (no estaba en la lista; lo añado)
- **Qué enseña:** la regla de Bayes para una prueba diagnóstica, P(H|+), y la sorpresa de que con una tasa base baja la mayoría de positivos son falsos.
- **Interactividad (comprobada):** dos paneles con los mismos tres sliders: `P(H)` (0–1, tasa base), `P(+|H)` (0–1, sensibilidad) y `P(+|Hᶜ)` (0–1, tasa de falsos positivos). Revisé los títulos de los gráficos solo por encima.
- **Datos:** ninguno (probabilidades).
- **Nodos:** `d_mclas` (precisión frente a sensibilidad; precisión = P(H|+)) y `d_deseq` (con clases desequilibradas la precisión se hunde).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**, menos de media jornada.
- **Adaptación:** dentro de `d_deseq`: *detección de fraude con un 0,5 % de fraudes*. Sliders tasa base, sensibilidad y FPR; matriz de confusión para 10 000 transacciones y la precisión resultante. Esto conecta con la curva PR.

### 5.3 `Interactive_Model_Fitting.ipynb`: «Interactive Model Fitting» (MCO frente a máxima verosimilitud)
- **Qué enseña:** ajusta una gaussiana a 35 datos (con 2 atípicos en 0,8 y 0,9) de dos maneras: por **mínimos cuadrados sobre la CDF empírica** (`curve_fit`) y por **máxima verosimilitud** (minimizando la log-verosimilitud negativa). Muestra los errores al cuadrado y las verosimilitudes de cada dato para el modelo que elige el usuario frente al óptimo. El cuaderno incluye además un muestreador de Gibbs, que queda fuera del temario.
- **Interactividad (comprobada):** `μ` (0–1) y `σ` (0,01–1) del modelo propuesto. Cuatro paneles: CDF con los residuos, histograma de los errores al cuadrado con la SSE, PDF con las verosimilitudes de cada dato, y su histograma con el producto de verosimilitudes y −log L. La parte de Gibbs usa `n_sample` y `ρ`.
- **Datos:** sintéticos (N(0,5; 0,1)), etiquetados como «cobre».
- **Nodos:** `d_train` (qué pérdida se minimiza); conceptualmente `logit`, `poisson`, `gamma` (los GLM se ajustan por máxima verosimilitud, es decir, minimizando la log-loss).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta** (la PDF/CDF normal y la optimización de 2 parámetros por Nelder-Mead o con el MLE cerrado). 1 jornada.
- **Adaptación:** para el nodo `logit`, la versión más útil cambiaría la gaussiana por una **logística**: sliders β₀ y β₁, con la log-verosimilitud de cada cliente (compra sí/no) y la comparación con el ajuste MCO del `mpl`. Esto ya es una adaptación libre: el cuaderno solo trata la gaussiana.

---

## 6. Remuestreo e incertidumbre (base de bagging, OOB y error típico)

### 6.1 `Interactive_Bootstrap.ipynb`: «Bootstrap for Uncertainty in Sample Statistics»
- **Qué enseña:** genera una muestra sintética, hace L = 1000 remuestreos con reemplazo y dibuja la distribución bootstrap de la media y de la desviación típica (con P10, P50 y P90). Un segundo panel cambia el tamaño del remuestreo y compara la incertidumbre nueva con la original: con menos datos hay más incertidumbre y la desviación típica sale sesgada a la baja.
- **Interactividad (comprobada):** desplegable `Dataset Distribution` (Triangular/Uniform/Gaussian), `Dataset: Mean / Mode` (0–100), `Dataset: St. Deviation` (0,01–30), `Dataset: Minimum`, `Dataset: Maximum` y `Dataset: Number Samples` (2–1000), todos sliders verticales. Después, `New Number Samples` (2–1000). Paneles: histograma de la muestra y, luego, histogramas bootstrap de la media y la desviación típica (original frente a nuevo). La celda bootstrap con L = 1000 **no es interactiva**.
- **Datos:** sintéticos.
- **Nodos:** `bagging` (el bootstrap como base), `d_cv` (OOB: probabilidad de quedar fuera ≈ 36,8 %) y `d_hiper` (error típico).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**, 0,5 jornadas.
- **Adaptación:** mejor como **pestaña previa del simulador de `bagging`** (3.3) que como simulador aparte: «¿qué es un remuestreo bootstrap?». Muestra qué filas se repiten y cuáles quedan fuera (OOB), con *tickets de venta de un día* como ejemplo.

### 6.2 `Interactive_Confidence_Interval.ipynb`: «Bootstrap and Analytical Confidence Intervals»
- **Qué enseña:** (a) bootstrap de una proporción (bolas rojas y verdes sacadas de un sombrero), realización a realización; (b) muchas realizaciones resumidas con diagramas de caja, CDF e intervalo de confianza con α; (c) el intervalo de confianza analítico de la media con t de Student.
- **Interactividad (comprobada):** (a) `n_red`, `n_green` (0–100) y `L` (1–16); (b) `n_red`, `n_green`, `L` (5–1000) y `α` (0,01–0,40); (c) `n` (1–20), `x̄` (1–4), `s_x` (0,1–2) y `α`.
- **Datos:** sintéticos.
- **Nodos:** `d_cv` (el error típico de la media de los k pliegues y su intervalo) y `d_hiper` (regla del error típico).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta** (necesita la inversa de la t de Student, con una aproximación numérica o jStat desde CDN).
- **Adaptación:** dentro de `d_cv`, una pestaña «¿cuánto me puedo fiar del error de CV?»: con k pliegues, el error medio ± ET y el intervalo, junto a la regla 1-ET sobre una curva de error contra hiperparámetro. Solo aprovecha la parte analítica del cuaderno; el resto es diseño nuevo.

### 6.3 `Interactive_Spurious_Correlations.ipynb`: «Too Few Samples May Result in Spurious Correlations»
- **Qué enseña:** genera m variables **independientes** con n muestras y dibuja la matriz de correlaciones (triángulo inferior). Con n pequeño y distribuciones sesgadas (lognormal) aparecen correlaciones grandes que son puro azar.
- **Interactividad (comprobada):** desplegable de distribución (Triangular/Uniform/Gaussian/LogNorm), `Sample: Mean/Mode`, `Sample: St.Dev.`, `Sample: Min.`, `Sample: Max.`, `Number Samples` (2–1000, por defecto 4) y `Number Features` (2–20). Panel: mapa de calor de la matriz de correlaciones (el histograma de coeficientes está comentado en el código).
- **Datos:** sintéticos.
- **Nodos:** `d_part`/`d_cv` (por qué seleccionar variables con todos los datos antes de validar engaña) y `d_interp` (cautela).
- **Duplicación:** no.
- **Viabilidad JS:** **Alta**, 0,5 jornadas.
- **Adaptación:** «Simular» en `d_part` (fuga de información en la selección de variables): *50 KPIs sin relación real y 24 meses de ventas*. Se eligen los 5 «mejores» por correlación con todos los datos, y luego se ve que en datos nuevos no predicen nada. La segunda parte no está en el cuaderno.

---

## 7. Flujos de scikit-learn (no interactivos)

### 7.1 `PythonDataBasics_Pipelines.ipynb`: «Machine Learning Modeling in Python with scikit-learn Pipelines»
- **Qué enseña:** el mismo flujo de kNN de dos maneras. Primero «a mano»: `StandardScaler().fit_transform` **sobre todo el conjunto de datos** (celda 15) y después `cross_val_score` con `KFold(4)` recorriendo k. Luego con `Pipeline([scaler, knear])` + `GridSearchCV`. Discute legibilidad y reproducibilidad, amplía la rejilla (`weights` uniform/distance) y repite con un árbol. El cuaderno **no** presenta el primer flujo como fuga de información; esa lectura es mía.
- **Interactividad:** **no interactivo**. **Datos:** `unconv_MV.csv`.
- **Nodos:** `d_prep`, `d_hiper`, `d_cv`, `d_part`.
- **Duplicación:** no.
- **Viabilidad JS:** la lógica sí es reimplementable (Alta), pero kNN queda fuera del mapa.
- **Adaptación:** idea para el simulador de `d_prep`/`d_part`: **«estandarizar antes o dentro de la CV»**. Con un modelo del mapa (ridge o LASSO con la casilla de 1.5) y pocos datos se compara el error de CV en los dos casos. La diferencia suele ser pequeña al estandarizar y grande al imputar o al seleccionar variables (ver 6.3), lo que hace bueno combinar las tres fugas en un mismo simulador.

### 7.2 `PythonDataBasics_PedictiveMachineLearning.ipynb`: «Predictive Machine Learning Modeling in Python with scikit-learn»
- **Qué enseña:** el ciclo instanciar → ajustar → predecir con un árbol 1D (`1D_Porosity.csv`): partición 75/25, MSE contra el nº de hojas, k-fold con `cross_val_score`, reentrenar con todos los datos tras elegir el hiperparámetro y la versión con `Pipeline` + `GridSearchCV`.
- **Interactividad:** **no interactivo**.
- **Nodos:** `d_part`, `d_cv`, `d_hiper`, `arbol_reg`.
- **Duplicación:** probablemente se solapa con lo que ya se cuenta en clase (no puedo comprobarlo).
- **Adaptación:** la secuencia «partición → curva de CV → reentrenar con todo» sirve de guion para un simulador de `d_hiper` con árbol 1D (Alta, porque es un árbol de un predictor).

### 7.3 `SubsurfaceDataAnalytics_Feature_Imputation.ipynb`: «Feature Imputation»
- **Qué enseña:** quita valores de `unconv_MV_v4.csv` y recorre los métodos de tratamiento: descartar variables, descartar muestras, borrado por lista, constante, media, moda, kNN y MICE (IterativeImputer), además de una variable indicadora de «faltaba un valor».
- **Interactividad:** **no interactivo**.
- **Nodos:** `d_prep` (imputar dentro del Pipeline).
- **Duplicación:** no.
- **Viabilidad JS:** Alta para la media, la moda y el indicador; Media para kNN; MICE no compensa.
- **Adaptación:** en el simulador de `d_prep`, un slider «% de valores faltantes» que muestra cómo la imputación por la media comprime la varianza y atenúa la correlación (*renta ~ gasto*). Además, la comparación de imputar antes o dentro de la CV. Las dos cosas son propuestas.

### 7.4 `SubsurfaceDataAnalytics_SupportVectorMachines.ipynb` (Wendi Liu) y `SuportVectorMachines.ipynb`
- **Qué enseñan:** clasificación binaria con `svm.SVC`. El primero usa `12_sample_data.csv` (impedancia acústica + porosidad → facies): kernels lineal, polinómico y RBF, efecto de C (margen y nº de vectores soporte) y una rejilla C × γ con la precisión de validación y ejemplos de modelos buenos, medios y malos. El segundo usa un modelo «verdad» espacial sintético truncado en ±1, kernel polinómico de grado 2, ajuste de C con k-fold y matrices de confusión.
- **Interactividad:** **no interactivos**.
- **Nodos:** `svc` (y `d_mclas` por la matriz de confusión); `svr` no aparece.
- **Duplicación:** no.
- **Viabilidad JS:** **Media-Baja**. Habría que programar SMO, o un SVM lineal por subgradiente (Pegasos) más un kernel RBF con SMO simplificado: con n ≤ 200 es viable, pero son 2–3 jornadas.
- **Adaptación:** «Simular» en `svc`: *clientes que compran o no, según edad e ingresos*. Sliders C, γ y kernel; frontera, margen y vectores soporte marcados. Merece la pena si no existe otra fuente más sencilla.

---

## 8. Descartados (una línea cada uno)

**Fuera del temario (geoestadística, espacial, clustering o métodos que no están en el mapa):**
- `Interactive_Uncertainty_Checking`: comprobación de incertidumbre con kriging simple y variograma (nug, azi, hmaj1…). Solo aprovecharía la idea de calibrar intervalos de predicción.
- `Interactive_RadialBasisFunctions`: `scipy.RBFInterpolator` sobre `1D_Porosity.csv` (ε, kernel, n, grado, suavizado). Es interpolación, no un estimador del mapa.
- `Interactive_Convolution_kNearest`: regresión por convolución y kNN en 1D (forma y tamaño de la ventana, k, proporción muestreada). kNN no está en el mapa, aunque ilustra bien el sesgo-varianza con k.
- `Interactive_Bayesian_Linear_Regression`, `SubsurfaceDataAnalytics_BayesianRegression`, `MachineLearning…Bayesian…`: Metropolis-Hastings/MCMC (slider ℓ = nº de muestras aceptadas). MCMC queda fuera.
- `Interactive_Gibbs_Sampler`, el bloque Gibbs de `Interactive_Model_Fitting`, `Interactive_Sivia_Coin_Toss`: MCMC o inferencia bayesiana pura.
- Kriging, variogramas, desagrupamiento, simulación espacial, efecto string, tendencia, PreDrill (`Interactive_Simple_Kriging*`, `Interactive_Variogram_*`, `Interactive_Declustering`, `Interactive_Simulation`, `Interactive_Spatial_Aggregate_Uncertainty`, `Interactive_String_Effect`, `Interactive_Trend`, `Interactive_PreDrill_Prediction`, `Spatial_Bootstrap`, `PyGSLIB_*`, `Variogram`): geoestadística.
- PCA, MDS, clustering y DBSCAN (`Interactive_PCA*`, `PCA_Demo`, `Interactive_kMeans_Clustering`, `Interactive_DBSCAN`, `Interactive_Spectral_Clustering`, `SubsurfaceDataAnalytics_*Clustering*`, `*Multidimensional_Scaling*`): reducción de dimensión y clustering.
- CNN y GAN (`SubsurfaceDataAnalytics_ConvolutionalNeuralNetworks*`, `*GenerativeAdversarialNetwork*`): fuera del temario.
- `SubsurfaceDataAnalytics_NaiveBayes`, `SubsurfaceDataAnalytics_kNearestNeighbour`: no son estimadores del mapa.
- `SubsurfaceDataAnalytics_IsotonicRegression`: regresión isotónica sobre `GrainSize_Por.csv` (local), que no está en el mapa. Como mucho, contexto para las restricciones de monotonía en XGBoost.

**Estadística básica (contexto, poco valor para «Simular»):**
- `Interactive_Central_Limit_Theorem`: TCL (distribución, m variables promediadas, L realizaciones). Fundamento del error típico, pero no es un nodo.
- `Interactive_Correlation_Coefficient_Issues` / `Interactive_Correlation_Coefficient`: Pearson frente a Spearman con un atípico, y correlación bivariante. Contexto para `d_interp`; se solapa con 1.8.
- `Interactive_Bootstrap_CowbowHat`, `Bootstrap.ipynb` (script mínimo de bootstrap con n = 10 y L = 100, sin widgets), `PythonDataBasics_Bootstrap*`, `SubsurfaceDataAnalytics_bootstrap`: los cubre 6.1.
- `Experiential_Bootstrap_MCS`: plantilla de ejercicio (funciones `bootstrap`, `OIP` y `MCS` vacías para que la complete el alumno), con un caso de reservas de petróleo.
- `Interactive_Hypothesis_Testing`, `Interactive_PP_Plot`, `Interactive_QQ_Plot`, `Interactive_ParametricDistributions`, `Interactive_MarginalJointConditional`, `Interactive_Monte_Carlo_*`, `Interactive_Sampling_Methods`, `Interactive_Distribution_Transformations`, `NSCORE`: estadística inferencial y distribuciones.
- Los `PythonDataBasics_*` de DataFrames, ndarrays, estadística univariante y bivariante y visualización: fundamentos de Python.
- `SubsurfaceDataAnalytics_LinearRegression`, `_RidgeRegression`, `_Lasso`, `_PolynomialRegression`, `_DecisionTree`, `_Feature_Transformations`, `_scikit_learn`, `PythonDataBasics_LinearRegression`, `PythonDataBasics_MachineLearning`: versiones estáticas de lo ya fichado (los títulos coinciden con nbsum.json; no los abrí en detalle).
- `make_*`, `soft_data_debiasing`, `LU+Decomposition`, `Lorenz_*`, `Ripley_K_demo`, `PGE383_ProjectTemplate`: generadores de datos, plantillas o temas de subsuelo.

---

## 9. Notas de rigor y límites

- **No he ejecutado** ningún cuaderno. Las descripciones de los gráficos salen del código, sin ver las figuras.
- Varios cuadernos cargan CSV **locales** (`unconv_MV.csv` en LASSO demo 2 y DT_Demo, `unconv_MV_v4.csv` en Experiential_DecisionTree, `GrainSize_Por.csv` en Isotonic) o descargan de GitHub en tiempo de ejecución. Para el mapa todo debería sustituirse por datos sintéticos de negocio generados en JS, cosa que el contexto ya exige.
- `nbsum.json` marca `Interactive_Polynomial_Solution` como no interactivo y `SubsurfaceDataAnalytics_ANN` como interactivo. Lo he comprobado: el primero no usa widgets y el segundo **importa** ipywidgets pero **no define ningún slider**. `Interactive_Optimization` tampoco tiene sliders: usa animación.
- Errores o puntos débiles que he visto en el código y que conviene no copiar: coeficientes «estandarizados» sin estandarizar (LASSO, demo 2); títulos «Ridge» en paneles de LASSO (LASSO demo 1 y Linear_Solutions); el panel de sesgos que dibuja pesos (ANN a mano); `cross_val_score` aplicado al conjunto de test (NeuralNetwork_SingleLayer, bloque de sobreajuste); `StandardScaler` ajustado con todos los datos antes de la CV en el flujo «a mano» de Pipelines.
- **Licencia:** MIT. Si se adapta código o ideas concretas, conviene citar «Adaptado de M. Pyrcz, PythonNumericalDemos (MIT)» en el simulador.
- Las extensiones marcadas como «propuesta» (regla 1-ET, slider α de Elastic Net, pestaña de umbral de clasificación, fuga en la selección de variables, logística en lugar de gaussiana, PDP/ICE) **no están en los cuadernos**: son ideas de diseño mías.
