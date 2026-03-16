"""API маршруты для оптимизации."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class OptimizationRequest(BaseModel):
    shop_id: str
    sku_ids: Optional[List[str]] = None
    horizon_days: int = 7


class OrderRecommendation(BaseModel):
    shop_id: str
    sku_id: str
    recommended_quantity: int
    current_stock: int
    safety_stock: int
    forecast_demand: float
    supplier: Optional[str] = None


class OptimizationResponse(BaseModel):
    recommendations: List[OrderRecommendation]
    total_items: int
    total_value: Optional[float] = None


@router.post("/optimize", response_model=OptimizationResponse)
async def optimize_order(request: OptimizationRequest):
    """Оптимизировать заказ для магазина."""
    logger.info(f"Оптимизация заказа: shop={request.shop_id}, horizon={request.horizon_days}")
    
    # Генерируем тестовые рекомендации
    recommendations = []
    sku_ids = request.sku_ids or [f"SKU-{str(i).zfill(5)}" for i in range(10)]
    
    for sku_id in sku_ids[:10]:  # Ограничим 10 для демо
        forecast_demand = 50 + hash(sku_id) % 100
        current_stock = hash(sku_id) % 50
        safety_stock = int(forecast_demand * 0.3)
        recommended_qty = max(0, int(forecast_demand - current_stock + safety_stock))
        
        recommendations.append(OrderRecommendation(
            shop_id=request.shop_id,
            sku_id=sku_id,
            recommended_quantity=recommended_qty,
            current_stock=current_stock,
            safety_stock=safety_stock,
            forecast_demand=forecast_demand,
            supplier=f"Supplier-{hash(sku_id) % 5}"
        ))
    
    return OptimizationResponse(
        recommendations=recommendations,
        total_items=sum(r.recommended_quantity for r in recommendations),
        total_value=None
    )


@router.get("/orders/{order_id}")
async def get_order_status(order_id: str):
    """Получить статус заказа."""
    return {
        "order_id": order_id,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "items_count": 10
    }
