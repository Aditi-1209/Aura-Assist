from pathlib import Path

import chromadb
import requests
from sentence_transformers import SentenceTransformer

DB_DIR = Path(__file__).parent.parent / "chroma_db"
COLLECTION_NAME = "faq_chunks"
EMBED_MODEL = "all-MiniLM-L6-v2"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:1.5b"

SYSTEM_PROMPT = """You are a helpful customer support assistant for several SaaS products. \
Answer the user's question using ONLY the context below, which is drawn from the products' \
official FAQ documentation. If the context does not contain the answer, say you don't have \
that information rather than guessing. Be concise and match the tone of a real help-center reply.

Context:
{context}

Question: {question}

Answer:"""


NO_MATCH_RESPONSE = (
    "I don't have information about that in the FAQ knowledge base. "
    "Please contact support or rephrase your question if it's related to one of our products."
)

# Squared-L2 distance on normalized embeddings; empirically, relevant FAQ
# matches land well under 1.0 while off-topic queries land above 1.3.
DISTANCE_THRESHOLD = 1.1


class RAGPipeline:
    def __init__(self, top_k: int = 4):
        self.top_k = top_k
        self.embed_model = SentenceTransformer(EMBED_MODEL)
        client = chromadb.PersistentClient(path=str(DB_DIR))
        self.collection = client.get_collection(COLLECTION_NAME)

    def retrieve(self, query: str, top_k: int | None = None):
        top_k = top_k or self.top_k
        query_embedding = self.embed_model.encode([query], normalize_embeddings=True).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
        )
        chunks = []
        for doc, meta, dist in zip(
            results["documents"][0], results["metadatas"][0], results["distances"][0]
        ):
            chunks.append({"text": doc, "metadata": meta, "distance": dist})
        return chunks

    def generate(self, question: str, chunks: list[dict]) -> str:
        context = "\n\n".join(c["text"] for c in chunks)
        prompt = SYSTEM_PROMPT.format(context=context, question=question)
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json()["response"].strip()

    def answer(self, question: str, top_k: int | None = None):
        chunks = self.retrieve(question, top_k=top_k)
        sources = [
            {
                "source": c["metadata"]["source"],
                "category": c["metadata"]["category"],
                "question": c["metadata"]["question"],
                "distance": c["distance"],
            }
            for c in chunks
        ]

        if not chunks or chunks[0]["distance"] > DISTANCE_THRESHOLD:
            return {"answer": NO_MATCH_RESPONSE, "sources": []}

        answer = self.generate(question, chunks)
        return {"answer": answer, "sources": sources}
