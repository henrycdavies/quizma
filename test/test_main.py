from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_generate():
    response = client.post("/generate")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
