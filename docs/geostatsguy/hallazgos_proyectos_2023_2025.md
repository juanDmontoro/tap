# Hallazgos: proyectos finales PGE 383 (Pyrcz) — 2023, 2025 y 2025b

Fuente: clon local de `GeostatsGuy/MachineLearningCourse` (licencia MIT del repositorio; **cada cuaderno es obra de su autor**, que se cita en cada ficha). Revisados por extracción del JSON con `python3 -I` (celdas markdown + código, búsqueda de `interact`/ipywidgets y de las llamadas de gráfico). **No se ejecutó ningún cuaderno**, así que los resultados numéricos citados son los que los autores escriben en sus markdown, no comprobados.

Formato común (README + `PGE383_ProjectTemplate.ipynb`): flujo «educativo» con Executive Summary, Import, Functions, Load Data, pasos numerados y Results. La mayoría usa los CSV sintéticos de subsuelo de Pyrcz (`unconv_MV*.csv`: Por, Perm, AI, Brittle, TOC, VR → Prod). **En las carpetas 2023/2025/2025b no hay ningún CSV incluido** (solo .ipynb y 3 ficheros R): los datos se cargan por URL o, en varios casos, desde rutas locales del autor que no son reproducibles.

Avisos generales:
- Casi ningún cuaderno es interactivo. Solo 5 de los relevantes usan ipywidgets (Barun Das, Samarkin, Suatcan Isikdogan, Dadzie; Sultan Dwier fuera de temario).
- Todos los gráficos son matplotlib/seaborn estáticos; la «portabilidad» a JS es siempre una reimplementación del concepto, no una traducción de código.
- Duplicados exactos de celdas: `Feras_Alsheikh.ipynb` = `RandomForestHyperparameters_Feras_Alsheikh.ipynb` (45/45 celdas iguales); `Haojun Xia.ipynb` = `LinearBagging_Haojun Xia.ipynb` (26/26). `OverfitRandomForest_Dalma_Cerro` y `OverfitRandomForestML_Dalma_Cerro` son dos versiones del mismo proyecto (48 frente a 36 celdas, mismo guion).

Leyenda de viabilidad JS: **Alta** = cálculo cerrado o barato, 1–3 días; **Media** = hay que implementar árboles/SVM/boosting pequeños o precalcular curvas, 3–6 días; **Baja** = depende de datos no disponibles, de cómputo pesado o de librerías sin equivalente razonable.

---

## Top 8 (resumen)

| # | Cuaderno (autor) | Nodos | Viabilidad | Por qué |
|---|---|---|---|---|
| 1 | ModelVarianceReduction (Abdulaziz Aldossary, 2025b) | ridge, mco, d_sesgo | Alta | Bootstrap de MCO frente a Ridge con muestra pequeña: varianza de predicción y de coeficientes frente a α. Cálculo cerrado. |
| 2 | ModelVariance (Xuesong Ma, 2025) | poli, d_sesgo | Alta | Bandas bootstrap de un polinomio de grado 3 frente a 6 con datos sintéticos; complementa «Elige el grado». |
| 3 | Partial_Dependence_Plot_vs_SHAP (Suin Choi, 2025b) | d_interp, rf | Media | Tres escenarios sintéticos con fórmulas explícitas (independiente, correlación, interacción): muestra cuándo engaña la PDP. |
| 4 | TreeDecorrelation (Nassima Bettir, 2025) | rf, bagging, d_cv (OOB) | Media | Error OOB y correlación media entre árboles frente a `max_features`: el mecanismo de RF frente a bagging. |
| 5 | Outliers_SupportVectorMachines (Barun Das, 2023) | svc | Alta | Ya interactivo: un slider de etiquetas erróneas mueve la frontera y el margen de un SVC lineal. |
| 6 | StudyDiffKernelsSVM (Yevgeniy Samarkin, 2023) | svc | Media | Botones lineal/sigmoide/RBF sobre círculos concéntricos, con vista 3D del «kernel trick». |
| 7 | FastGradientBoosting (David Dadzie, 2025b) | xgb, d_train, d_part | Alta (curvas precalculadas) / Media | Tasa de aprendizaje con parada temprana y curvas train/val; datos de negocio (ingresos de películas TMDB). |
| 8 | SGDvsBGD (Saris Visessumon, 2025b) + Robust_regression (Ali Mohamed, 2023) | d_train, mco | Alta | Tamaño de lote y tasa en el descenso del gradiente, y elección de la pérdida frente a atípicos. Solo se reimplementa el concepto. |

Otros buenos candidatos: LinearBagging (Haojun Xia), FeatureImportanceWrapperFunctions (Eric Hu), PolRegwShrinkage (Danielle Cotia), BaggingWithNonTreeModels (Suatcan Isikdogan), XGBoost (Omar Abukassab), Overfit_RandomForest (Sujin Park).

---

## Fichas — 2023_MLProjects

### Bias-variance_Trade-off_Jiaqi_Du.ipynb
- **Título / autor:** «Bias-variance trade-off for decision tree regressor» — Jiaqi Du.
- **Qué enseña:** descompone el error esperado en sesgo² y varianza con `mlxtend.evaluate.bias_variance_decomp` (pérdida MSE) para árbol, bagging y random forest, con profundidad máxima de 1 a 20 y número de árboles {1, 5, 10, 20}. En un segundo paso compara bagging (10 árboles) con gradient boosting para las tasas 0,2/0,4/0,6/0,8. El autor concluye que la tasa de aprendizaje «afecta sobre todo a la varianza» del boosting.
- **Interactividad:** no interactivo. Gráficos de líneas: pérdida, sesgo y varianza frente a profundidad, una curva por modelo.
- **Datos:** CSV `unconv_MV.csv` por URL; 250 filas de entrenamiento y 50 de test; Por y Brittle → Production.
- **Nodos:** d_sesgo (descomposición explícita), arbol_reg, bagging, rf, gb.
- **¿Duplica?** No hay en la asignatura una descomposición sesgo/varianza para árboles; «Elige el grado» la sugiere para polinomios, pero sin cuantificarla.
- **Viabilidad JS:** Media (3–4 días): árbol CART 1D/2D en JS + bootstrap repetido (≈100 réplicas × 20 profundidades es asumible con n≈250).
- **Adaptación «Simular»:** en arbol_reg, bagging y rf: slider de profundidad y selector de modelo; curvas de sesgo², varianza y error total que se actualizan. Ejemplo: predecir el gasto mensual de un cliente a partir de su antigüedad y del número de visitas (datos sintéticos).

### BoostingClassification_Santiago_Callerio.ipynb
- **Título / autor:** «Boosting models compared for classification» — Santiago Callerio.
- **Qué enseña:** AdaBoost frente a XGBoost en clasificación («¿lloverá mañana?»). Imputa con KNNImputer, ajusta con CV de 5 particiones la profundidad (2–25), el número de estimadores (5–100) y la tasa (0,1–2), y termina con RandomizedSearchCV. Compara tiempos y matrices de confusión, y señala que la clase «lluvia» está desequilibrada y que en ella acierta «50/50».
- **Interactividad:** no interactivo. Curvas de exactitud train/test frente a cada hiperparámetro y heatmaps de confusión.
- **Datos:** `weatherAUS.csv` (Kaggle, datos meteorológicos reales), cargado desde el GitHub del autor.
- **Nodos:** gb, xgb, d_hiper, d_cv, d_mclas, d_deseq (la exactitud oculta el mal recall de la clase minoritaria), d_prep (imputación).
- **¿Duplica?** Parcialmente `gbm_boosting.html` en el efecto de la tasa y del número de árboles (no he visto el simulador; lo deduzco por el nombre). Aporta clasificación y desequilibrio.
- **Viabilidad JS:** Media (precalcular curvas) / Baja (entrenar en el navegador con ~140 000 filas).
- **Adaptación:** en d_deseq, «la exactitud engaña»: un slider de umbral sobre probabilidades precalculadas que muestra exactitud, recall y precisión. Ejemplo: predecir impago de facturas con un 20 % de positivos.

### Fast Gradient Boosting_Tapiang_Preeda_Tapiang.ipynb
- **Título / autor:** «Fast Gradient Boosting Methods» — Preeda Tapiang.
- **Qué enseña:** GradientBoostingRegressor frente a XGBRegressor, barriendo la tasa (0,01–2), el número de árboles (10–1000) y la profundidad, y midiendo «accuracy score» y tiempo de entrenamiento.
- **Interactividad:** no interactivo (líneas e histogramas).
- **Datos:** `unconv_MV_modified.csv` **local, no incluido** en el repo (no reproducible).
- **Nodos:** gb, xgb, d_hiper.
- **¿Duplica?** Sí, en gran parte: es el terreno de `gbm_boosting.html`/`xgboost_penalizacion.html`.
- **Viabilidad JS:** Baja en valor añadido. Descartable salvo como referencia.

### RandomForestHyperparameters_Feras_Alsheikh.ipynb (= Feras_Alsheikh.ipynb)
- **Título / autor:** «Effects on Random Forest Regression» — Feras Alsheikh.
- **Qué enseña:** parte de un RF base (profundidad 15, 300 árboles, 2 variables) y varía de una en una `min_weight_fraction_leaf`, el número de variables, `max_depth` y `n_estimators`, mostrando el error medio. Según el autor, el mínimo está en profundidad 6 y el número de árboles deja de aportar hacia los 40.
- **Interactividad:** no interactivo (curvas de error y superficies del modelo con `imshow`).
- **Datos:** `USA_Housing.csv` (Kaggle; precio de vivienda frente a ingresos y población de la zona), desde el GitHub del autor. Es de las pocas con datos «de negocio».
- **Nodos:** rf, d_hiper.
- **¿Duplica?** No en la asignatura.
- **Viabilidad JS:** Media (RF pequeño en JS con n≈1000 y 2 variables).
- **Adaptación:** en rf, cuatro sliders (profundidad, nº de árboles, mtry, tamaño mínimo de hoja) con la superficie de precio predicha y el error de test. Ejemplo: tasar una vivienda a partir de la renta y la densidad de la zona.

### LinearBagging_Haojun Xia.ipynb (= Haojun Xia.ipynb)
- **Título / autor:** «Bootstrap with Linear regression» — Haojun Xia.
- **Qué enseña:** remuestrea 105 puntos con reemplazo y ajusta MCO en cada réplica (10, 100 y 1000 réplicas). Dibuja las rectas bootstrap y los histogramas de pendiente y ordenada con los percentiles 5 y 95. Es la varianza del estimador hecha visible.
- **Interactividad:** no interactivo (el código repite el bloque con B = 10/100/1000).
- **Datos:** `Density_Por_data.csv` (densidad–porosidad) por URL.
- **Nodos:** mco (incertidumbre de coeficientes), bagging (base del bootstrap), d_sesgo.
- **¿Duplica?** No.
- **Viabilidad JS:** **Alta** (1 día): MCO cerrado; 1000 réplicas son instantáneas.
- **Adaptación:** en mco o bagging: sliders B y n (tamaño muestral), con una nube de rectas grises y un histograma de la pendiente con su intervalo del 90 %. Ejemplo: ventas frente a inversión publicitaria; al bajar n el intervalo se ensancha.

### MARS_Hao_Wang.ipynb
- **Título / autor:** «Multivariate Adaptive Regression Splines (MARS)» — Hao Wang.
- **Qué enseña:** contrasta la regresión lineal con MARS (`pyearth.Earth`) en datos sintéticos 1D a tramos y muestra cómo `max_terms` (2, 3, 5, …) y `max_degree` añaden bisagras. Después ajusta precios de vivienda y afina hiperparámetros.
- **Interactividad:** no interactivo.
- **Datos:** sintéticos generados en el cuaderno (cuatro tramos lineales con ruido uniforme) + `house_price.csv` (Kaggle, Ames) por URL.
- **Nodos:** no hay nodo MARS. Encaja como contraste de poli (base de funciones local frente a global) y de arbol_reg (tramos).
- **¿Duplica?** No.
- **Viabilidad JS:** Media (2–3 días: el paso hacia delante de MARS en 1D con bisagras es sencillo). Ojo: `py-earth` está abandonado, así que no sirve de referencia en el Python del curso.
- **Adaptación:** opcional, como pestaña de poli: «polinomio global frente a bisagras», con un slider de número de nudos. Ejemplo: demanda frente a precio con umbrales psicológicos.

### ModelVariance_Ahmed_Aboahmed.ipynb
- **Título / autor:** «Demonstrate model variance … with Bootstrap of the training dataset» — Ahmed Aboahmed.
- **Qué enseña:** Lasso 1D (Por → Perm), 200 réplicas bootstrap del entrenamiento y λ de 0 a 5 (100 valores), con curvas de «varianza», «sesgo» y error total frente a λ.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v4.csv` por URL (160 de entrenamiento y 40 de test).
- **Nodos:** lasso, d_sesgo.
- **Advertencia (comprobada en el código):** la descomposición está **mal calculada**. «variance» es `np.var(lasso_predict)`, es decir, la varianza entre puntos de test de una sola réplica, no entre réplicas. «bias» es el MSE completo y «irreducible» es la varianza de y_test. Como idea es útil; el código no debe reutilizarse.
- **¿Duplica?** No.
- **Viabilidad JS:** Alta (Lasso 1D = umbral suave cerrado).
- **Adaptación:** en lasso: slider de λ con descomposición **correcta** (sesgo² y varianza entre réplicas en cada x de test). Se puede fusionar con la ficha de Aldossary (2025b) en un único simulador «penalizar reduce varianza».

### OrthogonalPoly_Axel_Jeconiah.ipynb
- **Título / autor:** «Orthogonal Polynomial» — Axel Jeconiah.
- **Qué enseña (según el autor):** usar polinomios de Legendre para «decorrelacionar» Por y Perm y mejorar una regresión lineal.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv` por URL.
- **Nodos:** poli (bases ortogonales), mco (multicolinealidad).
- **Advertencia (comprobada en el código):** usa `degree = 1` y toma la columna `P1(x) = x`, así que la «transformación» es la identidad sobre datos `MinMaxScaler` (en [0, 1], no en [−1, 1] como dice el texto). También transforma la respuesta. La conclusión de que mejora el MSE no puede venir de la ortogonalización tal como está escrito (no lo ejecuté). **No recomendable.**
- **Viabilidad JS:** n/a. Para bases ortogonales es mejor la ficha de PolRegwShrinkage (Cotia, 2025).

### Outliers_SupportVectorMachines_Barun Das.ipynb
- **Título / autor:** «Impact of Outliers on Margin Length of Support Vector Machines» — Barun Das.
- **Qué enseña:** cómo unas pocas etiquetas invertidas (los «atípicos») desplazan el hiperplano y estrechan o ensanchan el margen de un SVC lineal con C = 1.
- **Interactividad:** **sí**. `IntSlider num_outliers` (0–20) → `plot_svm`: invierte la etiqueta de `num_outliers` puntos al azar (semilla fija), reajusta `SVC(kernel='linear', C=1.0)` y redibuja la dispersión con las curvas de nivel −1/0/+1 de la función de decisión (margen). El código mostrado no marca explícitamente los vectores soporte (no lo comprobé al completo).
- **Datos:** sintéticos (`make_classification`, 100 puntos, 2 variables).
- **Nodos:** svc (margen, C, puntos que violan el margen); también d_prep, en la idea de que la calidad de las etiquetas importa.
- **¿Duplica?** No; no hay simulador de SVM en la asignatura.
- **Viabilidad JS:** **Alta** (1–2 días): SVM lineal 2D con Pegasos o SMO simplificado y 100 puntos; el dibujo de las tres rectas es trivial.
- **Adaptación:** en svc: slider de etiquetas erróneas **más un slider de C** (que en el original es fijo), resaltando los vectores soporte. Ejemplo: clasificar clientes «abandona/no abandona» a partir de uso y antigüedad, con errores en el CRM.

### OverfitRandomForest_Dalma_Cerro.ipynb (y versión ...ML_...)
- **Título / autor:** «Overfit for Random Forest» — Dalma Camila Cerro Arrieta.
- **Qué enseña:** añade ruido gaussiano (σ = 2000) a la producción y barre el número de árboles y `max_depth` (1–99), con errores de entrenamiento y de test y gráficos predicho frente a real.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v2.csv` por URL (una celda lee además `unconv_MV_v5.csv` desde una ruta local).
- **Nodos:** rf, d_sesgo, d_hiper.
- **Advertencia:** la autora afirma que «al aumentar el número de árboles aumenta el sobreajuste», lo que contradice la teoría habitual (más árboles reduce varianza y no sobreajusta). Es una interpretación dudosa; no la verifiqué ejecutando.
- **Viabilidad JS:** Media. Mejor tomar la idea de Garbino o Sujin Park.

### Overfit_ANN_Aun_Al_Ghaithi.ipynb
- **Título / autor:** «Overfitting an Artificial Neural Network (ANN)» — Aun Al Ghaithi.
- **Qué enseña:** red densa (Keras y `MLPRegressor`) sobre producción con ruido añadido (σ = 500). Ajusta con k-fold y GridSearchCV y luego fuerza el sobreajuste con más neuronas o capas: la pérdida de validación sube con las épocas.
- **Interactividad:** no interactivo (curvas de pérdida train/val por época).
- **Datos:** `unconv_MV_v5.csv` por URL.
- **Nodos:** mlp, d_train (épocas, parada temprana implícita), d_cv.
- **Viabilidad JS:** Media (MLP de una o dos capas en JS puro, o TensorFlow.js desde CDN; 200 puntos).
- **Adaptación:** en mlp: sliders de neuronas y épocas con curvas de pérdida train/val y una marca de «parar aquí». Ejemplo: previsión de demanda semanal con pocas observaciones.

### RandomForestOverfitting_Agustin_Garbino.ipynb
- **Título / autor:** «Random Forest Overfitting: Under what circumstances does it occur?» — Agustin Garbino.
- **Qué enseña:** cruza el nivel de ruido (σ ∈ {50, 500, 1000, 3000, 5000}) con la complejidad (profundidad) y el número de variables (2 frente a 6), y compara RF con bagging (máximo de variables por corte). Con poco ruido el RF es robusto; con mucho ruido la varianza explicada cae y aparecen «ciclos» inestables. Según el autor, bagging supera a RF con poco ruido.
- **Interactividad:** no interactivo (superficies del modelo y curvas de varianza explicada).
- **Datos:** `unconv_MV_v5.csv` por URL, con ruido añadido.
- **Nodos:** rf, bagging, d_sesgo.
- **Viabilidad JS:** Media (RF pequeño en 2D; las 6 variables piden precalcular).
- **Adaptación:** en rf: slider de ruido y de profundidad, con el R² de test y la superficie predicha. Ejemplo: ventas por tienda frente a superficie y tráfico.

### Robust_regression_Ali_Mohamed.ipynb
- **Título / autor:** «Towards more robust regression models» — Ali Mohamed.
- **Qué enseña:** sustituye la pérdida cuadrática de MCO por una basada en el «most frequent value» de Steiner, optimizada con un algoritmo genético propio. Muestra que con atípicos la recta de MCO se desvía y la MFV no (1D y 3D).
- **Interactividad:** no ipywidgets; usa plotly para 3D.
- **Datos:** sintéticos (`make_regression` + atípicos añadidos).
- **Nodos:** mco (sensibilidad a atípicos), d_train (la pérdida es una elección).
- **Advertencia de uso:** el autor escribe «This work is being considered for publishing. Please, ask a permission, first, before sharing or using in outside class work». **Pide permiso explícito**: no reutilizar su código ni su método MFV sin contactarle, aunque el repo sea MIT. Sí se puede usar la idea genérica (MCO frente a Huber/MAE), que es estándar.
- **Viabilidad JS:** Alta (1 día), con Huber o MAE estándar, no con MFV.
- **Adaptación:** en mco o d_train: arrastrar o añadir atípicos y comparar en vivo las rectas MCO, Huber y MAE. Ejemplo: ticket medio frente a visitas con unos pocos pedidos corporativos enormes.

### StudyDiffKernelsSVM_Yevgeniy_Samarkin.ipynb
- **Título / autor:** «Understanding the difference between different kernels in SVM models» — Yevgeniy Samarkin.
- **Qué enseña:** con un problema separable (blobs, 300 puntos) los tres kernels aciertan; con círculos concéntricos (`make_circles`, 500 puntos) solo RBF separa. Muestra en 3D la matriz de kernel para ilustrar el «kernel trick» y acompaña matrices de confusión.
- **Interactividad:** **sí (botones)**: `widgets.Button` «Linear / Sigmoid / RBF kernel» → `button1/2/3`, que redibujan una vista 3D del kernel sobre los círculos. No hay sliders de C ni de γ.
- **Datos:** sintéticos (`make_blobs`, `make_circles`).
- **Nodos:** svc (y por extensión svr).
- **¿Duplica?** No.
- **Viabilidad JS:** Media (2–3 días): SVM con kernel y SMO simplificado para unos 300–500 puntos; frontera por rejilla en canvas. La vista 3D puede sustituirse por un mapa φ(x) = (x₁, x₂, x₁²+x₂²) fácil de pintar.
- **Adaptación:** en svc: selector de kernel + sliders C y γ, con frontera y vectores soporte. Ejemplo: clientes «fieles» en el centro del espacio (gasto, frecuencia) rodeados de «esporádicos».

### SupportVectorMachineKernels_Vincent_indina.ipynb
- **Título / autor:** «Support Vector Machine Kernels» — Vincent Indina.
- **Qué enseña:** SVC lineal y polinómico (grados 3 y 5) con C = 0,01 frente a 100, sobre impago de préstamos usando `employ` y `debtinc` estandarizados, con fronteras y matrices de confusión.
- **Interactividad:** no interactivo.
- **Datos:** `bankloans.csv` (Kaggle, riesgo de crédito), desde el GitHub del autor. **Datos de negocio.**
- **Nodos:** svc, d_prep (estandarizar), d_mclas; potencialmente d_deseq (los impagos son minoría; el autor no lo trata a fondo, no comprobado).
- **Viabilidad JS:** Media (mismo motor SVM que la ficha anterior).
- **Adaptación:** mismo simulador svc con un segundo conjunto «crédito» sintético (antigüedad laboral, ratio deuda/ingresos) que imite el patrón.

### SupportVectorsRandomForestCatBoost_Nadia_Mouedden.ipynb
- **Título / autor:** «… Support Vector Regression, Random Forest and CatBoost» — Nadia Mouedden.
- **Qué enseña:** robustez de SVR, RF y CatBoost en una rejilla 20 × 20 de nivel de no linealidad (0–2) y de ruido (0–0,4) añadidos a los datos, con mapas de error. La autora recomienda CatBoost.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV.csv` por URL, modificado con ruido y no linealidad.
- **Nodos:** svr, rf, gb.
- **Viabilidad JS:** Baja-Media (400 combinaciones × 3 modelos; habría que precalcular).
- **Adaptación:** baja prioridad; la idea de un «mapa de robustez» podría ir en voting o stacking como comparación de modelos.

### TreeBaggingvsRandomforest_Fuqiao Bai.ipynb
- **Título / autor:** «Tree Bagging vs Random Forest: Does tree decorrelation actually improve prediction accuracy?» — Fuqiao Bai.
- **Qué enseña:** BaggingRegressor frente a RandomForestRegressor (con OOB), ambos con GridSearchCV, comparando importancia de variables e histogramas de MSE. Concluye que RF gana.
- **Interactividad:** no interactivo.
- **Datos:** `Project_Multiphaseflow data.csv` (flujo multifásico experimental), por URL del autor.
- **Nodos:** bagging, rf, d_hiper.
- **¿Duplica?** Solapa con TreeDecorrelation (2025), que lo hace mejor.
- **Viabilidad JS:** Media. Mejor usar la ficha de Bettir.

---

## Fichas — 2025_MLProjects

### BaggingNonTree_Deena_Elhossary.ipynb
- **Título / autor:** «Bagging with Non-Tree Base Models» — Deena Elhossary.
- **Qué enseña:** aplica bagging a regresión lineal, kNN, SVR (por defecto y con BayesSearchCV) y logística (producción alta/baja por la mediana), barriendo `n_estimators`. Según la autora, la lineal apenas mejora y SVR por defecto da R² ≈ 0,05 frente a ≈ 0,98 tras optimizar.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV.csv` por URL.
- **Nodos:** bagging, mco, svr, logit, d_hiper.
- **Viabilidad JS:** Media. La versión interactiva de 2025b (Isikdogan) es mejor base.

### ComparisonPDPsSHAPvalues_Lhalid_Alhajri.ipynb
- **Título / autor:** «Simple Comparison of PDPs and SHAP values» — Khalid Alhajri (el fichero dice «Lhalid»).
- **Qué enseña:** primero una ordenación de variables sin modelo (Pearson, Spearman, correlación parcial y semiparcial, coeficientes beta, información mutua, VIF). Después SHAP global y local y PDP sobre un RF, y una tabla comparativa: PDP global y barata; SHAP global y local, más cara y capaz de mostrar interacciones.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v4.csv` por URL.
- **Nodos:** d_interp.
- **¿Duplica?** Solapa con la de Suin Choi (2025b), que es más didáctica porque usa datos sintéticos con verdad conocida.
- **Viabilidad JS:** Media. Mejor tomar la de Choi.

### FeatureImportanceWrapperFunctions_Eric_Hu.ipynb
- **Título / autor:** «Feature Selection Wrapper Methods» — Eric Hu.
- **Qué enseña:** selección exhaustiva, hacia delante y hacia atrás (mlxtend) con regresión lineal sobre 6 variables, repetidas en réplicas bootstrap para contar con qué frecuencia entra cada variable. Valida con importancia por permutación. Según el autor, Por y Brittle salen siempre.
- **Interactividad:** no interactivo (barras de frecuencia de selección).
- **Datos:** `unconv_MV_v5.csv` por URL.
- **Nodos:** mco, d_interp (permutación), d_hiper (selección de variables como hiperparámetro), d_part.
- **¿Duplica?** No.
- **Viabilidad JS:** **Alta** (2 días): con 6 variables hay 63 subconjuntos de MCO cerrado; el bootstrap es barato.
- **Adaptación:** en mco o d_interp: «¿qué variables sobreviven?», con un slider de réplicas bootstrap y un selector de método (exhaustivo/adelante/atrás), mostrando barras de frecuencia y R² de test. Ejemplo: ventas frente a precio, promoción, temperatura, día festivo y dos variables de ruido.

### GradientBoosting_Yunfei_Zhang.ipynb
- **Título / autor:** «The Application of Gradient Boosting in Classification Tasks» — Yunfei Zhang.
- **Qué enseña:** GradientBoostingClassifier en cáncer de mama (30 variables), con importancia de variables, matriz de confusión, ROC/AUC y GridSearchCV sobre tasa, nº de árboles y profundidad. Según el autor, la exactitud pasa de ~92 % a 96,5 % y el AUC es 0,994. Incluye una guía para leer la matriz y la ROC.
- **Interactividad:** no interactivo.
- **Datos:** `load_breast_cancer` (scikit-learn).
- **Nodos:** gb, d_mclas, d_hiper.
- **Viabilidad JS:** Media-Baja; como simulador aporta poco frente a `gbm_boosting.html`. Su lectura guiada de la ROC puede inspirar texto para d_mclas.

### ModelBias_Bader_Alshammasi.ipynb
- **Título / autor:** «Model bias: demonstrating and calculating model bias with a simple predictive ML method» — Bader Al Shammasi.
- **Qué enseña:** ajusta una recta a log(perm) frente a porosidad en un conjunto no lineal y en otro «linealizado» quitando puntos, y compara residuos: el patrón sistemático indica sesgo.
- **Interactividad:** no interactivo.
- **Datos:** `nonlinear_facies_v1.csv` por URL.
- **Nodos:** mco, d_sesgo (los residuos con forma revelan sesgo).
- **Advertencia:** «linealizar» eliminando datos es pedagógicamente discutible.
- **¿Duplica?** Sí, en parte, «Elige el grado» (subajuste).
- **Viabilidad JS:** Alta pero de bajo valor; como mucho, añadir el gráfico de residuos a «Elige el grado».

### ModelVariance_Xuesong_Ma.ipynb
- **Título / autor:** «Model variance» — Xuesong Ma.
- **Qué enseña:** genera y = 2x + sin x + cos x + N(0,1) con 100 puntos, aplica una transformación a normal (QuantileTransformer) y hace 1000 réplicas bootstrap de una regresión polinómica de grado 3 frente a 6. Dibuja las curvas bootstrap y una banda de ±5 desviaciones, y la varianza del coeficiente de x para grados 1 a 6, que crece con el grado.
- **Interactividad:** no interactivo.
- **Datos:** **sintéticos con fórmula explícita** (reproducibles).
- **Nodos:** poli, d_sesgo.
- **¿Duplica?** Complementa «Elige el grado» (tema 1): aquella muestra el ajuste a una muestra; esta, la **dispersión entre muestras**, que es la varianza.
- **Viabilidad JS:** **Alta** (1–2 días): MCO polinómico cerrado (conviene centrar o escalar x por el condicionamiento).
- **Adaptación:** en poli o d_sesgo: sliders de grado (1–10), n y réplicas; nube de 50 curvas bootstrap y gráfico lateral de la varianza de la predicción en un x fijo frente al grado. Ejemplo: ventas estacionales frente a la semana del año.

### OverfitForRandomForest_Sadam_Hussain.ipynb
- **Título / autor:** «Overfit for Random Forest» — Sadam Hussain.
- **Qué enseña:** un RF sobreajustado con datos de núcleo con ruido; luego limpia datos (filas con ceros), ajusta hiperparámetros y estudia la sensibilidad a `max_depth` ∈ {3, 5, 7, 9} y a `n_estimators`.
- **Interactividad:** no interactivo.
- **Datos:** datos reales de núcleo (MSEEL Boggess 17) desde un `file_path` local: **no reproducible**.
- **Nodos:** rf, d_prep (limpieza).
- **Viabilidad JS:** Baja (los datos no están disponibles). Descartable.

### OverfitGraidentBoosting_Berit_Hudson_Rasmussen.ipynb
- **Título / autor:** «Exploring Overfit with Gradient Boosting» — Berit Hudson Rasmussen.
- **Qué enseña:** parte de un GB razonable (50 árboles, profundidad 3) y lo sobreajusta paso a paso: tasa de 0,01 a 1 (el test empeora por encima de ~0,3), nº de árboles de 1 a 300 con tasa 1 (mínimo de test hacia los 10 árboles) y profundidad de 1 a 20. Muestra curvas train/test y gráficos predicho frente a real.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v2.csv` por URL, con ruido añadido.
- **Nodos:** gb, d_sesgo, d_hiper.
- **¿Duplica?** Muy probablemente `gbm_boosting.html` (no lo he abierto). Como mucho, aporta la idea de «sobreajustar a propósito» combinando tasa alta y muchos árboles.
- **Viabilidad JS:** Media. Prioridad baja por solapamiento.

### OverfitRandomForest_Dinghan_Wang.ipynb
- **Título / autor:** «Demonstration of an Overfitting Random Forest Model» — Dinghan Wang.
- **Qué enseña:** análisis exploratorio completo (PDF/CDF, correlaciones, VIF, información mutua) y un RF con GridSearch cuyo «mejor» modelo sobreajusta (gran diferencia de R² entre train y test); efecto de cada hiperparámetro.
- **Interactividad:** no interactivo.
- **Datos:** flujo de calor geotérmico desde Excel por URL.
- **Nodos:** rf, d_hiper.
- **Viabilidad JS:** Baja-Media. Redundante con Sujin Park y Garbino.

### PolRegwShrinkage_Danielle_Cotia.ipynb
- **Título / autor:** «Polynomial Regression with Shrinkage Term» — Danielle Marques Raposo Cotia.
- **Qué enseña:** 40 puntos sintéticos de un polinomio cúbico con ruido. Compara recta, polinomio ortogonal de grado 8 con MCO y Lasso sobre esa base, con trayectoria de coeficientes frente a λ: los términos altos se anulan y queda en la práctica un cúbico (λ ≈ 0,02).
- **Interactividad:** no interactivo.
- **Datos:** CSV sintético (`pol-degree3-noisy-norm.csv`) desde el GitHub de la autora; regenerable en JS.
- **Nodos:** poli, lasso, d_hiper, d_part.
- **Advertencia:** λ se elige mirando el **MSE de test** (no hay validación cruzada): es una fuga de información y sirve de ejemplo para d_part.
- **¿Duplica?** Complementa «Elige el grado»: en vez de elegir el grado, se fija uno alto y se deja que Lasso pode.
- **Viabilidad JS:** **Alta** (2 días): Lasso por descenso coordinado sobre 9 columnas y 30 puntos.
- **Adaptación:** en lasso o poli: grado fijo 8–10, slider de λ (log), curva ajustada y gráfico de trayectorias de coeficientes con la λ actual marcada; un interruptor «elegir λ con test frente a con CV» que muestre la diferencia. Ejemplo: tendencia de ventas con pocos puntos.

### TreeDecorrelation_Nassima_Bettir.ipynb
- **Título / autor:** «Bagging vs. Random Forest: Impact of Tree Decorrelation On Prediction Accuracy» — Nassima Bettir.
- **Qué enseña:** barre `max_features` (m = 1 … 5; con m = 5 equivale a bagging) y mide (a) el **MSE OOB**, que según la autora es mínimo en m = 2, (b) la **correlación media de Pearson entre las predicciones de los árboles** (función `average_tree_correlation`, siguiendo a Zhang y Wang, 2009), que cae al bajar m, y (c) el cambio de importancia de variables. Explica bien por qué decorrelacionar reduce la varianza del promedio.
- **Interactividad:** no interactivo.
- **Datos:** datos reales de perforación (FORGE, pozo 58-32) desde **una ruta local de Windows**, no reproducibles.
- **Nodos:** rf, bagging, d_cv (OOB), d_interp (importancia).
- **¿Duplica?** No.
- **Viabilidad JS:** Media (3–4 días): RF de 50–100 árboles poco profundos sobre ~500 filas y 5 variables sintéticas; la correlación entre árboles es una matriz de 100 × 100, barata.
- **Adaptación:** en rf: slider de mtry de 1 a p, con tres paneles: error OOB, correlación media entre árboles y varianza de un árbol suelto, junto a la fórmula ρσ² + (1−ρ)σ²/B. Ejemplo: tiempo de entrega frente a distancia, tráfico, peso, hora y repartidor.

### XGBoost_Omar_Abukassab.ipynb
- **Título / autor:** «eXtreme Gradient Boosting (XGBoost)» — Omar Abukassab.
- **Qué enseña:** XGBClassifier para producción alta/baja con dos umbrales: uno equilibrado y otro desequilibrado (5000, con más negativos). Usa GridSearch con `scale_pos_weight` (1 frente a 3 = negativos/positivos), métricas de precisión, recall, F1 y kappa de Cohen, y SHAP. Incluye una tabla comparativa de GB y XGBoost (regularización L1/L2, etc.).
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv` por URL.
- **Nodos:** xgb, d_deseq (ponderar la clase), d_mclas, d_interp.
- **¿Duplica?** `xgboost_penalizacion.html` cubre la penalización; esto añade el desequilibrio.
- **Viabilidad JS:** Media (boosting de tocones en JS, o curvas precalculadas).
- **Adaptación:** en d_deseq: slider de proporción de positivos y de `scale_pos_weight` (o peso de clase), con matriz de confusión y recall/precisión. Ejemplo: detección de fraude.

### LinearDiscriminantAnalysis_KFold_Muiz_Adekomi.ipynb
- LDA (fuera del mapa) con validación cruzada estratificada de 5 particiones sobre `unconv_MV_v5`. Aporta poco a d_cv; descartado (ver lista).

---

## Fichas — 2025b_MLProjects

### BaggingWithNonTreeModels_Suatcan_Isikdogan.ipynb
- **Título / autor:** «Bagging with Non-Tree Models» — Suatcan Isikdogan.
- **Qué enseña:** bagging de regresión lineal (sin mejora, porque tiene poca varianza) y de kNN (mejora sobre todo con k pequeño: según el autor, R² de 0,900 a 0,921 con k = 1). Añade ruido gaussiano opcional a predictores.
- **Interactividad:** **sí**. `interact(knn_bagging_experiment)` con `IntSlider k` (1–25), `IntSlider n_estimators` (5–100) y `FloatSlider max_samples` (0,1–1,0) → reentrena BaggingRegressor(kNN) y redibuja predicho frente a medido en test, con MSE y R² en el título.
- **Datos:** `unconv_MV_v3.csv` por URL; 70/30.
- **Nodos:** bagging (la mejora depende de la varianza del modelo base), d_sesgo, mco.
- **¿Duplica?** No.
- **Viabilidad JS:** **Alta** (1–2 días): kNN y bagging son triviales; n≈200.
- **Adaptación:** en bagging: modelo base seleccionable (árbol profundo, kNN con k = 1, MCO), sliders B y fracción de muestra, y R² de test frente a B por modelo: «bagging ayuda a quien tiene varianza». Ejemplo: precio de alquiler frente a m² y distancia al centro.

### FastGradientBoosting_David_Dadzie.ipynb
- **Título / autor:** «Fast Gradient Boosting - Impact of Learning Rate on XGBoost Performance» — David Paa Kwesi Dadzie.
- **Qué enseña:** XGBRegressor (1000 árboles, profundidad 4, subsample y colsample 0,8, `early_stopping_rounds = 50`) con tasa ∈ {0,001; 0,01; 0,05; 0,1; 0,3; 0,5; 1,0}. Muestra curvas RMSE train/val por iteración, iteración óptima, tiempo y MAE en dólares. Según el autor, lo óptimo es 0,05–0,1, y con 1,0 converge rápido pero sobreajusta. La partición es 70/15/15.
- **Interactividad:** **sí**. `widgets.Dropdown` de tasa → `widgets.interactive_output(plot_selected_lr)`, que dibuja las curvas RMSE de entrenamiento (continua) y validación (discontinua) de esa tasa. El autor dice adaptarlo de `Interactive_Overfit.ipynb` de Pyrcz.
- **Datos:** **TMDB 5000 movies** (Kaggle; log de ingresos frente a presupuesto, popularidad, votos…), leído de un `tmdb_5000_movies.csv` **local** no incluido. Son datos de negocio, pero hay que descargarlos aparte (ojo con la licencia de Kaggle) o sustituirlos por sintéticos.
- **Nodos:** xgb, gb, d_train (tasa, parada temprana), d_part (train/val/test).
- **¿Duplica?** Puede solapar con `gbm_boosting.html` en el efecto de la tasa (no verificado). La **parada temprana con validación** quizá no esté cubierta.
- **Viabilidad JS:** **Alta** con curvas precalculadas en JSON (1 día); Media con boosting real en JS (árboles de profundidad 2–3, ~3000 filas).
- **Adaptación:** en d_train o xgb: slider continuo de tasa; curvas train/val y una línea vertical en la iteración de parada temprana (paciencia ajustable). Ejemplo: ingresos de taquilla o ventas de un producto nuevo.

### ModelVarianceReduction_Abdulaziz_Aldossary.ipynb
- **Título / autor:** «Demonstrating Model Variance Reduction through Bootstrap Resampling and Ridge Regularization» — Abdulaziz Aldossary.
- **Qué enseña:** toma a propósito una submuestra de **20 pozos** (16 de entrenamiento y 4 de test) para que MCO sea inestable. Hace 200 réplicas bootstrap con Pipeline(StandardScaler, Ridge) para α ∈ {0 (MCO), 0,1, 1, 10, 100}. Muestra la varianza de predicción frente a α, cajas de predicciones en puntos de test fijos (MCO frente a α = 10), la distribución del MSE de test por α, un histograma comparado y un **mapa de calor de la desviación típica de cada coeficiente** frente a α.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv` por URL (submuestra).
- **Nodos:** ridge, mco, d_sesgo, d_prep (estandarizar dentro del Pipeline).
- **¿Duplica?** No; es el complemento natural de ridge.
- **Viabilidad JS:** **Alta** (1–2 días): ridge cerrado (XᵀX + αI)⁻¹Xᵀy con p ≈ 6.
- **Adaptación:** en ridge: slider de α (log) y de n de entrenamiento, con (1) cajas de predicción bootstrap en 3–4 puntos, (2) barras de desviación típica de cada coeficiente y (3) MSE de test medio con su dispersión, y un aviso de que α = 0 es MCO. Ejemplo: 20 tiendas, ventas frente a 6 variables correlacionadas (superficie, empleados, aparcamiento…).

### Overfit_RandomForest_Sujin Park.ipynb
- **Título / autor:** «Random Forest Overfitting - When Do Random Forests Overfit?» — Sujin Park.
- **Qué enseña:** con `make_classification` (8000 × 100, 15 variables informativas, 15 % de etiquetas ruidosas) compara dos configuraciones. «Overfit»: sin bootstrap, `max_features = 1.0`, `max_depth = None`, hoja de 1. «Regularized»: bootstrap, `sqrt`, profundidad 12, hoja de 10. Añade una curva de validación sobre `max_depth` y la exactitud OOB frente a la de test.
- **Interactividad:** no interactivo (barras y líneas).
- **Datos:** sintéticos (reproducibles).
- **Nodos:** rf, d_cv (OOB como estimador del error de test), d_hiper.
- **Viabilidad JS:** Media (RF de clasificación en JS sobre un conjunto reducido, p. ej. 2000 × 10).
- **Adaptación:** en rf o d_cv: interruptores bootstrap sí/no y mtry = p/√p, y slider de profundidad; exactitud train/OOB/test con la diagonal OOB = test. Ejemplo: clasificar leads con etiquetas ruidosas.

### Partial_Dependence_Plot_vs_SHAP_Dependence_Plot_SuinChoi.ipynb
- **Título / autor:** «A Comparative Analysis: Partial Dependence Plots vs. SHAP Dependence Plots» — Suin Choi.
- **Qué enseña:** genera 1000 puntos con X1…X4 ~ U(0,1) y ruido N(0; 0,1²) en tres escenarios. (1) Independientes: Y = 2X1 + 5X2. (2) Correlacionadas: X2 = 0,8·X1 + 0,2·U, misma Y. (3) Interacción: Y = 2X1 + 5X2 + 10·X1·X2. Entrena un RF y compara PDP 1D, PDP 2D y la dependencia SHAP. Además, (4) la misma comparación con un modelo lineal (los métodos explican el **modelo**, no los datos), (5) clasificación con logit = 2X1 + 5X2 + 10X1X2 y (6) estabilidad en 8 submuestras. Según la autora, la PDP 1D sale casi igual en los tres escenarios; la dispersión vertical de SHAP delata la interacción, y SHAP tiene menos de la mitad de varianza entre submuestras.
- **Interactividad:** no interactivo.
- **Datos:** **sintéticos con fórmulas explícitas** (comprobadas en las celdas 9 y 12).
- **Nodos:** d_interp (PDP/ICE, Shapley), rf, mco.
- **¿Duplica?** No.
- **Viabilidad JS:** Media (3–5 días). La PDP/ICE es trivial con cualquier modelo. Para SHAP, con 2–4 variables se pueden calcular **Shapley exactos** recorriendo los 2^p subconjuntos con fondo marginal (sin TreeSHAP). Con un modelo sustituto rápido (árbol o RF pequeño en JS) es asumible.
- **Adaptación:** en d_interp: selector de escenario (independiente / correlacionado / interacción) y slider de la fuerza de la interacción, con PDP + ICE a un lado y dependencia SHAP coloreada por X2 al otro. Ejemplo: probabilidad de compra frente a descuento y antigüedad del cliente, donde el descuento solo funciona con clientes nuevos.

### RandomForest_VS_Bagging_Chingiz_Asgarli.ipynb
- **Título / autor:** «Bagging vs Random Forest for Subsurface Production Prediction» — Chingiz Asgarli.
- **Qué enseña:** recorre la secuencia árbol → bagging → RF → RF ajustado (GridSearchCV), con curvas de aprendizaje y una tabla train/test de MAE, RMSE y R². Usa solo 2 predictores (Por, AI), así que la decorrelación tiene poco margen.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv` desde una ruta local (también disponible en GeoDataSets).
- **Nodos:** arbol_reg, bagging, rf, d_hiper.
- **Viabilidad JS:** Media. La narrativa en escalera es útil como texto; el simulador ya lo cubren las fichas anteriores.

### SGDvsBGD_Saris_Visessumon.ipynb
- **Título / autor:** «Stochastic Gradient–Based Optimization» — Saris Visessumon.
- **Qué enseña:** con los mismos pesos iniciales compara descenso por lote completo, minilotes (B = 4, 16, …) y estocástico (B = 1) con distintas tasas. Lo hace en MNIST (MLP) y en una regresión (x, y) → porosidad sobre un campo gaussiano sintético. Según el autor, el lote completo converge despacio, B = 1 con tasa 0,1 diverge y los minilotes con la tasa bien elegida son los mejores; también compara varias semillas.
- **Interactividad:** no interactivo (pérdida frente a época).
- **Datos:** MNIST (torchvision) y un campo gaussiano generado en el cuaderno.
- **Nodos:** **d_train** (tasa, lotes) y mlp.
- **¿Duplica?** No consta en la asignatura un simulador de d_train.
- **Viabilidad JS:** **Alta** (1–2 días) reimplementando el concepto con regresión logística o lineal, no con MNIST.
- **Adaptación:** en d_train: sliders de tamaño de lote (1, 8, 32, n) y de tasa (log), con la curva de pérdida por época y la trayectoria en el plano (β₀, β₁) sobre curvas de nivel. Ejemplo: logit de conversión frente a precio y número de visitas.

### Robust regression (ver 2023) y BayesianRegression_Ryan_Mcguigan.ipynb
- **BayesianRegression — Ryan McGuigan.** Regresión lineal bayesiana con Metropolis-Hastings propio frente a MCO, ajustada por etapas a medida que crece la muestra (1000 sintéticos con coeficientes verdaderos conocidos). Muestra los intervalos que se estrechan y las trazas de la cadena. **Nodos:** mco (incertidumbre de coeficientes según n). Usa MCMC, que está fuera de temario. **Viabilidad JS:** Media. Si interesa, basta el MCO con intervalos frente a n (es la misma intuición que LinearBagging), sin MCMC.

### kNN_Noise_Sensitivity_Haidar_Almajed.ipynb
- kNN (fuera del mapa) con ruido en la respuesta {0, 100, …, 1000} y 50 réplicas por nivel: la k óptima sube con el ruido. Compara con Ridge y RF con σ = 700 (según el autor, RF resiste mejor). Solo la idea de que **el hiperparámetro óptimo se desplaza con el ruido** encaja en d_hiper. Viabilidad Alta, pero baja prioridad.

---

## Descartados (una línea, agrupados)

**Clustering / mezclas (fuera de temario):** AffinityPropagation (Deema Albadan), BIRCH (Meshack Nyiti, interactivo), Gaussian Mixture Models (Mariella El Khoury), KmeanClustering (Kulpitcha Sudyodprasert), Clustering (Karem Algaradi), GMMClustering (Ali Oshaish), GaussianMixtureModels (Asad Safarov), HierarchicalClustering (Amena Alelg, muy interactivo), Class-Conditional Prototype (Sibo Zhang), Fractals (Maria Fernanda Gonzalez), AIC_BIC_Gaussian_Mixture (Javid Aliyev; el AIC/BIC solo aparece aplicado a GMM), Clustering_using_SOM (Ameena AlJehairan), Fuzzy-C-Means (Prince Ikpabi), Gaussian_Clustering (Emma Martin), MeanShift (Tiago Gunter), Medoid (Amber Nguyen), SpectralClustering (Eddie Talen), k-Means (Anika Gupta).

**Reducción de dimensión / proyecciones:** DimensionalityReduction (Ahmed Alsubaih), MDS (Jonathan Markel), RandomProjection (Khalid Aldosary), UMAP (Lydia Mata Mireles), ImageComparison (Ahmed Merzoug; MDS/UMAP/t-SNE/LDA), KernelPCA (Naveen Raj Manoharan), DimensionalityReductiononDBSCAN (Yining Huang), VarianceVsSemantic (Leonardo Reginato), Mutual_Information (Yongle Zhou; información mutua desde la entropía, que como mucho sirve de contexto para d_interp).

**Maldición de la dimensión / kNN:** CoDKNN (Kartik Mawa), ModelBias_Mason_Farnsworth (pese al nombre, trata la maldición de la dimensión en kNN), CurseDimensionalityK-NN (Qianqian Zhou), Curse_Dimensionality (Manav Patel), CurseofDimensionality (Burak Firat), CurseOfDimensionality (Sultan Dwier, interactivo), KNN_OptimalK_SampleDensity (Xihan Yao).

**Redes profundas / imágenes / series:** CNN_LinePred y CNNinSML (Vivek Singh), ClassifyFractalShapes (Muhannad Alabdullateef), Overfit_Potential_of_ANNs_diagnosis (Dursun Dashdamirov; CNN en CIFAR-10, aunque su prueba de «etiquetas aleatorias» es una buena idea de diagnóstico), FNO_Robustness (Tao Wang), UnetVAutoencoder (Rhiannon Morris), BiLSTM (Alexander Ifenaike), ARIMA (Renato Poli; series temporales fuera del mapa).

**MCMC / bayesiano:** Intuitive MCMC (Sohini Dasgupta), MCMC_Approximation (Tien Phan), BayesianLASSORegression en R/Stan (Shaikha Aldossary; Lasso bayesiano frente a glmnet con λ = 10; fuera de temario, aunque ilustra Lasso como prior de Laplace).

**LDA:** Linear Discriminant Analysis (Abdulahi Raji), LinearDiscriminantAnalysis_KFold (Muiz Adekomi).

**Geoestadística / sesgo espacial:** ModelBias_Abdulrahim_AlMulhim (sesgo por muestreo agrupado con desagrupado espacial; fuera de temario).

**Poco aprovechables (datos no reproducibles o plantilla vacía):** KickClassification (Santiago Callerio; casi solo la plantilla), UnconventionalWellsEUR (Bruno Reinoso; lineal/SVR/RF con un CSV en ruta local), OverfitForRandomForest (Sadam Hussain; datos locales), OrthogonalPoly (Axel Jeconiah; método defectuoso, ver ficha), Fast Gradient Boosting (Preeda Tapiang; CSV local y duplica simuladores existentes).

---

## Notas de rigor
- Las afirmaciones «según el autor» son citas de sus celdas markdown; no se reprodujeron.
- Defectos detectados leyendo el código (sin ejecutar): descomposición sesgo/varianza mal calculada (Aboahmed 2023), transformación de Legendre que es la identidad (Jeconiah 2023), λ elegido con el test (Cotia 2025) e interpretación dudosa de «más árboles = más sobreajuste» (Cerro 2023).
- Restricción de uso: Ali Mohamed (Robust_regression) pide permiso antes de reutilizar su trabajo fuera de clase.
- No se ha abierto el contenido de los simuladores existentes de la asignatura; los posibles solapes con `gbm_boosting.html` y `xgboost_penalizacion.html` se deducen de sus nombres.
