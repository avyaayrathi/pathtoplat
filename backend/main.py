from fastapi import FastAPI
from backend.models import Submission
from backend.skill_engine import analyze_submissions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to PathToPlat 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(data: list[Submission]):
    weak = analyze_submissions(data)
    return {"weak_topics": weak}