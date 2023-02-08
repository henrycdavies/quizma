import re
from fastapi import FastAPI, Depends

from app.prompt import send_prompt
from app.settings import get_settings, Settings

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {"status": "OK"}

@app.post("/generate")
def generate_quiz(theme: str, question_count: int = 10, settings: Settings = Depends(get_settings)):
    prompt_response = send_prompt(f"Write a {theme}-themed pub quiz round with {question_count} questions and answers.", settings)
    prompt_text = prompt_response.choices[0].text
    # prompt_text = "\n\n1. Who was the first president of the United States? \nAnswer: George Washington\n\n2. What year did the American Revolutionary War end? \nAnswer: 1783\n\n3. Who wrote the Declaration of Independence? \nAnswer: Thomas Jefferson\n\n4. What country did the United States gain independence from? \nAnswer: Great Britain\n\n5. What year did World War II end? \nAnswer: 1945\n\n6. Who was the leader of Nazi Germany during World War II? \nAnswer: Adolf Hitler\n\n7. What year did the Berlin Wall fall? \nAnswer: 1989\n\n8. Who was the first Prime Minister of India? \nAnswer: Jawaharlal Nehru\n\n9. What year did the French Revolution begin? \nAnswer: 1789\n\n10. Who was the first Emperor of China? \nAnswer: Qin Shi Huang"
    questions = [{"question": re.sub(r'[\d]+\.\s+', r'', q), "answer": a.replace("Answer: ", "").strip()} for q, a in (i.split("\n") for i in prompt_text.split("\n\n") if i)]
    return {
        "total": len(questions),
        "items": questions
    }