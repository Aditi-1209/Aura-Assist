import { useEffect, useRef, useState } from "react";
import { SendHorizontal, Volume2, Square } from "lucide-react";
import "./App.css";

const API_URL = "http://localhost:8000/chat";

function App() {
  const [messages, setMessages] = useState([
    {
  role: "assistant",
  content: (
    <>
      <div className="welcome-title">
        Welcome to <span>Aura Assist.</span>
      </div>

      <div className="welcome-text">
        Get instant answers and discover our product
        capabilities - all at one place.
      </div>

      <div className="welcome-products">
        TaskFlow • InvoicePilot • HelpDeskly • CloudVault • MailBridge •
        RecruitEdge • PulseCRM • SurveyNest • TimeTrackr • DevPipe
      </div>
    </>
  )
}
  ]);
  const [input, setInput] = useState("");
const [loading, setLoading] = useState(false);
const [speakingIndex, setSpeakingIndex] = useState(null);

const bottomRef = useRef(null);
const speechRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);
  function toggleSpeech(text, index) {
  if (!("speechSynthesis" in window)) {
    alert("Text-to-speech is not supported in this browser.");
    return;
  }

  // If this response is currently speaking, stop it
  if (speakingIndex === index) {
    window.speechSynthesis.cancel();
    speechRef.current = null;
    setSpeakingIndex(null);
    return;
  }

  // Stop any previous speech
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);

  utterance.rate = 0.95;
  utterance.pitch = 1;
  utterance.volume = 1;

  utterance.onend = () => {
    if (speechRef.current === utterance) {
      speechRef.current = null;
      setSpeakingIndex(null);
    }
  };

  utterance.onerror = () => {
    if (speechRef.current === utterance) {
      speechRef.current = null;
      setSpeakingIndex(null);
    }
  };

  speechRef.current = utterance;
  setSpeakingIndex(index);

  window.speechSynthesis.speak(utterance);
}

  async function sendMessage(e) {
    e.preventDefault();
    const question = input.trim();
    if (!question || loading) return;

    setMessages((prev) => [...prev, { role: "user", text: question }]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      if (!res.ok) throw new Error(`Server returned ${res.status}`);
      const data = await res.json();
      setMessages((prev) => [
  ...prev,
  {
    role: "assistant",
    text: data.answer,
    sources: data.sources || [],
    suggestions: data.suggestions || [],
  },
]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: `Sorry, something went wrong talking to the server (${err.message}).`,
          sources: [],
          error: true,
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="chat-app">
      <header className="chat-header">
    <div className="header-glow"></div>
    <div className="header-stars"></div>
  <div className="header-left">

    <div className="bot-logo">
      <svg
        width="28"
        height="28"
        viewBox="0 0 100 100"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <linearGradient id="auraGradient" x1="0" y1="0" x2="100" y2="100">
    <stop offset="0%" stopColor="#fff4c8" />
    <stop offset="45%" stopColor="#f4d06f" />
    <stop offset="100%" stopColor="#c8942d" />
</linearGradient>
        </defs>

        <circle
          cx="50"
          cy="50"
          r="32"
          stroke="url(#auraGradient)"
          strokeWidth="8"
        />

        <circle
          cx="50"
          cy="50"
          r="10"
          fill="url(#auraGradient)"
        />
      </svg>
    </div>

    <div className="header-text">
  <h1>
    <span className="gold">Aura</span> Assist
</h1>



  <p className="subtitle">
  Ask. Discover. Resolve.
</p>
    </div>

  </div>

  <div className="header-right">
  <span className="header-badge">
    Enterprise&nbsp;AI
  </span>
</div>
</header>

      <div className="chat-window">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role} ${msg.error ? "error" : ""}`}>
            <div className="bubble">

    {msg.role === "assistant" ? (
  <div className="assistant-message">

    <span className="bot-sparkle">✨</span>

    <div className="assistant-content">

          {i === 0 ? (
        <>
          <h3 className="welcome-title">
            Welcome to <span className="gold">Aura Assist</span>.
          </h3>

          <p className="welcome-text">
            Get instant answers, discover product capabilities, and navigate our
            enterprise solutions—all in one place.
          </p>

          <div className="supported-products">
            <span className="supported-label">Supports</span>

            <span className="product-list">
              TaskFlow • InvoicePilot • HelpDeskly • CloudVault • MailBridge •
              RecruitEdge • PulseCRM • SurveyNest • TimeTrackr • DevPipe
            </span>
          </div>
        </>
      ) : (
        <div className="assistant-response">
          <p>{msg.text}</p>

          {msg.text && (
            <button
              type="button"
              className={`tts-button ${
                speakingIndex === i ? "speaking" : ""
              }`}
              onClick={() => toggleSpeech(msg.text, i)}
              title={
                speakingIndex === i
                  ? "Stop speaking"
                  : "Read response aloud"
              }
            >
              {speakingIndex === i ? (
                <Square size={14} />
              ) : (
                <Volume2 size={16} />
              )}

              <span>
                {speakingIndex === i ? "Stop" : "Listen"}
              </span>
            </button>
          )}
        </div>
      )}

    </div>

  </div>
) : (
  <p>{msg.text}</p>
)}
{msg.suggestions && msg.suggestions.length > 0 && (
  <div className="suggestions">
    <div className="suggestions-title">
      You may also want to ask:
    </div>

    <div className="suggestion-list">
      {msg.suggestions.map((suggestion, j) => (
        <button
          key={j}
          className="suggestion-button"
          onClick={() => {
            setInput(suggestion);
          }}
        >
          {suggestion}
        </button>
      ))}
    </div>
  </div>
)}
              {msg.sources && msg.sources.length > 0 && (
                <details className="sources">
                  <summary>{msg.sources.length} source(s)</summary>
                  <ul>
                    {msg.sources.map((s, j) => (
                      <li key={j}>
                        <strong>{s.source.replace("_FAQ.pdf", "")}</strong> · {s.category} —{" "}
                        <em>{s.question}</em>
                      </li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
        ))}
        {loading && (
          <div className="message assistant">
            <div className="bubble typing">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <form className="chat-input" onSubmit={sendMessage}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about any product's FAQ..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          <SendHorizontal size={22} strokeWidth={2} />
        </button>
      </form>
    </div>
  );
}

export default App;
