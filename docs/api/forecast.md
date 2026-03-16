# API Documentation

## Forecast API

### POST /api/v1/forecast

Получить прогноз спроса для SKU в магазине.

**Request:**
```json
{
  "shop_id": "STORE-001",
  "sku_id": "SKU-001",
  "horizon_days": 7
}
```

**Response:**
```json
{
  "shop_id": "STORE-001",
  "sku_id": "SKU-001",
  "predictions": [
    {
      "date": "2026-03-17",
      "value": 120.5,
      "lower_bound": 102.4,
      "upper_bound": 138.6
    }
  ],
  "wape": 18.4,
  "model_version": "1.0.0"
}
```

### GET /api/v1/forecast/batch

Получить пакет прогнозов.

**Parameters:**
- `shop_id` (optional): ID магазина
- `category` (optional): Категория товаров
- `limit` (optional): Лимит записей (default: 100)

---

## Optimization API

### POST /api/v1/optimization

Оптимизировать заказ для магазина.

**Request:**
```json
{
  "shop_id": "STORE-001",
  "sku_ids": ["SKU-001", "SKU-002"],
  "horizon_days": 7
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "shop_id": "STORE-001",
      "sku_id": "SKU-001",
      "recommended_quantity": 50,
      "current_stock": 20,
      "safety_stock": 15,
      "forecast_demand": 55.0
    }
  ],
  "total_items": 150
}
```

---

## Alerts API

### GET /api/v1/alerts

Получить список алертов.

**Parameters:**
- `severity`: low, medium, high, critical
- `shop_id`: ID магазина
- `unresolved_only`: true/false
- `limit`: лимит записей

### POST /api/v1/alerts/{alert_id}/resolve

Отметить алерт как решенный.
