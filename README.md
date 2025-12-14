
# 📦 Docker Docs RAG Chatbot

A production-style **Retrieval-Augmented Generation (RAG)** chatbot built using
Docker documentation and security PDFs.  
The system answers questions **strictly from provided documents**, with
transparent source attribution.

---

## 🚀 Features

- 📄 Supports **Markdown (.md)** and **PDF** documents
- 🔍 Semantic search with **FAISS**
- 🧠 Local LLM inference using **Ollama (LLaMA 3)**
- 💬 Interactive **Streamlit chat UI**
- 🔎 Source citations for every answer
- 🔒 Fully local / private (no OpenAI or external APIs)

---

## 🧱 Architecture

Documents (.md / .pdf)
↓
Text Extraction
↓
Chunking
↓
Embeddings (Sentence Transformers)
↓
FAISS Vector Store
↓
Retriever
↓
Ollama LLM
↓
Answer + Sources


---

## 📂 Project Structure

rag-chatbot/
├── data/
│ ├── raw_docs/ # Markdown & PDF files
│ ├── processed/
│ │ └── chunks.json
│ └── vectorstore/faiss/
├── src/
│ ├── ingest.py
│ ├── embed_faiss.py
│ ├── rag_chat.py
│ └── streamlit_app.py
├── requirements.txt
└── README.md


---

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

This allows:
- API usage
- Cloud deployment
- CI testing
- Separation of UI and logic

## Deploy to AWS EC2
EC2 Setup (one time)

Instance: t3.medium

OS: Ubuntu 22.04

Storage: 30–50 GB

Open ports:

22 (SSH)

8000 (API)

8501 (Streamlit)

🔹 SSH into EC2
ssh ubuntu@<EC2_PUBLIC_IP>

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

uvicorn src.api:app --host 0.0.0.0 --port 8000


Run Streamlit:

streamlit run src/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
=======
# docker-docs-rag-chatbot