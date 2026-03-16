"""Главное приложение Feature Store."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .config import settings
from .api.router import router as feature_router

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SmartReplenish Feature Store",
    description="Хранилище признаков для ML моделей",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(feature_router, prefix="/api/v1", tags=["features"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "feature-store", "version": "1.0.0"}


@app.on_event("startup")
async def startup_event():
    logger.info(f"Feature Store запущен на порту {settings.port}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Feature Store остановлен")
