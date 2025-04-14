import streamlit as st
import random
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Química Interactiva", layout="wide")

# Título principal
st.title("🧪 Curso de Química Interactiva")
st.markdown("Explora el fascinante mundo de la química con teoría, juegos, técnicas de estudio avanzadas e imágenes didácticas. Ideal para estudiantes, docentes y curiosos.")

# Barra lateral de navegación
menu = st.sidebar.radio("Selecciona una sección", [
    "📘 Teoría",
    "🎮 Juegos",
    "🧠 Técnicas de Estudio",
    "🖼️ Galería"
])

# 📘 Teoría
if menu == "📘 Teoría":
    st.header("📘 Fundamentos de la Química")

    st.subheader("🔹 La Tabla Periódica")
    try:
        st.image("images/tabla_periodica.png", use_column_width=True)
    except:
        st.warning("⚠️ Imagen 'tabla_periodica.png' no encontrada.")

    st.markdown("""
    La tabla periódica es una herramienta que organiza los elementos químicos por número atómico y propiedades.  
    Permite identificar metales, no metales, gases nobles y tendencias como electronegatividad y radio atómico.
    """)

    st.subheader("🔹 Tipos de Reacciones Químicas")
    try:
        st.image("images/reacciones.jpg", use_column_width=True)
    except:
        st.warning("⚠️ Imagen 'reacciones.jpg' no encontrada.")

    st.markdown("""
    - **Síntesis:** A + B → AB  
    - **Descomposición:** AB → A + B  
    - **Sustitución:** A + BC → AC + B  
    - **Doble Sustitución:** AB + CD → AD + CB  
    - **Combustión:** Compuestos + O₂ → CO₂ + H₂O
    """)

# 🎮 Juegos
elif menu == "🎮 Juegos":
    st.header("🎮 Juegos Didácticos de Química")

    juego = st.selectbox("Selecciona un juego", ["¿Cuál es el Elemento?", "Verdadero o Falso", "Adivina la Reacción"])

    # Juego 1
    if juego == "¿Cuál es el Elemento?":
        elementos = [
            {"nombre": "Hidrógeno", "simbolo": "H"},
            {"nombre": "Oxígeno", "simbolo": "O"},
            {"nombre": "Carbono", "simbolo": "C"},
            {"nombre": "Nitrógeno", "simbolo": "N"},
            {"nombre": "Sodio", "simbolo": "Na"},
            {"nombre": "Cloro", "simbolo": "Cl"},
        ]
        eleccion = random.choice(elementos)
        opciones = random.sample([e["nombre"] for e in elementos], 4)
        st.markdown(f"¿Qué elemento tiene el símbolo **{eleccion['simbolo']}**?")
        respuesta = st.radio("Selecciona:", opciones)
        if st.button("Verificar"):
            if respuesta == eleccion["nombre"]:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. Era {eleccion['nombre']}.")

    # Juego 2
    elif juego == "Verdadero o Falso":
        preguntas = [
            {"pregunta": "El oxígeno es un gas noble.", "respuesta": False},
            {"pregunta": "El agua está formada por H y O.", "respuesta": True},
            {"pregunta": "El sodio es un metal alcalino.", "respuesta": True},
        ]
        q = random.choice(preguntas)
        st.write(f"🔍 {q['pregunta']}")
        seleccion = st.radio("Tu respuesta:", ["Verdadero", "Falso"])
        if st.button("Comprobar"):
            correcto = "Verdadero" if q["respuesta"] else "Falso"
            if seleccion == correcto:
                st.success("✅ ¡Bien hecho!")
            else:
                st.error(f"❌ Incorrecto. La respuesta era {correcto}.")

    # Juego 3
    elif juego == "Adivina la Reacción":
        reacciones = [
            {"descripcion": "Reacción donde un solo reactivo se divide en dos productos.", "tipo": "Descomposición"},
            {"descripcion": "Reacción de un metal con oxígeno que genera óxido.", "tipo": "Síntesis"},
            {"descripcion": "Reacción entre un ácido y una base que forma sal y agua.", "tipo": "Doble Sustitución"},
        ]
        r = random.choice(reacciones)
        opciones = ["Síntesis", "Descomposición", "Sustitución", "Doble Sustitución"]
        st.markdown(f"🧪 {r['descripcion']}")
        seleccion = st.selectbox("¿Qué tipo de reacción es?", opciones)
        if st.button("Revisar respuesta"):
            if seleccion == r["tipo"]:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Era una reacción de tipo: {r['tipo']}.")

# 🧠 Técnicas de Estudio
elif menu == "🧠 Técnicas de Estudio":
    st.header("🧠 Estrategias Avanzadas para Aprender Química")

    st.markdown("""
    ### 🧩 Técnicas Sugeridas:

    - 🧠 **Mapas mentales y conceptuales:** Para conectar ideas visualmente.
    - 👨‍🏫 **Método Feynman:** Enseña lo que aprendes a otra persona.
    - 🕒 **Estudio espaciado:** Divide el aprendizaje en sesiones distribuidas.
    - 🧪 **Uso de simuladores virtuales:** Experimentación sin laboratorio físico.
    - ❓ **Resolución de problemas:** Aplica conocimientos en ejercicios prácticos.

    ### 🧰 Recursos:
    - [PhET Simulations](https://phet.colorado.edu/)
    - [Khan Academy: Química](https://es.khanacademy.org/science/chemistry)
    """)

# 🖼️ Galería
elif menu == "🖼️ Galería":
    st.header("🖼️ Galería de Imágenes Didácticas")

    try:
        st.image(["images/tabla_periodica.png", "images/reacciones.jpg"], 
                 caption=["Tabla Periódica", "Tipos de Reacciones"],
                 width=400)
    except:
        st.warning("⚠️ Asegúrate de subir las imágenes a la carpeta 'images'")



