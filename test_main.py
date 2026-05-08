from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando"}

def test_somar():
    response = client.get("/somar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 4}

def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 4}