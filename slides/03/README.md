# Tema 3: modelos lineales generalizados con regularización (deck único)

Deck creado el 01-10-2026 a partir del plan aprobado ese día, siguiendo los criterios de
`_tap_theme/guia_contenidos.md` y del deck del tema 2. Fuente canónica: `03_glm_familias.qmd`,
con notas. Sustituye, para 2026-27, al deck de 2025-26 `03_glms.qmd`, que el 01-10-2026 se
movió a `../legacy/2025_26_deck_glm/` junto con `03_classification_notes.qmd` (versión inglesa
antigua, con Naive Bayes, fuera del programa de 2026-27).

**07-10-2026: deck único del tema 3** (decisión del profesor). Se le añade la penalización (bloque
3), que iba a ir en un segundo deck (`../semana_2/`, nunca creado), y se aplican las reglas R29-R34
del 06-10 (`_tap_theme/reglas_edicion.md`). Los GAM y los *splines* no se tratan en
2026-27 (decisión del profesor): queda como material futuro, con `../../clabs/gams.ipynb` como
punto de partida. El nombre del fichero (`03_glm_familias`) se mantiene porque el manifiesto ya
lo publica. Versión anterior (deck, README y cuaderno del 01-10) en
`legacy/2026-10-07_antes_regularizacion/`. En `slides/` quedan sin tocar `desbalanceados.ipynb`, `ROC.xls`, `.Rhistory`, `pics/` y
`_extensions/` (este último, sin uso desde que se movió el deck de 2025-26).

**08-10-2026: revisión del profesor** (reglas R35-R39 en `_tap_theme/reglas_edicion.md`;
plan auditado por un segundo modelo antes de aplicarlo). Versión anterior (deck, README y cuaderno)
en `legacy/2026-10-08_antes_revision/`. Cambios:

- Sin D² ni desviación: los modelos se evalúan y se eligen con las métricas habituales del
  problema (RMSE de validación para el precio y las reseñas, log-loss y exactitud para las clases).
- Sin lectura de coeficientes (factores multiplicativos y odds ratios): salen las slides 11-12
  antiguas y no hay anexo (decisión del profesor).
- Bloque 1: la estimación se presenta solo como máxima verosimilitud (se maximiza ℓ(β)), con la
  definición de verosimilitud y la conexión con la RSS y con la log-loss de dos y de K clases.
  La curva en S del logit pasa al bloque 2, así que el enlace concreto solo aparece allí; la slide
  de componentes nombra las tres piezas del logit sin fórmula para que el bloque 1 responda a su
  pregunta.
- Bloque 2 en el orden logit, multinomial, Gamma, Poisson. La Poisson se centra en lo que predice
  el modelo (media predicha frente a observada por décimos); la sobredispersión pasa a las notas.
- Bloque 3: slide de elección del modelo del precio con RMSE (sustituye a la del D² y a la de
  Gamma frente a MCO), slide nueva de sobreajuste y, después, la penalización y sus ejemplos.
- *(Superada.)* Pendiente de confirmar por el profesor: la regla «un concepto concreto en un
  solo bloque» (R39). `guia_contenidos.md` no se modifica (decisión del profesor). El 08-10 la
  regla pasó a la guía; el 12-10 quedó como provisional (sección 0 de la guía).

**11-10-2026: edición del profesor** (manual en el `.qmd` y tres comentarios `<!-- JUAN: -->`). Su
versión, con el diff respecto al commit 70a0b91, está en `legacy/2026-10-11_edicion_juan/`. Cambios:

- Edición suya: redacción de las slides 2, 3, 5-7, 10-12, 15, 17-19 y 21; títulos «Solución:
  verosimilitud penalizada» y «Selección de predictores con Lasso (en el modelo logit)»; slides 6
  y 7 a dos columnas (definición a la izquierda, consecuencias y casos a la derecha, con
  sub-bullets «Ejemplos» y «Casos particulares»).
- Comentario 1 (notas): las notas pasan a ser un apoyo a la exposición en el aula, legibles sin
  ver la slide: minutos, qué muestra la figura, la afirmación, el motivo y la transición. Los
  detalles técnicos que llevaban se guardan abajo, en «Precisiones técnicas retiradas de las
  notas»; el guion por slides de las notas de la slide 3, en «Guion de la sesión».
- Comentario 2 (slide 5): la figura muestra las predicciones de los dos modelos en colores
  distintos (regresión lineal en terracota, logit en azul), con los anuncios ordenados por la
  predicción de la regresión lineal; eje vertical recortado entre −1 y 1,4 (decisión del profesor), con
  el número de puntos fuera en el pie. El eje no usa el predictor lineal ν, que se define en la
  slide 6.
- Comentario 3 (slide 15): el pie solo describe la tabla (RMSE). La log-loss del logit y del
  multinomial frente al nulo pasa a las notas de esa slide; la exactitud del multinomial, a las
  de la slide 10.
- Correcciones mías sobre su edición: líneas en blanco antes de las listas (sin ellas no se
  forman), `:::` que faltaba al cerrar las columnas de la slide 6 (dejaba un div abierto hasta
  el glosario), erratas («transforma mantiene», «Una proceso», «positoivas»), `\text{}` y
  `\mid` en $P(\text{superanfitrión}=1 \mid X)$, «función de verosimilitud ℓ(β)» →
  «log-verosimilitud ℓ(β)» y $\hat\beta$ sin subíndice, y el predictor lineal de la slide 6 en
  bloque porque se partía (R46). La pregunta 3 de «Tres preguntas» decía «¿Cómo evaluamos un
  GLM?» y la portada y la recapitulación «¿Cómo elegimos un GLM?» (R49): el profesor decidió
  «evaluamos» en las tres (la familia se elige en la pregunta 2; el GLM se evalúa).

**Cuaderno compañero**: `../../clabs/tema_03_glm_codigo.ipynb`. El deck no muestra código
(`echo: false`). El cuaderno reproduce cada figura y cifra con código legible, en el orden de
las slides. El 08-10-2026 se rehízo con un script (scratchpad de esa sesión) a partir del
anterior; se puede editar directamente el `.ipynb`. Se ejecuta con
`conda run -n tap jupyter nbconvert --to notebook --execute --inplace tema_03_glm_codigo.ipynb`.

## Objetivos de aprendizaje (R56)

Propuesta del 12-10-2026, pendiente de revisión de Juan. La guía docente 36520 no fija objetivos
por tema (solo competencias generales, como «Aplicar, utilizando software, técnicas de aprendizaje
automático supervisado»); estos se derivan de los contenidos del tema en `guia_2627.qmd` y de lo que
cubre el deck. Al terminar la sesión, el estudiante es capaz de:

1. Reconocer cuándo la regresión lineal no respeta el rango o el tipo de la respuesta (probabilidades fuera de [0, 1], precios o recuentos negativos, clases sin distancia).
2. Identificar los tres componentes de un GLM (distribución, predictor lineal y enlace) y explicar su estimación por máxima verosimilitud.
3. Elegir la familia según la respuesta (Bernoulli con logit, multinomial, Gamma y Poisson) y ajustarla en scikit-learn.
4. Evaluar y elegir GLMs por validación cruzada frente a un modelo nulo, con la métrica adecuada al problema (R35).
5. Detectar el sobreajuste, aplicar una penalización Ridge o Lasso con λ elegido por validación cruzada e interpretar un coeficiente nulo de Lasso.

«Para pensar» y objetivo que comprueba: «¿Qué dice un coeficiente igual a cero?» → 5. La columna «Métrica»
de la actividad final (12-10-2026) comprueba 3 y 4. Los objetivos 1-4
no tienen todavía una pregunta al aula propia (pendiente al revisar el deck).

## Encuadre

- **Martes 20-10, en una sola sesión de 60 min** (reajuste del 14-10-2026; el jueves 22 empieza con el deck de código esencial del tema 2 y sigue con E1). Antes: martes 13-10 y jueves 15-10. Reparto original en las
  notas de la slide 3: el martes, slides 2-17 (unos 42 min y margen); el jueves, 18-22 (unos
  17 min). Variante en una sola sesión de 60 min, también en esas notas. La práctica usa la
  EES 2022 con el cuaderno de agenteTAP del tema 3 (en revisión el 08-10); las notas del deck no
  describen su contenido hasta que el profesor lo apruebe.
- Tres bloques, que son las tres preguntas de las portadas y de la recapitulación:
  1. ¿Qué tienen en común la regresión lineal y el logit? (componentes y máxima verosimilitud)
  2. ¿Qué familia elegimos para cada respuesta? (logit, multinomial, Gamma, Poisson y tabla)
  3. ¿Cómo evaluamos un GLM? (métrica del problema, sobreajuste, penalización, Lasso)
- 26 slides con portada y cierre. Tres de glosario (23-25), que no se presentan en clase. Oculta
  con `.content-hidden`: «Lo que viene», como en el tema 2. Sin celdas pyodide.

## Promesa del tema 2 y dónde se cumple

| Promesa (tema 2, «Lo que viene» y slide del superanfitrión) | Slide |
|---|---|
| El logit como GLM: componentes y función de enlace | 6 y 9 |
| La log-loss es la pérdida del GLM binomial (ahora: maximizar ℓ equivale a minimizar la log-loss) | 7 |
| La misma penalización de la semana 2 (`LogisticRegressionCV`) | 17 y 19 |
| Tema 1, «Lo que viene»: la misma penalización en el GLM, con otra pérdida y otra función de enlace | 17-18 |

## Mapa de slides

| Slide | Contenido |
|--:|:--|
| 2-3 | Gancho («¿Sirve la regresión lineal para estas cuatro variables?»: media condicional, rango, clases sin distancia) y tres preguntas |
| 4-7 | Bloque 1: probabilidades lineales fuera de [0, 1], componentes de un GLM (con las piezas del logit), máxima verosimilitud |
| 8-13 | Bloque 2: logit (curva en S), multinomial (probabilidades por capacidad), Gamma (dispersión creciente), Poisson (media predicha frente a observada), tabla de familias |
| 14-21 | Bloque 3: elección del modelo del precio (RMSE, con MAE y R²), métricas de clasificación según el problema (superanfitrión y tramo), sobreajuste del Gamma con 300 anuncios, penalización, curvas de validación en RMSE, Lasso en el logit, «¿Qué dice un coeficiente igual a cero?» |
| 22-28 | Recapitulación, actividad final (distribución, enlace y métrica), glosario (4) y cierre |

## Datos y protocolo

- `datos/airbnb_vlc/listados.csv`: **la misma población, división y preparación que el tema 2**
  (30-400 €/noche, alojamientos enteros y habitaciones, 30 % de test con semilla 42). Todo se
  calcula con el conjunto de entrenamiento (5 324 anuncios); el test no se usa en este deck.
- Preprocesado común: el `preprocesador_c` del tema 2 (imputación por la mediana,
  estandarización, barrio y tipo con categoría de referencia, barrios con menos de 50 anuncios
  agrupados), con la lista de numéricas de cada modelo.
- Cuatro respuestas y sus modelos, sin penalización en los bloques 1-2 y en las slides 15-16:

| Respuesta | GLM | Predictores |
|---|---|---|
| `superhost` | `LogisticRegression(C=np.inf)` | los del tema 2: sin superanfitrión y con log(precio); sin los anuncios sin dato |
| tramo de precio (terciles del entrenamiento: 85 y 126 €) | `LogisticRegression(C=np.inf)` multinomial | los de `price`; el precio no entra |
| `price` | `GammaRegressor(alpha=0)`, enlace log | los 12 numéricos de la semana 2 del tema 1 + barrio y tipo |
| `number_of_reviews_ltm` | `PoissonRegressor(alpha=0)`, enlace log | sin las otras variables de reseñas (misma información) ni la valoración (falta si no hay reseñas): fuga |

- **Métricas** (08-10-2026): un solo estimador en todo el deck, la **media de las 5 particiones**
  de validación cruzada (`cross_val_score`, `cross_validate`, `GridSearchCV`; `KFold`, y
  `StratifiedKFold` para superanfitrión y tramo). RMSE para el precio y las reseñas, log-loss y
  exactitud para las clases. Modelo nulo: `DummyRegressor(strategy="mean")`,
  `DummyClassifier(strategy="prior")`. Las predicciones de `cross_val_predict` se usan solo en
  figuras (Gamma, Poisson) y para contar predicciones negativas.
- **Elección del precio** (slide 15): regresión lineal sobre el precio, MCO sobre log(precio)
  (`TransformedTargetRegressor(func=np.log, inverse_func=np.exp)`: ajuste con el logaritmo y RMSE
  en euros con `cross_val_score`) y Gamma. Diferencias emparejadas por partición en las notas.
- **Sin bucles donde scikit-learn tiene la función** (decisión del profesor, 08-10-2026): la
  figura del multinomial usa `partial_dependence` (columna de capacidad en `float`) y MCO sobre
  log, `TransformedTargetRegressor`; ambos dan exactamente las cifras de los bucles anteriores.
  Queda el bucle de los coeficientes activos del Lasso por valor de C (no hay función).
- **Poisson** (slide 12): diez grupos del mismo tamaño según la predicción de validación cruzada
  (`pd.qcut`). scikit-learn no tiene herramienta para esta figura (R30).
- **Sobreajuste y penalización** (slides 16-18):
  - Gamma del precio con los **300 anuncios de la semana 2 del tema 1** (`entreno.sample(300,
    random_state=42)`) y una columna por barrio (`min_barrio=None`; con `min_frequency=50` la
    categoría de referencia queda agrupada y el ajuste falla), frente al entrenamiento completo
    con el preprocesado común.
  - Sobreajuste: `cross_validate(..., return_train_score=True)`, RMSE medio de entrenamiento y de
    validación sin penalización.
  - `GridSearchCV` sobre `alpha` en `np.logspace(-4, 1, 11)` con
    `scoring="neg_root_mean_squared_error"`. El modelo sin penalización se dibuja como línea
    horizontal (el eje log no admite 0).
  - Logit de superanfitrión con Lasso: `LogisticRegressionCV(Cs=np.logspace(-3, 1, 9),
    l1_ratios=[1.0], solver="saga", scoring="neg_log_loss", use_legacy_attributes=False)`
    (scikit-learn 1.9.1: `penalty` obsoleto). Regla del error típico calculada con `scores_`.
    Coeficientes activos: un `LogisticRegression` por valor de C con todo el entrenamiento.
  - Gamma y Poisson solo admiten Ridge en scikit-learn (`alpha`); se dice en la slide 17.
- **Salvaguardas** (asserts del chunk de configuración):
  - slide 15: los tres modelos del precio difieren en menos de 2 € y mejoran al nulo en más de
    10 €; la lineal da algún precio negativo y Gamma y MCO sobre log ninguno;
  - slide 12: la lineal da algún recuento negativo y la Poisson ninguno;
  - sobreajuste con 300 anuncios (entrenamiento más de 10 € por debajo de validación) y no con
    todo el entrenamiento (menos de 5 €);
  - con 300 anuncios la penalización baja el RMSE de validación más de 5 € respecto a alpha = 0 y
    también en los anuncios de entrenamiento no usados; con todo el entrenamiento, la curva es
    plana (menos de 0,1 € entre alpha = 0,0001 y el mínimo);
  - `LogisticRegressionCV` elige el mínimo de la log-loss; Lasso deja coeficientes en cero; el
    texto de la slide 20 coincide con el modelo.
- `ConvergenceWarning` se trata como error al renderizar: ningún modelo avisa.

## Cifras del deck comprobadas con el cuaderno (12-10-2026, R35)

Cuaderno ejecutado entero (*Restart & Run All*, entorno `tap`) y deck renderizado en los dos perfiles
el 12-10-2026. Coinciden, como medias de las 5 particiones:

- Precio (slide 15): RMSE nulo 61,5, lineal 47,3, MCO sobre log 48,3, Gamma 48,0 €; MAE 45,2, 32,5,
  31,2 y 32,5 €; R² 0,00, 0,41, 0,38 y 0,39.
- Superanfitrión (slide 16): nulo log-loss 0,615, AUC 0,500, AP 0,305, exactitud 69,5 %; logit
  0,491, 0,804, 0,652 y 77,2 %. Tramo: tercios de 33,8, 33,2 y 33,0 %; log-loss nulo 1,10 y
  multinomial 0,80; exactitud 34 % y 64 %.
- Reseñas (notas de la slide 12): RMSE nulo 17,8 y Poisson 15,9; MAE 13,7 y 11,4.

Capturas a 1920x1080 de las slides 15, 16, 23 (las dos pestañas) y 27 sin desborde.

## Cifras del deck comprobadas con el cuaderno (08-10-2026)

*Restart & Run All* en `tap`, Linux, scikit-learn 1.9.1, unos 23 s. Coinciden todas:

- Fuera de [0, 1] 3,9 %. Tramos: cortes 85 y 126 €; exactitud 64 % (nulo 34 %).
- Log-verosimilitud / n = −log-loss: 0,479 (logit ajustado) y 0,7804 (multinomial ajustado).
- Poisson: media predicha frente a observada por décimos de 3,6/3,9 a 32,6/30,1; la regresión
  lineal predice recuentos negativos para el 1,1 %; RMSE 15,9 (Poisson), 16,4 (lineal), 17,8 (nulo).
- Precio, RMSE de validación: nulo 61,5 €, regresión lineal 47,3 €, MCO sobre log 48,3 €, Gamma
  48,0 €. Diferencias emparejadas: lineal − MCO log −0,94 ± 0,52; lineal − Gamma −0,65 ± 0,57;
  MCO log − Gamma 0,29 ± 0,16. Precios negativos de la lineal 0,11 %. Medias: observada 114,2 €,
  Gamma 114,4 €, MCO sobre log 107,0 €.
- Clases: log-loss de superanfitrión 0,61 (nulo) y 0,49 (logit); del tramo 1,10 y 0,80.
- Sobreajuste: con 300 anuncios (61 barrios, 73 columnas), RMSE 45,0 € en entrenamiento y 64,0 € en
  validación (nulo 67,6 €); con 5 324, 47,2 y 48,0 €. Habitación de 45 € en El Palmar con 483 €
  predichos (326 € con alpha = 0,0001).
- Curvas: con 300 anuncios, 59,1 € (alpha = 0,0001), mínimo 54,7 € (alpha = 0,1), 63,9 €
  (alpha = 10). Con 5 324, casi plana (≈ 47,9 €) hasta alpha = 0,01; elige 0,003. En los 5 024
  anuncios de entrenamiento no usados: 56,1 € sin penalización y 49,2 € con alpha = 0,1.
- Logit con Lasso (46 coeficientes): mínimo con C = 0,32 (log-loss 0,4889, 30 activos); regla del
  error típico C = 0,03 (0,4935, 10 activos), 4,6 milésimas más. Correlación
  capacidad-dormitorios 0,66.

## Comprobación del 08-10-2026

- Reglas consolidadas el 08-10 (R46-R50): la fórmula ℓ(β) = log L(β) de la slide 7 pasa a
  bloque (R46); el guion de la slide 3 suma los minutos de las notas con 1 min por portada (R47);
  las preguntas de bloque son idénticas en portada, «Tres preguntas» y recapitulación (R49); RMSE
  como media de las particiones en todo el deck (R50). Ninguna fórmula en línea partida (CDP).

- `&nbsp;` tras el título en todas las slides de contenido (R6 revisada el 08-10). Para que
  quepan, `aula.scss` baja la altura máxima de las figuras de `.fig-side` de 720 a 650 px.

- Render de los dos perfiles sin avisos (solo el del kernel por TCP).
- Capturas por CDP de las 26 slides (`_sn`, 1920×1080, cada pestaña por separado), midiendo el
  borde inferior del contenido: ninguna pasa de 952 px.
- Búsqueda de «D²», «desviaci», «deviance» y «d2_» en el texto visible del deck y en el cuaderno:
  sin resultados.
- Barrido del texto visible (`;`, `, no `, `sino`, `mientras que`).

## Comprobación del 11-10-2026

- Render de los dos perfiles sin avisos; las salvaguardas pasan. Capturas headless de las slides
  2, 5, 6, 7, 11 y 15 (`_sn`, 1920×1080).
- Cuaderno compañero reejecutado en `tap` (Mac): celda de la slide 5 con la nueva figura y
  títulos de las slides 17 y 19 actualizados. Coinciden fuera de [0, 1] 3,9 %; log-loss 0,61/0,49
  y 1,10/0,80; exactitud 64 % (nulo 34 %).
- Minutos de las notas sin cambios (suman 57, más 1 min por portada).
- Barrido del texto visible (`;`, `, no `, `sino`, `mientras que`): sin resultados fuera de fórmulas.

## Guion de la sesión (retirado de las notas de la slide 3 el 11-10-2026)

28 slides con portada y cierre (desde el 12-10-2026); las 4 del glosario (24-27) no se presentan.
Sesión de teoría de 60 min, martes 20-10 (reajuste del 14-10-2026), con la variante en una sola sesión; cada
bloque con 1 min de portada: apertura (2-3) 5; bloque 1, componentes y estimación (4-7) 11; bloque 2,
familias (8-13) 15; bloque 3, elección del precio, métricas de clasificación, sobreajuste y
penalización (14-18) 15; margen 14 (preguntas, o la curva del Gamma, 19, si sobra tiempo). Al inicio
de la práctica siguiente, unos 20 min: curvas de validación y Lasso (19-21) 11, recapitulación y
actividad final (22-23) 7. Variante en una sola sesión de 60 min: la actividad final pasa a la
práctica y la slide del coeficiente cero (21) se cuenta en una frase. Las notas suman 62 min por
bloque (`comprobar_deck.py`); el guion suma 64 por el minuto de dos portadas sin notas.

## Precisiones técnicas retiradas de las notas (11-10-2026)

Texto completo en `legacy/2026-10-11_edicion_juan/03_glm_familias.qmd`. Resumen, por si salen
preguntas:

- Slide 5: el modelo de probabilidad lineal se usa en econometría para estimar efectos medios.
- Slide 6: notación ν (material de 2025-26) frente a η en muchos textos; supuestos
  (independencia, media correcta con ese enlace).
- Slide 7: fórmula de la log-loss de K clases; Gamma y Poisson tienen log-verosimilitud propia
  sin métrica habitual equivalente; los estimadores minimizan −ℓ con métodos iterativos
  (lbfgs, Newton), de ahí `max_iter`.
- Slide 9: odds y enlace logit; el probit predice casi lo mismo y no se usa.
- Slide 10: `multi_class` obsoleto en scikit-learn 1.8; K predictores lineales en scikit-learn
  frente a K − 1 en `statsmodels`; logit ordenado fuera del curso.
- Slide 12: sobredispersión (varianza entre `razon_min` y `razon_max` veces la media), binomial
  negativa, `TweedieRegressor`, exposición; la figura por grupos se hace con `pd.qcut`.
- Slide 13: `TweedieRegressor(power=p)`; enlace canónico de la Gamma (inverso) frente al log.
- Slide 15: diferencias emparejadas entre candidatos con su error típico; media geométrica de
  MCO sobre log y corrección de Duan (*smearing*).
- Slide 17: escalas exactas de `alpha` y `C`; `l1_ratio` y `solver` para Lasso; Gamma y Poisson
  sin Lasso en scikit-learn (`glum` sí).
- Slide 18: precio predicho más alto con alpha = 0,0001; comprobación con los anuncios de
  entrenamiento no usados; signo negativo de `neg_root_mean_squared_error`.
- Slide 19: `LogisticRegressionCV`, `C_`, `scores_`; lista de coeficientes que conserva la regla
  del error típico.
- Slide 22: Tweedie con 1 < p < 2 si los ingresos pueden ser 0; huéspedes − 1.

## Pendiente

- Revisión del profesor de la versión del 11-10.
- Confirmar R39 («un concepto concreto en un solo bloque»).
- Publicación: `publicacion/publicar.sh slides/03` y `clabs/03`. En el clon público hay que borrar
  a mano `slides/03/03_glms.html` (deck de 2025-26).
- El cuaderno de agenteTAP del tema 3 se titula «Tema 1 · Modelos Lineales Generalizados»: hay
  que corregirlo en su proyecto, no desde aquí.

- *(Hecho el 12-10-2026.)* **R35 reescrita** (la métrica se elige según el problema, con énfasis en una y las alternativas a la vista). Cambios aplicados, versión anterior en `legacy/2026-10-12_antes_r35/`: slide 15 con MAE y R² (con el MAE gana MCO sobre log(precio), que predice la mediana); slide 16 nueva, «La métrica de clasificación depende del problema» (superanfitrión con log-loss, AUC, AP y exactitud frente al nulo; tramo con exactitud y log-loss); MAE del Poisson en las notas de la slide 12; recapitulación 3 («diciendo por qué»); actividad final con columna «Métrica»; glosario 4/4 de métricas; cuaderno compañero con las mismas cifras (secciones de las slides 12, 15 y 16; las secciones siguientes, renumeradas).
- *(Resuelto el 14-10-2026: tema 3 el martes 20-10 en una sola sesión, E1 el jueves 22-10; ver `calendario_sesiones_2627.qmd`.)* **Planificación pendiente (12-10-2026).** El martes 13-10 no se ve el tema 3: se termina el tema 2 (clasificación con clases desequilibradas). Juan decide no modificar todavía la planificación (`guia_2627.qmd`, `calendario_sesiones_2627.qmd`): se revisa hacia el final de la semana del 12-10 según cómo vaya.
