import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de venta de autos en EE.UU.')

# ---------------- Vista de Datos ----------------
st.subheader('Vista de Datos')
include_small_manufacturers = st.checkbox(
    'Incluir fabricantes con menos de 1000 anuncios', value=True)

# Asegurar columna 'manufacturer'
if 'manufacturer' not in car_data.columns:
    car_data['manufacturer'] = car_data['model'].str.split().str[0]

# Filtro solo para la vista de datos
view_data = car_data.copy()
if not include_small_manufacturers:
    manufacturer_counts = view_data['manufacturer'].value_counts()
    valid_manufacturers = manufacturer_counts[manufacturer_counts >= 1000].index
    view_data = view_data[view_data['manufacturer'].isin(valid_manufacturers)]

st.dataframe(view_data)

st.header('Histograma y diagrama de dispersión')

# ---------------- Histograma: odómetro ----------------
build_histogram = st.checkbox('Construir histograma')

if build_histogram: 
    st.subheader('Distribución del Odómetro')
    st.write('Histograma del kilometraje (odometer)')
    histogram = px.histogram(car_data, x="odometer")
    st.plotly_chart(histogram, use_container_width=True)

# ---------------- Diagrama de dispersión ----------------
build_scatter_plot = st.checkbox('Construir diagrama de dispersión')

if build_scatter_plot:
    st.subheader('Dispersión Odómetro vs Precio')
    st.write('Gráfico de dispersión entre odómetro y precio')
    scatter_plot = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(scatter_plot, use_container_width=True)

# ---------------- Tipos de vehículo por fabricante ----------------
st.subheader('Tipos de Vehículo por Fabricante')
fig3 = px.histogram(car_data, x="manufacturer", color="type", barmode="group")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- Histograma condición vs año del modelo ----------------
st.subheader('Condición del Vehículo por Año del Modelo')
fig4 = px.histogram(car_data, x="model_year", color="condition", barmode="group")
st.plotly_chart(fig4, use_container_width=True)

# ---------------- Comparación de precios entre fabricantes ----------------
st.subheader('Comparar Distribución de Precios entre Fabricantes')

manufacturers = sorted(car_data['manufacturer'].dropna().unique())

manufacturer1 = st.selectbox('Selecciona el fabricante 1', manufacturers, index=0)
manufacturer2 = st.selectbox('Selecciona el fabricante 2', manufacturers, index=1)

normalize_hist = st.checkbox('Normalizar histograma')

if manufacturer1 and manufacturer2:
    filtered_data = car_data[car_data['manufacturer'].isin([manufacturer1, manufacturer2])]
    fig5 = px.histogram(
        filtered_data, x="price", color="manufacturer",
        barmode="overlay" if normalize_hist else "group",
        histnorm='percent' if normalize_hist else None
    )
    st.plotly_chart(fig5, use_container_width=True)
