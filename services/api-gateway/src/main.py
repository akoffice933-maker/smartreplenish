"""Главное приложение API Gateway."""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import time

from .config import settings
from .middleware.auth import AuthMiddleware
from .middleware.rate_limit import RateLimitMiddleware
from .middleware.logging import LoggingMiddleware
from .routes import forecast, optimization, alerts, health

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SmartReplenish API Gateway",
    description="Единая точка входа для системы прогнозирования и оптимизации",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В production ограничить
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware, requests=settings.rate_limit_requests, period=settings.rate_limit_period)
app.add_middleware(AuthMiddleware, secret_key=settings.jwt_secret_key)


@app.middleware("http")
async def add_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}


# Роуты
app.include_router(forecast.router, prefix="/api/v1/forecast", tags=["forecast"])
app.include_router(optimization.router, prefix="/api/v1/optimization", tags=["optimization"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["alerts"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])


@app.on_event("startup")
async def startup_event():
    logger.info(f"API Gateway запущен на порту {settings.port}")
    logger.info(f"Forecasting URL: {settings.forecasting_url}")
    logger.info(f"Optimization URL: {settings.optimization_url}")
    logger.info(f"Alerting URL: {settings.alerting_url}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("API Gateway остановлен")
