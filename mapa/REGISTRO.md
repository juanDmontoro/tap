# Registro del mapa mental de TAP

Este archivo recoge el estado del mapa de *Técnicas Avanzadas de Predicción en Negocios*: las decisiones tomadas con su motivo, lo que queda pendiente y el historial de versiones. Las reglas generales, válidas también para otras asignaturas, están en [`DIRECTRICES.md`](DIRECTRICES.md).

Antes de cambiar el mapa hay que leer este archivo, para no deshacer una decisión deliberada. Al terminar cada iteración hay que actualizarlo.

## Decisiones tomadas

| Fecha | Decisión | Motivo |
|:--|:--|:--|
| 30-10-2026 | Tres tipos de nodo con un color cada uno: objetivo (marino), estimadores (azul) y decisiones (terracota). | Petición inicial del profesor. Paleta de `tap_web.scss`. |
| 30-10-2026 | Disposición en columnas: objetivo, familias, estimadores y decisiones, con los vínculos entre estimadores y decisiones en el hueco central. | Permite ver los vínculos sin que crucen el resto del árbol. |
| 30-10-2026 | Botón «Simular» desactivado con `data-simulador="<id>"` en cada estimador y en su panel. **Sustituida el 16-11-2026.** | Los simuladores llegarán en una fase posterior. |
| 30-10-2026 | Ejemplos generales de negocio, sin datos de Airbnb ni de la EES ni cifras de los decks. | Indicación del profesor: los ejemplos ligados a un conjunto de datos son demasiado específicos. |
| 30-10-2026 | Redacción según las reglas anti-IA del autor: frases completas, sin contrastes binarios con punto y coma ni «no X, sino Y». | Indicación del profesor. |
| 31-10-2026 | «Equilibrio sesgo-varianza» en lugar de «compromiso». | Indicación del profesor. |
| 31-10-2026 | «Interpretar» en lugar de «leer» y «predictor» en lugar de «columna». | Indicación del profesor. «Columna» solo se usa para la matriz de datos tras codificar. |
| 31-10-2026 | Cada ficha empieza por «Por qué este modelo» e incluye la especificación del modelo y qué se estima. | Indicación del profesor: el mapa es una herramienta de aprendizaje para quien ve la materia por primera vez. |
| 31-10-2026 | La regresión polinómica, Ridge, Lasso y Elastic Net se muestran como variantes de MCO; el multinomial, del logit; el árbol de clasificación, el bagging y el gradient boosting, del árbol de regresión; el random forest, del bagging; y XGBoost, del gradient boosting. | Sugerencia del profesor para la polinómica, extendida al resto con el mismo criterio. |
| 31-10-2026 | SVR y SVC son dos nodos. AdaBoost, HistGradientBoosting y LightGBM no tienen nodo propio y aparecen en la ficha del gradient boosting. | Regla 3.2 de las directrices: el deck de SVM trata cada una con su pérdida, y los otros tres métodos solo ocupan una fila de una tabla. |
| 31-10-2026 | Tablas separadas para clases de scikit-learn (con módulo e importación), hiperparámetros (nombre en castellano, argumento y efecto) y otros argumentos. | Indicación del profesor: no mezclar hiperparámetros con otros argumentos ni valores con nombres de argumentos. |
| 31-10-2026 | «mtry en R» junto al `max_features` del random forest. | Petición del profesor, aunque no aparece en los decks. |
| 31-10-2026 | Panel lateral al 40 % del ancho, entre 460 y 760 px. | Se compararon 35, 40 y 45 % a 1280, 1440 y 1920 px. Con 35 % las tablas se estrechan demasiado y con 45 % el mapa queda muy reducido. |
| 31-10-2026 | Enlaces a la slide concreta, con `#/<id>`, en una ventana nueva. | Indicación del profesor: el estudiante no debe perder el recorrido por el mapa. |
| 31-10-2026 | Pantalla completa con botón y tecla F. Las teclas + y − acercan y alejan, y 0 ajusta el mapa a la pantalla. | Petición del profesor, al estilo de reveal.js. Antes, + y − plegaban la familia con el foco; plegar queda en el botón de cada nodo. |
| 31-10-2026 | Decisiones universales: la partición de los datos y la validación cruzada se vinculan a todos los modelos predictivos, y las métricas de regresión y de clasificación a todos los de su tipo. Estos vínculos solo se dibujan al seleccionar. | La partición solo se unía a 6 de 22 modelos y podía sugerir que los demás no necesitan test. |
| 31-10-2026 | Comparador de dos estimadores. El resumen se genera con reglas a partir de las fichas, sin texto escrito para cada pareja. | Petición del profesor. Con 22 estimadores predictivos hay 231 parejas, y un texto por pareja sería imposible de mantener. |
| 31-10-2026 | Escala orientativa de 0 a 4 (`NIVELES`) para flexibilidad, interpretabilidad y coste, con intervalos cuando el nivel depende de los hiperparámetros. | Los decks no tienen una escala común, pero cada ficha califica esas tres dimensiones con una palabra («Baja», «Muy alta»). La escala resume esa palabra. Los casos sin palabra en la ficha se decidieron por comparación con los demás (ver Pendientes). |
| 31-10-2026 | DoubleML no entra en el comparador. | No es un modelo predictivo, así que flexibilidad, métricas o coste no se comparan en los mismos términos. |
| 02-11-2026 | Versión en R con selector de cuatro opciones (Python, tidymodels, caret y mlr3) en un único mapa, en lugar de un mapa de R aparte. | Decisión del profesor. Así el contenido conceptual no se duplica y una corrección vale para todas las versiones. |
| 02-11-2026 | El código en R se toma de la documentación oficial de cada paquete y se comprueba ejecutándolo con las versiones actuales de conda-forge. | Decisión del profesor: los materiales del curso solo usan Python. Una primera comprobación con versiones de 2023 detectó cambios importantes al repetirla con las actuales, como la estratificación de `partition()` en mlr3, los pesos de `caretEnsemble()` y la incompatibilidad de caret con xgboost 3. |
| 02-11-2026 | mlr3 en lugar de mlr. | mlr está superado por mlr3. |
| 02-11-2026 | En tidymodels y mlr3, el gradient boosting usa xgboost. | parsnip no tiene motor para gbm y mlr3learners no incluye gbm. caret sí usa gbm (`method = "gbm"`). |
| 02-11-2026 | Voting: tidymodels y caret no tienen función propia. El mapa indica que se promedian las predicciones y que `stacks` y `caretEnsemble()` corresponden al stacking. | `caretEnsemble()` y `blend_predictions()` estiman los pesos con un modelo. |
| 31-10-2026 | Panel de comparación al 55 % del ancho (entre 600 y 1040 px). | Muestra dos columnas de texto. Al 40 %, cada columna se queda en unos 240 px a 1440 px de ancho. |
| 16-11-2026 | Primera versión para publicar en la web. El mapa no muestra botones «Simular». | Decisión del profesor: las simulaciones quedan como trabajo futuro, y un botón desactivado en cada nodo no aporta nada al estudiante. |
| 16-11-2026 | La ficha del perceptrón multicapa usa Keras (`keras.Sequential` con capas `Dense`) y solo cita `MLPRegressor` y `MLPClassifier`. | Los decks del tema 6 definen y entrenan las redes con Keras. La sección de código de esa ficha se titula «En Keras» (`implTitulo`). |
| 16-11-2026 | En las SVM, \(\gamma\) se describe como el parámetro que fija el alcance de la semejanza entre observaciones, y los pesos de los vectores de soporte se escriben \(v_i\). | Es la redacción y la notación del deck publicado del tema 5, que sustituye a «la anchura de cada campana». |
| 16-11-2026 | Ayudas de estudio: índice de secciones al principio de cada ficha, tabla resumen de los estimadores en la vista en lista y ayuda «Cómo usar el mapa» (botón «?», `#ayuda`). | Revisión pedagógica: el mapa se presenta a los estudiantes como resumen de estimadores y técnicas transversales. Las fichas son largas, faltaba una vista de conjunto y nada explicaba cómo usarlo. |
| 16-11-2026 | Al elegir Python, la URL conserva `?infra=py`. | Revisión de Copilot (PR 2): sin el parámetro, un enlace compartido se abría en R si el destinatario tenía guardada esa preferencia. |
| 16-11-2026 | En R, el GLM Gamma se muestra sin penalización y sus vínculos con las decisiones lo dicen. mlr3 necesita `link = "log"` y caret usa `poly(..., raw = TRUE)`. | Revisión de Copilot (PR 2), comprobada ejecutando el código: sin `link`, `regr.glm` ajusta el enlace inverso, y sin `raw`, `poly()` crea polinomios ortogonales. |

## Pendientes

- Redactar la ficha de DoubleML y añadir su deck a `DECKS` cuando se publique el tema 7 (15 dic). Es la única ficha provisional.
- Simuladores: no forman parte de esta versión. La exploración de los repositorios de GeostatsGuy (2-11-2026) propone candidatos por nodo, prioridades y motores de cálculo comunes en [`docs/simuladores_geostatsguy.md`](../docs/simuladores_geostatsguy.md). La web ya publica tres simuladores propios (`slides/04/simuladores/` y `slides/06/simuladores/`), que serían el primer paso.
- Ideas de la revisión pedagógica del 16-11-2026 que no se han aplicado porque exigen contenido nuevo que debe validar el profesor: una pregunta de autoevaluación por ficha, tomada de los «Para pensar» de los decks, y una línea «Cuándo no usarlo» en cada estimador.
- Añadir el cuaderno de prácticas de SVM y los de Keras a los materiales de sus fichas cuando se publiquen. Ahora enlazan los decks y la sección de materiales del tema.
- Código en R: comprobado el 2-11-2026 con R 4.5.3, tidymodels 1.4.1 (parsnip 1.6.1, tune 2.1.0, recipes 1.4.0, yardstick 1.4.0, rsample 1.3.2), caret 7.0.1, caretEnsemble 4.0.2, mlr3 1.8.0, mlr3learners 0.15.1, mlr3pipelines 0.12.0, mlr3tuning 1.6.1, mlr3extralearners 1.1.0, glmnet 5.0, ranger 0.18.0, xgboost 3.4.2.1, kernlab 0.9-33, e1071 1.7-17, gbm 2.3.1, stacks 1.1.1, DALEX 2.5.4 y DALEXtra 2.3.1. Hay que repasarlo cuando cambie la versión mayor de alguno de estos paquetes.
  - Solo queda sin ejecutar el motor brulee de parsnip, porque no está en conda-forge. Sus argumentos se tomaron de `show_model_info("mlp")`.
  - Con caret 7.0.1 y xgboost 3.4, `method = "xgbTree"` falla al ajustar. La ficha de XGBoost lo indica. Hay que revisarlo cuando se publique una versión de caret compatible.
- Revisar los niveles de `NIVELES` (DIRECTRICES, 4.4). Hay dos grupos de casos dudosos:
  - Fichas sin una palabra que fije el nivel, en las que se asignó por comparación con las demás: el coste de Lasso, Elastic Net, bagging, random forest, gradient boosting, XGBoost, SVR, SVC y MLP; la flexibilidad del bagging y del logit multinomial (media, porque tiene un conjunto de coeficientes por clase); y la interpretabilidad del logit multinomial (media).
  - Fichas en las que el nivel se aparta de la palabra: la flexibilidad de los árboles y del MLP es «muy alta» en la ficha (la del MLP se reescribió el 16-11-2026 con el deck del tema 6 y mantiene esa palabra), pero se codifica de baja a muy alta porque la ficha dice que se controla con los hiperparámetros; la de XGBoost es «alta», y se codifica de alta a muy alta porque la ficha dice que la limitan sus hiperparámetros, como en el gradient boosting.

## Historial de versiones

| Fecha | Commit | Cambios |
|:--|:--|:--|
| 30-10-2026 | `37055f0` | Primera versión: 22 estimadores, 10 decisiones, buscador, vista en lista, panel lateral e integración en la web y en Moodle. |
| 30-10-2026 | `eca97cb` | Redacción revisada con las reglas anti-IA y ejemplos generales de negocio. |
| 31-10-2026 | `5a8a681` | Fichas reestructuradas, contenido de boosting, voting, stacking, interpretación y SVM (SVR y SVC), variantes sangradas, enlaces a slides, vocabulario, panel al 40 % y `DIRECTRICES.md`. |
| 31-10-2026 | `1e5425b` | Pantalla completa y atajos de zoom. |
| 31-10-2026 | `1fa6e8d` | Decisiones universales y este registro. |
| 31-10-2026 | `2d04040` | Comparador de dos estimadores, con enlace directo `#comparar=`. |
| 02-11-2026 | `d4b0432` | Enlaces al deck de boosting (`t4b`), ya publicado. Los 13 ids de slide del mapa existen en `slides/04/04_boosting_sn.html`. |
| 02-11-2026 | `befea76` | Selector de infraestructura de código (Python, tidymodels, caret y mlr3), con `?infra=` en la URL. La versión Python no cambia. |
| 02-11-2026 | este commit | Código en R revisado con las versiones actuales de los paquetes (R 4.5.3, parsnip 1.6.1, caret 7.0.1, mlr3 1.8.0). |
| 16-11-2026 | este commit | Primera versión para publicar. Decks de los temas 4 (combinar e interpretar), 5 y 6 enlazados, con los 210 ids de slide comprobados contra el HTML publicado. Ficha del MLP reescrita con Keras, fichas de SVM adaptadas al deck publicado y fechas de sesiones y entregas según la planificación del 11-11-2026. Sin botones «Simular». Índice de ficha, tabla resumen y ayuda. Correcciones de las dos revisiones de Copilot (5 en el PR 1 y 5 en el PR 2). |
