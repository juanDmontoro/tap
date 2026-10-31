# Registro del mapa mental de TAP

Este archivo recoge el estado del mapa de *Técnicas Avanzadas de Predicción en Negocios*: las decisiones tomadas con su motivo, lo que queda pendiente y el historial de versiones. Las reglas generales, válidas también para otras asignaturas, están en [`DIRECTRICES.md`](DIRECTRICES.md).

Antes de cambiar el mapa hay que leer este archivo, para no deshacer una decisión deliberada. Al terminar cada iteración hay que actualizarlo.

## Decisiones tomadas

| Fecha | Decisión | Motivo |
|:--|:--|:--|
| 30-10-2026 | Tres tipos de nodo con un color cada uno: objetivo (marino), estimadores (azul) y decisiones (terracota). | Petición inicial del profesor. Paleta de `tap_web.scss`. |
| 30-10-2026 | Disposición en columnas: objetivo, familias, estimadores y decisiones, con los vínculos entre estimadores y decisiones en el hueco central. | Permite ver los vínculos sin que crucen el resto del árbol. |
| 30-10-2026 | Botón «Simular» desactivado con `data-simulador="<id>"` en cada estimador y en su panel. | Los simuladores llegarán en una fase posterior. |
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

## Pendientes

- Añadir a `DECKS` la ruta de los decks cuando se publiquen: boosting (`t4b`, 3 nov), combinar e interpretar (`t4c`, 10 nov) y SVM (`t5`, 17 nov). Después hay que comprobar que los ids de sus slides coinciden con el HTML publicado (directrices, 8 y 11).
- Revisar la ficha del perceptrón multicapa cuando se publique el deck del tema 6. Ahora se basa en un esquema didáctico y su fórmula de una capa oculta no aparece en los materiales.
- Redactar la ficha de DoubleML cuando haya material del tema 7.
- Implementar los simuladores que activarán los botones «Simular».

## Historial de versiones

| Fecha | Commit | Cambios |
|:--|:--|:--|
| 30-10-2026 | `37055f0` | Primera versión: 22 estimadores, 10 decisiones, buscador, vista en lista, panel lateral e integración en la web y en Moodle. |
| 30-10-2026 | `eca97cb` | Redacción revisada con las reglas anti-IA y ejemplos generales de negocio. |
| 31-10-2026 | `5a8a681` | Fichas reestructuradas, contenido de boosting, voting, stacking, interpretación y SVM (SVR y SVC), variantes sangradas, enlaces a slides, vocabulario, panel al 40 % y `DIRECTRICES.md`. |
| 31-10-2026 | `1e5425b` | Pantalla completa y atajos de zoom. |
| 31-10-2026 | este commit | Decisiones universales y este registro. |
