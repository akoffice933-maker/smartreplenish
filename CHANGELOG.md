# Changelog

Все изменения в проекте SmartReplenish.

Формат: [Keep a Changelog](https://keepachangelog.com/ru/1.0.0/)

## [Unreleased]

### Добавлено
- ROADMAP.md с планом развития
- Issue templates для feature requests и bug reports

### Изменено
- Удалены черновики из корня репозитория
- Добавлены CI/CD и Issues бейджи в README

## [1.0.0] - 2026-03-16

### Добавлено
- 🎉 Initial release SmartReplenish
- 7 микросервисов (api-gateway, forecasting, optimization, alerting, feature-store, data-ingestion, frontend)
- Инфраструктура (ClickHouse, PostgreSQL, Kafka, Prometheus, Grafana)
- ML модели (LightGBM + CatBoost)
- Docker Compose для быстрого развёртывания
- Документация (README, INVESTMENT_MEMO, API docs)
- CI/CD pipeline (GitHub Actions)
- Демо-интерфейс (smartreplenish_demo.html)

### Технические детали
- Python 3.11
- FastAPI 0.104+
- LightGBM 4.1+
- CatBoost 1.2+
- ClickHouse 23.8
- PostgreSQL 15
- Kafka 7.5
- React 18

[Unreleased]: https://github.com/akoffice933-maker/smartreplenish/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/akoffice933-maker/smartreplenish/releases/tag/v1.0.0
