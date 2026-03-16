"""Конфигурация Optimization Service."""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки сервиса оптимизации."""
    
    host: str = "0.0.0.0"
    port: int = 8000
    
    forecasting_url: str = "http://forecasting:8000"
    
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
