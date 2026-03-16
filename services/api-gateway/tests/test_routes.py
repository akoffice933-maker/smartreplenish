"""Тесты для API Gateway."""
import pytest
from fastapi.testclient import TestClient


def test_health_check(client):
    """Тест проверки здоровья API Gateway."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_forecast_request(client):
    """Тест запроса прогноза."""
    response = client.post(
        "/api/v1/forecast",
        json={"shop_id": "STORE-001", "sku_id": "SKU-001", "horizon_days": 7}
    )
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert len(data["predictions"]) == 7
