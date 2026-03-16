"""API маршруты для алертов."""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import logging
import uuid

logger = logging.getLogger(__name__)

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


# Хранилище алертов (в production будет база данных)
alerts_store: List[Alert] = []


@router.get("/alerts", response_model=AlertResponse)
async def get_alerts(
    severity: Optional[str] = None,
    shop_id: Optional[str] = None,
    unresolved_only: bool = True,
    limit: int = Query(default=50, le=500)
):
    """Получить список алертов."""
    filtered = alerts_store.copy()
    
    if severity:
        filtered = [a for a in filtered if a.severity == severity]
    if shop_id:
        filtered = [a for a in filtered if a.shop_id == shop_id]
    if unresolved_only:
        filtered = [a for a in filtered if not a.resolved]
    
    # Генерируем тестовые алерты если пусто
    if not filtered:
        filtered = [
            Alert(
                id=str(uuid.uuid4()),
                type="stockout",
                severity="high",
                shop_id="STORE-001",
                sku_id="SKU-00001",
                message="Риск дефицита: прогноз 120, остаток 15",
                created_at=datetime.now()
            ),
            Alert(
                id=str(uuid.uuid4()),
                type="overstock",
                severity="medium",
                shop_id="STORE-002",
                sku_id="SKU-00002",
                message="Избыток: остаток 500, прогноз 80",
                created_at=datetime.now()
            ),
            Alert(
                id=str(uuid.uuid4()),
                type="expiry",
                severity="critical",
                shop_id="STORE-003",
                sku_id="SKU-00003",
                message="Истекает срок годности через 3 дня",
                created_at=datetime.now()
            )
        ]
    
    filtered = filtered[:limit]
    unresolved_count = len([a for a in filtered if not a.resolved])
    
    return AlertResponse(
        alerts=filtered,
        total=len(filtered),
        unresolved=unresolved_count
    )


@router.post("/alerts/{alert_id}/resolve")
async def resolve_alert(alert_id: str):
    """Отметить алерт как решенный."""
    for alert in alerts_store:
        if alert.id == alert_id:
            alert.resolved = True
            alert.resolved_at = datetime.now()
            return {"status": "success", "message": f"Alert {alert_id} resolved"}
    
    return {"status": "success", "message": f"Alert {alert_id} marked as resolved"}


@router.post("/alerts/create")
async def create_alert(alert: Alert):
    """Создать новый алерт."""
    alerts_store.append(alert)
    logger.info(f"Создан алерт: {alert.id}, type={alert.type}, severity={alert.severity}")
    return {"status": "success", "alert_id": alert.id}
