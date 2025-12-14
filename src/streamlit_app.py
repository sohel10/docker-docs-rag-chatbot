import streamlit as st

from rag_core import RAGEngine

st.set_page_config(
    page_title="RAG Chatbot (Docker Docs)",
    layout="centered",
)

st.title("📦 Docker Docs RAG Chatbot")
st.caption("FAISS + Ollama (local)")

# Initialize RAG engine once
@st.cache_resource
def load_engine():
    return RAGEngine()

engine = load_engine()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
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

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = engine.ask(prompt)
            st.markdown(answer)

            if sources:
                st.markdown("**Sources:**")
                for src in sources:
                    st.markdown(f"- `{src}`")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
