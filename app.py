
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="K.A.T.E.",
    page_icon="🤖",
    layout="centered"
)

# Identidad de K.A.T.E.
st.title("K.A.T.E. 🤖")
st.subheader("Personal Virtual Assistant")

st.write(
    "Hola, soy K.A.T.E. Estoy aquí para ayudarte "
    "con tus actividades cotidianas."
)

# Inicializar historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Entrada del usuario
prompt = st.chat_input("Escribe un mensaje...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = (
        "¡Hola! Soy K.A.T.E. Mi interfaz ya está funcionando. "
        "Pronto podré conversar contigo mediante inteligencia artificial."
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
