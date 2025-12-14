from pathlib import Path
import json
import pickle

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

CHUNKS_PATH = Path("data/processed/chunks.json")
VECTOR_DB_DIR = Path("data/vectorstore/faiss")


def load_chunks():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        raw_chunks = json.load(f)

    docs = [
        Document(
            page_content=chunk["text"],
            metadata={"source": chunk["source"]},
        )
        for chunk in raw_chunks
    ]
    return docs


def build_faiss(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(docs, embeddings)


def save_faiss(db):
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    db.save_local(VECTOR_DB_DIR)


if __name__ == "__main__":
    docs = load_chunks()
    db = build_faiss(docs)
    save_faiss(db)
    print(f"FAISS index saved to {VECTOR_DB_DIR}")
