"""Конфигурация Alerting Service."""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки сервиса алертов."""
    
    host: str = "0.0.0.0"
    port: int = 8000
    
    clickhouse_host: str = "clickhouse"
    clickhouse_port: int = 9000
    clickhouse_database: str = "smartreplenish"
    
    forecasting_url: str = "http://forecasting:8000"
    
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
