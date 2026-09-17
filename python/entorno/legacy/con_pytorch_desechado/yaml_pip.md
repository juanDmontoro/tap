
### ✅ Herramientas  de visualización:

* `plotly` – gráficos interactivos
* `dash` – dashboards web con Python
* `streamlit` – dashboards rápidos y amigables para prototipado
* `altair` – visualización declarativa
* `bokeh` – visualización interactiva en navegador

### 🔍 Por qué pytorch en lugar de tensorflow:

* En investigación y docencia, PyTorch es ampliamente preferido hoy en día por su sintaxis más intuitiva y enfoque más "pythónico", especialmente en prototipado y notebooks.
* TensorFlow sigue siendo fuerte en producción y despliegue móvil, pero para tus fines, PyTorch es la mejor elección.
* 💡 Si no tienes GPU o no la necesitas, puedes omitir la línea pytorch-cuda=11.8.

---

## ✅ YAML final para entorno `conda`

```yaml
name: ds_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - scipy
  - scikit-learn
  - matplotlib
  - seaborn
  - jupyterlab
  - ipykernel
  - shap
  - xgboost
  - lightgbm
  - pytorch
  - torchvision
  - torchaudio
  - pytorch-cuda=11.8  # Omitir si no se usa GPU
  - plotly
  - bokeh
  - altair
  - pip
  - pip:
      - dash
      - streamlit
```

> ⚠️ `dash` y `streamlit` se instalan mejor vía `pip`, ya que no siempre están bien mantenidos en `conda`.

---

💡 Guarda esto como environment.yml, luego ejecuta:

`conda env create -f environment.yml`
`conda activate ds_env`

---

## ✅ Versión `requirements.txt` para `venv` + `pip`

```txt
numpy
pandas
scipy
scikit-learn
matplotlib
seaborn
jupyterlab
ipykernel
shap
xgboost
lightgbm
torch
torchvision
torchaudio
plotly
bokeh
altair
dash
streamlit
notebook
```
---

Y los pasos para crear el entorno serían:

### Crear entorno virtual

`python3 -m venv ds_env`
`source ds_env/bin/activate  # En Windows: ds_env\Scripts\activate`


### Instalar paquetes

`pip install --upgrade pip`
`pip install -r requirements.txt`

---

## 🚀 Listo para investigación y docencia

Con esto tienes un entorno robusto para:

* Análisis de datos
* Modelado clásico y deep learning
* Interpretación de modelos (Shapley)
* Visualización avanzada y dashboards interactivos

---

## 🚀 Mantener versiones actualizadas

- Conda: puedes actualizar regularmente con: `conda update --all`
- pip: puedes verificar las versiones más recientes disponibles con: `pip list --outdated`
¿Deseas también una versión `environment.yml` + `requirements.txt` combinada en un solo archivo descargable? Puedo generarla por ti.
