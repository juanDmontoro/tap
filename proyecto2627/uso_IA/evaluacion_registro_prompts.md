# Evaluación del registro de prompts: enfoque y diseño

Fecha: 2026-09-14
Estado: diseño, sin implementar
Origen: conversación sobre la slide "Uso de IA y registro" de
`TAP_project/0_presentacion/presentacion_2627.qmd` (líneas 222-236).

## 1. Problema

- La slide actual pide demasiada información por conversación (integrante,
  fecha, herramienta, modelo, qué se utilizó, qué se modificó, cómo se
  verificó, enlaces a archivos). Confunde y carga al alumno.
- Los alumnos tienen conocimientos tecnológicos medio-bajos. Es muy poco
  probable que usen git. Cualquier diseño que dependa de commits o diffs
  no es realista.
- La nota del ponente cita un protocolo `uso_IA.md` que no existe en el
  proyecto (solo hay `pics/uso_IA.png`).

## 2. Principio de diseño

Aligerar la carga del alumno y valorar la transparencia. El objeto de
auditoría es la **congruencia entre el uso declarado y el resultado
entregado**. Tres piezas bastan:

1. Registro de prompts (conversaciones exportadas).
2. Memoria.
3. Notebook con el código.

En caso de desajuste, reunión con el grupo. No hay sanción automática ni
dimensión adicional en la rúbrica (coherente con la slide "IA y
comprobación del aprendizaje").

## 3. Registro mínimo exigido al alumno

Una conversación = un archivo exportado. Integrante, fecha y herramienta
van en el nombre del archivo. Sin índice CSV, sin git, sin anotaciones.

```
registro_ia/
  2026-10-03_ana_chatgpt.md
  2026-10-05_luis_claude.html
  ...
```

Se descarta pedir:

- Modelo: suele constar en el export y los alumnos a menudo no lo saben.
- Qué se utilizó / qué se modificó: se deduce comparando conversación y
  entrega. El agente hace ese emparejamiento.
- Cómo se verificó: es lo que comprueban la auditoría y la defensa oral.
  Declararlo no aporta evidencia independiente.
- Archivos afectados: sin git no tiene sentido; el agente localiza el
  fragmento en notebook y memoria.

Texto propuesto para la slide (sustituye las dos líneas actuales):

```markdown
- Guardad cada conversación exportada en `registro_ia/` con el nombre
  `fecha_integrante_herramienta`. La conversación es la evidencia; lo
  demás se contrasta con la memoria, el notebook y en la defensa.
```

## 4. Agente de detección de desajustes

### 4.1 Qué hace

Produce un informe por grupo de "puntos a preguntar" con evidencia
citada. No emite veredicto. El profesor decide.

Comprobaciones:

1. **Cobertura del resultado**. Para cada celda de código del notebook y
   cada sección o tabla de la memoria, busca la respuesta de IA más
   parecida en el registro. Clasifica el fragmento como:
   - cubierto (coincide con una respuesta),
   - modificado (parte de una respuesta, con cambios),
   - sin rastro (no aparece en el registro).
2. **Cobertura inversa**. Conversaciones cuyo contenido no aparece en la
   entrega. Normalmente intentos descartados; conviene verlo.
3. **Coherencia interna**. Reejecuta el notebook y compara salidas con
   cifras y figuras de la memoria. Detecta resultados inventados o
   desactualizados. Es independiente del registro de IA.
4. **Preguntas para la reunión**. Tres o cuatro preguntas concretas por
   grupo, ancladas a los hallazgos.

### 4.2 Qué no hace

- No determina autoría.
- No detecta uso de IA no declarado si no hay registro. Un fragmento
  "sin rastro" puede ser código propio, copiado de apuntes o generado con
  autocompletado (Copilot y similares no dejan conversación exportable).
- No distingue si el alumno verificó lo que incorporó. Eso lo aporta la
  defensa oral.
- No usa detectores probabilísticos de texto generado.

### 4.3 Pipeline

```
entrada (por grupo)
  registro_ia/*.{md,txt,html,json}
  memoria.{pdf,qmd,docx}
  notebook.ipynb
        |
        v
1. normalizar  -> registro a texto plano (turnos usuario/asistente)
                  memoria a párrafos y tablas
                  notebook a celdas (código y markdown)
        |
        v
2. emparejar   -> por celda/párrafo, k respuestas más parecidas
                  código: coincidencia exacta y aproximada (difflib)
                  texto: similitud semántica (embeddings)
                  ignorar fragmentos cortos o genéricos (imports,
                  train_test_split, etc.) para evitar falsos positivos
        |
        v
3. reejecutar  -> notebook en entorno limpio; extraer cifras y figuras;
                  comparar con memoria
        |
        v
4. juzgar      -> llamada a modelo con el material emparejado; devuelve
                  hallazgos con citas (celda, párrafo, archivo de
                  conversación) y preguntas propuestas
        |
        v
salida
  informe_<grupo>.md  (tabla de hallazgos + preguntas)
```

Coste: una llamada por grupo con el material en contexto. Asumible para
un curso.

### 4.4 Estructura de directorios propuesta (sin implementar)

```
proyecto/proyecto2627/uso_IA/
  evaluacion_registro_prompts.md   <- este documento
  code/
    01_normalizar.py
    02_emparejar.py
    03_reejecutar.py
    04_juzgar.py
    run_all.py
  data/
    entregas/<grupo>/              <- registro_ia/, memoria, notebook
    temp/
  output/
    informe_<grupo>.md
  batch_logs/
```

## 5. Riesgos

- Falsos positivos en código genérico. Mitigación: umbral de longitud y
  lista de fragmentos comunes a ignorar.
- Exports heterogéneos (HTML de ChatGPT, texto pegado, capturas). Hace
  falta normalización; las capturas quedan fuera salvo OCR.
- Alumnos que no exportan nada. El informe lo indicará como "registro
  vacío", no como irregularidad. Se trata en la reunión.

## 6. Decisiones pendientes

- Formato de entrega de la memoria: PDF o Quarto. Condiciona el paso 1.
- Si se permiten herramientas de autocompletado. Condiciona qué cuenta
  como "sin rastro".
- Si se aplica el texto propuesto en la slide y qué hacer con la
  referencia a `uso_IA.md` en la nota del ponente (redactar el protocolo
  o eliminar la cita).
- Herramienta para el paso 4: API de Claude directamente o Claude Code
  con un skill.

## 7. Próximos pasos

1. Cerrar las decisiones del punto 6.
2. Aplicar el cambio en la slide.
3. Prototipo sobre una entrega de ejemplo (puede ser sintética) con los
   pasos 1, 2 y 4. El paso 3 (reejecución) se añade después.

## Anexo. Contenido retirado de la presentación (2026-09-14)

Slide "IA y comprobación del aprendizaje", retirada de la primera clase
por exceso de detalle. Material para la guía específica del proyecto.

```markdown
## IA y comprobación del aprendizaje {style="color:#447099"}

&nbsp;

- El registro se contrasta con el repositorio y la memoria para comprobar la coherencia y la verificación del trabajo.
- Un agente puede ayudar a localizar evidencias y proponer preguntas. **El profesor revisa los hallazgos y decide la evaluación** con la rúbrica publicada.
- El agente no califica, no determina autoría y no genera sanciones automáticas. No se utilizan detectores probabilísticos de texto generado.
- La ausencia de un prompt no demuestra por sí sola una irregularidad. Las discrepancias materiales se contrastan con el grupo.

::: {.callout-important title="Comprobaciones individuales"}
La defensa oral, la participación en el aula y el examen comprueban vuestro aprendizaje. **No se permite utilizar IA en el examen ni en la defensa.** Cada integrante debe poder explicar el trabajo y modificar código en vivo.
:::

::: {.notes}
La auditoría no añade una dimensión a la rúbrica. No están permitidos los resultados o referencias inventados ni la ocultación, selección retrospectiva o alteración del registro. El grupo puede conocer y explicar cualquier discrepancia material antes de una decisión del profesor.
:::
```
