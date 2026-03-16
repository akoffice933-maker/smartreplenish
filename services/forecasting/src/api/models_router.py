"""Маршруты для управления моделями."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class ModelInfo(BaseModel):
    name: str
    version: str
    wape: float
    trained_at: datetime
    status: str


class TrainRequest(BaseModel):
    force_retrain: bool = False
    sku_ids: Optional[List[str]] = None


class TrainResponse(BaseModel):
    status: str
    message: str
    models_trained: int


@router.get("", response_model=List[ModelInfo])
async def list_models():
    """Получить список обученных моделей."""
    return [
        ModelInfo(
            name="LightGBM_ensemble",
            version="1.0.0",
            wape=18.4,
            trained_at=datetime.now(),
            status="active"
        ),
        ModelInfo(
            name="CatBoost_ensemble",
            version="1.0.0",
            wape=18.7,
            trained_at=datetime.now(),
            status="active"
        )
    ]


@router.post("/train", response_model=TrainResponse)
async def train_models(request: TrainRequest):
    """Запустить переобучение моделей."""
    logger.info(f"Запуск обучения: force={request.force_retrain}, skus={request.sku_ids}")
    
    # В production здесь будет запуск пайплайна обучения
    return TrainResponse(
        status="success",
        message="Модели успешно обучены",
        models_trained=2
    )


@router.get("/{model_name}/metrics")
async def get_model_metrics(model_name: str):
    """Получить метрики модели."""
    return {
        "model_name": model_name,
        "wape": 18.4,
        "mape": 22.1,
        "smape": 19.8,
        "bias": 2.1,
        "mae": 15.3
    }
