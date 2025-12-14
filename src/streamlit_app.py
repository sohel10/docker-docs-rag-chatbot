import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Docker Docs RAG Chatbot",
    layout="centered",
)

st.title("📦 Docker Docs RAG Chatbot")
st.caption("FAISS + Ollama (local) via FastAPI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask a Docker question...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": prompt},
                timeout=120,
            )

            if response.status_code == 200:
                data = response.json()
                answer = data["answer"]
                sources = data.get("sources", [])

                st.markdown(answer)

                if sources:
                    st.markdown("**Sources:**")
                    for src in sources:
                        st.markdown(f"- {src}")

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            else:
                st.error("API Error")
