"""Модели запросов."""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class BaseRequest(BaseModel):
    """Базовый класс для запросов."""
    pass


class ForecastRequest(BaseRequest):
    """Запрос на прогноз."""
    shop_id: str = Field(..., description="ID магазина")
    sku_id: str = Field(..., description="ID товара")
    horizon_days: int = Field(default=7, ge=1, le=30, description="Горизонт прогноза в днях")


class BatchForecastRequest(BaseRequest):
    """Запрос на пакетный прогноз."""
    shop_ids: Optional[List[str]] = None
    sku_ids: Optional[List[str]] = None
    category: Optional[str] = None
    horizon_days: int = Field(default=7, ge=1, le=30)
    limit: int = Field(default=1000, ge=1, le=10000)


class OptimizationRequest(BaseRequest):
    """Запрос на оптимизацию заказа."""
    shop_id: str
    sku_ids: Optional[List[str]] = None
    horizon_days: int = Field(default=7, ge=1, le=30)
    constraints: Optional[dict] = None


class AlertFilterRequest(BaseRequest):
    """Фильтр для алертов."""
    severity: Optional[str] = None
    shop_id: Optional[str] = None
    sku_id: Optional[str] = None
    alert_type: Optional[str] = None
    unresolved_only: bool = True
