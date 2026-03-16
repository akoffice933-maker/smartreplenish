"""Тесты для Forecasting Service."""
import pytest


def test_forecast_endpoint(client):
    """Тест эндпоинта прогноза."""
    response = client.post(
        "/api/v1/forecast",
        json={"shop_id": "STORE-001", "sku_id": "SKU-001", "horizon_days": 7}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["shop_id"] == "STORE-001"
    assert data["sku_id"] == "SKU-001"
    assert len(data["predictions"]) == 7


def test_models_list(client):
    """Тест списка моделей."""
    response = client.get("/api/v1/models")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
