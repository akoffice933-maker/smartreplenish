-- Инициализация ClickHouse для SmartReplenish

CREATE DATABASE IF NOT EXISTS smartreplenish;

-- Таблица продаж
CREATE TABLE IF NOT EXISTS smartreplenish.sales
(
    sale_id String,
    shop_id String,
    sku_id String,
    quantity UInt32,
    price Float64,
    sale_timestamp DateTime,
    promo_flag UInt8 DEFAULT 0,
    category String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(sale_timestamp)
ORDER BY (shop_id, sku_id, sale_timestamp);

-- Таблица остатков
CREATE TABLE IF NOT EXISTS smartreplenish.inventory
(
    record_id String,
    shop_id String,
    sku_id String,
    quantity Int32,
    reserved UInt32 DEFAULT 0,
    timestamp DateTime
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (shop_id, sku_id, timestamp);

-- Таблица товаров
CREATE TABLE IF NOT EXISTS smartreplenish.products
(
    sku_id String,
    name String,
    category String,
    subcategory String,
    unit String,
    supplier_id String,
    min_order_qty UInt32 DEFAULT 1,
    shelf_life_days UInt32 DEFAULT 0,
    is_active UInt8 DEFAULT 1
) ENGINE = MergeTree()
ORDER BY sku_id;

-- Таблица магазинов
CREATE TABLE IF NOT EXISTS smartreplenish.shops
(
    shop_id String,
    name String,
    address String,
    city String,
    region String,
    format String,
    area_sqm Float32,
    is_active UInt8 DEFAULT 1
) ENGINE = MergeTree()
ORDER BY shop_id;

-- Таблица прогнозов
CREATE TABLE IF NOT EXISTS smartreplenish.forecasts
(
    forecast_id String,
    shop_id String,
    sku_id String,
    forecast_date Date,
    predicted_value Float64,
    lower_bound Float64,
    upper_bound Float64,
    model_version String,
    created_at DateTime
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(forecast_date)
ORDER BY (shop_id, sku_id, forecast_date);

-- Таблица заказов
CREATE TABLE IF NOT EXISTS smartreplenish.orders
(
    order_id String,
    shop_id String,
    sku_id String,
    quantity UInt32,
    status String,
    supplier_id String,
    created_at DateTime,
    expected_at DateTime,
    received_at Nullable(DateTime)
) ENGINE = MergeTree()
ORDER BY (order_id, created_at);

-- Materialized View для агрегации продаж по дням
CREATE TABLE IF NOT EXISTS smartreplenish.sales_daily
(
    shop_id String,
    sku_id String,
    date Date,
    total_quantity UInt64,
    total_revenue Float64,
    avg_price Float64
) ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(date)
ORDER BY (shop_id, sku_id, date);

CREATE MATERIALIZED VIEW IF NOT EXISTS smartreplenish.sales_daily_mv
TO smartreplenish.sales_daily
AS SELECT
    shop_id,
    sku_id,
    toDate(sale_timestamp) as date,
    sum(quantity) as total_quantity,
    sum(quantity * price) as total_revenue,
    avg(price) as avg_price
FROM smartreplenish.sales
GROUP BY shop_id, sku_id, date;
