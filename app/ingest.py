import re
from pathlib import Path

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

DATA_DIR = Path(__file__).parent.parent / "data"
DB_DIR = Path(__file__).parent.parent / "chroma_db"
COLLECTION_NAME = "faq_chunks"
EMBED_MODEL = "all-MiniLM-L6-v2"


def extract_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


KNOWN_CATEGORIES = {
    "Account & Billing",
    "Setup & Installation",
    "Features & Usage",
    "Troubleshooting",
    "Integrations",
    "Security & Privacy",
}


def chunk_qa_pairs(text: str, source: str):
    """Split extracted PDF text into one chunk per Q&A pair, tagged with its category."""
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    chunks = []
    category = "General"
    current_q = None
    current_a_lines = []

    def flush():
        if current_q is not None and current_a_lines:
            answer = " ".join(current_a_lines).strip()
            chunks.append({
                "text": f"Q: {current_q}\nA: {answer}",
                "category": category,
                "question": current_q,
                "source": source,
            })

    for line in lines:
        if "Frequently Asked Questions" in line:
            continue
        if line in KNOWN_CATEGORIES:
            category = line
            continue
        if line.startswith("Q:"):
            flush()
            current_q = line[2:].strip()
            current_a_lines = []
        elif current_q is not None:
            current_a_lines.append(line)
    flush()
    return chunks


def main():
    pdf_files = sorted(DATA_DIR.glob("*.pdf"))
    if not pdf_files:
        raise SystemExit(f"No PDFs found in {DATA_DIR}")

    print(f"Found {len(pdf_files)} PDFs")
    all_chunks = []
    for pdf_path in pdf_files:
        text = extract_text(pdf_path)
        chunks = chunk_qa_pairs(text, source=pdf_path.name)
        print(f"  {pdf_path.name}: {len(chunks)} Q&A chunks")
        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    print(f"Loading embedding model: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    print("Embedding chunks...")
    texts = [c["text"] for c in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True, normalize_embeddings=True)

    print(f"Writing to Chroma at {DB_DIR}")
    client = chromadb.PersistentClient(path=str(DB_DIR))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.create_collection(COLLECTION_NAME)

    ids = [f"{c['source']}-{i}" for i, c in enumerate(all_chunks)]
    metadatas = [
        {"category": c["category"], "question": c["question"], "source": c["source"]}
        for c in all_chunks
    ]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas,
    )

    print(f"Done. Indexed {len(all_chunks)} chunks into collection '{COLLECTION_NAME}'.")


if __name__ == "__main__":
    main()
