from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from main import ask_question  # Import the chatbot logic

# Load environment variables
load_dotenv()
os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Avoid Hugging Face warning

app = FastAPI(title="Medical Chatbot API")

# Serve frontend static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Request model
class QuestionRequest(BaseModel):
    question: str

# Serve the chat UI
@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())

# Chat API
@app.post("/ask")
def ask_chatbot(request: QuestionRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    answer = ask_question(question)
    return {"answer": answer}
