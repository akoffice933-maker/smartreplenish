"""Нагрузочное тестирование с Locust."""
from locust import HttpUser, task, between


class SmartReplenishUser(HttpUser):
    """Пользователь для нагрузочного тестирования."""
    
    wait_time = between(1, 3)
    
    @task(3)
    def get_forecast(self):
        """Запрос прогноза."""
        self.client.post(
            "/api/v1/forecast",
            json={"shop_id": "STORE-001", "sku_id": "SKU-001", "horizon_days": 7}
        )
    
    @task(2)
    def get_health(self):
        """Проверка здоровья."""
        self.client.get("/health")
    
    @task(1)
    def get_alerts(self):
        """Получение алертов."""
        self.client.get("/api/v1/alerts")
    
    @task(1)
    def optimize_order(self):
        """Оптимизация заказа."""
        self.client.post(
            "/api/v1/optimization",
            json={"shop_id": "STORE-001", "horizon_days": 7}
        )
