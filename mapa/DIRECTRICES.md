# Directrices para elaborar el mapa mental de una asignatura

Este documento fija cómo se construye y se mantiene `mapa_mental_tap.html`. Está escrito para que una persona o un agente pueda rehacer el mapa, ampliarlo con temas nuevos o crear el de otra asignatura de aprendizaje supervisado sin tomar decisiones por su cuenta. Las palabras **debe** y **no debe** indican obligaciones. **Conviene** indica una preferencia que solo se abandona con un motivo escrito en el pull request.

El documento tiene doce secciones:

1. Propósito y público
2. Fuentes
3. Inventario: qué es un nodo
4. Ficha de un estimador
5. Decisiones transversales y vínculos
6. Redacción
7. Tablas de scikit-learn
8. Enlaces a las slides
9. Diseño
10. Implementación
11. Verificación antes de entregar
12. Adaptar el mapa a otra asignatura

Al final se recogen los errores detectados en la primera versión, como ejemplos de lo que no hay que hacer.

---

## 1. Propósito y público

- El mapa es una herramienta de aprendizaje para estudiantes que cursan la asignatura por primera vez. No es un resumen para el profesor ni un glosario para expertos.
- Debe dar una visión completa de la asignatura: todos los estimadores de los materiales, incluidos los de temas todavía no impartidos, y las decisiones de aprendizaje supervisado que los conectan.
- Cada ficha debe poder entenderse sin haber visto la sesión. Si un concepto necesita una figura, la ficha enlaza la slide que la contiene (sección 8).

## 2. Fuentes

### 2.1 Qué fuentes se usan y en qué orden

1. `planificacion.qmd`: temas, sesiones y fechas, incluidos los temas futuros.
2. `materiales.qmd`: decks y cuadernos publicados.
3. Los decks publicados en `slides/` (HTML renderizado). Para leerlos, se extrae el texto de cada `<section>` de reveal.js.
4. Los `.qmd` de decks aún no publicados que facilite el profesor.
5. Los cuadernos de `clabs/` y `resueltos/`, para comprobar qué clases e importaciones de scikit-learn se usan.

### 2.2 Qué contenido de las fuentes se usa

- El contenido de una ficha debe aparecer en las slides, es decir, en el texto que ven los estudiantes. Las notas del profesor (bloques `{.notes}`) solo sirven para entender una slide. Ninguna afirmación del mapa debe apoyarse únicamente en una nota.
- Si algo no aparece en los materiales, no se añade. Se anota en la descripción del pull request.
- Cuando un tema no tiene material, su ficha se marca como provisional (`pendiente: true`) y se limita a lo que dice la planificación.

### 2.3 Qué no se sube al repositorio

- Los `.qmd` no publicados, sus textos extraídos y cualquier archivo de trabajo deben guardarse fuera del repositorio, en un directorio temporal. No deben añadirse a ningún commit.
- En `mapa/` solo viven `mapa_mental_tap.html`, `README.md` y este documento.

## 3. Inventario: qué es un nodo

### 3.1 Tipos de nodo

Hay tres tipos de nodo, cada uno con un color (sección 9):

| Tipo | Qué representa | Ejemplo |
|:--|:--|:--|
| Objetivo | La raíz: aprender $f(X)$ para predecir $y$ | Un único nodo |
| Estimadores | Familias (nodo intermedio) y estimadores (hojas) | «Modelos lineales y regularización» → «Ridge» |
| Decisiones | Nodo «Decisiones de aprendizaje supervisado» y una hoja por decisión | «Validación cruzada» |

### 3.2 Cuándo un método es un nodo de estimador

- Un método es un nodo de estimador si al menos una slide de los materiales trata sobre él: su idea, su pérdida, sus hiperparámetros o su evaluación.
- Un método que solo aparece en una fila de una tabla o se nombra de pasada no es un nodo. Se menciona en la tabla «En scikit-learn» de la ficha más cercana. Ejemplos en TAP: AdaBoost, `HistGradientBoostingRegressor` y LightGBM aparecen en la ficha de gradient boosting.
- Si un deck trata por separado la versión de regresión y la de clasificación de un método, y cada una tiene su propia pérdida o su propia lógica, son dos nodos. En TAP, SVR y SVC son dos nodos, mientras que el árbol de clasificación es un nodo derivado del de regresión.
- El modelo nulo es un nodo de estimador, porque todo modelo se compara con él.
- Las herramientas que no son estimadores, como `permutation_importance` o `GridSearchCV`, no son nodos de estimador. Se describen dentro de la decisión transversal que les corresponde.

### 3.3 Familias

- Cada estimador pertenece a una única familia. La familia agrupa estimadores que comparten la forma de la función o el tema en que se presentan.
- Las familias se ordenan según el orden de los temas.

### 3.4 Relación «extiende»

- Si un estimador se entiende como una modificación de otro de la misma familia, la ficha lo declara con `base: "<id>"`. En el mapa, el estimador derivado aparece sangrado debajo de su base y unido a ella. En el panel se muestra «Extiende: <base>».
- Ejemplos en TAP: la regresión polinómica, Ridge, Lasso y Elastic Net extienden la regresión lineal; el random forest extiende el bagging; XGBoost extiende el gradient boosting.
- Un estimador tiene como máximo una base, y la base debe ir antes que él en la lista de su familia.

## 4. Ficha de un estimador

### 4.1 Campos y orden

Cada estimador debe tener estos campos, que el panel muestra en este orden:

| Campo | Sección del panel | Contenido obligatorio |
|:--|:--|:--|
| `porque` | «Por qué este modelo» | Qué añade frente a los modelos anteriores: qué permite hacer que los otros no permiten, o cómo lo hace mejor. Dos o tres frases. |
| `idea` | Primer párrafo | Cómo funciona, en una o dos frases y sin fórmulas. |
| `modelo` | «Especificación» | La ecuación del modelo o de su pérdida (`formula`) y qué se estima en el aprendizaje (`texto`). Por ejemplo, en la regresión lineal: $y=\beta_0+\beta_1x_1+\dots+\beta_px_p+\epsilon$ y «el aprendizaje estima $\beta_0,\dots,\beta_p$». |
| `peculiar` | «Qué lo hace peculiar» | Cuatro entradas: supuestos, flexibilidad, interpretabilidad y coste computacional. Cada entrada es una o más frases completas. |
| `sklearn` | «En scikit-learn» | Las clases con su módulo y su uso (sección 7). |
| `hp` | «Hiperparámetros» | Los hiperparámetros, con nombre en castellano, argumento y efecto (sección 7). |
| `args` | «Otros argumentos» | Argumentos que no son hiperparámetros, si los materiales los usan (sección 7). |
| `links` | «Decisiones vinculadas» | Vínculos con las decisiones transversales (sección 5). |
| `slides` | «Para verlo en las slides» | Enlaces a las slides que muestran las figuras o ejemplos clave (sección 8). |
| `vocab` | «Vocabulario» | Términos técnicos que usa la ficha y que un estudiante nuevo puede no conocer. Cada término se define una vez en el diccionario `VOCAB`. |
| `sesion`, `tema` | Cabecera | Sesiones de teoría y práctica donde se ve el estimador, tomadas de la planificación. |
| `materiales` | «Materiales del tema» | Enlaces a los decks y a la página de materiales. |

### 4.2 El campo «Por qué este modelo»

- Debe responder a la pregunta «¿por qué se introduce este estimador en la asignatura?». Hay que explicar qué problema de los modelos anteriores resuelve, o qué tipo de relación puede capturar que los anteriores no capturan.
- Ejemplo correcto (regresión polinómica): «Permite capturar relaciones no lineales entre un predictor y la respuesta sin abandonar el marco de la regresión lineal».
- Ejemplo incorrecto: «Es una regresión lineal sobre potencias de $x$». Esto describe cómo funciona, pero no por qué se usa, así que corresponde al campo `idea`.

### 4.3 Botón «Simular»

Cada nodo de estimador debe llevar un botón «Simular» desactivado con `data-simulador="<id del estimador>"`. El panel repite el botón con el mismo atributo. No se implementan simuladores hasta que el profesor lo pida.

## 5. Decisiones transversales y vínculos

### 5.1 Decisiones mínimas

El nodo «Decisiones de aprendizaje supervisado» debe incluir al menos estas decisiones:

- Equilibrio sesgo-varianza.
- Selección de hiperparámetros.
- Validación cruzada, entendida como evaluación del método (procedimiento de ajuste + valores de los hiperparámetros), no de un modelo concreto ajustado.
- Partición en entrenamiento, validación y test.
- Preprocesado dentro del `Pipeline`.
- Minimizar una pérdida: pérdidas, descenso del gradiente, tasa de aprendizaje y lotes.
- Métricas de regresión.
- Métricas de clasificación.
- Clases desequilibradas.
- Interpretación: coeficientes, importancias y valores de Shapley.

### 5.2 Cómo se escribe un vínculo

- Cada vínculo es `[id de la decisión, motivo, slide opcional]`.
- El motivo debe explicar en qué afecta esa decisión a ese estimador concreto. No vale una frase genérica que serviría para cualquier estimador.
- Si el motivo se refiere a una figura, una simulación o un ejemplo de las slides, el vínculo debe llevar el enlace a esa slide. No se describe la figura con palabras que solo entiende quien la vio («el haz de curvas», «el rombo»).
- Un estimador se vincula a una decisión solo si los materiales tratan esa relación.

## 6. Redacción

### 6.1 Público

- Hay que escribir para un estudiante que ve la materia por primera vez. Antes de dar un texto por terminado, se comprueba si ese estudiante entendería cada frase sin haber asistido a clase.
- Todo término técnico se define en su primer uso dentro de la ficha o en su «Vocabulario».
- Las ideas se explican con su consecuencia. Por ejemplo, en lugar de «más $\lambda$, más sesgo», se escribe «al aumentar $\lambda$, los coeficientes se contraen y el modelo gana sesgo a cambio de menos varianza».

### 6.2 Terminología fija

| Usar | No usar | Motivo |
|:--|:--|:--|
| equilibrio sesgo-varianza | compromiso sesgo-varianza | Decisión del profesor |
| interpretar, interpretable, interpretabilidad | leer, legible (con el sentido de interpretar) | Precisión terminológica |
| predictor | columna (para referirse a un predictor) | Una columna solo es un predictor si no se ha codificado. Se usa «columna» solo para las columnas de la matriz de diseño, por ejemplo tras la codificación one-hot. |
| coste computacional | coste (a secas, si puede confundirse con el coste $C$ de las SVM o con el coste de los errores) | Ambigüedad |
| la notación de los decks: $y$, $X$, $\epsilon$, $\hat f$, $\lambda$, $\nu$, $\gamma$, $C$ | otras notaciones | Coherencia con las slides |

### 6.3 Ejemplos

- Los ejemplos deben ser generales de empresa y negocio: ventas, abandono de clientes, impago de un préstamo, importes, número de compras o de visitas.
- No se usan los conjuntos de datos concretos de los decks (en TAP, Airbnb Valencia o la EES 2022), ni sus variables, ni las cifras que dan sobre ellos (RMSE, número de hojas, porcentajes). Esas cifras se ven en la slide enlazada.
- Sí se pueden usar cifras que ilustran una propiedad general, por ejemplo que con $R_j^2=0{,}9$ la varianza de un coeficiente se multiplica por 10.

### 6.4 Reglas de estilo

Estas reglas adaptan al castellano las reglas anti-IA del autor:

- Se escriben frases completas, con sujeto y verbo. No se usa estilo telegráfico. Por ejemplo, no se escribe «Buena con grado bajo; los coeficientes de grado alto no se leen», sino «Disminuye a medida que crece el grado del polinomio y, con él, la flexibilidad del modelo».
- No se usan contrastes binarios separados por punto y coma («Sesgo y varianza son reducibles; $\sigma^2$ no»). Se escribe la relación con conectores: «Mientras el sesgo y la varianza del estimador son reducibles, el ruido no lo es».
- No se usan como plantilla las estructuras «no X, sino Y», «no solo X, sino también Y» ni las enumeraciones de tres elementos añadidas por ritmo.
- No se usan palabras de relleno o de elogio: «clave», «crucial», «fundamental», «potente», «robusto» (salvo en su sentido técnico), «poner de manifiesto», «cabe destacar», «es importante señalar que».
- No se terminan los párrafos con una frase que solo repite lo dicho.
- Los títulos y las etiquetas de los nodos no llevan comas.
- Conviene preferir verbos a nominalizaciones: «el modelo estima los coeficientes» mejor que «la estimación de los coeficientes es realizada por el modelo».

## 7. Tablas de scikit-learn

### 7.1 Estimadores («En scikit-learn»)

- Una fila por clase: clase, módulo del que se importa y uso. Ejemplo: `Ridge` · `sklearn.linear_model` · Regresión.
- Se incluyen las variantes que aparecen en los materiales (`RidgeCV`, `LinearSVR`) y las bibliotecas externas (`xgboost`, `lightgbm`, `tensorflow.keras`).
- El panel genera debajo la línea de importación: `from sklearn.linear_model import Ridge, RidgeCV`.

### 7.2 Hiperparámetros

- Un hiperparámetro es un valor que controla la complejidad o el proceso de ajuste y que se elige comparando valores con datos de validación.
- Columnas: **Hiperparámetro** (nombre en castellano, con su símbolo si los decks lo usan), **Argumento** (el nombre del argumento del estimador, sin valores) y **Efecto al aumentarlo** (una frase completa).
- Ejemplo correcto: «Profundidad máxima del árbol» · `max_depth` · «Al aumentarla, el árbol hace más preguntas seguidas y es más complejo».
- No se escribe el estimador completo en la columna del argumento (`DecisionTreeRegressor(max_depth=...)`), y no se mezclan argumentos con valores de argumentos.

### 7.3 Otros argumentos

- Los argumentos que no son hiperparámetros van en una tabla aparte, «Otros argumentos», con las columnas **Argumento**, **Valores** y **Para qué sirve**. Son argumentos que no se eligen por validación: la pérdida (`criterion`, `loss`), la estrategia del modelo nulo (`strategy`), la semilla (`random_state`), el número máximo de iteraciones (`max_iter`) o los pesos de clase (`class_weight`).
- Ejemplo correcto: `criterion` · `"squared_error"` (por defecto) · «Medida de error que minimiza cada corte».

## 8. Enlaces a las slides

- Los decks se declaran una vez en el objeto `DECKS`, con su título, su ruta y la fecha de la sesión. Un deck no publicado tiene `url: null`, y sus enlaces se muestran como texto con la indicación «por publicar». Cuando se publique, basta con poner su ruta.
- Un enlace a una slide es `[clave del deck, id de la slide, texto del enlace]`. El enlace se construye como `<url del deck>#/<id>`, porque los decks de Quarto usan `hash: true`.
- El id de una slide se toma del atributo `id` de su `<section>` en el HTML publicado. Para un deck no publicado, se calcula a partir del título con la regla de Pandoc: minúsculas; se eliminan los signos que no sean letras, números, guiones o guiones bajos; los espacios se sustituyen por guiones; se conservan las tildes. Por ejemplo, «Tasa de aprendizaje y número de árboles» da `tasa-de-aprendizaje-y-número-de-árboles`. Cuando el deck se publique, hay que comprobar los ids contra el HTML.
- No se enlazan slides cuyo título contiene fórmulas, porque su id no es predecible.
- Todos los enlaces se abren en una ventana nueva (`target="_blank" rel="noopener"`), para que el estudiante no pierda el recorrido por el mapa.

## 9. Diseño

- Paleta y tipografía de `tap_web.scss`: azul `#447099`, marino `#1F3A5F`, terracota `#E07A5F`, salvia `#81B29A`, gris `#6C757D`, crema `#F7F3EF` y fondo `#F2F5F8`.
- Un color por tipo de nodo: marino para el objetivo, azul para familias y estimadores, y terracota para las decisiones. La salvia marca la selección y las coincidencias del buscador. El borde discontinuo marca las fichas provisionales.
- El panel lateral ocupa el 40 % del ancho de la ventana, entre 440 px y 760 px. En pantallas de menos de 760 px de ancho, el panel se muestra como una hoja inferior a pantalla completa de ancho. Las tablas del panel no deben partir los nombres de clases ni de argumentos. Si no caben, la tabla se desplaza en horizontal.
- Interacción: los nodos con hijos se pliegan y despliegan. Al pulsar un estimador se resaltan sus vínculos con las decisiones y se abre el panel. Hay buscador, vista en lista y enlaces directos `#nodo=<id>`.

## 10. Implementación

- El mapa es un único archivo HTML con el CSS y el JS en línea. La única dependencia externa permitida es KaTeX desde cdnjs, con versión fija. Si no carga, las fórmulas se ven como texto LaTeX y el resto funciona.
- Debe funcionar dentro de un `<iframe>` (Moodle) y en GitHub Pages, sin `localStorage` obligatorio ni acceso a la ventana padre.
- Todo el contenido está en el bloque `CONTENIDO` del `<script>`: `DECKS`, `VOCAB`, `ROOT`, `HUB`, `FAMILIAS`, `DECISIONES` y `ESTIMADORES`. El mapa, los resaltados y los paneles se generan a partir de esos objetos. No se escribe contenido en el código de presentación.
- Los textos con fórmulas usan ``String.raw`...` `` (alias `R`), para conservar las barras invertidas de LaTeX. Las fórmulas en línea van entre `\(` y `\)`, y las de bloque entre `\[` y `\]`.
- `_quarto.yml` debe incluir `mapa/**` en `resources`, y `materiales.qmd` debe tener un botón `tap-btn` que abra el mapa.

## 11. Verificación antes de entregar

1. Abrir el HTML en Chromium sin interfaz gráfica, en escritorio (1440 × 900) y en móvil (390 × 844), y dentro de un `<iframe>`. Comprobar que no hay errores en la consola.
2. Hacer capturas con el mapa completo, con un estimador seleccionado, con una decisión seleccionada, con el buscador en uso, con las familias plegadas y con la vista en lista. Revisar las capturas y corregir lo que no se vea bien antes de seguir.
3. Comprobar que todos los ids de `links`, `slides`, `base` y `vocab` existen. El script los valida al cargar y escribe un error en la consola si alguno falta.
4. Comprobar que los ids de las slides de los decks publicados existen en el HTML.
5. Buscar en el texto del mapa las palabras y estructuras prohibidas de la sección 6: «compromiso», «leer», «legible», «columna» (revisar cada caso), el nombre de los conjuntos de datos de los decks y « no … sino ».
6. Comprobar que hay 1 botón «Simular» por estimador en el mapa.

## 12. Adaptar el mapa a otra asignatura

1. Leer las fuentes de la sección 2 de la nueva asignatura y hacer el inventario con las reglas de la sección 3.
2. Sustituir el contenido de `DECKS`, `VOCAB`, `ROOT`, `HUB`, `FAMILIAS`, `DECISIONES` y `ESTIMADORES`. El código de presentación no debe cambiar.
3. Revisar la lista de decisiones mínimas (5.1) y añadir las que la asignatura trate como transversales.
4. Cambiar la paleta solo si la asignatura tiene otra hoja de estilo, manteniendo un color por tipo de nodo.
5. Seguir la verificación de la sección 11.

---

## Anexo. Errores de la primera versión

Estos errores se corrigieron y sirven como ejemplos de lo que hay que evitar:

| Error | Ejemplo | Regla |
|:--|:--|:--|
| Ejemplos ligados a un conjunto de datos | «el precio anunciado de un alojamiento», «ser superanfitrión» | 6.3 |
| Contraste binario con punto y coma | «Sesgo y varianza son reducibles; $\sigma^2$ no» | 6.4 |
| Redacción comprimida | «Buena con grado bajo; los coeficientes de grado alto no se leen» | 6.4 |
| «Leer» por «interpretar» y «columna» por «predictor» | «cada columna tiene un coeficiente que se puede leer directamente» | 6.2 |
| Referencia a una figura sin enlace | «el haz de curvas que resulta al cambiar de muestra» | 5.2 y 8 |
| Falta la especificación del modelo | La ficha de MCO no escribía $y=\beta_0+\beta_1x_1+\dots$ ni qué se estima | 4.1 |
| Falta la justificación del estimador | Ninguna ficha explicaba qué añade el modelo frente a los anteriores | 4.2 |
| Hiperparámetros mezclados con otros argumentos | `criterion` junto a `max_depth` en la misma tabla | 7.2 y 7.3 |
| Primera columna de la tabla en inglés | `max_leaf_nodes` como nombre del hiperparámetro | 7.2 |
| Valores y llamadas en la columna del argumento | `squared_error` y `DecisionTreeRegressor(max_depth=...)` | 7.2 |
| No se indicaba la clase ni el módulo | Faltaba `from sklearn.linear_model import LinearRegression` | 7.1 |
| Panel demasiado estrecho | `LinearRegression()` partido en tres líneas | 9 |
| Variantes presentadas como modelos independientes | La regresión polinómica aparecía al mismo nivel que MCO | 3.4 |
