-- Инициализация PostgreSQL для SmartReplenish

-- Метаданные пользователей
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Метаданные моделей ML
CREATE TABLE IF NOT EXISTS models (
    model_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    model_type VARCHAR(50),
    hyperparameters JSONB,
    metrics JSONB,
    trained_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- История обучений моделей
CREATE TABLE IF NOT EXISTS model_training_history (
    training_id VARCHAR(50) PRIMARY KEY,
    model_id VARCHAR(50) REFERENCES models(model_id),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status VARCHAR(20),
    metrics JSONB,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Конфигурация алертов
CREATE TABLE IF NOT EXISTS alert_configs (
    config_id VARCHAR(50) PRIMARY KEY,
    alert_type VARCHAR(50) NOT NULL,
    threshold_value FLOAT,
    threshold_type VARCHAR(20),
    notification_channels JSONB,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- История алертов
CREATE TABLE IF NOT EXISTS alerts_history (
    alert_id VARCHAR(50) PRIMARY KEY,
    alert_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20),
    shop_id VARCHAR(50),
    sku_id VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    resolved_by VARCHAR(50),
    metadata JSONB
);

-- Логи системы
CREATE TABLE IF NOT EXISTS system_logs (
    log_id SERIAL PRIMARY KEY,
    service_name VARCHAR(50),
    log_level VARCHAR(20),
    message TEXT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для ускорения запросов
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_models_active ON models(is_active);
CREATE INDEX IF NOT EXISTS idx_alerts_created ON alerts_history(created_at);
CREATE INDEX IF NOT EXISTS idx_logs_service ON system_logs(service_name);
CREATE INDEX IF NOT EXISTS idx_logs_created ON system_logs(created_at);

-- Вставка тестовых данных
INSERT INTO users (user_id, username, email, role) VALUES
    ('admin', 'admin', 'admin@smartreplenish.com', 'admin'),
    ('manager', 'manager', 'manager@smartreplenish.com', 'manager'),
    ('analyst', 'analyst', 'analyst@smartreplenish.com', 'analyst')
ON CONFLICT (user_id) DO NOTHING;
