from pathlib import Path
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from pypdf import PdfReader

RAW_DOCS_DIR = Path("data/raw_docs")
OUTPUT_PATH = Path("data/processed/chunks.json")


def load_markdown(file: Path) -> str:
    return file.read_text(encoding="utf-8")


def load_pdf(file: Path) -> str:
    reader = PdfReader(file)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)


def load_docs():
    docs = []

    for file in RAW_DOCS_DIR.iterdir():
        if file.suffix == ".md":
            text = load_markdown(file)
        elif file.suffix == ".pdf":
            text = load_pdf(file)
        else:
            continue

        text = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "source": file.name,
                    "file_type": file.suffix,
                },
            )
        )

    return docs


def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        separators=["\n## ", "\n### ", "\n", " "],
    )
    return splitter.split_documents(docs)


def save_chunks(chunks):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "text": c.page_content,
                    "source": c.metadata["source"],
                    "file_type": c.metadata["file_type"],
                }
                for c in chunks
            ],
            f,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    docs = load_docs()
    chunks = chunk_docs(docs)
    save_chunks(chunks)
    print(f"Saved {len(chunks)} chunks to {OUTPUT_PATH}")
