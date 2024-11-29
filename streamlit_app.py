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



# Crear un diccionario con los datos de ejemplo
data = {
    'Nombre': ['Juan Pérez', 'María López', 'Pedro Gómez'],
    'Novedad': ['Llegada tarde', 'Incapacidad', 'Ausencia'],
    'Fecha': ['2023-11-28', '2023-11-29', '2023-11-30']
}

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)


    
