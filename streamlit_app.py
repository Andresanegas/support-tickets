import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="RRHH YesBpo", page_icon="🌏")
st.title("🌏 RRHH YesBpo")
st.write("Tu herramienta para un registro eficiente💯")



import streamlit as st
import pandas as pd

# Cargar el DataFrame existente (si ya lo tienes)
df = pd.read_csv('novedades.csv')  # Reemplaza 'novedades.csv' con la ruta correcta

# Título de la aplicación
st.title("Formulario de Novedades")

# Campos del formulario
nombre = st.text_input("Nombre")
novedad = st.selectbox("Novedad", ["Llegada tarde", "Incapacidad", "Ausencia"])
fecha = st.date_input("Fecha")

# Botón para agregar una nueva fila
if st.button("Agregar"):
    # Crear un nuevo diccionario con los datos del formulario
    new_data = {'Nombre': [nombre], 'Novedad': [novedad], 'Fecha': [fecha]}
    # Convertir el diccionario en un DataFrame
    new_df = pd.DataFrame(new_data)
    # Agregar la nueva fila al DataFrame original
    df = pd.concat([df, new_df], ignore_index=True)
    # Guardar los cambios en el archivo CSV
    df.to_csv('novedades.csv', index=False)
    st.success("Nueva fila agregada correctamente")

# Mostrar el DataFrame actualizado
st.write("Datos actuales:")
st.dataframe(df)


    
