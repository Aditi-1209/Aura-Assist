from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

from app.rag import RAGPipeline

app = FastAPI(title="FAQ Bot RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:\d+",
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline: RAGPipeline | None = None
GREETINGS = {
    "hi",
    "hello",
    "hey",
    "hii",
    "hiii",
    "good morning",
    "good afternoon",
    "good evening",
    "thanks",
    "thank you",
    "bye",
    "goodbye",
    "help",
    "who are you",
    "what can you do"
}

GREETING_RESPONSES = {
    "hi": "Hello! 👋 I'm Aura Assist. How can I help you today?",
    "hello": "Hello! 👋 I'm Aura Assist. How can I help you today?",
    "hey": "Hey! 👋 How can I help you today?",
    "hii": "Hi there! 👋 How can I help you today?",
    "hiii": "Hi there! 👋 How can I help you today?",

    "good morning": "Good morning! ☀️ How can I help you today?",
    "good afternoon": "Good afternoon! 👋 How can I help you today?",
    "good evening": "Good evening! 👋 How can I help you today?",

    "thanks": "You're welcome! 😊",
    "thank you": "You're welcome! Happy to help.",

    "bye": "Goodbye! 👋 Have a wonderful day.",
    "goodbye": "Take care! 👋",

    "help": "Ask me anything about TaskFlow, InvoicePilot, HelpDeskly, CloudVault, MailBridge, RecruitEdge, PulseCRM, SurveyNest, TimeTrackr or DevPipe.",

    "who are you": "I'm Aura Assist, your enterprise AI assistant for answering questions across all supported products.",

    "what can you do": "I can answer questions, explain product features, guide you through workflows, and help you navigate our enterprise products."
}


@app.on_event("startup")
def load_pipeline():
    global pipeline
    pipeline = RAGPipeline(top_k=4)


class ChatRequest(BaseModel):
    question: str
    top_k: int | None = None


class Source(BaseModel):
    source: str
    category: str
    question: str
    distance: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    suggestions: list[str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    query = req.question.strip().lower()

    # Handle greetings without using RAG
    if query in GREETING_RESPONSES:
        return {
            "answer": GREETING_RESPONSES[query],
            "sources": [],
            "suggestions": []
        }

    result = pipeline.answer(req.question, top_k=req.top_k)

    # Generate follow-up question suggestions
    suggestions = []

    for source in result.get("sources", []):
        suggested_question = source.get("question")

        if (
            suggested_question
            and suggested_question.lower().strip() != query
            and suggested_question not in suggestions
        ):
            suggestions.append(suggested_question)

    # Show maximum 3 suggestions
    result["suggestions"] = suggestions[:3]

    return result
