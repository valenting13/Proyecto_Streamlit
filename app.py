import streamlit as st
from inicio import cargar_archivo
from eda import eda
from entrenamiento import entrenamiento
from preprocesamiento import preprocesamiento
from prediccion import prediccion
from reporte import reporte

st.set_page_config(page_title="GrowUp",
                   page_icon='assets/growup.png',
                   layout='wide', 
                   initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

logo = "assets/growup.png"
st.sidebar.image(logo, width=100)

configuracion="""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(configuracion,unsafe_allow_html=True)
nombresPaginas = {
    "Inicio": cargar_archivo,
    "Análisis Exploratorio de Datos": eda,
    "Preprocesamiento de Datos":preprocesamiento,
    "Entrenamiento y Prueba": entrenamiento,
    "Predicción": prediccion,
    "Reporte": reporte
}

nombre_paginas = st.sidebar.selectbox("Escoja una página", nombresPaginas.keys())
st.sidebar.divider()
nombresPaginas[nombre_paginas]()