"""Конфигурация приложения."""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки API Gateway."""
    
    # Сервер
    host: str = "0.0.0.0"
    port: int = 8000
    
    # JWT
    jwt_secret_key: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    
    # Rate limiting
    rate_limit_requests: int = 100
    rate_limit_period: int = 60
    
    # URL сервисов
    forecasting_url: str = "http://forecasting:8000"
    optimization_url: str = "http://optimization:8000"
    alerting_url: str = "http://alerting:8000"
    
    # Логирование
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
