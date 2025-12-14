from fastapi import FastAPI
from pydantic import BaseModel

from src.rag_core import RAGEngine

app = FastAPI(title="Docker Docs RAG API")

rag = RAGEngine()


class Question(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Docker Docs RAG API is running",
        "docs": "/docs"
    }


@app.post("/ask")
def ask_question(payload: Question):
    answer, sources = rag.ask(payload.question)
    return {
        "answer": answer,
        "sources": sources,
    }
