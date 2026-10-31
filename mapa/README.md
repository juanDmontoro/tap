# Mapa mental de la asignatura

`mapa_mental_tap.html` es un mapa interactivo de *Técnicas Avanzadas de Predicción en Negocios*: el objetivo del aprendizaje supervisado (aproximar $f(X)$ para predecir $y$), todos los estimadores del curso agrupados por familias y las decisiones transversales que los conectan.

- Es un único archivo autocontenido (CSS y JS en línea). La única dependencia externa es KaTeX (cdnjs) para las fórmulas del panel; sin conexión a cdnjs, las fórmulas se ven como texto LaTeX y todo lo demás funciona.
- Se publica con la web del curso (`mapa/**` está en `resources` de `_quarto.yml`): <https://juandmontoro.github.io/tap/mapa/mapa_mental_tap.html>
- Cada nodo de estimador lleva un botón **Simular** desactivado con `data-simulador="<id del estimador>"`, reservado para los simuladores de una fase posterior. El panel lateral repite el botón con el mismo atributo.
- Se puede enlazar directamente a un nodo con `#nodo=<id>`, por ejemplo `mapa_mental_tap.html#nodo=lasso` o `#nodo=d_cv`.

## Insertar en Moodle

En el editor de Moodle (Aula Virtual), cambia a la vista de código HTML (botón `</>`) y pega:

```html
<iframe src="https://juandmontoro.github.io/tap/mapa/mapa_mental_tap.html"
        title="Mapa mental de Técnicas Avanzadas de Predicción en Negocios"
        width="100%" height="720" style="border:1px solid #d5dee8; border-radius:8px; max-width:100%;"
        loading="lazy" allowfullscreen></iframe>
<p><a href="https://juandmontoro.github.io/tap/mapa/mapa_mental_tap.html" target="_blank" rel="noopener">Abrir el mapa a pantalla completa</a></p>
```

Para abrir el iframe directamente en un nodo, añade el ancla a la URL, por ejemplo `.../mapa_mental_tap.html#nodo=rf`, con los identificadores de la tabla siguiente.

## Identificadores de los nodos

| Tipo | Identificadores |
|:--|:--|
| Objetivo | `objetivo` |
| Estimadores | `nulo`, `mco`, `poli`, `ridge`, `lasso`, `enet`, `mpl`, `logit`, `multinomial`, `gamma`, `poisson`, `arbol_reg`, `arbol_clas`, `bagging`, `rf`, `gb`, `xgb`, `voting`, `stacking`, `svr`, `svc`, `mlp`, `doubleml` |
| Decisiones | `decisiones`, `d_sesgo`, `d_hiper`, `d_cv`, `d_part`, `d_prep`, `d_train`, `d_mreg`, `d_mclas`, `d_deseq`, `d_interp` |

## Mantenimiento

Las reglas para elaborar, ampliar o rehacer el mapa están en [`DIRECTRICES.md`](DIRECTRICES.md): fuentes, inventario de estimadores, estructura de cada ficha, redacción, tablas de scikit-learn, enlaces a slides, diseño y verificación. Sirven también para crear el mapa de otra asignatura.

El contenido está en el bloque `CONTENIDO` del `<script>` (`DECKS`, `VOCAB`, `ROOT`, `HUB`, `FAMILIAS`, `DECISIONES` y `ESTIMADORES`). Cuando se publique un deck que ahora figura como pendiente (boosting, combinar e interpretar, SVM), basta con poner su ruta en `DECKS`: los enlaces a sus slides se activan solos. Las fichas con `pendiente: true` (redes neuronales y DoubleML) se revisan cuando haya deck.
