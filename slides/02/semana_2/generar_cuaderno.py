"""Genera 02_codigo_esencial.ipynb a partir de 02_codigo_esencial.qmd.

Uso (desde esta carpeta, entorno tap):  python generar_cuaderno.py

El cuaderno es el respaldo sin red del deck y la chuleta para las prácticas: para cada slide
con celda pyodide copia el título, las preguntas «Para pensar» y el código, en el mismo orden.
Volver a ejecutar el script cada vez que cambie el .qmd.
"""
import re

import nbformat

ORIGEN = "02_codigo_esencial.qmd"
DESTINO = "02_codigo_esencial.ipynb"

texto = open(ORIGEN, encoding="utf-8").read()
# Quitar la cabecera YAML
texto = texto.split("---", 2)[2]

celdas = [nbformat.v4.new_markdown_cell(
    "# El código esencial de un proyecto con datos\n\n"
    "Técnicas Avanzadas de Predicción en Negocios · Tema 2\n\n"
    "Mismo código que el deck interactivo, en el mismo orden. Ejecuta las celdas en orden "
    "con el entorno `tap`. Para cada celda, responde a las preguntas «Para pensar» "
    "modificando la misma celda.")]

# Partir en slides: «## » abre una slide y «# » una portada de sección, solo fuera de los
# bloques de código (dentro, «# » es un comentario de Python)
bloques = [[]]
dentro_de_codigo = False
for linea in texto.splitlines():
    if linea.startswith("```"):
        dentro_de_codigo = not dentro_de_codigo
    if not dentro_de_codigo and re.match(r"#{1,2} ", linea):
        bloques.append([])
    bloques[-1].append(linea)

for lineas in bloques:
    bloque = "\n".join(lineas) + "\n"
    cabecera = bloque.splitlines()[0] if bloque.strip() else ""
    titulo = re.sub(r"\s*\{.*\}\s*$", "", cabecera.lstrip("# ")).strip()
    if cabecera.startswith("# ") and titulo:
        celdas.append(nbformat.v4.new_markdown_cell(f"# {titulo}"))
        continue
    codigo = re.search(r"```\{pyodide-python\}\n(.*?)```", bloque, flags=re.S)
    # La slide sobre los botones de las celdas pyodide no aplica en Jupyter
    if not codigo or titulo.startswith("¿Cómo se usan las celdas"):
        continue
    preguntas = re.search(r"### Para pensar\n(.*?)\n### ", bloque, flags=re.S)
    markdown = f"## {titulo}"
    if preguntas:
        markdown += "\n\n**Para pensar**\n\n" + preguntas.group(1).strip()
    celdas.append(nbformat.v4.new_markdown_cell(markdown))
    celdas.append(nbformat.v4.new_code_cell(codigo.group(1).rstrip()))

cuaderno = nbformat.v4.new_notebook(cells=celdas)
cuaderno.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(cuaderno, DESTINO)
n_codigo = sum(c.cell_type == "code" for c in celdas)
print(f"{DESTINO}: {len(celdas)} celdas, {n_codigo} de código")
