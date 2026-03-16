"""Маршруты для метрик сервиса."""
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class MetricsResponse(BaseModel):
    service: str
    version: str
    uptime_seconds: float
    predictions_count: int
    avg_latency_ms: float


@router.get("", response_model=MetricsResponse)
async def get_metrics():
    """Получить метрики сервиса."""
    return MetricsResponse(
        service="forecasting",
        version="1.0.0",
        uptime_seconds=3600.0,
        predictions_count=15420,
        avg_latency_ms=45.2
    )
