"""Маршруты для работы с прогнозами."""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import httpx

router = APIRouter()


class ForecastRequest(BaseModel):
    shop_id: str
    sku_id: str
    horizon_days: int = 7


class ForecastPrediction(BaseModel):
    date: str
    value: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None


class ForecastResponse(BaseModel):
    shop_id: str
    sku_id: str
    predictions: List[ForecastPrediction]
    wape: Optional[float] = None
    model_version: str


@router.post("", response_model=ForecastResponse)
async def get_forecast(request: ForecastRequest):
    """Получить прогноз спроса для SKU в магазине."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://forecasting:8000/api/v1/forecast",
                json=request.dict(),
                timeout=30.0
            )
            response.raise_for_status()
            return ForecastResponse(**response.json())
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Forecast service error: {str(e)}")


@router.get("/batch")
async def get_batch_forecast(
    shop_id: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = Query(default=100, le=1000)
):
    """Получить пакет прогнозов для магазина или категории."""
    async with httpx.AsyncClient() as client:
        try:
            params = {"limit": limit}
            if shop_id:
                params["shop_id"] = shop_id
            if category:
                params["category"] = category
            
            response = await client.get(
                "http://forecasting:8000/api/v1/forecast/batch",
                params=params,
                timeout=60.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Forecast service error: {str(e)}")
