from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "0.1.0"
