# =============================================================================
# primer_ejemplo.py — Cómo trabajar con un script de Python en VS Code
# =============================================================================
#
# Un script .py es un fichero de texto con código. En VS Code podemos ejecutarlo
# de dos maneras:
#
#   (a) POR CELDAS (lo habitual en clase). Las líneas que empiezan por "# %%"
#       dividen el script en celdas, como en un notebook. Coloca el cursor en
#       una celda y pulsa  Shift+Enter : se ejecuta esa celda y el resultado
#       aparece en la "Interactive Window" (a la derecha). El cursor salta a la
#       celda siguiente.
#
#   (b) COMPLETO. Botón ▶ (arriba a la derecha) o, en la terminal con el
#       entorno activo:  python primer_ejemplo.py
#
# Antes de empezar: abajo a la derecha, en la barra de estado, debe aparecer
# el intérprete  tap (Python 3.11.x) . Si no, haz clic ahí y selecciónalo.
#
# En la Interactive Window, el valor de la ÚLTIMA línea de cada celda se
# muestra automáticamente (igual que en un notebook). Para mostrar algo que no
# está en la última línea, usa print().
# =============================================================================

# %% 1. Importar librerías
# Convención: las importaciones van al principio y con estos alias.
import numpy as np                # cálculo numérico, vectores y matrices
import pandas as pd               # tablas de datos (DataFrame)
import matplotlib.pyplot as plt   # gráficos

# %% 2. Números aleatorios
# Fijamos la semilla para que los resultados sean reproducibles:
# cada vez que se ejecute el script saldrán los mismos números.
np.random.seed(1)

# 10 valores de una normal estándar (media 0, desviación típica 1)
np.random.normal(0, 1, 10)

# %% 3. Simular datos con una relación no lineal
n = 1000
x = np.random.normal(0, 1, n)                        # predictor
y = 0.3 * x - 1.5 * x**2 + np.random.normal(0, 2, n) # respuesta = señal + ruido

type(x)      # ndarray: el tipo básico de NumPy

# %% 4. Un gráfico
# El gráfico aparece en la Interactive Window al ejecutar la celda.
plt.scatter(x, y, s=8, alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Relación entre x e y (datos simulados)")
plt.show()

# %% 5. Guardar los datos en un DataFrame
# Un DataFrame es una tabla: cada columna es una variable, cada fila una
# observación. Es el formato con el que trabajaremos casi siempre.
datos = pd.DataFrame({"respuesta": y, "predictor": x})
datos            # última línea de la celda -> se muestra la tabla

# %% 6. Inspeccionar el DataFrame
# Cada una de estas líneas se puede ejecutar por separado seleccionándola
# y pulsando Shift+Enter (solo se ejecuta lo seleccionado).
print(datos.shape)        # (filas, columnas)
print(datos.columns)      # nombres de las variables
datos.describe()          # resumen estadístico

# %% 7. Un primer modelo: regresión lineal con scikit-learn
# Anticipo de lo que haremos en el curso. Ajustamos y ~ x + x^2.
from sklearn.linear_model import LinearRegression

X = np.column_stack([x, x**2])    # matriz de predictores (n filas, 2 columnas)
modelo = LinearRegression().fit(X, y)

print("Coeficientes estimados:", modelo.coef_.round(3))   # verdaderos: 0.3, -1.5
print("Término independiente:", round(modelo.intercept_, 3))
print("R2:", round(modelo.score(X, y), 3))

# %% 8. Predicciones y gráfico del ajuste
malla = np.linspace(x.min(), x.max(), 200)          # valores de x ordenados
y_hat = modelo.predict(np.column_stack([malla, malla**2]))

plt.scatter(x, y, s=8, alpha=0.3, label="datos")
plt.plot(malla, y_hat, color="red", linewidth=2, label="ajuste")
plt.legend()
plt.show()

# %% 9. Ayuda sobre una función
# En VS Code, al pasar el ratón sobre una función aparece su documentación.
# También se puede pedir explícitamente:
help(np.linspace)
