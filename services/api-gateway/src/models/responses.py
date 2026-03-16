"""Модели ответов."""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class BaseResponse(BaseModel):
    """Базовый класс для ответов."""
    success: bool = True
    message: Optional[str] = None


class Prediction(BaseModel):
    """Прогноз на один день."""
    date: str
    value: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None


class ForecastResponse(BaseResponse):
    """Ответ с прогнозом."""
    shop_id: str
    sku_id: str
    predictions: List[Prediction]
    wape: Optional[float] = None
    mape: Optional[float] = None
    model_version: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class OrderRecommendation(BaseModel):
    """Рекомендация по заказу."""
    shop_id: str
    sku_id: str
    recommended_quantity: int
    current_stock: int
    safety_stock: int
    forecast_demand: float
    supplier: Optional[str] = None
    estimated_cost: Optional[float] = None


class OptimizationResponse(BaseResponse):
    """Ответ с оптимизацией заказа."""
    recommendations: List[OrderRecommendation]
    total_items: int
    total_value: Optional[float] = None
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class Alert(BaseModel):
    """Алерт."""
    id: str
    type: str
    severity: str
    shop_id: str
    sku_id: str
    message: str
    created_at: datetime
    resolved: bool = False
    resolved_at: Optional[datetime] = None


class AlertResponse(BaseResponse):
    """Ответ со списком алертов."""
    alerts: List[Alert]
    total: int
    unresolved: int


class ServiceHealth(BaseModel):
    """Статус сервиса."""
    status: str
    latency_ms: Optional[float] = None
    error: Optional[str] = None


class HealthResponse(BaseResponse):
    """Ответ проверки здоровья."""
    status: str
    services: Dict[str, ServiceHealth]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
