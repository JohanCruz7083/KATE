
import streamlit as st

from src.algorithms.search import (
    busqueda_lineal,
    construir_tabla_hash,
    busqueda_hash
)

st.set_page_config(
    page_title="K.A.T.E. | Asistente Virtual",
    page_icon="🤖",
    layout="centered"
)

# Información de demostración
recuerdos = [
    {
        "id": 1,
        "clave": "correo_profesor",
        "valor": "algoritmos@universidad.edu"
    },
    {
        "id": 2,
        "clave": "repo_proyecto",
        "valor": "https://github.com/JohanCruz7083/KATE"
    },
    {
        "id": 3,
        "clave": "hora_entrega",
        "valor": "Jueves 23:59"
    }
]

tabla_hash = construir_tabla_hash(recuerdos)

st.title("🤖 K.A.T.E.")
st.caption("Knowledge Assistant & Task Executor")
st.divider()

st.write(
    "¡Hola! Soy K.A.T.E. Puedes preguntarme "
    "por información que tengo almacenada."
)

algoritmo = st.selectbox(
    "Algoritmo de búsqueda",
    ["Tabla Hash", "Búsqueda Lineal"]
)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar conversación anterior
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

pregunta = st.chat_input(
    "Escribe qué información necesitas..."
)

if pregunta:
    st.session_state.mensajes.append({
        "role": "user",
        "content": pregunta
    })

    clave = pregunta.strip().lower().replace(" ", "_")

    if algoritmo == "Tabla Hash":
        resultado = busqueda_hash(tabla_hash, clave)
    else:
        resultado = busqueda_lineal(recuerdos, clave)

    if resultado:
        respuesta = (
            f"Encontré la información solicitada:\n\n"
            f"**{resultado['valor']}**"
        )
    else:
        respuesta = (
            "No encontré esa información en mis registros. "
            "Intenta con: correo_profesor, repo_proyecto "
            "o hora_entrega."
        )

    st.session_state.mensajes.append({
        "role": "assistant",
        "content": respuesta
    })

    st.rerun()
