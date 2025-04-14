import streamlit as st
import random
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Química Interactiva", layout="wide")

# Título principal
st.title("🧪 Curso de Química Interactiva")
st.markdown("Bienvenido al curso más didáctico de química. Aprende jugando, explorando y aplicando técnicas de estudio avanzadas.")

# Menú lateral de navegación
seccion = st.sidebar.selectbox("Selecciona una sección", [
    "📘 Teoría", 
    "🎮 Juegos", 
    "🧠 Técnicas de Estudio", 
    "🖼️ Galería"
])

# 📘 SECCIÓN: Teoría
if seccion == "📘 Teoría":
    st.header("📘 Conceptos Clave")

    st.subheader("🔹 La Tabla Periódica")
    try:
        st.image("images/tabla_periodica.png", use_column_width=True)
    except:
        st.warning("⚠️ Imagen 'tabla_periodica.png' no encontrada en la carpeta /images")

    st.markdown("""
    La tabla periódica organiza los elementos químicos según su número atómico, configuración electrónica y propiedades químicas.
    """)

    st.subheader("🔹 Tipos de Reacciones Químicas")
    try:
        st.image("images/reacciones.jpg", use_column_width=True)
    except:
        st.warning("


