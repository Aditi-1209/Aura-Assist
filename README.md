# FAQ Bot

This repository contains an FAQ retrieval-augmented generation (RAG) assistant for enterprise product documentation.

## Project Structure

- `app/`
  - `main.py` - FastAPI backend exposing a `/chat` endpoint and a health check.
  - `rag.py` - RAG pipeline implementation using Chroma for retrieval, SentenceTransformers for embeddings, and Ollama for generation.
  - `ingest.py` - ingestion script that reads FAQ PDF files, extracts Q&A chunks, computes embeddings, and writes them into the Chroma database.
- `data/` - source FAQ documents used to build the knowledge base.
- `chroma_db/` - persistent Chroma database directory storing indexed FAQ chunks.
- `frontend/` - web UI for interacting with the FAQ bot.
- `requirements.txt` - Python dependency list.

## Requirements

- Python 3.11+ (recommended)
- `pip` package manager
- Local Ollama server available at `http://localhost:11434`
- `chromadb` backend accessible with the repository `chroma_db` folder

## Setup

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Python dependencies.

```powershell
pip install -r requirements.txt
```

3. Start the Ollama model server and make sure the model endpoint is available.

4. Build the knowledge base from FAQ source documents, if needed.

```powershell
python app/ingest.py
```

## Running the API

Start the FastAPI app with Uvicorn:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

### Endpoints

- `GET /health` - basic health check
- `POST /chat` - chat endpoint accepting JSON:

```json
{
  "question": "How do I reset my password?",
  "top_k": 4
}
```

The response includes an `answer`, `sources`, and optional `suggestions`.

## Frontend

The `frontend/` directory contains the web UI source for this project. If you want to run it locally, install Node packages and launch the Vite app in that folder.

To run the frontend:

```powershell
cd frontend
npm install
npm run dev
```

Then open the URL shown in the terminal (typically `http://127.0.0.1:5173`).

## Notes

- The RAG pipeline uses `SentenceTransformer(all-MiniLM-L6-v2)` for embeddings.
- Answers are generated only when retrieved FAQ context is sufficiently close; otherwise, a fallback response is returned.
- The project currently expects an Ollama endpoint at `http://localhost:11434/api/generate` and the model `qwen2.5:1.5b`.

