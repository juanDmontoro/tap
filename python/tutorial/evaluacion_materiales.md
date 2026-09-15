# Evaluación de los tutoriales de introducción a Python y cambios realizados

Fecha: 2026-09-14. Origen: `bigDataEcon/python_things/install_and_intro2_Python/quarto_docs/` (copiado íntegro en `original_en/`). Resultado: `introduccion_python.qmd` (+ `partes/`), renderizado en `introduccion_python.html`.

## 1. Decisión: fusionar en un solo documento

Los tres tutoriales originales (`0_programming_flow`, `1_Data_structures`, `2_matplotlib`; `Data_structures.qmd` es una versión anterior del segundo) se han fusionado en **un único documento con seis partes** por tres razones pedagógicas:

1. **Orden de dependencias.** El tutorial de control de flujo (0) usa listas, `range` y `append` antes de que se definan en el de estructuras de datos (1). En el documento fusionado el orden es: fundamentos → listas/tuplas/diccionarios → control de flujo y funciones → NumPy → pandas → matplotlib.
2. **Un solo punto de entrada** con índice, numeración automática y referencias cruzadas (`@sec-...`), en lugar de tres ficheros con numeración manual (que era inconsistente, véase §3).
3. **Mantenimiento**: cada parte es un fichero independiente en `partes/` incluido con `{{< include >}}`, de modo que se puede editar o reutilizar por separado, pero se distribuye un único HTML autocontenido (`embed-resources: true`).

Se mantiene el formato Quarto + extensión `pyodide` (celdas ejecutables en el navegador, sin instalación), coherente con el uso que ya se hace de la extensión en las diapositivas del curso. Se ha usado la copia más reciente de la extensión (`TAP_project/pyodide_copiar_en_extensions`, Pyodide 0.27.2) en lugar de la del origen (0.26.2).

## 2. Carencias detectadas (contenido necesario, no accesorio)

| Parte | Carencia en el original | Añadido |
|---|---|---|
| Fundamentos | **No existía**: se empezaba en `if-else` sin haber presentado variables, tipos, `print`, comentarios, sangría, `import`. | Parte 1 nueva: operadores, variables, tipos básicos y conversión, cadenas y f-strings, comparaciones y `and/or/not`, funciones vs. métodos (notación con punto), argumentos por nombre, `import` y alias, sangría como sintaxis, cómo leer un *traceback*. |
| Listas | Sin rebanadas (`a[1:3]`), sin índices negativos, sin `len`, `in`, `sorted`; sin advertencia sobre copia por referencia. | Añadido todo lo anterior (las rebanadas se reutilizan en NumPy y pandas). |
| Diccionarios | Solo `.get()`; sin añadir/modificar entradas, sin recorrido con `.items()`. | Añadido, y enlazado con su uso en el curso (DataFrames, rejillas de hiperparámetros). |
| Control de flujo | Sin `range` explicado, sin `enumerate`/`zip`, sin `break`/`continue`, sin expresión condicional en una línea. | Añadido. |
| Funciones | Sin argumentos por nombre, sin retorno múltiple, sin **`lambda`** (que luego se usa en pandas `.apply()`/`.agg()` sin haberse presentado). | Añadido. |
| NumPy | Sin **rebanadas** en arrays/matrices, sin **indexación booleana** (base del filtrado en pandas), sin operaciones con escalares, sin **agregaciones con `axis`**, sin producto matricial `@`, sin `reshape`/`shape` explicados, sin **semilla** (reproducibilidad). | Añadido; números aleatorios con `np.random.default_rng(seed)` (API recomendada) y nota sobre `random_state` en scikit-learn. |
| pandas | Sin **lectura de ficheros** (`read_csv`) ni escritura; sin inspección (`shape`, `info`, `dtypes`, `head`); sin selección de varias columnas; sin filtros con varias condiciones (`&`, `|`, `isin`); sin `sort_values`; sin **valores ausentes**; sin `np.where`/`pd.cut`; sin **`merge`**. | Añadido, con un conjunto de datos real (`tips`, 244 filas, cargado por URL en el navegador; copia en `datos/tips.csv` para VS Code). Se explican `sep`, `decimal`, `encoding` para ficheros españoles. |
| matplotlib | Sin **diagrama de dispersión** como sección (solo aparecía dentro de un subplot), sin **boxplot**, sin **guardar figuras** (`savefig`), sin la **interfaz orientada a objetos** (`fig, ax = plt.subplots()`), que es la de la documentación y la de los notebooks del curso; sin `.plot()` de pandas. | Añadido; el bloque 3D se mantiene como "complemento". |
| General | Sin soluciones a los ejercicios (material de autoestudio). | Cada "Tu turno" lleva la solución plegada. Ejercicios: 8 (antes 4). |

## 3. Errores en los materiales originales y corrección

| Fichero (original) | Error | Corrección |
|---|---|---|
| Los tres | YAML `execute: conda: environment: base`: no es una opción de Quarto (se ignora). | Eliminado. |
| `1_Data_structures.qmd` | Chunk `{r}` con rutas absolutas a `RETICULATE_PYTHON` de otras máquinas; exige R para renderizar y no aporta nada a un documento pyodide. Callout "Source" vacío. | Eliminados. |
| `0_programming_flow` | Ejercicio IMC: categorías incorrectas e incompletas ("regular entre 25 y 30, sobrepeso >30", sin el tramo 18,5–25). | Clasificación OMS: <18,5 / 18,5–25 / 25–30 / ≥30. |
| `0_programming_flow` | Plantilla `def function_name(parameter1, parameter2, ...):` en una celda ejecutable: da `SyntaxError` al pulsar Run. | Pasada a bloque no ejecutable. |
| `0_programming_flow` | Numeración: secciones 1, 2, 4 (falta la 3). | Numeración automática. |
| `1_Data_structures` | Celda de diccionarios con sangría inicial de 3 espacios: `IndentationError` al ejecutar. | Corregida. |
| `1_Data_structures` | "Dictionaries are unordered" y, en la tabla, "preserves order since 3.7": contradicción. | Conservan el orden de inserción desde 3.7. |
| `1_Data_structures` | `x[[0, 1]] # Output: array([0.1, 1.3])`: el resultado correcto es `[0.3, 0.1]`. | Corregido. |
| `1_Data_structures` | "`np.zeros([i, i])` creates a ixj matrix": índices incoherentes. | `np.zeros((i, j))`. |
| `1_Data_structures` | Texto corrupto "between 10start10start and 10stop10stop" (fórmula perdida). | $10^a$ y $10^b$. |
| `1_Data_structures` | Dos subsecciones numeradas 2.1.3; encabezado `####` 3.4.1 seguido de `###` 3.4.2. | Numeración automática y jerarquía coherente. |
| `1_Data_structures` | Lista de constructores con sangría de 4 espacios: se renderiza como bloque de código. | Reformateado. |
| `1_Data_structures` | `df.groupby('Category')['Values'].sd()`: el método no existe (`AttributeError`); es `.std()`. | Corregido. |
| `1_Data_structures` | Cinco celdas seguidas usan `df.groupby('Group')['Value']` cuando el DataFrame tiene columnas `Category`/`Values`: `KeyError` en todas (agg, lambda, cumsum, filter, quantile). | Reescritas sobre el conjunto `tips`. |
| `1_Data_structures` | `.mad()` listado como función de grupo: eliminada en pandas 2.0. | Retirada de la tabla. |
| `1_Data_structures` | `value_counts()` ilustrado sobre una columna numérica con valores todos distintos (no muestra nada útil). | Sobre una columna categórica. |
| `1_Data_structures` | Columna `Pets` con valores `'F'`, `'M'`: ejemplo confuso. | Ejemplo sustituido. |
| `1_Data_structures` | `pd.concat(axis=1)` de dos tablas con las mismas columnas: produce columnas duplicadas sin explicarlo. | Ejemplo con columnas distintas e `ignore_index`. |
| `1_Data_structures` | `np.random.rand`/`standard_normal` sin semilla (resultados no reproducibles). | `default_rng(seed)`. |
| `1_Data_structures` | Erratas: "simultaneaous", "ssee", "Furtermore", "increating". | Traducción. |
| `2_matplotlib.qmd` | Segundo callout titulado "Seaborn library" cuando describe Plotnine. | Corregido; añadido plotly (está en `tap.yml`). |
| `2_matplotlib.qmd` | Enlace a `tutorials/colors/colormaps.html` (ruta antigua de la documentación). | `users/explain/colors/colormaps.html`. |
| `2_matplotlib.qmd` | `plt.subplots_adjust(hspace=0.5)` como solución al solapamiento. | `plt.tight_layout()`, que es la recomendación general. |
| `2_matplotlib.qmd` | "If you wanna clear": registro informal. | Eliminado. |

## 4. Verificación

- Las **130 celdas ejecutables** (incluidas las 8 soluciones) se han ejecutado en orden, en un mismo espacio de nombres, con el entorno conda `tap` (Python 3.11.9, NumPy 2.1.3, pandas 2.3.3, matplotlib 3.10.6, SciPy 1.16.3): 0 errores. Las 2 celdas que provocan un error a propósito (`"42" + 1`, asignar a una tupla) lo producen.
- `quarto render introduccion_python.qmd` (Quarto 1.8.26) genera el HTML sin avisos; las referencias cruzadas resuelven; 125 celdas interactivas.
- **Ejecución en el navegador** (Pyodide 0.27.2: NumPy 2.0, pandas 2.2): el HTML se ha abierto en Chrome headless y se ha pulsado "Run Code" en las 124 celdas en orden. 122 correctas, las 2 de error a propósito fallan como deben, 22 celdas muestran gráfico (incluida la lectura del CSV por URL y el boxplot/scatter sobre `tips`). Duración total de la prueba: unos 12 minutos, dominados por la descarga de pandas y SciPy la primera vez.

## 5. Cómo renderizar

```bash
cd python/tutorial
quarto render introduccion_python.qmd
```

No hace falta Python para renderizar (las celdas no se ejecutan en el render; las ejecuta el navegador). El HTML resultante es autocontenido y se distribuye solo, pero **necesita conexión a internet** al abrirse (descarga Pyodide y el editor desde un CDN, y el CSV desde GitHub).

**Iconos de los botones (corregido).** Con `embed-resources: true`, Quarto/pandoc incrusta la hoja de estilos de Font Awesome que inyecta la extensión y escribe las fuentes como `url(data:application/octet-stream; charset=utf-8;base64,...)`. El espacio dentro de un `url()` sin comillas es CSS inválido, el navegador descarta las `@font-face` y los iconos (▶ ejecutar, reiniciar, copiar) aparecen como cuadros vacíos. Solución aplicada en la copia local de la extensión (`_extensions/coatless-quarto/pyodide/qpyodide.lua`): los dos `<link>` a CDN (Monaco y Font Awesome) llevan `data-external="1"`, con lo que pandoc no los incrusta y se cargan desde el CDN como el resto (el HTML pasa de 6,5 MB a 2,2 MB). Verificado en Chrome headless: las fuentes `Font Awesome 6 Free` 400/900 cargan y los iconos se pintan. La copia de la extensión en `TAP_project/pyodide_copiar_en_extensions` no se ha tocado; si allí se usa `embed-resources`, tendrá el mismo problema.

**Salidas con `<...>` en blanco (corregido).** La extensión insertaba la salida de cada celda con `div.innerHTML = result`, de modo que cualquier texto con forma de etiqueta (`<class 'int'>`, `<function ...>`, `<matplotlib... at 0x...>`) lo interpretaba el navegador como HTML y desaparecía; `print(type(x))` mostraba una línea vacía. Corregido en `_extensions/coatless-quarto/pyodide/qpyodide-cell-classes.js` (línea 449): `div.textContent = result`. Ninguna salida de la extensión es HTML a propósito, así que no se pierde formato. Verificado en Chrome headless: la celda de tipos muestra `<class 'int'>`, `<class 'float'>`, `<class 'str'>`, `<class 'bool'>`, `<class 'NoneType'>`. El mismo fallo está en la copia de `TAP_project`.

**Figuras de matplotlib en blanco (corregido).** La extensión creaba el elemento `<figure>` fuera del documento, lo asignaba a `document.pyodideMplTarget`, ejecutaba la celda y solo al final lo colgaba en la salida. El backend de matplotlib de Pyodide (0.27.2, `matplotlib_pyodide` 0.2.3: el backend "html5 canvas" redirige al WASM/Agg) localiza el lienzo con `document.getElementById()`, que no encuentra elementos desconectados, de modo que el dibujo síncrono de `plt.show()` se perdía y la figura dependía de un `setTimeout(draw, 1)` programado durante la ejecución. En Chrome ese temporizador vencido se ejecuta después de colgar la figura (medido: figura colgada con 0 píxeles, pintada 3 ms después por el temporizador); en Firefox y Safari puede ejecutarse antes y la figura queda en blanco. Corrección en `_extensions/coatless-quarto/pyodide/qpyodide-cell-classes.js` (`runCode`): se limpian las áreas de salida y se cuelga la `<figure>` en la salida **antes** de ejecutar el código. Verificado con un `MutationObserver` en Chrome headless: el lienzo aparece ya pintado (47.510 píxeles no blancos) antes de que se ejecute ningún temporizador. El mismo fallo está en la copia de `TAP_project`.

## 6. Pendiente de decidir

- Añadir `python/tutorial/` al mapa de directorios de `AGENTS.md` (sección 3).
- `original_en/` conserva los `.html` y carpetas `_files` del origen (4,8 MB). Pueden borrarse dejando solo los `.qmd` si se prefiere.
- Si el documento resulta pesado en navegadores modestos (125 editores), cada parte puede renderizarse por separado añadiéndole su propio YAML.
