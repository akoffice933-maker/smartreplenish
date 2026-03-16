"""Маршруты для работы с оптимизацией заказов."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import httpx

router = APIRouter()


class OrderRecommendation(BaseModel):
    shop_id: str
    sku_id: str
    recommended_quantity: int
    current_stock: int
    safety_stock: int
    forecast_demand: float
    supplier: Optional[str] = None


class OptimizationRequest(BaseModel):
    shop_id: str
    sku_ids: Optional[List[str]] = None
    horizon_days: int = 7


class OptimizationResponse(BaseModel):
    recommendations: List[OrderRecommendation]
    total_items: int
    total_value: Optional[float] = None


@router.post("", response_model=OptimizationResponse)
async def optimize_order(request: OptimizationRequest):
    """Оптимизировать заказ для магазина."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://optimization:8000/api/v1/optimize",
                json=request.dict(),
                timeout=30.0
            )
            response.raise_for_status()
            return OptimizationResponse(**response.json())
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Optimization service error: {str(e)}")


@router.get("/{order_id}")
async def get_order_status(order_id: str):
    """Получить статус заказа."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"http://optimization:8000/api/v1/orders/{order_id}",
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Optimization service error: {str(e)}")
