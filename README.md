# Sprint-7---Valeria-Robles
Sprint 7 proyecto

# Análisis de Anuncios de Venta de Autos en EE.UU

Esta aplicación web, construida con **Streamlit**, permite visualizar y explorar un conjunto de datos de vehículos usados en venta en los Estados Unidos.

## 🎯 Objetivo

La aplicación tiene como propósito facilitar el análisis visual de los anuncios de autos en EE.UU., ayudando a detectar tendencias, distribuciones de precios, estado del vehículo, año del modelo y diferencias entre fabricantes.

## ⚙️ Funcionalidades

- ✅ **Visualización interactiva de los datos crudos** (con opción para excluir fabricantes poco comunes).
- 📊 **Histograma del odómetro**: analiza la distribución del kilometraje de los vehículos.
- 🔘 **Diagrama de dispersión**: relación entre odómetro y precio.
- 🏷️ **Distribución de tipos de vehículos por fabricante**.
- 🛠️ **Distribución del estado del vehículo por año del modelo**.
- 💵 **Comparación de precios entre dos fabricantes** con opción de normalizar los datos para comparación relativa.

## 📁 Datos

El archivo de datos utilizado es `vehicles_us.csv`, que contiene información como:

- Precio (`price`)
- Kilometraje (`odometer`)
- Año del modelo (`model_year`)
- Condición (`condition`)
- Fabricante (`manufacturer`)
- Tipo de vehículo (`type`)

## 🚀 Cómo ejecutar la aplicación

1. Asegúrate de tener instaladas las librerías necesarias:

   ```bash
   pip install streamlit pandas plotly
   ```

2. Ejecuta la aplicación:

   ```bash
   streamlit run app.py
   ```

3. Abre el navegador en la dirección que te indique (por lo general `http://localhost:8501`).

## 📝 Notas

- La aplicación es completamente interactiva: los gráficos solo se muestran cuando se seleccionan sus respectivos checkbox.
- La columna `manufacturer` se genera automáticamente si no está presente, extrayendo la primera palabra del modelo.
