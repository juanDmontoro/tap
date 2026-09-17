# %% [markdown]
# # Comprobación del entorno `tap`
# Ejecuta esta celda con el kernel `tap` seleccionado. Si todo está bien,
# verás "OK" en cada línea y un gráfico al final.

# %%
import sys, platform, importlib

print(f"Python {sys.version.split()[0]}  |  {platform.system()} {platform.machine()}")
print(f"Ejecutable: {sys.executable}")
print("-" * 60)

paquetes = ["numpy", "pandas", "scipy", "sklearn", "statsmodels",
            "matplotlib", "seaborn", "plotly", "xgboost", "lightgbm",
            "shap", "optuna", "doubleml", "graphviz", "tensorflow", "keras"]

errores = []
for p in paquetes:
    try:
        m = importlib.import_module(p)
        print(f"OK   {p:<12} {getattr(m, '__version__', '')}")
    except Exception as e:
        errores.append(p)
        print(f"FALLA {p:<12} -> {type(e).__name__}: {e}")

print("-" * 60)
print("TODO CORRECTO" if not errores else f"Faltan: {errores}")

# %%
# Prueba mínima de Keras (red de una capa sobre datos aleatorios)
import numpy as np
from tensorflow import keras

X = np.random.normal(size=(200, 3))
y = X @ np.array([1.0, -2.0, 0.5]) + np.random.normal(scale=0.1, size=200)

modelo = keras.Sequential([keras.Input(shape=(3,)), keras.layers.Dense(1)])
modelo.compile(optimizer="adam", loss="mse")
hist = modelo.fit(X, y, epochs=5, verbose=0)
print("Keras entrena correctamente. Pérdida final:", round(hist.history["loss"][-1], 3))

# %%
# Prueba de gráfico
import matplotlib.pyplot as plt
plt.plot(hist.history["loss"], marker="o")
plt.title("Si ves este gráfico, el entorno funciona")
plt.xlabel("época"); plt.ylabel("pérdida")
plt.show()
