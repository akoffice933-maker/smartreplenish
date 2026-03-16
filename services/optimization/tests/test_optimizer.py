"""Тесты для Optimization Service."""
import pytest


def test_optimize_order(client):
    """Тест оптимизации заказа."""
    response = client.post(
        "/api/v1/optimize",
        json={"shop_id": "STORE-001", "horizon_days": 7}
    )
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert data["total_items"] >= 0
