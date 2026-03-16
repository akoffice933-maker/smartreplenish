"""Конфигурация Forecasting Service."""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки сервиса прогнозирования."""
    
    # Сервер
    host: str = "0.0.0.0"
    port: int = 8000
    
    # ClickHouse
    clickhouse_host: str = "clickhouse"
    clickhouse_port: int = 9000
    clickhouse_database: str = "smartreplenish"
    clickhouse_user: str = "default"
    clickhouse_password: str = ""
    
    # Feature Store
    feature_store_url: str = "http://feature-store:8000"
    
    # Модель
    model_path: str = "/app/models"
    forecast_horizon: int = 7
    wape_threshold: float = 22.0
    
    # Логирование
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
