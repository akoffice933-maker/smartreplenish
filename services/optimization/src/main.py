"""Главное приложение Optimization Service."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .config import settings
from .api.router import router as optimization_router

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SmartReplenish Optimization Service",
    description="Сервис оптимизации заказов",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(optimization_router, prefix="/api/v1", tags=["optimization"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "optimization", "version": "1.0.0"}


@app.on_event("startup")
async def startup_event():
    logger.info(f"Optimization Service запущен на порту {settings.port}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Optimization Service остановлен")
