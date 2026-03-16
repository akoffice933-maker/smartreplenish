"""Главное приложение Alerting Service."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .config import settings
from .api.router import router as alerting_router

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SmartReplenish Alerting Service",
    description="Сервис алертов и уведомлений",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alerting_router, prefix="/api/v1", tags=["alerts"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "alerting", "version": "1.0.0"}


@app.on_event("startup")
async def startup_event():
    logger.info(f"Alerting Service запущен на порту {settings.port}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Alerting Service остановлен")
