"""Главное приложение Forecasting Service."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .config import settings
from .api.forecast_router import router as forecast_router
from .api.models_router import router as models_router
from .api.metrics_router import router as metrics_router

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SmartReplenish Forecasting Service",
    description="Сервис прогнозирования спроса на основе ML",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forecast_router, prefix="/api/v1", tags=["forecast"])
app.include_router(models_router, prefix="/api/v1/models", tags=["models"])
app.include_router(metrics_router, prefix="/api/v1/metrics", tags=["metrics"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "forecasting", "version": "1.0.0"}


@app.on_event("startup")
async def startup_event():
    logger.info(f"Forecasting Service запущен на порту {settings.port}")
    logger.info(f"ClickHouse: {settings.clickhouse_host}:{settings.clickhouse_port}")
    logger.info(f"Feature Store: {settings.feature_store_url}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Forecasting Service остановлен")
