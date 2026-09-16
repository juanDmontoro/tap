# Proyecto en grupo 2026-27

Materiales del proyecto del cuatrimestre (35 % de la nota; véase `externos/propuesta_docente/propuesta_docente.qmd`). Sustituye a `evaluacion/proyecto/` (2025-26), que se conserva como referencia.

Última actualización: 2026-09-15.

## Estructura

```
proyecto/proyecto2627/
├── README.md            ← este archivo: calendario de hitos y estructura
├── instrucciones/       ← proyecto_2627.qmd (enunciado para el alumnado; sucesor de
│                           evaluacion/proyecto/instrucciones/proyecto.qmd)
├── hitos/               ← una plantilla de entrega por hito (S02_datos, S04_eda, ...)
├── rubrica/             ← rúbrica de 5 dimensiones (formulación y datos, proyecto
│                           reproducible, modelización, interpretación y comunicación,
│                           defensa oral individual)
└── uso_IA/              ← registro y auditoría del uso de IA
    └── evaluacion_registro_prompts.md  ← diseño del registro de prompts (2026-09-14)
```

Las carpetas `instrucciones/`, `hitos/` y `rubrica/` están vacías a 2026-09-15: son el destino acordado para el material que se vaya creando.

## Calendario de hitos (14 semanas lectivas)

Clases del 14 de septiembre al 23 de diciembre de 2026 (calendario UV). Por decisión del profesor (2026-09-15) la programación se cierra en la **semana 14** (14-18 de diciembre); la semana del 21-23 de diciembre no cuenta como semana lectiva de la asignatura. Sesiones: teoría los martes (1 h) y práctica los jueves (3 h). Respecto a la propuesta docente se suprimen los hitos S9 (SVM) y S13 (extensión causal) y la entrega final con defensa oral pasa de S15 a S14.

| Semana | Fechas (lunes) | Hito | Tema en curso |
|:--:|:--|:--|:--|
| 2 | 21 sep | Formación de grupos (3-4), pregunta de negocio y elección de datos | 2. Selección y evaluación |
| 4 | 5 oct | Análisis exploratorio de datos (EDA) | 3. GLM con regularización |
| 6 | 19 oct | Modelo base del proyecto | 4. Ensambles |
| 8 | 2 nov | Ensambles | 4. Ensambles |
| 10 | 16 nov | Revisión intermedia con retroalimentación: comparación de modelos (ensambles o SVM) | 6. Redes neuronales |
| 14 | 14 dic | Entrega final (repositorio, memoria, registro de IA) y defensa oral | 7. Predicción y efectos causales |

Cinco hitos previos a la entrega final (S2, S4, S6, S8, S10). El factor de corrección por hitos no completados de `0_presentacion/presentacion_2627.qmd` está ajustado a 5 (2026-09-15).

El registro de uso de IA se entrega de forma acumulada en cada hito y se congela con la entrega final (protocolo en `externos/propuesta_docente/uso_IA.md`; diseño simplificado en `uso_IA/evaluacion_registro_prompts.md`).

## Datos

- Las prácticas de los temas 1-6 usan el conjunto de datos de referencia del curso: Encuesta de Estructura Salarial 2022 del INE, `TAP_project/datos/estructura_salarial_ine/ees_2022.csv.gz`.
- Cada grupo elige su propio conjunto de datos para el proyecto en la semana 2.
