"""Маршруты для работы с алертами."""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import httpx

router = APIRouter()


class Alert(BaseModel):
    id: str
    type: str  # stockout, overstock, expiry
    severity: str  # low, medium, high, critical
    shop_id: str
    sku_id: str
    message: str
    created_at: datetime
    resolved: bool = False


class AlertResponse(BaseModel):
    alerts: List[Alert]
    total: int
    unresolved: int


@router.get("", response_model=AlertResponse)
async def get_alerts(
    severity: Optional[str] = None,
    shop_id: Optional[str] = None,
    unresolved_only: bool = True,
    limit: int = Query(default=50, le=500)
):
    """Получить список алертов."""
    async with httpx.AsyncClient() as client:
        try:
            params = {"limit": limit, "unresolved_only": unresolved_only}
            if severity:
                params["severity"] = severity
            if shop_id:
                params["shop_id"] = shop_id
            
            response = await client.get(
                "http://alerting:8000/api/v1/alerts",
                params=params,
                timeout=10.0
            )
            response.raise_for_status()
            return AlertResponse(**response.json())
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Alerting service error: {str(e)}")


@router.post("/{alert_id}/resolve")
async def resolve_alert(alert_id: str):
    """Отметить алерт как решенный."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"http://alerting:8000/api/v1/alerts/{alert_id}/resolve",
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Alerting service error: {str(e)}")
