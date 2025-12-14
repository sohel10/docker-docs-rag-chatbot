from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_DIR = Path("data/vectorstore/faiss")


def load_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        VECTOR_DB_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})
    return retriever


def run_query(question: str):
    retriever = load_retriever()
    docs = retriever.invoke(question)

    print(f"\nQUESTION: {question}\n")
    for i, doc in enumerate(docs, 1):
        print(f"--- Result {i} ---")
        print(f"Source: {doc.metadata.get('source')}")
        print(doc.page_content[:500])
        print()


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        run_query(q)
