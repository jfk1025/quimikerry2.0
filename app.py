import streamlit as st
from utils.juegos import mostrar_juegos
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Química Interactiva", layout="wide")

st.title("🧪 Curso de Química Interactiva")
st.markdown("Bienvenido al curso más didáctico de química. Aprende jugando, explorando y aplicando técnicas de estudio avanzadas.")

# Secciones
seccion = st.sidebar.selectbox("Selecciona una sección", ["📘 Teoría", "🎮 Juegos", "🧠 Técnicas de Estudio", "🖼️ Galería"])

if seccion == "📘 Teoría":
    st.header("📘 Conceptos Clave")
    st.subheader("La Tabla Periódica")
    st.image("images/tabla_periodica.png", use_column_width=True)
    st.markdown("""
    La tabla periódica organiza los elementos químicos según su número atómico, configuración electrónica y propiedades químicas.
    """)

    st.subheader("Tipos de Reacciones Químicas")
    st.image("images/reacciones.jpg", use_column_width=True)
    st.markdown("""
    - Síntesis
    - Descomposición
    - Sustitución
    - Doble sustitución
    - Combustión
    """)

elif seccion == "🎮 Juegos":
    st.header("🎮 Juegos Educativos")
    mostrar_juegos()

elif seccion == "🧠 Técnicas de Estudio":
    st.header("🧠 Técnicas Avanzadas de Estudio")
    st.markdown("""
    - **Mapas mentales y conceptuales**
    - **Método Feynman**
    - **Estudio espaciado**
    - **Uso de simulaciones interactivas**
    - **Análisis de casos y resolución de problemas**
    """)

elif seccion == "🖼️ Galería":
    st.header("🖼️ Galería de Imágenes Didácticas")
    st.image(["images/tabla_periodica.png", "images/reacciones.jpg"], caption=["Tabla Periódica", "Tipos de Reacciones"])

