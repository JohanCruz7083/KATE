
import streamlit as st

from src.algorithms.search import (
    busqueda_lineal,
    construir_tabla_hash,
    busqueda_hash
)

# ----------------------------------
# 1. Configuración de la aplicación
# ----------------------------------

st.set_page_config(
    page_title="K.A.T.E.",
    page_icon="🤖",
    layout="centered"
)

# ----------------------------------
# 2. Información de demostración
# ----------------------------------

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

# ----------------------------------
# 3. Identidad de K.A.T.E.
# ----------------------------------

st.title("K.A.T.E. 🤖")
st.subheader("Personal Virtual Assistant")

st.write(
    "Hola, soy K.A.T.E. Estoy aquí para ayudarte "
    "a recuperar información de tus actividades."
)

st.divider()

# ----------------------------------
# 4. Selección del algoritmo
# ----------------------------------

algoritmo = st.selectbox(
    "Selecciona el algoritmo de búsqueda:",
    ["Tabla Hash", "Búsqueda Lineal"]
)

# ----------------------------------
# 5. Historial de conversación
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ----------------------------------
# 6. Entrada del usuario
# ----------------------------------

prompt = st.chat_input(
    "Escribe una clave, por ejemplo: repo_proyecto"
)

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    clave = prompt.strip().lower().replace(" ", "_")

    # ----------------------------------
    # 7. Ejecución del algoritmo
    # ----------------------------------

    if algoritmo == "Tabla Hash":
        resultado = busqueda_hash(tabla_hash, clave)
    else:
        resultado = busqueda_lineal(recuerdos, clave)

    # ----------------------------------
    # 8. Generación de respuesta
    # ----------------------------------

    if resultado:
        respuesta = (
            f"Encontré la información solicitada:\n\n"
            f"**{resultado['valor']}**"
        )
    else:
        respuesta = (
            "No encontré esa información en mis registros.\n\n"
            "Puedes intentar con:\n"
            "- correo_profesor\n"
            "- repo_proyecto\n"
            "- hora_entrega"
        )

    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta
    })

    st.rerun()
