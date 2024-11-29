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



import tkinter as tk
from datetime import date

def guardar_datos():
    nombre = entry_nombre.get()
    novedad = text_novedad.get("1.0", "end-1c")  # Obtener todo el texto del Text
    observacion = text_observacion.get("1.0", "end-1c")
    fecha = date.today()  # Obtener la fecha actual

    # Aquí puedes hacer algo con los datos, por ejemplo, guardarlos en un archivo o base de datos
    print(f"Nombre: {nombre}")
    print(f"Novedad: {novedad}")
    print(f"Observación: {observacion}")
    print(f"Fecha: {fecha}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Novedades")

# Crear los labels y entradas
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_novedad = tk.Label(ventana, text="Novedad:")
label_novedad.pack()
text_novedad = tk.Text(ventana, height=5)
text_novedad.pack()

label_observacion = tk.Label(ventana, text="Observación:")
label_observacion.pack()
text_observacion = tk.Text(ventana, height=5)
text_observacion.pack()

# Crear el botón para guardar los datos
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.pack()

ventana.mainloop()
