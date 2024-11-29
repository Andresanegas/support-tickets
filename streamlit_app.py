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



import pandas as pd

def crear_dataframe(nombre_archivo, datos):
    """
    Crea un DataFrame si no existe, de lo contrario lo carga.

    Args:
        nombre_archivo (str): Nombre del archivo CSV donde se guardará el DataFrame.
        datos (dict): Diccionario con los datos para crear el DataFrame.
    """

    try:
        # Intentar cargar el DataFrame existente
        df = pd.read_csv(nombre_archivo)
        print("DataFrame cargado exitosamente.")
    except FileNotFoundError:
        # Si el archivo no existe, crear un nuevo DataFrame
        df = pd.DataFrame(datos)
        df.to_csv(nombre_archivo, index=False)
        print("Nuevo DataFrame creado y guardado.")

    return df

# Ejemplo de uso:
datos = {
    'Nombre': ['Juan Pérez', 'María López'],
    'Edad': [30, 25]
}

nuevo_df = crear_dataframe('mi_dataframe.csv', datos)
