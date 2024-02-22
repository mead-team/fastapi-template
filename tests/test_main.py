from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_api_health_check():
    response = client.get("/api-health-check")
    assert response.status_code == 200
    assert response.json() == {
        "api_health_check": "api-server is Ok",
        "debug-mode": True,
    }
