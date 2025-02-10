import streamlit as st
from openai import OpenAI
from entities import ThreadsChat
import time

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
OPENAI_ASSISTANT_ID = st.secrets.get("OPENAI_ASSISTANT_ID")
VECTOR_STORE_ID = st.secrets.get("VECTOR_STORE_ID")


# Initialize OpenAI client
if 'client' not in st.session_state:
    if 'OPENAI_API_KEY' not in st.secrets:
        st.error("Missing OpenAI API Key in secrets")
        st.stop()
    st.session_state.client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)

client = st.session_state.client
st.session_state.threads_manager = ThreadsChat()

# Get Assistant ID (set in secrets or input)
if 'assistant_id' not in st.session_state:
    if 'OPENAI_ASSISTANT_ID' in st.secrets:
        st.session_state.assistant_id = st.secrets.OPENAI_ASSISTANT_ID
    else:
        st.session_state.assistant_id = st.text_input("Digite o ID do Assistente:")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Create thread once per session
if 'thread' not in st.session_state:

    st.session_state.thread = st.session_state.threads_manager.create()

# App config
st.set_page_config(
   initial_sidebar_state="collapsed"
)


# App layout
st.title("Especialista em legislação de Consórcios")
st.write("Conectado ao Assistente!")

def click_thread_id(thread_id):
    st.session_state.chat_history = st.session_state.threads_manager.get_messages_from_thread_id(thread_id)

with st.sidebar:
    st.title("Threads Anteriores")
    st.session_state.past_threads = ThreadsChat().get_threads()
    for thread_id in st.session_state.past_threads:
        st.button(thread_id, on_click=click_thread_id, args=(thread_id,))
    

# Display chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Digite sua mensagem...")

if user_input and st.session_state.assistant_id:
    # Add user message to chat
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add message to thread
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread.id,
        role="user",
        content=user_input
    )

    # Create run
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread.id,
        assistant_id=st.session_state.assistant_id
    )

    # Wait for completion
    with st.spinner("Pensando..."):
        while run.status not in ["completed", "failed"]:
            try:
                time.sleep(2)
                run = client.beta.threads.runs.retrieve(
                    thread_id=st.session_state.thread.id,
                    run_id=run.id
                )
                print(run.status)
            except Exception as e:
                print(e)


    # Get response
    if run.status == "completed":
        messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread.id
        )
        
        # Find the latest assistant message
        assistant_messages = [
            msg for msg in messages.data 
            if msg.role == "assistant" and msg.run_id == run.id
        ]
        
        if assistant_messages:
            response = assistant_messages[0].content[0].text.value
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response}
            )
            with st.chat_message("assistant"):
                st.markdown(response)
    else:
        st.error("Falha ao obter retorno do Assistente")