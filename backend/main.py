from fastapi import FastAPI
from backend.models import Submission
from backend.skill_engine import analyze_submissions
from backend.database import Base, engine
import backend.db_models
from backend.database import SessionLocal
from backend.db_models import SubmissionDB


Base.metadata.create_all(bind=engine)
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

@app.post("/submit")
def submit(data: Submission):
    db = SessionLocal()
    db_item = SubmissionDB(**data.dict())
    db.add(db_item)
    db.commit()
    db.close()
    return {"status": "saved"}

@app.get("/submissions/{username}")
def get_submissions(username: str):
    db = SessionLocal()
    items = db.query(SubmissionDB).filter(SubmissionDB.username == username).all()
    db.close()
    return items