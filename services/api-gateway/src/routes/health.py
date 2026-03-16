"""Маршруты для проверки здоровья системы."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import httpx
import asyncio

router = APIRouter()


class ServiceHealth(BaseModel):
    status: str
    latency_ms: Optional[float] = None
    error: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    services: Dict[str, ServiceHealth]


async def check_service_health(name: str, url: str) -> tuple[str, ServiceHealth]:
    """Проверить здоровье отдельного сервиса."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{url}/health", timeout=5.0)
            response.raise_for_status()
            return name, ServiceHealth(status="healthy", latency_ms=response.elapsed.total_seconds() * 1000)
    except Exception as e:
        return name, ServiceHealth(status="unhealthy", error=str(e))


@router.get("", response_model=HealthResponse)
async def health_check():
    """Проверить здоровье всех сервисов."""
    services = {
        "forecasting": "http://forecasting:8000",
        "optimization": "http://optimization:8000",
        "alerting": "http://alerting:8000",
    }
    
    tasks = [check_service_health(name, url) for name, url in services.items()]
    results = await asyncio.gather(*tasks)
    
    services_health = dict(results)
    
    # Определяем общий статус
    all_healthy = all(s.status == "healthy" for s in services_health.values())
    any_healthy = any(s.status == "healthy" for s in services_health.values())
    
    if all_healthy:
        overall_status = "healthy"
    elif any_healthy:
        overall_status = "degraded"
    else:
        overall_status = "unhealthy"
    
    return HealthResponse(status=overall_status, services=services_health)
