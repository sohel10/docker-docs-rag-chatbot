from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

VECTOR_DB_DIR = Path("data/vectorstore/faiss")


def load_components():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        VECTOR_DB_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(
        model="llama3",
        temperature=0.1,
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}
"""
    )

    return retriever, llm, prompt


def run_rag(question: str):
    retriever, llm, prompt = load_components()

    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)

    messages = prompt.format_messages(
        question=question,
        context=context,
    )

    answer = llm.invoke(messages)

    print("\nANSWER:\n")
    print(answer)

    print("\nSOURCES:")
    for d in docs:
        print("-", d.metadata.get("source"))


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        run_rag(q)
