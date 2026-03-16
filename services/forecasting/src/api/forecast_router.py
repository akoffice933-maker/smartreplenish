"""Маршруты для работы с прогнозами."""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class ForecastRequest(BaseModel):
    shop_id: str
    sku_id: str
    horizon_days: int = 7


class Prediction(BaseModel):
    date: str
    value: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None


class ForecastResponse(BaseModel):
    shop_id: str
    sku_id: str
    predictions: List[Prediction]
    wape: Optional[float] = None
    model_version: str = "1.0.0"


@router.post("/forecast", response_model=ForecastResponse)
async def get_forecast(request: ForecastRequest):
    """Получить прогноз спроса для SKU в магазине."""
    logger.info(f"Запрос прогноза: shop={request.shop_id}, sku={request.sku_id}, horizon={request.horizon_days}")
    
    # Генерируем тестовые данные (в production здесь будет вызов ML модели)
    predictions = []
    base_value = 100.0
    
    for i in range(request.horizon_days):
        date = (datetime.now() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        # Имитация прогноза с сезонностью по дням недели
        dow_factor = 1.0 + 0.1 * (i % 7)  # Простая недельная сезонность
        value = base_value * dow_factor + (i - request.horizon_days/2) * 2
        
        predictions.append(Prediction(
            date=date,
            value=round(value, 2),
            lower_bound=round(value * 0.85, 2),
            upper_bound=round(value * 1.15, 2)
        ))
    
    return ForecastResponse(
        shop_id=request.shop_id,
        sku_id=request.sku_id,
        predictions=predictions,
        wape=18.4
    )


@router.get("/forecast/batch")
async def get_batch_forecast(
    shop_id: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = Query(default=100, le=1000)
):
    """Получить пакет прогнозов."""
    logger.info(f"Пакетный запрос: shop={shop_id}, category={category}, limit={limit}")
    
    # Генерируем тестовые данные
    results = []
    for i in range(min(limit, 10)):
        results.append({
            "shop_id": shop_id or f"STORE-{str(i).zfill(3)}",
            "sku_id": f"SKU-{str(i*100).zfill(5)}",
            "predictions": [
                {
                    "date": (datetime.now() + timedelta(days=j+1)).strftime("%Y-%m-%d"),
                    "value": round(50 + i*10 + j*2, 2)
                }
                for j in range(7)
            ]
        })
    
    return {"forecasts": results, "total": len(results)}
