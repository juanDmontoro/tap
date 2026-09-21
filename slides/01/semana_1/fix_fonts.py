#!/usr/bin/env python3
"""Post-render de Quarto: repara las fuentes incrustadas con `embed-resources`.

Quarto 1.8 incrusta los .woff/.woff2/.eot de Font Awesome (botones Run/Reset/Copy
de las celdas pyodide y el icono del menú de reveal) como
    url(data:application/octet-stream; charset=utf-8;base64,...)
El espacio dentro de url(...) invalida la declaración en todos los navegadores
(bad-url token), la @font-face queda sin `src` y los iconos desaparecen. Este
script reescribe el tipo MIME en los HTML generados. Se registra en _quarto.yml:
    project:
      post-render: fix_fonts.py
"""
import os
import sys

MALO = "data:application/octet-stream; charset=utf-8;base64,"
BUENO = "data:font/woff2;base64,"   # el navegador detecta el formato real por el contenido

salidas = [f for f in os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").split("\n") if f]
if not salidas:
    salidas = [a for a in sys.argv[1:] if a.endswith(".html")]

for ruta in salidas:
    if not ruta.endswith(".html") or not os.path.exists(ruta):
        continue
    with open(ruta, encoding="utf-8") as f:
        html = f.read()
    n = html.count(MALO)
    if n:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(html.replace(MALO, BUENO))
    print(f"fix_fonts: {os.path.basename(ruta)}: {n} fuentes reparadas")
