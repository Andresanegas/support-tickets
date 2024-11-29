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

opciones_novedades = ["Incapacidad", "Llegada tarde", "Permiso"]


def main():
    st.title("Formulario de Novedades")

    nombre = st.text_input("Nombre:")
    novedad = st.multiselect("Novedades:", opciones_novedades, default=["Incapacidad"])
    observacion = st.text_area("Observación:")

    # Crear un DataFrame vacío para almacenar los datos
    data = pd.DataFrame(columns=['Nombre', 'Novedades', 'Observación'])

    if st.button("Guardar"):
        # Agregar una nueva fila al DataFrame con los datos ingresados
        new_row = {'Nombre': nombre, 'Novedades': ', '.join(novedad), 'Observación': observacion}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

        # Mostrar el DataFrame en Streamlit
        st.write(data)

data.to_excel('novedades.xlsx', index=False)

if __name__ == "__main__":
    main()

