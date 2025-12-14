# 📦 Docker Docs RAG Chatbot

## 🚀 FastAPI Backend

<p align="center">
  <img src="./api.png" alt="FastAPI RAG API" width="900"/>
</p>

<p align="center">
  <em>FastAPI service exposing document-grounded RAG inference</em>
</p>


A production-style Retrieval-Augmented Generation (RAG) system that answers questions strictly from Docker documentation and security PDFs, with transparent source attribution.
Built with FastAPI, Streamlit, FAISS, Ollama, and Docker Compose, this project demonstrates end-to-end AI system design, from document ingestion to API + UI deployment. 
The system answers questions **strictly from provided documents**, with
transparent source attribution.
# 🚀 Why This Project Matters

# This repository is designed to showcase real-world AI engineering skills

✅ Document-grounded answers 

✅ API-first architecture

✅ Containerized deployment

✅ Local LLM inference (privacy-preserving)

✅ Recruiter-ready, production layout


## 🚀 Features

## 💬 Streamlit Chat UI

<p align="center">
  <img src="streamlit.png" alt="Streamlit RAG Chat UI" width="900"/>
</p>

<p align="center">
  <em>Interactive chat UI for querying Docker documentation with source attribution</em>
</p>

- 📄 Supports **Markdown (.md)** and **PDF** documents
- 🔍 Semantic search with **FAISS**
- 🧠 Local LLM inference using **Ollama (LLaMA 3)**
- 💬 Interactive **Streamlit chat UI**
- 🔎 Source citations for every answer
- 🔒 Fully local / private (no OpenAI or external APIs)



## 🧱 RAG Architecture

<p align="center">
  <img src="rag.png" alt="RAG Pipeline Architecture" width="300"/>
</p>

<p align="center">
  <em>
    Document ingestion → embeddings → FAISS retrieval → Ollama (LLaMA 3) → FastAPI → Streamlit UI
  </em>
</p>


# Why this works (important)

api.png, streamlit.png, rag.png are in repo root

GitHub README automatically resolves relative paths

<p align="center"> keeps it clean and recruiter-friendly

Width keeps it readable on laptop & mobile


## 📁 Project Structure

## 📂 Project Structure

```text
docker-docs-rag-chatbot/
├── data/
│   ├── raw_docs/                 # Markdown & PDF source documents
│   ├── processed/                # Intermediate artifacts
│   │   └── chunks.json
│   └── vectorstore/faiss/         # FAISS vector index
│       ├── index.faiss
│       └── index.pkl
│
├── src/
│   ├── ingest.py                 # Extract text from docs
│   ├── embed_faiss.py            # Create embeddings + FAISS index
│   ├── rag_core.py               # RAG engine (retriever + LLM)
│   ├── api.py                    # FastAPI backend
│   └── streamlit_app.py          # Streamlit chat UI
│
├── Dockerfile.api                # FastAPI container
├── Dockerfile.streamlit          # Streamlit UI container
├── docker-compose.yml            # API + UI + Ollama orchestration
├── requirements.txt              # Python dependencies
├── README.md
└── LICENSE



## ⚙️ Setup

### 1️⃣ Create environment

```bash
conda create -n rag-chatbot python=3.10
conda activate rag-chatbot
pip install -r requirements.txt

# Install & start Ollama
data/raw_docs/
python src/ingest.py
python src/embed_faiss.py

# Run the Chatbot
streamlit run src/streamlit_app.py

# MIT License


✅ **Commit this first**  
This alone already makes your repo look serious.



# ✅ STEP 2 — Add FastAPI Backend

## 🚀 Deployment

Designed for production-style deployment on **AWS EC2** using Docker Compose.

- API (FastAPI) and UI (Streamlit) run as separate services
- Ollama runs locally inside a container for private LLM inference
- Services can be scaled independently

```bash
docker compose up --build
Access:

API Docs → http://localhost:8000/docs

Chat UI → http://localhost:8501



🔹 Install system deps
sudo apt update
sudo apt install -y python3-pip git


Install Ollama:

curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3

🔹 Deploy project
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
pip install -r requirements.txt


Run API:

## ✅ 5️⃣ Add a short “Deployment” visual explanation

Under **Deployment** section:

```md
## 🚀 Deployment (Docker Compose + AWS EC2)


- API (FastAPI) and UI (Streamlit) run as separate services
- Ollama runs locally inside a container for private LLM inference
- Services can be scaled independently
