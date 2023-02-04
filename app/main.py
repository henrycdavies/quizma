from fastapi import FastAPI

from app.prompt import send_prompt

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {"status": "OK"}

@app.post("/generate")
def generate_quiz(question_count: int = 10):
    return send_prompt(f"Write a pub quiz question. Delimit the question and answer with a newline character.")