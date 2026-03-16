#!/bin/bash
# Скрипт для генерации тестовых данных

echo "Генерация тестовых данных для SmartReplenish..."

# Генерация тестовых продаж
python3 << 'EOF'
import random
import json
from datetime import datetime, timedelta

shops = [f"STORE-{str(i).zfill(3)}" for i in range(1, 11)]
skus = [f"SKU-{str(i).zfill(5)}" for i in range(1, 101)]

sales_data = []
for shop in shops:
    for sku in skus:
        base_sales = random.randint(50, 200)
        for days_ago in range(365):
            date = datetime.now() - timedelta(days=days_ago)
            dow = date.weekday()
            weekend_factor = 1.3 if dow >= 5 else 1.0
            seasonal_factor = 1.0 + 0.1 * random.gauss(0, 1)
            quantity = int(base_sales * weekend_factor * seasonal_factor + random.gauss(0, 10))
            
            if quantity > 0:
                sales_data.append({
                    "sale_id": f"SALE-{shop}-{sku}-{days_ago}",
                    "shop_id": shop,
                    "sku_id": sku,
                    "quantity": max(1, quantity),
                    "price": round(random.uniform(50, 500), 2),
                    "sale_timestamp": date.isoformat(),
                    "promo_flag": 1 if random.random() < 0.1 else 0,
                    "category": random.choice(["Молочное", "Хлеб", "Мясо", "Овощи"])
                })

print(f"Сгенерировано {len(sales_data)} записей о продажах")

with open("tests/fixtures/sample_sales.json", "w") as f:
    json.dump(sales_data[:1000], f, indent=2)

print("Первые 1000 записей сохранены в tests/fixtures/sample_sales.json")
EOF

echo "Готово!"
