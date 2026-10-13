# Tema 2, semana 2: el código esencial de un proyecto con datos

Deck creado el 09-10-2026 tras la práctica del tema 2 (jueves 8-10), que fue lenta porque buena
parte de los alumnos se atascaba en Python. Fuente canónica: `02_codigo_esencial.qmd`, con notas.

## Encuadre (decisiones del profesor, 09-10-2026)

- **Deck de código interactivo.** Es la excepción natural a la política «sin código visible» de
  los decks de teoría (2026-10-01): aquí el código es el contenido. Todo el código va en celdas
  pyodide que el alumno ejecuta en su navegador. Quarto no ejecuta Python al renderizar (no hay
  `engine: jupyter` ni celdas ocultas de las que dependa el alumno).
- **Núcleo de 30 min al inicio del jueves 15-10**, antes de la práctica del tema 3. Guion en las
  notas de la slide «Tres partes de cualquier proyecto». La curva ROC es opcional (trabajo
  autónomo); la chuleta y el glosario quedan para casa.
- **Datos: Airbnb Valencia reducido** (regla de §5.2 de AGENTS.md: las slides usan Airbnb).
  `airbnb_mini.csv` lo crea `TAP_project/datos/airbnb_vlc/airbnb_mini.py` a partir de
  `listados.csv` (sin modificarlo): filtros de los decks de los temas 2-3 (30-400 €/noche,
  alojamientos enteros y habitaciones privadas), `dist_km` y `superhost` calculados, 10 columnas,
  sin valores ausentes. 6 487 anuncios, 379 KB. `listados.csv` (19,5 MB) es inviable con 40
  navegadores a la vez.
- La URL del deck es `https://juandmontoro.github.io/tap/data/airbnb_mini.csv`. **El csv debe
  estar publicado antes del jueves 15** (línea `copiar` en `publicacion/manifiesto.csv`).

## Diseño

- Plantilla de slide `.codigo`: celda pyodide a la izquierda (62 %) y, a la derecha, pestañas
  «Para pensar» (1-3 modificaciones de la misma celda) y «Respuestas» (resultado esperado,
  con las cifras reales). El botón de flechas (*Start over*) devuelve el código original.
- Las celdas comparten intérprete y se ejecutan en orden. La celda de clasificación reutiliza
  los nombres `X`, `y`, `X_train`… con los datos de clasificación (dicho en las notas).
- Nombres de los pasos iguales a los del clab del tema 2 (`"preprocesado"`, `"modelo"`,
  `"numericas"`, `"categoricas"`), para que el alumno los reconozca en los cuadernos.
- Sin plegado ni ejecución automática (a diferencia de §3.7 de `guia_contenidos.md`): el alumno
  pulsa Run. Del JS de `../semana_1/_quarto.yml` solo queda el indicador `span.pyodide-estado`
  (slide 2).
- **Diagramas de estimadores como en Jupyter** (09-10-2026, a petición del profesor). La extensión muestra el
  valor final de la celda y lo impreso como HTML sin escapar, pero convierte los objetos con `str()`, que da
  texto. El JS de `_quarto.yml`, en cuanto el intérprete está listo, carga scikit-learn y hace que
  `str(estimador)` devuelva `estimator_html_repr` (con protección contra la recursión: esa función llama a
  `str()` por dentro; sin la protección, la celda se colgaba). El código de las celdas no cambia: `pipe` al
  final de una celda dibuja el diagrama, igual que en un cuaderno. Estilo compacto en `aula.scss`. Las
  celdas `context: setup` no sirven para esto: la extensión las crea pero no las ejecuta.
- Extensión `coatless-quarto/pyodide` 0.0.1-dev.3, instalada por el profesor con `quarto add`.
  El editor Monaco fija su fuente en 17,5 pt dentro de la extensión; no se cambia.
- `02_codigo_esencial.ipynb`: las mismas celdas como respaldo sin red y chuleta. Lo genera
  `generar_cuaderno.py` desde el `.qmd`; volver a ejecutarlo si cambia el deck.

## Comprobación (09-10-2026)

- Todas las celdas ejecutadas en el entorno `tap` (scikit-learn 1.9.1) y en pyodide (Chrome
  headless, con el csv servido en local): mismas cifras. El intérprete queda listo en 2-9 s; la
  primera celda con scikit-learn tarda unos 6 s; la CV anidada, 3,6 s; el resto, menos de 2 s.
- Cifras de «Respuestas»: RMSE de Ridge (alpha = 1) 46,2 € en entrenamiento y 45,4 € en
  test, nulo 59,3 €; búsqueda: alpha = 31,62 y 46,46 €; regla del error típico: alpha = 316,23
  (límite 47,21 €); CV anidada 46,44 €; logit: exactitud 0,698 frente a 0,666 del nulo, log-loss
  0,529 frente a 0,637; matriz con umbral 0,5: VN 1 111, FP 186, FN 402, VP 248; con 0,3: 732,
  565, 111, 539; AUC 0,76.
- El cuaderno, ejecutado con `nbconvert --execute` (copia con la URL local): 14 celdas sin error.
- Botón *Start over*: tras cambiar el código de una celda, devuelve el original (comprobado por programa).
- Clic en el editor con el lienzo escalado por reveal: a 1920×1080 (escala 0,90) y a 1366×768 (escala 0,64),
  un clic en la línea 2, columna 10 coloca el cursor en ese carácter y lo tecleado entra ahí (slides 2 y 5).
- El cuaderno `.ipynb` del deck no tiene salidas: ejecutarlo en su sitio cuando el csv esté publicado.
- Pendiente: probar en Firefox y con la URL publicada.

## Revisión del 10-10-2026

- El deck selecciona 1000 observaciones con `sample(n=1000, random_state=42)`:
  762 alojamientos enteros y 238 habitaciones privadas. División de regresión: 700/300.
- Celdas ejecutadas en `tap` con el CSV local. Respuestas y notas actualizadas:
  Ridge: RMSE 43,0 € en entrenamiento, 48,8 € en test; nulo: 56,9 €.
  Con alpha=1000: 48,2/49,5 €. CV de 5 particiones: alpha=10, RMSE=43,68 €;
  con 10 particiones: alpha=10, RMSE=43,62 €. Regla del error típico: límite=46,52 €,
  alpha=316,23. CV anidada: 44,21 €. Las cifras del apartado de 09-10 corresponden
  a los 6487 anuncios originales.
- Clasificación: exactitud nulo/logit 0,663/0,737, log-loss 0,639/0,538, AUC=0,766.
  Matriz a 0,5 (VN, FP, FN, VP): 181, 18, 61, 40; a 0,3: 106, 93, 16, 85.
- El error típico usa `busqueda.n_splits_`, para que siga siendo correcto si se cambia
  el número de particiones en la actividad anterior.
- `_quarto.yml` configura `plt.show()` para insertar PNG en la salida gráfica de cada
  celda con el backend Agg. Evita depender del canvas interactivo de la extensión,
  sin cambiar el código de las celdas ni el cuaderno. También cubre la curva ROC.
- Verificación en Chrome con Pyodide y la URL publicada: ajuste real del logit sobre
  1000 observaciones, exactitud 0,737 y log-loss 0,538; PNG visible con VN=181,
  FP=18, FN=61 y VP=40. No se ha reproducido ni comprobado el fallo en Firefox.
- Regenerados el cuaderno de respaldo y los HTML con notas y sin notas.
