# Production Deployment Guide

## Предварительные требования

- Kubernetes кластер (1.25+)
- Helm 3.x
- Docker registry
- SSL сертификаты

## Установка

### 1. Подготовка namespace

```bash
kubectl create namespace smartreplenish
```

### 2. Создание секретов

```bash
kubectl create secret generic smartreplenish-secrets \
  --from-literal=jwt-secret-key=$(openssl rand -hex 32) \
  --from-literal=postgres-password=$(openssl rand -hex 16) \
  --from-literal=clickhouse-password=$(openssl rand -hex 16) \
  -n smartreplenish
```

### 3. Установка через Helm

```bash
helm install smartreplenish ./helm/smartreplenish \
  --namespace smartreplenish \
  -f values-production.yaml
```

## Конфигурация

### Production значения (values-production.yaml)

```yaml
replicaCount: 3

resources:
  limits:
    cpu: 2000m
    memory: 4Gi
  requests:
    cpu: 500m
    memory: 1Gi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

ingress:
  enabled: true
  tls: true
  host: api.smartreplenish.com
```

## Мониторинг

### Prometheus метрики

- `http_requests_total`: Количество запросов
- `http_request_duration_seconds`: Время обработки
- `forecast_wape`: Точность прогнозов
- `model_inference_latency`: Время инференса модели

### Grafana дашборды

- System Health
- Forecast Accuracy
- Business KPIs
- Resource Usage

## Backup

### PostgreSQL

```bash
pg_dump -h postgres -U admin smartreplenish > backup.sql
```

### ClickHouse

```bash
clickhouse-client --query "BACKUP TABLE sales TO DISK 'backups'"
```

## Disaster Recovery

1. Восстановление из backup
2. Пересоздание pod'ов
3. Проверка health endpoints
4. Валидация данных

## Security

- TLS для всех внешних соединений
- JWT аутентификация
- Rate limiting
- Network policies
- Pod security policies
