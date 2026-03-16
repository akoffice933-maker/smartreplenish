"""E2E тесты для SmartReplenish."""
import pytest
import requests

API_BASE = "http://localhost:8080"


def test_full_pipeline():
    """Тест полного пайплайна: прогноз -> оптимизация -> алерты."""
    # 1. Получаем прогноз
    forecast_response = requests.post(
        f"{API_BASE}/api/v1/forecast",
        json={"shop_id": "STORE-001", "sku_id": "SKU-001", "horizon_days": 7}
    )
    assert forecast_response.status_code == 200
    forecast = forecast_response.json()
    assert len(forecast["predictions"]) == 7
    
    # 2. Получаем оптимизацию заказа
    optimization_response = requests.post(
        f"{API_BASE}/api/v1/optimization",
        json={"shop_id": "STORE-001", "horizon_days": 7}
    )
    assert optimization_response.status_code == 200
    optimization = optimization_response.json()
    assert "recommendations" in optimization
    
    # 3. Получаем алерты
    alerts_response = requests.get(f"{API_BASE}/api/v1/alerts")
    assert alerts_response.status_code == 200
    alerts = alerts_response.json()
    assert "alerts" in alerts
    
    # 4. Проверяем здоровье системы
    health_response = requests.get(f"{API_BASE}/api/v1/health")
    assert health_response.status_code == 200
    health = health_response.json()
    assert health["status"] in ["healthy", "degraded"]


def test_health_check():
    """Тест проверки здоровья."""
    response = requests.get(f"{API_BASE}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
