# Hallazgos: MachineLearningDemos y proyectos de estudiantes 2020–2022 (GeostatsGuy)

Análisis de solo lectura. Extraje con `python3 -I` los encabezados y las celdas markdown y de código de cada cuaderno, sin ejecutarlos. **Qué comprobé:** encabezados, resumen ejecutivo, `read_csv` y generadores de datos, imports de sklearn, todas las líneas con widgets (`Slider`, `Dropdown`, `Checkbox`, `interactive_output`…) y, en los cuadernos clave, el cuerpo de la función que dibuja. **Qué no comprobé:** las salidas renderizadas (imágenes) ni si el código corre con versiones actuales de sklearn. Varios usan API antigua, como `loss='ls'`, `'lad'`, `criterion='mse'` o `base_estimator`, que hoy fallan.

## Licencias (condicionan la reutilización)

- **MachineLearningDemos**: **CC BY-SA 4.0** (Attribution-ShareAlike, según `LICENSE`). Copiar o adaptar su código o su texto exige atribuir y publicar la obra derivada con la **misma licencia**. Se puede evitar reimplementando la *idea* desde cero en JS, sin copiar código ni texto.
- **MachineLearningCourse**: el repo es **MIT** («Copyright (c) 2022 Michael Pyrcz»). Cada proyecto es obra de su estudiante, así que se anota el autor en cada ficha. Conviene atribuir al estudiante si se reutiliza algo, aunque solo sea la idea.
  - Caso especial: el cuaderno 2020 de **Laide Ojomo** abre con una petición de no difundirlo hasta diciembre de 2021. El plazo ya pasó, pero es otro motivo para no tocarlo, además de su tema (geotecnia).
- **Datos**: casi todos usan CSV de subsuelo de `GeostatsGuy/GeoDataSets` (`unconv_MV*.csv`, `Density_Por_data.csv`, `1D_Porosity.csv`, `12_sample_data.csv`, `sample_data_biased.csv`). El mapa pide datos de negocio o sintéticos, así que en todas las adaptaciones **se reemplazan por datos sintéticos generados en JS**.

---

## 1. MachineLearningDemos (Michael Pyrcz, CC BY-SA 4.0)

Hallazgo general: **ninguno de los 16 cuadernos es interactivo**. No hay ipywidgets: todos son secuencias de celdas que barren un hiperparámetro en un bucle y dibujan gráficos estáticos con matplotlib. Su valor está en el **diseño didáctico de los gráficos**, no en controles que se puedan portar.

### 1.1 `MachineLearning_linear_regression.ipynb`: «Linear Regression»
- **Qué enseña:** MCO de porosidad sobre densidad, contrastes de hipótesis sobre la pendiente, r², intervalos de confianza de los parámetros (t crítica) y diagnóstico de residuos (histograma, ŷ frente a y, residuo frente a ŷ).
- **Interactividad:** no interactivo.
- **Datos:** `Density_Por_data.csv`, con ruido gaussiano opcional añadido.
- **Nodos:** `mco` (inferencia y residuos) y `d_mreg`.
- **Duplica:** no hay simulador de MCO en la asignatura.
- **Viabilidad JS:** **Alta**, ½–1 día. MCO univariante en forma cerrada; la t crítica se puede tabular.
- **Idea «Simular»:** ventas frente a inversión publicitaria. Sliders de ruido y de n. Recta con banda de confianza de la media y banda de predicción, más el gráfico de residuos. Muestra cómo se estrechan los intervalos al crecer n.

### 1.2 `MachineLearning_polynomial_regression.ipynb`: «Polynomial Regression»
- **Qué enseña:** expansión de la base polinómica, transformación gaussiana de x, correlación entre los términos x, x², x³… (colinealidad), **polinomios de Hermite y polinomios ortogonales** como base sin correlación, y comparación con un árbol y un random forest. Termina con `Pipeline(StandardScaler, PolynomialFeatures, LinearRegression)`.
- **Interactividad:** no interactivo.
- **Datos:** `1D_Porosity.csv`.
- **Nodos:** `poli` y `d_prep` (el Pipeline).
- **Duplica:** **sí, en parte**, con la slide «Elige el grado» del tema 1 (subajuste/sobreajuste). Lo nuevo es la matriz de correlación de la base monómica frente a la de Hermite.
- **Viabilidad JS:** Alta, 1 día para el complemento.
- **Idea «Simular»:** complementar «Elige el grado» con un conmutador de base «monomios / ortogonal» que muestre la matriz de correlación de las columnas y la inestabilidad de los coeficientes. No volver a hacer el slider de grado.

### 1.3 `MachineLearning_ridge_regression.ipynb`: «Ridge Regression»
- **Qué enseña:** ridge frente a MCO; barrido de λ de 0 a 100 con R² y MSE en train y test; **«Model Variance»**: L remuestreos bootstrap de n = 20 por cada λ, de donde sale la varianza del modelo (dispersión de rectas) en función de λ; y λ elegido por CV de 10 particiones.
- **Interactividad:** no interactivo; son bucles sobre λ.
- **Datos:** `Density_Por_data.csv`.
- **Nodos:** `ridge`, `d_sesgo` (la varianza del modelo cae al crecer λ), `d_hiper` y `d_cv`.
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1–1½ días. Ridge univariante en forma cerrada y bootstrap trivial.
- **Idea «Simular»:** demanda frente a precio con muestras pequeñas. Slider de λ. Se dibujan unas 50 rectas ajustadas a remuestras bootstrap (abanico que se cierra al subir λ). Debajo, la curva de MSE de test frente a λ y la descomposición sesgo² / varianza.

### 1.4 `MachineLearning_LASSO_regression.ipynb`: «LASSO Regression»
- **Qué enseña:** MCO, ridge y LASSO sobre los mismos datos univariantes. Barrido de λ en logspace(−2, 5) con el MSE de test. Después, datos multivariantes **estandarizados** para seguir los coeficientes al variar λ (traza: los coeficientes se anulan uno a uno).
- **Interactividad:** no interactivo.
- **Datos:** `Density_Por_data.csv` y `unconv_MV_v5.csv` (6 predictores).
- **Nodos:** `lasso`, `ridge`, `enet` (por contraste), `d_prep` (estandarizar antes de penalizar) y `d_interp` (coeficientes).
- **Duplica:** no.
- **Viabilidad JS:** **Media-Alta**, 1½–2 días. Un descenso por coordenadas para LASSO o Elastic Net en JS ocupa unas 40 líneas.
- **Idea «Simular»:** precio de vivienda con 6–8 predictores sintéticos, 2–3 de ellos irrelevantes y 2 correlacionados. Slider de log λ y slider de `l1_ratio` (0 = ridge, 1 = LASSO), lo que cubre `ridge`, `lasso` y `enet` en un solo simulador. Traza de coeficientes con una línea vertical en λ y la curva de error de CV con la regla del error típico.

### 1.5 `MachineLearning_Bayesian_linear_regression.ipynb`: «Bayesian Linear Regression with Metropolis-Hastings MCMC»
- **Qué enseña:** priori normal sobre pendiente, ordenada y σ; muestreador Metropolis-Hastings implementado a mano; cadenas, burn-in y nube posterior en el plano pendiente–ordenada.
- **Interactividad:** no interactivo.
- **Datos:** **sintéticos generados en el cuaderno** (x uniforme y y = b1·x + b0 + ruido).
- **Nodos:** ninguno directo (MCMC está fuera del temario). Como mucho, el contexto de `ridge` como MAP con priori gaussiana.
- **Viabilidad JS:** Media (MH sencillo), pero **bajo interés**.
- **Idea:** descartar o dejar como nota al margen de `ridge`.

### 1.6 `MachineLearning_decision_tree.ipynb`: «Decision Trees» (con revisiones de Evan Morreale y Chih-Yu Tung)
- **Qué enseña:** árbol de regresión con 2 predictores. Partición del plano en rectángulos (`plot_decision_tree_regions`), ŷ escalonado frente a y, árbol subajustado (3 hojas) frente a sobreajustado (50 hojas), **curva de MSE de train y test frente a `max_leaf_nodes`** (`tree_tuning`), selección con CV de 5 particiones, extracción de reglas, importancia de variables y Pipeline.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv` (porosidad y fragilidad → producción).
- **Nodos:** `arbol_reg` y `d_sesgo` (curva de complejidad), `d_hiper` y `d_cv`; `d_interp` (importancia).
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 2 días. Un CART de regresión con 2 predictores y crecimiento best-first hasta N hojas es corto de escribir.
- **Idea «Simular»:** precio de alquiler frente a (m², distancia al centro). Slider de número de hojas. Mapa de calor del plano con los rectángulos y los puntos de train y test, curva de MSE de train y test frente al número de hojas con un marcador en la posición actual, y el árbol en texto.

### 1.7 `MachineLearning_ensemble_trees.ipynb`: «Ensemble Trees, Bagging and Random Forest»
- **Qué enseña:** bagging «a mano». Seis modelos de un solo árbol entrenados con semillas distintas muestran la **varianza del modelo**. Después, bagging con un número creciente de árboles (el mapa se suaviza) y la relación «varianza del modelo frente a promedio del conjunto». Termina con random forest, MSE **OOB** (`oob_prediction_`), importancia de variables y Pipeline.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv`.
- **Nodos:** `bagging`, `rf`, `d_cv` (OOB) y `d_sesgo`.
- **Duplica:** no. El tema 4 solo tiene simuladores de boosting y XGBoost.
- **Viabilidad JS:** **Alta-Media**, 2–3 días, reutilizando el CART de 1.6 más el bootstrap y `max_features`.
- **Idea «Simular»:** sliders de nº de árboles (1–200), profundidad y `max_features` (que convierte el bagging en un RF). A la izquierda, el mapa de predicción del conjunto; a la derecha, 3 árboles individuales; debajo, la curva de MSE OOB y de test frente al nº de árboles. Ejemplo de negocio: precio de vivienda.

### 1.8 `MachineLearning_gradient_boosting.ipynb`: «Gradient Boosting Trees»
- **Qué enseña:** boosting con tocones (1 a 6 árboles, mapa paso a paso), después 5 → 5000 árboles y árboles más profundos que los tocones, y la tasa de aprendizaje como hiperparámetro de descenso del gradiente.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv`.
- **Nodos:** `gb` y `d_train` (tasa).
- **Duplica:** **sí**, con `slides/04/simuladores/gbm_boosting.html`.
- **Viabilidad JS:** Alta, pero redundante.
- **Idea:** no hacer otro simulador; como mucho, inspirarse en la vista «mapa 2D tras k tocones» si el existente es 1D (no lo comprobé).

### 1.9 `MachineLearning_support_vector_machines.ipynb`: «Support Vector Machines»
- **Qué enseña:** SVC con kernel lineal (barrido de C), polinómico (grado × C) y RBF (γ ∈ {0,1; 1; 10}) con los vectores soporte marcados; **el efecto de no estandarizar**; rejilla C × γ con `GridSearchCV` y `StratifiedShuffleSplit` y su mapa de calor de exactitud; y modelos de rendimiento alto, medio y bajo.
- **Interactividad:** no interactivo.
- **Datos:** `12_sample_data.csv` (clasificación de facies en 2D).
- **Nodos:** `svc`, `d_prep` (estandarizar), `d_hiper` (rejilla) y `d_mclas`.
- **Duplica:** no.
- **Viabilidad JS:** **Media**, 3–4 días. Requiere un SMO simplificado o un SVM por subgradiente (Pegasos) con kernel. Es factible con n ≤ 200, pero hay más trabajo numérico que en un árbol.
- **Idea «Simular»:** abandono de clientes (antigüedad frente a gasto mensual), con datos en forma de luna o de anillo. Sliders de C y γ, selector de kernel y casilla «estandarizar». Frontera, márgenes, vectores soporte y exactitud en test.

### 1.10 `MachineLearning_knearest_neighbours.ipynb`: «k-nearest Neighbours Regression»
- **Qué enseña:** kNN con k = 1, 10 y 100, `p` y `weights`, ajuste de k con test y con CV de k particiones, y Pipeline con estandarización.
- **Nodos:** kNN está **fuera del temario**. Solo encaja como ejemplo de `d_prep` y `d_sesgo`.
- **Viabilidad:** Alta, pero de bajo interés.

### 1.11 `MachineLearning_naive_Bayes.ipynb`: «Naive Bayes Classifier»
- **Qué enseña:** GaussianNB tras discretizar la producción en clases, con matriz de confusión y mapa de probabilidad.
- **Nodos:** fuera del temario. Como mucho, ilustra `d_mclas`.
- **Interés:** bajo.

### 1.12 `MachineLearning_feature_ranking.ipynb`: «Feature Ranking»
- **Qué enseña:** catálogo de métodos de ranking: cobertura, correlación de Pearson, de Spearman, parcial y semiparcial, VIF, coeficientes B y β, importancia de un RF, información mutua (incluida la versión de relevancia y redundancia), RFE y **valores de Shapley globales** de un RF.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v4.csv`.
- **Nodos:** `d_interp` (coeficientes estandarizados, importancia, Shapley) y algo de `mco` (VIF, colinealidad).
- **Duplica:** no.
- **Viabilidad JS:** Media para un subconjunto. Correlaciones, VIF y β estandarizados son fáciles; Shapley exacto con pocos predictores es posible.
- **Idea «Simular»:** «¿Qué variable importa?» con datos sintéticos de ventas (precio, promoción, temperatura y una variable ruido correlacionada con promoción). Slider de correlación entre dos predictores, y en paralelo cómo cambian el |β| estandarizado, la importancia por permutación y el VIF. Enseña que la colinealidad reparte o confunde la importancia.

### 1.13 `MachineLearning_feature_transformations.ipynb`: «Feature Transformations»
- **Qué enseña:** truncado, corrección afín, estandarización, normalización min-max, normalizador L1/L2, binarización, discretización en k intervalos, transformación gaussiana, cuantílica y transformaciones a medida, todas con sklearn.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v4.csv`.
- **Nodos:** `d_prep`.
- **Viabilidad JS:** Alta, 1 día, pero de **valor didáctico moderado** (son histogramas antes y después).
- **Idea:** si se hace, mejor integrada en un simulador de «por qué estandarizar», por ejemplo el de la ficha 1.9 o el de LASSO, que como pieza aparte.

### 1.14 `MachineLearning_multivariate_analysis.ipynb`: «Multivariate Analysis»
- **Qué enseña:** covarianza, correlación de Pearson y de Spearman, matrices de dispersión, distribuciones marginales y condicionales.
- **Nodos:** contexto de EDA; no hay nodo estimador. **Interés bajo.**

### 1.15 No supervisados (despachados)
- `MachineLearning_PCA.ipynb` (PCA, cargas, gráfico de sedimentación, reducción de dimensión) y `MachineLearning_clustering.ipynb` (k-means paso a paso): **fuera del temario**. Se descartan.

---

## 2. Proyectos de estudiantes (MachineLearningCourse, repo MIT; autoría de cada estudiante)

### 2.1 Interactivos y muy alineados con el mapa

#### `2022_MLProjects/InteractiveModelVarianceModelComplexity_Stephanie_Molitor.ipynb`: «Interactive Demo of Model Complexity & Model Variance» (Stephanie Molitor)
- **Qué enseña:** 5 modelos polinómicos de grado elegible, cada uno ajustado sobre 5 particiones aleatorias 70/30, en una cuadrícula 5 × 5 de ajustes. Debajo, el MSE medio y la varianza del MSE frente al grado.
- **Interactividad:** 5 `IntSlider` (grado de 1 a 50 para cada modelo) → `interactive_output(run_plot)`, que redibuja la cuadrícula de 25 ajustes y los dos gráficos resumen.
- **Datos:** `1D_Porosity.csv` (normalizado).
- **Nodos:** `poli` y `d_sesgo`.
- **Duplica:** **en parte** la slide «Elige el grado» del tema 1. Añade la idea de **varias realizaciones** para ver la varianza.
- **Fallos en el original** (no copiarlos):
  1. Lo llama «bootstrap», pero son 5 `train_test_split` con semillas distintas.
  2. La «varianza del modelo» se calcula como varianza del **MSE de entrenamiento**, no de las predicciones ni del error de test.
- **Viabilidad JS:** **Alta**, 1–1½ días.
- **Idea «Simular»:** complemento de «Elige el grado». Un slider de grado y un botón «nuevas muestras» que superpone unas 30 curvas ajustadas a bootstrap reales. Debajo, sesgo², varianza de la predicción y error de test frente al grado. Ejemplo: ventas frente a mes.

#### `2022_MLProjects/Boosting_Ethan_Conrad.ipynb`: «BOOST A MOVE – Exploring boosting for Regression» (Ethan Conrad)
- **Qué enseña:** GradientBoosting y AdaBoost (con `DecisionTreeRegressor` como base) sobre 2 predictores. Mapa de predicción y gráfico de estimado frente a real. Se precalculan rejillas de MSE (CSV en el repo del autor) para comparar la importancia de cada hiperparámetro.
- **Interactividad:** 3 GUIs, cada una con `IntSlider` de nº de árboles (1–500), `IntSlider` de `max_leaf_nodes` (2–15) y `FloatSlider` de `learning_rate` (0,01–1). La de GB llama a `GradBoost_make` y las dos de AdaBoost a `AdaBoost_make`; cada una redibuja el mapa 2D y el gráfico de estimado frente a real con el MSE.
- **Datos:** `unconv_MV.csv`.
- **Nodos:** `gb`, `d_train` (tasa) y `d_hiper`.
- **Duplica:** **sí, en gran parte**, `gbm_boosting.html` del tema 4.
- **Fallo en el original:** `check_model` pone «Training» en el texto, pero recibe los datos de test.
- **Viabilidad JS:** Alta, pero redundante. La comparación con AdaBoost queda fuera del mapa.
- **Idea:** solo añadir a `gbm_boosting.html` la vista del mapa 2D y la interacción «tasa × nº de árboles», si es que no la tiene (no lo comprobé).

#### `2021_MLProjects/Interactive_Basis_Regression_Derek_Burmaster.ipynb`: «Multiple Basis Regression» (Derek Burmaster)
- **Qué enseña:** dos paneles. En el primero, el usuario **construye la función verdadera** con sliders de coeficientes para x⁻⁵…x⁵, a·eᵇˣ y a·ln(bx), más ruido y semilla. En el segundo, **elige con casillas qué funciones base incluir** en la regresión lineal y ve el ajuste y el MSE frente a la verdad sin ruido.
- **Interactividad:** unos 19 `FloatSlider`/`IntSlider` (coeficientes, ruido, semilla, ejes) → `data_generator`; 13 `Checkbox` → `perform_regression`; `RadioButtons` para elegir entre datos generados y subidos.
- **Datos:** **sintéticos generados en el cuaderno**, o un CSV subido por el usuario.
- **Nodos:** `mco`, `poli` y `d_sesgo` (base insuficiente frente a sobrante).
- **Duplica:** no exactamente. Es «regresión lineal con base elegida», más general que el grado polinómico.
- **Limitación:** no tiene partición train/test. El MSE es dentro de muestra frente a la verdad.
- **Viabilidad JS:** **Alta**, 1½ días. Es MCO con columnas elegidas, resuelto con ecuaciones normales o QR.
- **Idea «Simular»** para `mco`/`poli`: «¿lineal en qué?». La demanda verdadera es, por ejemplo, a + b·ln(precio). El alumno marca bases (x, x², ln x, 1/x) y ve el ajuste, el MSE de train y test y los coeficientes. Enseña que «lineal» se refiere a los parámetros.

#### `2020_MLProjects/Saif Alkaabi/PGE383_Project_Saif_Alkaabi.ipynb`: «Interactive Bootstrap Demo» (Saif Alkaabi)
- **Qué enseña:** bootstrap de un estadístico (selector entre varios), con realizaciones que se acumulan hasta formar la distribución de incertidumbre, y desesgado por pesos opcional.
- **Interactividad:** `IntSlider` de realizaciones (100 a máx.), `FloatSlider` de % de datos, `IntSlider` de nº de realización, `Dropdown` de estadístico, `Dropdown` de variable y `ToggleButtons` de desesgado → `interactive_output(f_make)`, que redibuja el histograma de la realización y la distribución bootstrap.
- **Datos:** `sample_data_biased.csv` (porosidad y permeabilidad, muestreo preferencial).
- **Nodos:** base de `bagging`; `d_cv` (OOB/remuestreo) y `d_part` (muestreo sesgado).
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1 día.
- **Idea «Simular»:** prólogo del nodo `bagging`. Ticket medio de clientes con una muestra pequeña. Slider de nº de remuestras y de n. Se ve cómo se forma la distribución bootstrap de la media o la mediana y su intervalo, y qué fracción de observaciones queda fuera de cada remuestra (≈ 36,8 %, la base del OOB).

#### `2021_MLProjects/Logistic_Regression_Bernard_Chang.ipynb`: «Logistic Regression as a Method of Predicting NCAA Men's Basketball Tournament Games» (Bernard Chang)
- **Qué enseña:** logit con 2 estadísticas de partido frente a un modelo base (siempre gana el mejor cabeza de serie), F1 y matriz de confusión, efecto de la cantidad de datos de entrenamiento, penalización (l1, l2, elasticnet) y C.
- **Interactividad:** **mínima**. Un `Dropdown` para ver la distribución de cada estadística según y = 1 / y = 0 y un `RadioButtons` «sigmoide / lineal» que muestra cómo la sigmoide transforma el predictor lineal. Ambos con `observe`.
- **Datos:** Kaggle «March Machine Learning Mania 2021» (precompilados); **no son de subsuelo**.
- **Nodos:** `logit`, `mpl` (el contraste lineal frente a sigmoide del RadioButtons), `nulo` (modelo base) y `d_mclas`.
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1–2 días (logit por descenso del gradiente o IRLS).
- **Idea «Simular»:** conversión de un lead según su nº de visitas. Conmutador MPL / logit (recta que se sale de [0, 1] frente a sigmoide) y slider de umbral con la matriz de confusión y F1. Comparación con el modelo nulo (clase mayoritaria).

### 2.2 No interactivos pero con un experimento valioso y portable

#### `2021_MLProjects/kFold_kImpact_Dillon_Luke.ipynb`: «Examining the Impact of k in k-fold Cross-Validation on Test MSE» (Dillon Luke)
- **Qué enseña:** para k de 2 a n (LOO), repite L = 10 veces la CV de k particiones con `shuffle` y semilla distinta, y mide la **media** y la **varianza** del MSE de test entre particiones. Lo hace con MCO y con ridge (5 valores de λ), con varios niveles de ruido añadido, y además con kNN y GridSearch.
- **Conclusión del autor:** el MSE medio baja de forma no lineal al crecer k, pero la varianza sube de forma lineal; recomienda k de 5 a 20.
- **Interactividad:** no interactivo; son bucles largos y avisa del tiempo de ejecución.
- **Datos:** `unconv_MV_v5.csv`, con ruido.
- **Nodos:** **`d_cv`** (k y error típico) y `d_hiper`.
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1½ días. Con MCO o ridge en forma cerrada, LOO es barato.
- **Idea «Simular»** para `d_cv`: slider de k (2…n) y de ruido; botón «repetir 20 veces». Muestra el MSE de CV medio ± su error típico entre repeticiones y la partición de los datos coloreada por fold.

#### `2021_MLProjects/ModelVariance_Ibrahim_Gomaa.ipynb`: «Demonstrate Model Variance for a Simple Predictive ML Method with Bootstrap» (Ibrahim Gomaa)
- **Qué enseña:** ridge sobre remuestras bootstrap del train. Para 100 valores de λ en [0, 100], calcula **varianza, sesgo y ruido irreducible** «a mano» y los compara con MCO.
- **Interactividad:** no interactivo.
- **Datos:** `Density_Por_data.csv` (copia en el GitHub del autor).
- **Nodos:** **`d_sesgo`** y `ridge`.
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1 día. Se fusiona con la ficha 1.3.
- **Idea:** es el mismo simulador que la ficha 1.3, con la descomposición sesgo² + varianza + ruido apilada frente a λ.

#### `2022_MLProjects/HermitePolynomial_Peter_Miller.ipynb`: «Model variance using Hermite polynomial regression» (Peter Miller)
- **Qué enseña:** regresión con base de Hermite (`scipy.special.eval_hermitenorm`) tras una transformación normal. Con más de 1000 particiones train/test (`bootstrap_var`), mide cómo crecen el MSE y la varianza del modelo con el orden, y discute la correlación entre las funciones base.
- **Interactividad:** no interactivo.
- **Datos:** `U1417_MAD.csv` (datos geofísicos marinos del autor; Vp con ruido añadido).
- **Nodos:** `poli` y `d_sesgo`.
- **Duplica:** conceptualmente, «Elige el grado» y Molitor.
- **Viabilidad JS:** Alta. Aporta poco frente a las fichas 1.2 y Molitor.
- **Idea:** como opción «base ortogonal» dentro del complemento de la ficha 1.2.

#### `2021_MLProjects/TreeBagging_vs_RandomForest_Andres_Gonzales.ipynb`: «Tree Bagging vs Random Forests» (Andres Gonzalez)
- **Qué enseña:** con `make_regression` (1000 × 10, sin ruido) ajusta el bagging según nº de árboles y `max_depth` (1–100) con CV de 5 particiones, y después varía `max_features` de 10 a 1 en el RF (decorrelación) contra un test reservado del 30 %.
- **Interactividad:** no interactivo; avisa de 10–12 min de ejecución.
- **Datos:** **sintéticos** (`make_regression`; también importa `make_friedman1`).
- **Nodos:** `bagging`, `rf` y `d_hiper`.
- **Duplica:** no.
- **Viabilidad JS:** Media-Alta. Se integra en el simulador de la ficha 1.7 (slider `max_features`).
- **Idea:** dentro de 1.7, el gráfico «MSE frente a `max_features`», donde `max_features` = p equivale a bagging, junto con la correlación media entre las predicciones de los árboles.

#### `2022_MLProjects/BaggingVRandomForest_Jose_UbillusAlcivar.ipynb`: «Tree Bagging vs Random Forest – Does tree decorrelation actually improve prediction accuracy?» (José Ubillús Alcívar)
- **Qué enseña:** lo mismo que Gonzalez, pero con datos reales de perforación (ROP en Ecuador), dispersados a propósito, y GridSearch.
- **Conclusión del autor:** el RF es «un poco mejor, pero no fiable».
- **Interactividad:** no interactivo.
- **Nodos:** `bagging` y `rf`.
- **Viabilidad / idea:** la misma que Gonzalez; **duplica** a Gonzalez.

#### `2022_MLProjects/BaggedVnonBagged_Keivan_Khaleghi_.ipynb`: «Comparing the Performance of Non-bagged and Bagged Regression Methods Applied to a High Dimensional and Sparse Dataset» (Keivan Khaleghi)
- **Qué enseña:** MCO, ridge, LASSO, Elastic Net (con `RidgeCV`/`ElasticNetCV`), polinómica de grado 2 y árbol, frente a bagging del polinomio, bagging de árboles y RF, para predecir el **LCOE** (coste nivelado de la electricidad) de plantas geotérmicas simuladas con GEOPHIRES. Usa bootstrap del test para obtener intervalos de confianza del ajuste.
- **Interactividad:** no interactivo.
- **Datos:** Excel descargado de una URL (no lo comprobé).
- **Nodos:** `bagging`, `rf`, `enet` y `d_mreg`.
- **Viabilidad JS:** Baja como simulador. Sirve como referencia para la idea «el bagging ayuda a modelos inestables, no a MCO».
- **Idea:** contrastar con Sebastián Prez (siguiente ficha).

#### `2021_MLProjects/LinearRegression_Bagging_Sebasitan_Prez.ipynb`: «Linear Regression Bagging» (Sebastián Prez)
- **Qué enseña:** bagging de una regresión lineal. Con B remuestras, el R² y el MSE de test apenas cambian; **el bagging no ayuda a un modelo de bajo sesgo y baja varianza**.
- **Interactividad:** no interactivo.
- **Datos:** `Density_Por_data.csv`.
- **Nodos:** `bagging` y `d_sesgo`.
- **Viabilidad JS:** **Alta**, ½ día como modo extra.
- **Idea:** selector «modelo base: árbol profundo / MCO» en el simulador de bagging. Con MCO la curva de error frente a nº de modelos se queda plana; con el árbol baja.

#### `2022_MLProjects/BootstrapLinearRegression_Yuanrui_Zhu.ipynb`: «Bootstrap Linear Regression» (Yuanrui Zhu)
- **Qué enseña:** distribución bootstrap de la pendiente y la ordenada por dos métodos (**remuestrear observaciones** frente a **remuestrear residuos**), comparada con el IC analítico, más el efecto de outliers y de heterocedasticidad.
- **Interactividad:** no interactivo.
- **Datos:** `Density_Por_data.csv`.
- **Nodos:** `mco` (inferencia).
- **Viabilidad JS:** **Alta**, 1 día.
- **Idea:** en el simulador de `mco` (ficha 1.1), casillas «añadir outlier» y «heterocedasticidad» que muestran cómo el IC analítico y el bootstrap se separan.

#### `2021_MLProjects/Treee_Pruning_Olin_Carty.ipynb`: «Predicting NFL positions by exploring the effect of tree pruning…» (Olin R. Carty)
- **Qué enseña:** árbol de **clasificación**, la ruta de poda por coste-complejidad (`cost_complexity_pruning_path`) y la exactitud en train y test frente a `ccp_alpha` (gráfico escalonado). Con `ccp_alpha` óptimo pasa de 973 a 120 hojas; con `max_depth` ajustado antes de podar, a 69 hojas con ≈ 1 % menos de exactitud.
- **Interactividad:** no interactivo.
- **Datos:** combine de la NFL 2012–2021 (deportivos, **no de subsuelo**).
- **Nodos:** **`arbol_clas`**, `d_hiper` (regla del error típico aplicable) y `d_sesgo`.
- **Duplica:** no.
- **Viabilidad JS:** **Media-Alta**, 2–3 días. Hacen falta un CART de clasificación (Gini) y la poda de enlace más débil; esto último es lo más delicado.
- **Idea «Simular»** para `arbol_clas`: impago de crédito (renta frente a ratio de deuda). Slider de α de poda. Frontera rectangular, número de hojas y curva de exactitud (o log-loss) de train y test frente a α, con la regla 1-SE marcada.

#### `2021_MLProjects/SupportVectorMachines_Kernels_Ruoyu_Li.ipynb`: «Evaluation of Different Kernels in Support Vector Machines» (Ruoyu Li)
- **Qué enseña:** SVC con kernels lineal, polinómico (grados 3, 5, 7, 9 y barrido de C), gaussiano, laplaciano y sigmoide sobre **4 patrones de frontera**: lineal, circular, en franjas y diagonal. Incluye exactitud frente a C en log-log según el grado.
- **Interactividad:** no interactivo.
- **Datos:** `Modified_12_sample_data.csv` (variante de un CSV de Pyrcz, con las etiquetas reasignadas a cada patrón).
- **Nodos:** `svc` y `d_hiper`.
- **Duplica:** no, aunque se solapa con la ficha 1.9.
- **Viabilidad JS:** Media (la misma que la ficha 1.9).
- **Idea:** el **selector de patrón** (lineal, círculo, franjas, diagonal) es lo más aprovechable para el simulador de `svc`.

#### `2022_MLProjects/SupportVectorMachinesKernels_Kristen_Stewart.ipynb`: «Impact of Various Kernels for Support Vector Machines» (Kristen Stewart)
- **Qué enseña:** datos multigaussianos **sintéticos** (`rng.multivariate_normal`), con ajuste por GridSearch del kernel lineal, polinómico, RBF y sigmoide, y un **kernel exponencial a medida** (`create_exp_kernel`).
- **Interactividad:** no interactivo.
- **Nodos:** `svc`.
- **Viabilidad / idea:** la misma que Ruoyu Li, con quien se solapa. El generador sintético es reutilizable como idea.

#### `2022_MLProjects/BalancedRandomForestClassification_Haoyu_Wang.ipynb`: «Random Forest and Balanced Random Forest for Subsurface Classification» (Haoyu Wang)
- **Qué enseña:** binariza la producción (≥ 5000 = 1, clase minoritaria) y compara `RandomForestClassifier` con `imblearn.BalancedRandomForestClassifier` (submuestreo por árbol) mediante matrices de confusión, `classification_report` (precisión y exhaustividad) e importancias.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV.csv`, con ruido gaussiano.
- **Nodos:** **`d_deseq`**, `rf` y `d_mclas`.
- **Duplica:** no.
- **Viabilidad JS:** Media, 2–3 días; requiere un RF de clasificación.
- **Idea «Simular»** para `d_deseq` (se puede hacer con logit para no necesitar RF): detección de fraude con el 5 % de positivos. Conmutadores «sin tratar / ponderar clases / submuestrear» y slider de umbral, con la matriz de confusión, la curva PR y el coste esperado con costes asimétricos editables.

#### `2021_MLProjects/GradientBoosting_LearningRate_Chuxi_Liu.ipynb`: «Impact of learning rate on the robustness of gradient boosting» (Chuxi Liu)
- **Qué enseña:** 8 tasas de aprendizaje × 3 combinaciones de predictores × 3 pérdidas (L2 `ls`, L1 `lad` y `quantile`), mostrado en **gráficos tornado** de % de cambio en MSE, varianza explicada y R².
- **Conclusión del autor:** L1 y la pérdida cuantil mejoran cerca de la tasa óptima, pero empeoran en los extremos.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV.csv`.
- **Nodos:** `gb` y `d_train` (tasa, pérdida).
- **Duplica:** sí en parte (`gbm_boosting.html`).
- **Viabilidad / idea:** Media. La única idea nueva es un **selector de pérdida L2 / L1 / Huber con outliers** en el simulador de boosting existente.

#### `2022_MLProjects/BoostingHyperparameterSensitivity_Almostafa_Alhadi.ipynb`: «Investigating the Sensitivity of Hyperparameters in Gradient-Boosting» (Almostafa Alhadi)
- **Qué enseña:** sensibilidad «de uno en uno» (tasa, después nº de estimadores, después profundidad) frente a una búsqueda conjunta con GridSearchCV.
- **Conclusión del autor:** el óptimo de uno en uno difiere del conjunto, y el error diverge con tasas muy altas (≈ 10).
- **Interactividad:** no interactivo.
- **Nodos:** `gb` y **`d_hiper`**.
- **Duplica:** parcialmente el simulador de boosting.
- **Viabilidad / idea:** Media. Sirve para `d_hiper`: un mapa de calor tasa × nº de árboles donde se compara el camino «de uno en uno» con el óptimo conjunto. Puede reutilizar el motor de `gbm_boosting.html`.

#### `2022_MLProjects/HyperparameterTuningMethods_Yoon_Dongyoung.ipynb` (Dongyoung Yoon) y `2022_MLProjects/GridSearchRandomSearchANN_Ivan_Feng_.ipynb` (Ivan Feng)
- **Qué enseñan:** rejilla frente a búsqueda aleatoria frente a bayesiana (`skopt`). Yoon lo hace con RF y ANN sobre `unconv_MV.csv`; Feng con ANN sobre producción sintética generada con Carman-Kozeny y Darcy. Feng dibuja contornos del espacio de hiperparámetros con los puntos evaluados por cada método.
- **Interactividad:** no interactivos.
- **Nodos:** **`d_hiper`** y `mlp` (provisional).
- **Viabilidad JS:** **Alta** si la función objetivo es una superficie analítica sintética en lugar de entrenar modelos (1 día).
- **Idea «Simular»** para `d_hiper`: superficie de error de validación sobre (log tasa, nº de árboles), con un presupuesto de N evaluaciones. Se compara rejilla con aleatoria y se ve que la aleatoria explora mejor cuando un hiperparámetro importa poco.

#### `2022_MLProjects/Pipelines_Nataly_ChaconBuitrago.ipynb`: «Algorithm Chains and Pipeline Tutorial» (Nataly Chacón Buitrago)
- **Qué enseña:** código paso a paso frente a `Pipeline`; `StandardScaler` + PCA + estimador; Pipeline dentro de GridSearchCV; `make_pipeline`; `ColumnTransformer` con `OneHotEncoder` y `SimpleImputer` para columnas mixtas.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV.csv`.
- **Nodos:** **`d_prep`** y `d_part` (fuga de información si se escala fuera del Pipeline).
- **Duplica:** probablemente con el material Python del curso (no lo comprobé).
- **Viabilidad JS:** Media como simulador. Es más bien una referencia de código.
- **Idea «Simular»** para `d_part`/`d_prep`: un «detector de fuga». Muchos predictores de ruido; selección de variables o escalado **antes** frente a **dentro** de la CV. Se ve el error de CV optimista frente al error real de test.

#### `2022_MLProjects/Shapley_Ensemble_Abraham_Montes.ipynb`: «Global Ensemble Shapley Values» (Abraham Montes)
- **Qué enseña:** entrena 15 modelos (3 MLP, 4 SVR con kernels lineal, RBF, poli-2 y poli-3, MCO, ridge, kNN, 3 árboles y 2 RF) y calcula Shapley con `shap.KernelExplainer` en cada uno. Muestra que **el ranking de importancia cambia según el modelo** y propone agregarlo sobre el conjunto.
- **Interactividad:** no interactivo.
- **Datos:** `Well_5832_data.csv` (perforación, del GitHub del autor).
- **Nodos:** **`d_interp`** (Shapley), con contexto de `voting`/`stacking`.
- **Duplica:** no.
- **Viabilidad JS:** Media. Shapley exacto con 3–4 predictores sobre modelos simples (lineal, árbol) es factible en JS.
- **Idea «Simular»** para `d_interp`: con 4 predictores de ventas, Shapley exacto (enumerando coaliciones) para un MCO y para un árbol, mostrados lado a lado. Se ve que los rankings difieren cuando hay interacción o colinealidad.

#### `2022_MLProjects/ModelGeneralizationOverfit_Angela_Luciano.ipynb`: «Model Generalization and Overfit» (Angela Luciano)
- **Qué enseña:**
  - Primera parte: polinomios de grados 1, 3, 5 y n ajustados a sin(x) en un rango, con el MSE dentro y fuera de ese rango. **El error de extrapolación explota con la complejidad.**
  - Segunda parte: un RF entrenado solo con producción baja (o solo alta) infra- o sobreestima en el resto (`production(productionwindow)`).
- **Interactividad:** no interactivo.
- **Datos:** sintéticos (sin(x)) en la primera parte y `unconv_MV.csv` en la segunda.
- **Nodos:** `d_part` (representatividad, desplazamiento de covariables), `poli` y `rf` (los árboles no extrapolan).
- **Duplica:** no.
- **Viabilidad JS:** **Alta**, 1 día para la primera parte.
- **Idea «Simular»:** «fuera del rango». Slider del rango de entrenamiento y del grado (o un conmutador polinomio / árbol). Muestra cómo el polinomio se dispara y el árbol se queda plano fuera del rango observado. Ejemplo: demanda con precios nunca vistos.

#### `2022_MLProjects/VarianceBiasTradeOff_Shunxiang_Xia.ipynb`: «The Bias-Variance Tradeoff within Random Forest Approach» (Shunxiang Xia)
- **Qué enseña:** RF sobre resistencia del hormigón (Kaggle): reducción de variables por importancia (error y tiempo frente a nº de variables), RandomizedSearch frente a GridSearch, efecto de `n_estimators` y `max_depth`, de `bootstrap` y de `max_features`.
- **Interactividad:** no interactivo.
- **Datos:** `Concrete_Data.csv` (Kaggle, **no es de subsuelo**).
- **Nodos:** `rf`, `d_hiper` y `d_sesgo`.
- **Viabilidad / idea:** Baja-Media. Duplica las fichas 1.7 y Gonzalez; solo añade la dimensión de **tiempo de ajuste**.

#### `2022_MLProjects/GBDT_Model_ByungTark_Lee.ipynb`: «Model Bias» con GBDT (Byungtark Lee)
- **Qué enseña:** elimina al azar un % creciente de datos, imputa lo eliminado con un modelo de boosting y mide el sesgo frente a la complejidad. **Ojo:** el modelo es `CatBoostRegressor`, no sklearn; usa además `geostatspy`.
- **Interactividad:** no interactivo.
- **Datos:** `unconv_MV_v5.csv`.
- **Nodos:** `gb`, `d_prep` (imputación) y `d_sesgo`.
- **Viabilidad:** Baja-Media. **Interés bajo**; el enfoque es confuso.

#### `2022_MLProjects/LinearVsDecisionTree_Ram_Disabar_.ipynb` (Ram Disabar) y `2021_MLProjects/Linear_vs_Nonlinear_Prediction_Oriyomi_Raheem.ipynb` (Oriyomi Raheem)
- **Qué enseñan:**
  - Disabar: regresión múltiple frente a árbol con GridSearch para el potencial zeta (datos de laboratorio propios).
  - Raheem: MCO frente a polinómica (ajuste del orden) frente a kNN (ajuste de k) para la saturación de agua desde GR y NPHI.
- **Interactividad:** no interactivos.
- **Nodos:** `mco`, `poli`, `arbol_reg` y `d_sesgo` (paramétrico frente a no paramétrico).
- **Viabilidad / idea:** baja como simulador propio. Como idea, un conmutador «MCO / polinómica / árbol» sobre los mismos datos sintéticos, que puede ser un modo de la ficha 1.6.

#### `2021_MLProjects/ModelBias_Blazej_Ksiazek.ipynb`: «Demonstrating and Calculating Model Bias with Simple Predictive ML Methods» (Blazej Ksiazek)
- **Qué enseña:** «sesgo» en el sentido de **muestreo preferencial**: con submuestras con sesgo bajo y alto, compara las distribuciones de la permeabilidad predicha por MCO. No es el sesgo del equilibrio sesgo-varianza.
- **Interactividad:** no interactivo.
- **Datos:** `12_sample_data.csv`.
- **Nodos:** `d_part` (muestra no representativa).
- **Viabilidad / idea:** baja. Se solapa con Luciano y con Saif (desesgado).

#### `2021_MLProjects/Bayesian_LASSO_Rahmat_Ashari.ipynb`: «The Bayesian LASSO Regression» (Rahmat Ashari)
- **Qué enseña:** LASSO como modo de la posteriori con una priori de Laplace, comparado con el LASSO frecuentista según λ.
- **Datos:** `unconv_MV_v4.csv`.
- **Nodos:** `lasso`, como curiosidad.
- **Viabilidad / idea:** interés bajo. Como mucho, una nota que muestre la priori de Laplace frente a la gaussiana (lasso frente a ridge) en un gráfico de densidades.

### 2.3 Proyectos 2020 (títulos sacados del primer encabezado)

Son sobre todo aplicaciones de dominio con flujos estándar; ninguno es didáctico-interactivo salvo el de Saif (§2.1).

| Autor | Título (del 1.er encabezado) | Métodos | Encaje |
|---|---|---|---|
| Muneeb (Muhammad) Akmal | Elastic net regression workflow (porosidad desde AI y permeabilidad) | ElasticNet frente a MCO y ridge, ajuste de α y `l1_ratio` | `enet`; no interactivo. Referencia menor para el simulador de LASSO/ENet (ficha 1.4) |
| Rui Zhang | Boston House Prices Prediction | ranking de variables (MI, β, RF, RFE) + MCO, ridge, LASSO con barrido de λ | `mco`, `ridge`, `lasso`, `d_interp`; único 2020 con datos «de negocio» (Boston, dataset hoy desaconsejado por sesgo racial) |
| Zihao Zhao | Ensemble Trees Prediction model of production rate | ranking + bagging (nº de árboles), RF, OOB | `bagging`, `rf`; calco de la ficha 1.7 |
| Ademide O. Mabadeje | Prediction of Gas Production Using ML Techniques | RF, GB (LightGBM) con optimización bayesiana, LASSO; gráficos de fuerza de SHAP | `rf`, `gb`, `d_hiper`, `d_interp`; aplicación |
| Fritz Palacios | Random Forest for classification of depositional environments | RF de clasificación, matriz de confusión, F1 | `rf`, `d_mclas`; aplicación de subsuelo |
| Evelin Gutierrez | Predicting river depth from river width | ranking + MCO + árbol | `mco`, `arbol_reg`; aplicación |
| Athreya Suresh | PC-based Decision Tree Regression for Pilot Plant Energy | PCA + árbol | aplicación |
| Muhammad Alhotan | Response Feature Sensitivity… Using kNN | kNN | fuera del temario |
| Saif Alkaabi | Interactive Bootstrap Demo | bootstrap interactivo | **ver §2.1** |

**Descartados en 2020** (aplicaciones de dominio, no supervisados o métodos fuera del mapa):
- Brendan Elliott: mapa de tendencia al deslizamiento de fallas. Tiene widgets, pero de geomecánica.
- Eduardo Maldonado Cruz: clustering de pozos.
- Fernando Rey: barras mareales.
- Kanan Patel: ANN para PM1 en Nueva Delhi.
- Laide Ojomo: geotecnia; pedía no difundirlo.
- Lei Liu: k-means, DBSCAN y GMM.
- Lucas Mejia: segmentación microfluídica.
- Miguel Mejia: MDS + RF en experimentos de fases.
- Mohammad Abdullah: coeficientes de Carreau para un polímero.
- Moises Velasco: recuperación de petróleo en núcleos.
- Qiwei Li: PCA y clasificación.
- Ricardo Lara: red neuronal con restricción de masa.
- Ritabrata Santra: naive Bayes.
- Sofiane Achour: correlación para cálculo flash.
- Tongzhou Zeng: comportamiento de fases de un surfactante.
- Ysabel Witt-Doerring: estado del equipo de perforación.
- Zach Quintanilla: PCA.

### 2.4 Descartados de 2021 y 2022 (agrupados)

- **Clustering y no supervisado (fuera del temario):**
  - 2021: ClusterAnalysis_Fractures, ClusteringAnalysis_Hierarchical, ClusteringAnalysis_kMeansHeuristic, ClusteringMethods_Anu, Clustering_DBSCAN_multiscale, Interactive_ClusteringMethods_Syed_Tirmizi, Interactive_Clustering_PhysicsInformed_Spectral, Interactive_Clustering_k-means_vs_MeanShift, kMeansClassification, RandomProjection_Limitations, SingularValueDecomposition_DictionaryLearning.
  - 2022: ClusteringAffinityPropagation, ClusteringGaussianMixtureModels (×2), ClusteringMethods_Timur_Kuru, HierarchicalDBSCAN, K-means_vs_DBSCAN, OPTICSClustering, ImproveHWClusters, KernelPCA, NonLinearDimensionalityReduction, Random_Projection.
  - Varios de estos tienen widgets, pero de clustering.
- **Redes profundas y otros fuera del mapa:** ANNvsCNN, GraphNeuralNetworks, Fractal_Pretraining, FractalAnalysis, LSTM, NeuralNetworksClassifiers_Sandra_Vallejo (ANN en PyTorch para facies), OverfitANN_Laaiba_Akmal. Este último trata del sobreajuste de una ANN según el nº de capas, sería tangencial para `mlp`, y la propia autora reconoce problemas de entrenamiento.
- **MCMC y Monte Carlo:** Interactive_MCMC_Hector_CorzoPola, MetropolisHastings_GabrielGiozza, MonteCarloSimulation_Sabyasachi_Dash. Este último tiene widgets de muestreo de distribuciones para reservas de petróleo; fuera del mapa.
- **kNN, LDA y maldición de la dimensión** (fuera del temario): CurseofDimensionality_Yajie_Zhao, CurseofDimensionality_kNearest_Daniel_Hatchell, HighDimensionalkNN, kNNClassification, kNNFacies, kNN_Dvyadipeshkumar_Shah, kNNVsRandomForest_Mohamed_Awad, LinearDiscriminantAnalysis (×2).
- **Otros métodos o aplicaciones:**
  - IsotonicRegression_Julio_Villarroel: curvas de declinación; la regresión isotónica no está en el mapa.
  - Outlier_Detection_Evan_Sivil: Isolation Forest; fuera del mapa.
  - ROPPrediction_Eldar_Sharafutdinov: RF y GB aplicados a perforación, sin nada didáctico nuevo.

---

## 3. Síntesis: candidatos a simulador por nodo

Ordenados por valor didáctico frente a esfuerzo, sin duplicar lo existente:

| Nodo(s) | Simulador propuesto | Fuentes de inspiración | Viab. | Esfuerzo |
|---|---|---|---|---|
| `ridge`, `d_sesgo` | Abanico de rectas bootstrap frente a λ, con sesgo² / varianza / ruido | Demo ridge §«Model Variance» + Ibrahim Gomaa | Alta | 1–1½ d |
| `lasso`, `enet`, `d_prep` | Traza de coeficientes con sliders log λ y `l1_ratio`, error de CV y regla 1-SE | Demo LASSO + Akmal (ENet) | Media-Alta | 1½–2 d |
| `d_cv` | Efecto de k en la CV: media ± error típico del MSE con repeticiones | Dillon Luke | Alta | 1½ d |
| `arbol_reg` | Rectángulos 2D + curva MSE train/test frente al nº de hojas | Demo decision_tree | Alta | 2 d |
| `bagging`, `rf` | Nº de árboles / profundidad / `max_features`, OOB; modo «base = MCO» | Demo ensemble_trees + Gonzalez + Prez + Saif (bootstrap) | Alta-Media | 2–3 d (reutiliza el CART) |
| `arbol_clas` | Poda por coste-complejidad con α y regla 1-SE | Olin Carty | Media-Alta | 2–3 d |
| `logit`, `mpl`, `d_mclas` | MPL frente a sigmoide + umbral → matriz de confusión / F1 frente al modelo nulo | Bernard Chang | Alta | 1–2 d |
| `d_deseq` | Ponderar / submuestrear / mover el umbral, PR y coste | Haoyu Wang | Media | 2 d (con logit) |
| `svc` | C, γ, kernel, estandarizar; patrones lineal / círculo / franjas | Demo SVM + Ruoyu Li + Kristen Stewart | Media | 3–4 d |
| `mco`, `poli` | «Lineal en los parámetros»: elegir bases (x, x², ln x, 1/x) | Derek Burmaster | Alta | 1½ d |
| `d_part` | Extrapolación fuera del rango (polinomio frente a árbol) | Angela Luciano | Alta | 1 d |
| `d_hiper` | Rejilla frente a búsqueda aleatoria sobre una superficie sintética | Yoon, Ivan Feng, Alhadi | Alta | 1 d |
| `d_interp` | Shapley exacto con 4 predictores, MCO frente a árbol | Abraham Montes + demo feature_ranking | Media | 2 d |
| `poli` (complemento) | Varianza con bootstrap real y base ortogonal | Molitor + Peter Miller + demo polynomial | Alta | 1 d |
| `gb` | — (ya existe `gbm_boosting.html`); como mucho, un selector de pérdida L2 / L1 con outliers | Chuxi Liu, Ethan Conrad | — | — |

**Reutilizar código:** no se recomienda. Todo está en Python con sklearn y matplotlib, y además el repo de demos es CC BY-SA, que obliga a compartir igual. Lo práctico es **reimplementar las ideas en JS** con datos sintéticos de negocio y citar la fuente de inspiración (Pyrcz o el estudiante) como reconocimiento.
