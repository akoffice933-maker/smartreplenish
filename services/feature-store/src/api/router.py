"""API маршруты для Feature Store."""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class FeatureRequest(BaseModel):
    shop_id: str
    sku_id: str
    features: List[str]


class FeatureResponse(BaseModel):
    shop_id: str
    sku_id: str
    features: Dict[str, Any]
    timestamp: datetime


@router.get("/features", response_model=FeatureResponse)
async def get_features(
    shop_id: str,
    sku_id: str,
    features: Optional[str] = None
):
    """Получить признаки для SKU в магазине."""
    logger.info(f"Запрос признаков: shop={shop_id}, sku={sku_id}")
    
    # Генерируем тестовые признаки
    feature_list = features.split(",") if features else [
        "lag_7d", "lag_14d", "lag_28d",
        "rolling_mean_7d", "rolling_std_7d",
        "day_of_week", "month", "is_weekend"
    ]
    
    features_dict = {
        "lag_7d": 120,
        "lag_14d": 115,
        "lag_28d": 110,
        "rolling_mean_7d": 118.5,
        "rolling_std_7d": 15.2,
        "day_of_week": datetime.now().weekday(),
        "month": datetime.now().month,
        "is_weekend": datetime.now().weekday() >= 5
    }
    
    return FeatureResponse(
        shop_id=shop_id,
        sku_id=sku_id,
        features={k: v for k, v in features_dict.items() if k in feature_list},
        timestamp=datetime.now()
    )


@router.post("/features/compute")
async def compute_features(request: FeatureRequest):
    """Вычислить признаки для SKU."""
    logger.info(f"Вычисление признаков: shop={request.shop_id}, sku={request.sku_id}")
    
    return {
        "status": "success",
        "shop_id": request.shop_id,
        "sku_id": request.sku_id,
        "computed_features": len(request.features)
    }


@router.get("/features/list")
async def list_features():
    """Получить список доступных признаков."""
    return {
        "features": [
            {"name": "lag_7d", "description": "Продажи 7 дней назад", "type": "numeric"},
            {"name": "lag_14d", "description": "Продажи 14 дней назад", "type": "numeric"},
            {"name": "lag_28d", "description": "Продажи 28 дней назад", "type": "numeric"},
            {"name": "rolling_mean_7d", "description": "Среднее за 7 дней", "type": "numeric"},
            {"name": "rolling_std_7d", "description": "Стд отклонение за 7 дней", "type": "numeric"},
            {"name": "day_of_week", "description": "День недели", "type": "categorical"},
            {"name": "month", "description": "Месяц", "type": "categorical"},
            {"name": "is_weekend", "description": "Выходной день", "type": "boolean"},
            {"name": "is_promo", "description": "Идет промоакция", "type": "boolean"},
            {"name": "price", "description": "Цена товара", "type": "numeric"},
        ]
    }
