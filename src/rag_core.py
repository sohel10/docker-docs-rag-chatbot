from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

VECTOR_DB_DIR = Path("data/vectorstore/faiss")


class RAGEngine:
    def __init__(self):
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = FAISS.load_local(
            VECTOR_DB_DIR,
            embeddings,
            allow_dangerous_deserialization=True,
        )

        self.retriever = self.db.as_retriever(search_kwargs={"k": 3})

        self.llm = Ollama(
            model="llama3",
            temperature=0.1,
        )

        self.prompt = ChatPromptTemplate.from_template(
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

    def ask(self, question: str):
        docs = self.retriever.invoke(question)
        context = "\n\n".join(d.page_content for d in docs)

        messages = self.prompt.format_messages(
            question=question,
            context=context,
        )

        answer = self.llm.invoke(messages)

        sources = list({d.metadata.get("source") for d in docs})

        return answer, sources
