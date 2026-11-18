# Simuladores posibles para el mapa mental de TAP a partir de los repositorios de GeostatsGuy

Exploración realizada el 2-11-2026 sobre los repositorios públicos de [GeostatsGuy](https://github.com/GeostatsGuy). **No se incorpora nada al mapa:** este documento solo enumera ideas de simuladores y de código que podrían activar los botones «Simular» del mapa o completar sus fichas.

## 1. Resumen

- **Qué se analizó.** Tres repositorios de Michael Pyrcz (GitHub `GeostatsGuy`):
  - `MachineLearningDemos`: 16 cuadernos.
  - `PythonNumericalDemos`: 163 cuadernos.
  - `MachineLearningCourse`: 191 proyectos finales de estudiantes, de 2020 a 2025.

  Se leyó el contenido de cada cuaderno candidato (texto, código y controles interactivos) sin ejecutarlo.
- **Poca interactividad aprovechable.** Las 16 demos de `MachineLearningDemos` son flujos estáticos. En `PythonNumericalDemos` unos 60 cuadernos usan ipywidgets, pero la mayoría trata de geoestadística o de estadística básica. Solo una docena encaja con los nodos del mapa.
- **Nada se puede copiar tal cual.** Todo está en Python, con scikit-learn y matplotlib. Un simulador del mapa tiene que funcionar en el navegador, en JavaScript y sin servidor, así que siempre se trataría de **reimplementar la idea**, no de traducir código.
- **Los datos tampoco sirven.** Casi todos son del subsuelo (porosidad, permeabilidad, producción de pozos), del repositorio `GeoDataSets`. Habría que sustituirlos por datos sintéticos con un contexto general de negocio, como piden las directrices del mapa.
- **Dos mejoras inmediatas sin código nuevo.** La asignatura ya tiene `slides/04/simuladores/gbm_boosting.html` y `xgboost_penalizacion.html`, que aceptan parámetros en la URL. Los botones «Simular» de `gb` y `xgb` podrían enlazarlos directamente.
- **Ideas más valiosas,** ordenadas por valor y esfuerzo (sección 4):
  1. la varianza de MCO frente a Ridge con bootstrap (`ridge`, `d_sesgo`);
  2. la geometría de las penalizaciones L1 y L2 (`lasso`, `enet`);
  3. el efecto de *k* en la validación cruzada (`d_cv`);
  4. un simulador de bagging y random forest con error OOB (`bagging`, `rf`);
  5. las regiones de un árbol junto con la curva de error frente al número de hojas (`arbol_reg`);
  6. la sigmoide frente a la recta, con el umbral (`logit`, `mpl`);
  7. las pérdidas asimétricas, con el problema del vendedor de periódicos (`d_deseq`);
  8. MAE frente a MSE con un atípico que se arrastra (`d_mreg`).

## 2. Licencias y condiciones de uso

| Repositorio | Licencia | Consecuencia práctica |
|:--|:--|:--|
| `MachineLearningDemos` | CC BY-SA 4.0 | Copiar o adaptar su código o su texto obliga a publicar la obra derivada con la misma licencia. Reimplementar la idea desde cero, citando la fuente de inspiración, evita esa obligación. |
| `PythonNumericalDemos` | MIT (© 2018 M. Pyrcz) | Se puede adaptar el código conservando el aviso de copyright. |
| `MachineLearningCourse` | MIT para el repositorio (© 2022 M. Pyrcz) | Cada proyecto es obra de su estudiante, así que conviene citar al autor aunque solo se tome la idea. |

Excepciones dentro de `MachineLearningCourse`:
- Ali Mohamed (`Robust_regression`, 2023) pide de forma expresa que se le consulte antes de usar su trabajo fuera de clase.
- Laide Ojomo (2020) pedía no difundir su proyecto hasta diciembre de 2021. Además, trata de geotecnia, fuera del temario.

**Recomendación:** escribir los simuladores desde cero en JavaScript, con datos sintéticos, y añadir en cada uno una línea de crédito, por ejemplo «Idea inspirada en M. Pyrcz, *PythonNumericalDemos* (MIT)».

## 3. Criterios usados

- **Encaje:** un simulador debe ilustrar un estimador o una decisión transversal del mapa, con los mismos nombres (ids de nodo entre comillas invertidas).
- **No duplicar lo que ya existe:**
  - la slide «Elige el grado» del tema 1;
  - los dos simuladores de boosting del tema 4;
  - las celdas de Pyodide de los decks de los temas 2 y 4.
- **Viabilidad en el navegador:**
  - **Alta:** cálculo cerrado o barato, de 0,5 a 1,5 días.
  - **Media:** hay que programar un algoritmo como un árbol CART, un SVM o un Shapley exacto, de 2 a 4 días.
  - **Baja:** depende de librerías pesadas (shap, TensorFlow) o de datos no disponibles.
- **Esfuerzo:** jornadas de una persona, sin contar la revisión pedagógica ni la redacción de textos.

## 4. Propuestas por nodo del mapa

Prioridad 1 = mucho valor y poco esfuerzo. Prioridad 3 = interesante pero secundario o en un tema provisional.

| Prior. | Nodo(s) | Simulador propuesto | Fuentes de inspiración | Viab. | Esfuerzo |
|:-:|:--|:--|:--|:-:|:-:|
| 0 | `gb`, `xgb` | Enlazar los simuladores que ya existen | `slides/04/simuladores/*.html` | — | 0,5 d |
| 1 | `ridge`, `mco`, `d_sesgo` | Varianza de MCO frente a Ridge con bootstrap | Demo ridge (§ Model Variance); Aldossary 2025b; Gomaa 2021 | Alta | 1–1,5 d |
| 1 | `ridge`, `lasso`, `enet`, `d_train` | Geometría de la pérdida penalizada en el plano (β₁, β₂) | `Interactive_Linear_Solutions` | Alta | 1–1,5 d |
| 1 | `lasso`, `enet`, `d_prep`, `d_hiper` | Traza de coeficientes frente a λ, con mezcla y casilla «estandarizar» | `Interactive_LASSO_Regression`; demo LASSO; Cotia 2025 | Alta | 1,5–2 d |
| 1 | `d_cv`, `d_hiper` | Efecto de *k*: media y error típico del error de validación cruzada | Dillon Luke 2021; `Interactive_Confidence_Interval` | Alta | 1,5 d |
| 1 | `bagging`, `rf`, `d_cv` | Bootstrap, número de árboles, `max_features`, error OOB y modelo base | Demo ensemble_trees; `SubsurfaceDataAnalytics_EnsembleTrees`; Bettir 2025; Isikdogan 2025b; Saif Alkaabi 2020 | Alta (1D) / Media (2D) | 2–3 d |
| 1 | `arbol_reg`, `d_hiper` | Regiones del árbol y error de entrenamiento y test frente al número de hojas | `Interactive_Decision_Tree`; demo decision_tree | Media | 2 d |
| 1 | `logit`, `mpl`, `nulo`, `d_mclas` | Recta frente a sigmoide, y umbral con la matriz de confusión | Bernard Chang 2021; `Interactive_Model_Fitting` (idea de verosimilitud) | Alta | 1–2 d |
| 1 | `d_deseq`, `d_mclas` | Costes asimétricos y tasa base: vendedor de periódicos, umbral y fraude | `Interactive_DecisionMaking`; `Interactive_Bayesian_Updating` | Alta | 1 d |
| 1 | `d_mreg`, `mco` | MAE frente a MSE frente a Lᵖ con un atípico que se arrastra | `Interactive_Norms`; idea genérica de Ali Mohamed 2023 | Alta | 0,5–1 d |
| 2 | `d_train` | Descenso del gradiente: tasa, momento, tamaño de lote y trayectoria | `Interactive_Optimization`; Visessumon 2025b | Alta | 1–1,5 d |
| 2 | `arbol_clas`, `d_hiper` | Poda por coste-complejidad, con la regla del error típico | Olin Carty 2021 | Media | 2–3 d |
| 2 | `svc` (y `svr`) | C, γ, núcleo, estandarizar, etiquetas erróneas y patrones de datos | Barun Das 2023; Samarkin 2023; demo SVM; Ruoyu Li 2021 | Media | 3–4 d |
| 2 | `d_interp` | Dependencia parcial (PDP/ICE) frente a Shapley, en tres escenarios | Suin Choi 2025b; `Interactive_Shapley_Values` | Media | 3–4 d |
| 2 | `d_part` | Tres fugas: seleccionar variables antes de validar, elegir λ con el test y extrapolar | `Interactive_Spurious_Correlations`; Luciano 2022; Cotia 2025; `PythonDataBasics_Pipelines` | Alta | 1,5–2 d |
| 2 | `d_hiper` | Búsqueda en rejilla frente a búsqueda aleatoria sobre una superficie sintética | Yoon 2022; Ivan Feng 2022; Alhadi 2022 | Alta | 1 d |
| 2 | `mco`, `poli` | «¿Lineal en qué?»: elegir funciones base | Derek Burmaster 2021 | Alta | 1,5 d |
| 2 | `mco` | Incertidumbre de los coeficientes: rectas bootstrap según *n* | Haojun Xia 2023; Yuanrui Zhu 2022 | Alta | 1 d |
| 3 | `poli`, `d_sesgo` | Complemento de «Elige el grado»: curvas bootstrap y error con bandas | `Interactive_Overfit`; Xuesong Ma 2025; Molitor 2022 | Alta | 1 d |
| 3 | `mlp` (provisional) | Red construida a mano y red entrenable con curvas de pérdida | `Interactive_NeuralNetwork_SingleLayer`; `SubsurfaceDataAnalytics_ANN` | Alta / Media | 1–3 d |
| 3 | `xgb`, `d_deseq` | Desequilibrio y `scale_pos_weight` | Omar Abukassab 2025 | Media | 2 d |
| 3 | `gb` | Selector de pérdida (L2, L1, Huber) con atípicos en el simulador existente | Chuxi Liu 2021 | Media | 1 d |

Nodos sin candidato en estos repositorios: `multinomial`, `gamma`, `poisson`, `voting`, `stacking` y `doubleml`. El `nulo` no necesita simulador propio, porque puede aparecer como línea de referencia en los demás.

## 5. Fichas de las propuestas

Cada ficha resume qué hace la fuente, qué mostraría el simulador y con qué ejemplo. Las extensiones que no están en las fuentes se marcan como *propuesta*.

### 5.0 `gb` y `xgb`: enlazar lo que ya existe

- `gbm_boosting.html` tiene sliders de número de árboles, tasa de aprendizaje y profundidad, con la predicción y las curvas de RMSE de entrenamiento y validación. Acepta `?arboles=12&tasa=0.3&prof=2`.
- `xgboost_penalizacion.html` tiene sliders de árboles, λ y γ, con la ganancia de cada corte. Acepta `?arboles=10&lambda=0&gamma=0`.
- **Acción posible:** que los botones «Simular» de `gb` y `xgb` abran esos archivos en una ventana nueva. Varios cuadernos de los repositorios (demo gradient_boosting, Ethan Conrad, Berit Hudson, Tapiang) duplican estos simuladores y no aportan nada nuevo.

### 5.1 `ridge` · `mco` · `d_sesgo`: varianza de MCO frente a Ridge

- **Fuentes:**
  - **Demo ridge** (sección «Model Variance»): remuestras bootstrap de *n* = 20 para cada λ, y la dispersión de las rectas en función de λ.
  - **Aldossary** (2025b): 16 observaciones de entrenamiento, 200 réplicas y λ ∈ {0; 0,1; 1; 10; 100}. Muestra cajas de las predicciones en puntos fijos y un mapa de calor de la desviación típica de cada coeficiente.
  - **Gomaa** (2021): sesgo, varianza y ruido frente a λ.
- **Simulador:** sliders de log λ y de *n*. Muestra un abanico de unas 50 rectas o predicciones bootstrap, que se cierra al subir λ, la desviación típica de cada coeficiente y una descomposición sesgo² + varianza + ruido frente a λ.
- **Ejemplo:** las ventas de 20 tiendas frente a 6 variables correlacionadas (superficie, empleados, aparcamiento…).
- **Viabilidad:** alta. Ridge tiene solución cerrada, (XᵀX + λI)⁻¹Xᵀy.
- **Cuidado:** Aboahmed (2023) calcula mal la varianza, porque la mide entre puntos de una sola réplica y no entre réplicas. No conviene tomar su código.

### 5.2 `ridge` · `lasso` · `enet` · `d_train`: geometría de la penalización

- **Fuente:** `Interactive_Linear_Solutions`. Con 2 predictores dibuja contornos del RSS, de la penalización y de la pérdida total en el plano (β₁, β₂), y la trayectoria de la solución al variar λ.
  - Tiene tres sliders: λ de Ridge (escala log 10¹–10⁶), λ de LASSO (lineal 10–3000) y «λ level» (1–20) para compararlos.
  - Usa datos sintéticos (*n* = 50, y = 3x₁ + 2x₂ + ruido).
- **Simulador:** sliders de λ y de la mezcla α (*propuesta*, para cubrir `enet`), y slider de la correlación entre x₁ y x₂ (*propuesta*). Se ve el círculo, el rombo y la forma intermedia, y el punto donde LASSO toca el eje y anula un coeficiente.
- **Ejemplo:** ventas frente a gasto en televisión y gasto en radio, dos predictores correlacionados.
- **Viabilidad:** alta. Basta una rejilla de 100 × 100 y contornos dibujados a mano o con d3-contour.
- **Nota:** algunos títulos del cuaderno dicen «Ridge» en paneles de LASSO, por un error de copia.

### 5.3 `lasso` · `enet` · `d_prep` · `d_hiper`: traza de coeficientes

- **Fuentes:**
  - **`Interactive_LASSO_Regression`:** sliders de *n*, % de test, ruido y λ (10⁻⁵–10⁵). Muestra el MSE de entrenamiento y de test frente a λ con bandas de 20 particiones, y la trayectoria de los coeficientes.
  - **Demo LASSO:** la traza con predictores estandarizados.
  - **Cotia** (2025): base polinómica de grado 8 que LASSO poda hasta dejar un cúbico.
- **Simulador:** sliders de log λ y de la mezcla. Traza de coeficientes con la λ actual marcada, error de validación cruzada con la regla del error típico (*propuesta*) y una casilla «estandarizar dentro del Pipeline».
- **Ejemplo:** qué variables explican las ventas de una tienda (precio, promoción, temperatura, tráfico web y cuatro variables de ruido).
- **Contraejemplo útil para `d_prep`:** el panel del cuaderno se titula «Standardized Model Coefficients», pero el código no estandariza antes de ajustar. El orden en que LASSO anula los coeficientes depende entonces de las unidades. Esto está comprobado en el código.
- **Contraejemplo útil para `d_part`:** Cotia elige λ mirando el error de test.
- **Viabilidad:** alta. LASSO y Elastic Net por descenso por coordenadas ocupan unas 40 líneas.

### 5.4 `d_cv` · `d_hiper`: efecto de *k* y error típico

- **Fuentes:**
  - **Dillon Luke** (2021): para *k* de 2 a *n* (LOO), repite la validación cruzada 10 veces con otro reparto y mide la media y la varianza del MSE, con MCO y con Ridge. Recomienda *k* entre 5 y 20. Está comprobado en el código: usa `KFold(shuffle=True)` en un bucle de L repeticiones.
  - **`Interactive_Confidence_Interval`:** el error típico y el intervalo de una media.
- **Simulador:** slider de *k* y de ruido, y un botón «repetir 20 veces». Muestra el error medio ± error típico entre repeticiones, la partición coloreada por pliegue y la curva de error frente a un hiperparámetro con la regla del error típico.
- **Ejemplo:** previsión del gasto mensual de clientes.
- **Viabilidad:** alta. Con MCO o Ridge en forma cerrada, incluso LOO es barato.

### 5.5 `bagging` · `rf` · `d_cv`: bootstrap, OOB y decorrelación

- **Fuentes:**
  - **Demo ensemble_trees** y **`SubsurfaceDataAnalytics_EnsembleTrees`:** árboles bootstrap, promedio progresivo, error OOB e importancia.
  - **Bettir** (2025): error OOB y correlación media entre las predicciones de los árboles frente a `max_features`.
  - **Isikdogan** (2025b), interactivo: bagging con modelos base distintos, y la idea de que solo ayuda a modelos con varianza.
  - **Prez** (2021) y **Haojun Xia** (2023): el bagging de MCO no mejora.
  - **Saif Alkaabi** (2020), interactivo: distribución bootstrap de un estadístico.
- **Simulador, en tres pestañas:**
  1. **Qué es una remuestra bootstrap:** qué filas se repiten y cuáles quedan fuera, alrededor del 36,8 %.
  2. **Bagging:** número de árboles, profundidad y modelo base (árbol profundo o MCO), con las curvas de error de test y OOB frente al número de árboles.
  3. **Random forest:** slider de `max_features` (mtry) de 1 a p, con el error OOB, la correlación media entre árboles y la fórmula ρσ² + (1 − ρ)σ²/B.
- **Ejemplo:** ventas diarias frente a temperatura (1D), y precio de alquiler frente a m² y distancia al centro (2D).
- **Viabilidad:** alta en 1D y media en 2D. Puede reutilizar el árbol de regresión que ya está programado en `gbm_boosting.html`.

### 5.6 `arbol_reg` · `d_hiper`: regiones del árbol

- **Fuentes:**
  - **`Interactive_Decision_Tree`:** un slider de `max_leaf_nodes` (2–150). Muestra el mapa de regiones con la predicción de cada hoja, el gráfico de predicho frente a real y el MSE de entrenamiento y de test frente al número de hojas.
  - **Demo decision_tree:** la misma idea, con la extracción de reglas.
  - **`DT_Demo` y `Experiential_DecisionTree`:** el árbol escrito como reglas «si… entonces».
- **Simulador:** slider de número de hojas, mapa de regiones 2D, curva de error con el punto actual y el árbol escrito como reglas legibles, que conecta con `d_interp`.
- **Ejemplo:** ventas frente a precio y gasto en promoción, con un precio óptimo intermedio.
- **Viabilidad:** media. Hay que programar un CART con crecimiento *best-first*, que es lo que hace scikit-learn con `max_leaf_nodes`. Unos 2 días.

### 5.7 `logit` · `mpl` · `nulo` · `d_mclas`: recta frente a sigmoide

- **Fuentes:**
  - **Bernard Chang** (2021): logit frente a un modelo de referencia, con un botón que alterna «sigmoide» y «lineal», F1 y la matriz de confusión. Usa datos deportivos de Kaggle, no de subsuelo.
  - **`Interactive_Model_Fitting`:** la idea de ajustar por máxima verosimilitud, con la verosimilitud de cada dato a la vista, aplicada en el cuaderno a una gaussiana.
- **Simulador:** un conmutador MPL / logit, en el que la recta se sale de [0, 1] y la sigmoide no, y sliders de β₀ y β₁ con la log-verosimilitud de cada cliente (*propuesta*). Un slider de umbral con la matriz de confusión, la precisión, la sensibilidad y F1, comparadas con el clasificador nulo.
- **Ejemplo:** conversión de un cliente potencial según su número de visitas.
- **Viabilidad:** alta. El logit se ajusta por IRLS o por descenso del gradiente.

### 5.8 `d_deseq` · `d_mclas`: costes asimétricos y tasa base

- **Fuentes:**
  - **`Interactive_DecisionMaking`:** sliders de μ y σ de la incertidumbre, y de la pendiente y el exponente de la pérdida por infraestimar y por sobreestimar. Muestra la pérdida esperada frente a la estimación y marca el óptimo, que con una pérdida lineal asimétrica es un cuantil.
  - **`Interactive_Bayesian_Updating`:** sliders de la tasa base, la sensibilidad y la tasa de falsos positivos, para calcular P(H | +).
- **Simulador, en tres pestañas:**
  1. **El vendedor de periódicos:** demanda incierta, coste de quedarse sin existencias y coste del sobrante. La cantidad óptima es el cuantil crítico c_u / (c_u + c_o).
  2. **Umbral óptimo de clasificación** con costes FN y FP (*propuesta*), que conecta con la fórmula C_FP / (C_FP + C_FN) del mapa.
  3. **Fraude con una tasa base del 0,5 %:** matriz de confusión para 10 000 transacciones y la precisión que resulta.
- **Viabilidad:** alta, alrededor de 1 día.
- **Complemento posible:** ponderar las clases frente a mover el umbral (Haoyu Wang 2022 y Omar Abukassab 2025, con random forest y XGBoost). Se puede hacer con un logit para no necesitar árboles.

### 5.9 `d_mreg` · `mco`: qué pérdida y qué métrica

- **Fuente:** `Interactive_Norms`. Sliders de la p de la norma (0,1–10), de *n*, del ruido y de la posición (x, y) de un punto añadido. Dibuja las rectas L1, L2, L3 y Lᵖ.
- **Simulador:** el usuario arrastra un pedido anómalo y ve a la vez las rectas MSE, MAE y Huber, con una tabla de RMSE, MAE y R² de cada una. Mensaje: la pérdida que se optimiza decide la recta, y la métrica que se comunica debe ser coherente con ella.
- **Ejemplo:** tiempo de entrega frente a distancia.
- **Viabilidad:** alta. La recta L2 tiene solución cerrada, y las demás se ajustan con IRLS o Nelder-Mead.
- **Aviso:** la idea de la regresión robusta aparece también en Ali Mohamed (2023), que pide permiso para reutilizar su trabajo. MAE y Huber son métodos estándar, así que no hace falta su método MFV.

### 5.10 `d_train`: descenso del gradiente

- **Fuentes:**
  - **`Interactive_Optimization`:** animación del descenso del gradiente con momento y decaimiento de la tasa sobre una superficie con mínimos locales. No tiene sliders: los parámetros están fijos en el código.
  - **Visessumon** (2025b): lote completo frente a minilotes frente a descenso estocástico, con varias tasas.
- **Simulador:** sliders de tasa (en escala log), momento, decaimiento y tamaño de lote (1, 8, 32 o *n*), y clic para elegir el punto de inicio. Muestra la trayectoria sobre las curvas de nivel y la pérdida por epoch. Un selector de superficie permite elegir entre una convexa (logit) y otra con mínimos locales (red neuronal).
- **Viabilidad:** alta.

### 5.11 `arbol_clas` · `d_hiper`: poda por coste-complejidad

- **Fuente:** Olin Carty (2021). Usa `cost_complexity_pruning_path` y muestra la exactitud de entrenamiento y de test frente a `ccp_alpha`: de 973 hojas pasa a 120 con el α óptimo.
- **Simulador:** slider de α, frontera rectangular, número de hojas y curva de exactitud o de log-loss frente a α con la regla del error típico.
- **Ejemplo:** impago de un crédito según la renta y la ratio de deuda.
- **Viabilidad:** media. Hay que programar un CART de clasificación con Gini y la poda de enlace más débil, que es la parte delicada.

### 5.12 `svc` (y `svr`): núcleos, C y γ

- **Fuentes:**
  - **Barun Das** (2023), interactivo: un slider de número de etiquetas erróneas (0–20) mueve la frontera y el margen de un SVC lineal con C = 1. Está comprobado en el código.
  - **Samarkin** (2023), con botones: núcleos lineal, sigmoide y RBF sobre círculos concéntricos, y la idea del «truco del núcleo».
  - **Demo SVM:** C, γ, el efecto de no estandarizar y la rejilla C × γ.
  - **Ruoyu Li** (2021): un selector de patrones de frontera (lineal, círculo, franjas, diagonal).
- **Simulador:** selector de núcleo, sliders de C y γ, selector de patrón de datos, casilla «estandarizar» y slider de etiquetas erróneas. Muestra la frontera, el margen y los vectores de soporte.
- **Ejemplo:** clientes que abandonan o se quedan, según su uso y su antigüedad.
- **Viabilidad:** media. Requiere un SMO simplificado, que es viable con *n* ≤ 300. El mismo motor serviría para un simulador de `svr` con la anchura del tubo ε (*propuesta*; no hay fuente específica).

### 5.13 `d_interp`: dependencia parcial frente a Shapley

- **Fuentes:**
  - **Suin Choi** (2025b), con datos sintéticos de fórmula conocida. Tres escenarios:
    - predictores independientes, Y = 2X₁ + 5X₂;
    - predictores correlacionados, X₂ = 0,8X₁ + 0,2U;
    - con interacción, Y = 2X₁ + 5X₂ + 10X₁X₂.

    En los tres compara la dependencia parcial (PDP) con la dependencia Shapley, y muestra que la PDP no deja ver la interacción.
  - **`Interactive_Shapley_Values`:** sliders de b₁, b₂, ρ, ruido, número de hojas y número de árboles. Usa `shap` y scikit-learn.
  - **Abraham Montes** (2022): el orden de importancia cambia según el modelo.
- **Simulador:** selector de escenario y slider de la fuerza de la interacción. A un lado, la PDP y las curvas ICE; al otro, la dependencia Shapley coloreada por X₂.
- **Ejemplo:** probabilidad de compra frente a descuento y antigüedad, cuando el descuento solo funciona con clientes nuevos.
- **Viabilidad:** media. Con 2 a 4 predictores, el valor de Shapley exacto se obtiene recorriendo todos los subconjuntos con un conjunto de fondo, sin necesidad de TreeSHAP.

### 5.14 `d_part`: tres formas de engañarse

- **Fuentes:**
  - **`Interactive_Spurious_Correlations`:** con pocas observaciones aparecen correlaciones altas entre variables independientes.
  - **Luciano** (2022): el error de un polinomio se dispara fuera del rango de entrenamiento, mientras que un árbol se queda plano.
  - **Cotia** (2025): elegir λ mirando el test.
  - **`PythonDataBasics_Pipelines`:** el flujo «a mano» estandariza con todos los datos antes de la validación cruzada. El cuaderno no lo presenta como fuga.
- **Simulador, en tres pestañas** (la segunda parte de cada una es *propuesta*):
  1. **Seleccionar los 5 «mejores» de 50 KPIs sin relación real** usando todos los datos, y comprobar que en datos nuevos no predicen nada.
  2. **Elegir λ con el test** o con validación cruzada, y comparar el error que se comunica con el error real.
  3. **Predecir la demanda con precios nunca vistos:** extrapolación con un polinomio frente a un árbol.
- **Viabilidad:** alta.

### 5.15 `d_hiper`: rejilla frente a búsqueda aleatoria

- **Fuentes:** Yoon (2022) e Ivan Feng (2022) comparan la búsqueda en rejilla, la aleatoria y la bayesiana. Alhadi (2022) compara el ajuste de un hiperparámetro cada vez con la búsqueda conjunta.
- **Simulador:** una superficie analítica de error de validación sobre (log tasa, número de árboles) y un presupuesto de N evaluaciones. Se ve que la búsqueda aleatoria explora mejor cuando un hiperparámetro importa poco, y que el camino «de uno en uno» no llega al óptimo conjunto.
- **Viabilidad:** alta, porque no entrena modelos.

### 5.16 `mco` · `poli`: funciones base e incertidumbre

- **Funciones base.** Fuente: **Derek Burmaster** (2021), interactivo. Unos 19 sliders construyen la función verdadera y 13 casillas eligen las funciones base de la regresión. Comprobado en el código.
  - *Simulador:* «¿lineal en qué?». La demanda verdadera es a + b·ln(precio), y el alumno marca bases (x, x², ln x, 1/x) para ver el ajuste y el error de test. Enseña que «lineal» se refiere a los parámetros.
- **Incertidumbre de los coeficientes.** Fuentes: **Haojun Xia** (2023) y **Yuanrui Zhu** (2022). Muestran rectas bootstrap e histogramas de la pendiente según *n*, y Zhu compara remuestrear observaciones con remuestrear residuos.
  - *Simulador:* sliders de *n* y de número de réplicas, casillas «atípico» y «heterocedasticidad». Muestra el intervalo analítico frente al bootstrap.
- **Viabilidad:** alta en los dos casos.

### 5.17 Prioridad 3

- **`poli` y `d_sesgo`, complemento de «Elige el grado».** Fuentes: `Interactive_Overfit`, Xuesong Ma (2025) y Molitor (2022).
  - `Interactive_Overfit` tiene sliders de *n*, % de test, ruido y grado, y muestra el error de entrenamiento y de test frente al grado con bandas de 20 particiones.
  - *Simulador:* curvas bootstrap y bandas de error, en lugar de otro slider de grado.
  - *Aviso:* Molitor llama «bootstrap» a lo que son particiones, y calcula la varianza sobre el error de entrenamiento.
- **`mlp`, provisional.** Fuentes:
  - `Interactive_NeuralNetwork_SingleLayer`: sliders de funciones de activación, de pesos y sesgos a mano, y de una red de Keras con anchura, capas, tasa y épocas;
  - `SubsurfaceDataAnalytics_ANN`: una red 3-2-1 con retropropagación escrita a mano.

  *Simulador:* uno para construir la red a mano y otro para entrenarla con curvas de pérdida y parada temprana. Conviene esperar al deck del tema 6.
- **`xgb` y `d_deseq`.** Fuente: Omar Abukassab (2025), con `scale_pos_weight` y un umbral desequilibrado. Mejor integrarlo en la ficha 5.8.
- **`gb`.** Fuente: Chuxi Liu (2021), con pérdidas L2, L1 y cuantil. *Idea:* añadir un selector de pérdida con atípicos al simulador `gbm_boosting.html` que ya existe.

## 6. Motores comunes en JavaScript

Varios simuladores comparten cálculo. Programar estos motores una vez, en un archivo común, reduce el esfuerzo total.

| Motor | Lo usan | Notas |
|:--|:--|:--|
| Generador aleatorio con semilla y datos sintéticos de negocio | Todos | Reproducibilidad: la misma semilla da los mismos datos en clase. |
| MCO y Ridge en forma cerrada (con QR o Cholesky) | 5.1, 5.3, 5.4, 5.9, 5.14, 5.16, 5.17 | Centrar y escalar x en los polinomios de grado alto. |
| LASSO y Elastic Net por descenso por coordenadas | 5.2, 5.3, 5.14 | Unas 40 líneas. |
| Árbol CART de regresión y de clasificación, *best-first* | 5.5, 5.6, 5.11, 5.13, 5.14 | `gbm_boosting.html` ya contiene un árbol de regresión que se puede reutilizar. |
| Bootstrap y error OOB | 5.1, 5.5, 5.16 | Trivial. |
| Logit (IRLS o descenso del gradiente) | 5.7, 5.8, 5.10 | — |
| SVM con SMO simplificado | 5.12 | El más costoso. |
| Shapley exacto, PDP e ICE | 5.13 | Exponencial en p, pero p ≤ 4. |
| Gráficos | Todos | SVG o canvas propios, con la misma paleta y la misma tipografía que el mapa y los simuladores del tema 4. |

**Forma de integrarlos en el mapa:** cada simulador como una página HTML aparte, como los del tema 4, a la que el botón «Simular» del nodo enlaza con `data-simulador`. Así el mapa sigue siendo un único archivo ligero.

## 7. Contraejemplos útiles para las fichas

Algunos cuadernos contienen errores que pueden servir de ejemplo en clase o en las fichas de decisiones:

| Error | Dónde | Nodo |
|:--|:--|:--|
| Gráfico titulado «Standardized Model Coefficients» sin estandarizar antes de LASSO | `Interactive_LASSO_Regression` (comprobado) | `d_prep` |
| λ elegido mirando el error de test | Cotia 2025 | `d_part`, `d_hiper` |
| Escalado aprendido con todos los datos antes de la validación cruzada | `PythonDataBasics_Pipelines` | `d_prep`, `d_part` |
| `cross_val_score` aplicado al conjunto de test | `Interactive_NeuralNetwork_SingleLayer` | `d_cv` |
| Varianza «del modelo» calculada entre puntos de una réplica, en lugar de entre réplicas | Aboahmed 2023 | `d_sesgo` |
| «Bootstrap» que en realidad son particiones train/test | Molitor 2022 | `bagging`, `d_cv` |
| «Más árboles sobreajusta» en un random forest | Cerro 2023 (afirmación dudosa) | `rf` |

## 8. Descartados

- **Fuera del temario:**
  - geoestadística (kriging, variogramas, desagrupamiento, simulación espacial);
  - clustering y reducción de dimensión (PCA, MDS, UMAP, k-means, DBSCAN, GMM…);
  - redes profundas (CNN, GAN, LSTM, U-Net, FNO);
  - MCMC y regresión bayesiana;
  - kNN, naive Bayes, LDA, MARS y regresión isotónica.
- **Estadística básica:** teorema central del límite, contrastes, distribuciones y gráficos Q-Q o P-P. Pueden servir de contexto, pero no corresponden a ningún nodo.
- **Duplicados de los simuladores del tema 4:** los cuadernos de gradient boosting de Pyrcz, Ethan Conrad, Berit Hudson y Preeda Tapiang.
- **No reproducibles:** proyectos que leen archivos locales del autor, como Sadam Hussain, Bruno Reinoso o el de Bettir (de este se aprovecha la idea, no los datos).
- **Duplicados exactos:** `Feras_Alsheikh.ipynb` (idéntico a `RandomForestHyperparameters_Feras_Alsheikh.ipynb`) y `Haojun Xia.ipynb` (idéntico a `LinearBagging_Haojun Xia.ipynb`).

## 9. Límites del análisis

- No se ejecutó ningún cuaderno. Lo que se dice de los gráficos se deduce del código, no de ver las figuras.
- Las cifras que se atribuyen a los autores («según el autor») salen de su texto y no se han reproducido.
- **Comprobaciones directas en el código:**
  - los controles de `Interactive_Linear_Solutions`, Barun Das, Derek Burmaster y Dillon Luke;
  - el título sin estandarización de `Interactive_LASSO_Regression`;
  - la petición de permiso de Ali Mohamed;
  - que `Interactive_Shapley_Values` usa `shap` y un `RandomForestRegressor`.

  El resto procede de la lectura de tres agentes de análisis, cuyos informes detallados se citan abajo.
- Algunos cuadernos usan una versión antigua de scikit-learn (`loss='ls'`, `criterion='mse'`, `base_estimator`) y hoy no funcionarían sin cambios. Esto no afecta a las ideas.

## Anexos: informes detallados

Una ficha por cuaderno, con controles, datos, nodos y viabilidad, en la carpeta [`geostatsguy/`](geostatsguy/):
- [`hallazgos_PythonNumericalDemos.md`](geostatsguy/hallazgos_PythonNumericalDemos.md): `PythonNumericalDemos`, unas 40 fichas.
- [`hallazgos_MachineLearningDemos_proyectos_2020_2022.md`](geostatsguy/hallazgos_MachineLearningDemos_proyectos_2020_2022.md): `MachineLearningDemos` y los proyectos de 2020 a 2022.
- [`hallazgos_proyectos_2023_2025.md`](geostatsguy/hallazgos_proyectos_2023_2025.md): proyectos de 2023, 2025 y 2025b.

Los informes se redactaron con un resumen automático de los cuadernos (`nbsum.json`) que no se guarda en el repositorio. Los repositorios analizados están en `https://github.com/GeostatsGuy/` y se clonaron el 2-11-2026.
