from fastapi import FastAPI
from pydantic import BaseModel
from rag_core import build_qa_chain

app = FastAPI(title="Docker Docs RAG API")
qa = build_qa_chain()

class Query(BaseModel):
    question: str

@app.post("/query")
def query_rag(q: Query):
    result = qa.invoke({"query": q.question})
    return {
        "answer": result["result"],
        "sources": [d.metadata.get("source") for d in result["source_documents"]]
    }
