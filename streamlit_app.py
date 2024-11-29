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

import streamlit as st

def main():
    st.title("Formulario de Novedades")

    nombre = st.text_input("Nombre:")
    novedad = st.multiselect("Novedades:", opciones_novedades, default=["Incapacidad"])
    observacion = st.text_area("Observación:")

    if st.button("Guardar"):
        st.success("Datos guardados.")
        # Aquí puedes agregar código para guardar los datos en una base de datos, archivo, etc.
        # Por ejemplo, usando pandas y csv:
        import pandas as pd

        data = {'Nombre': [nombre], 'Novedad': [novedad], 'Observación': [observacion]}
        df = pd.DataFrame(data)

        # Guardar en un archivo CSV
        df.to_csv('novedades.csv', mode='a', header=False, index=False)

if __name__ == "__main__":
    main()
