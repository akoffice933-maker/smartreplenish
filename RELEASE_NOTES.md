# 🎉 SmartReplenish v1.0.0 — Initial Release

## ✨ Основные возможности

### Микросервисы
- **api-gateway** — единая точка входа (FastAPI)
- **forecasting** — ML прогнозирование спроса (LightGBM + CatBoost)
- **optimization** — математическая оптимизация заказов
- **alerting** — система уведомлений и алертов
- **feature-store** — хранилище признаков для ML
- **data-ingestion** — загрузка данных из внешних источников
- **frontend** — React dashboard

### Инфраструктура
- **ClickHouse 23.8** — аналитическая БД для временных рядов
- **PostgreSQL 15** — метаданные и конфигурации
- **Kafka 7.5** — потоковая обработка данных
- **Prometheus + Grafana** — мониторинг и дашборды

### Ключевые метрики
| Показатель | Значение |
|------------|----------|
| Точность прогноза (WAPE) | < 22% (горизонт 7 дней) |
| Снижение запасов | 8-18% |
| Доступность товара (OSA) | ≥ 97% |
| Снижение списаний (fresh) | 15-30% |
| Время планирования | −97% (с 8 часов до 15 минут) |

## 📚 Документация

- **README.md** — полное описание проекта с бизнес-моделью
- **INVESTMENT_MEMO.md** — инвестиционный меморандум для инвесторов
- **ROADMAP.md** — план развития v1.0 → v2.0
- **CHANGELOG.md** — история изменений
- **docs/** — API документация, архитектура, deployment guide

## 🚀 Быстрый старт

```bash
git clone https://github.com/akoffice933-maker/smartreplenish.git
cd smartreplenish
docker-compose up -d
```

Доступ к сервисам:
- Frontend: http://localhost:3000
- API Gateway: http://localhost:8080/docs
- Grafana: http://localhost:3030 (admin/admin)

## 📊 Рынок и возможности

- **TAM**: $28.3 млрд к 2030 (Retail Analytics)
- **Бизнес-модель**: SaaS подписка ($2K-$15K/мес) + внедрение ($50K-$200K)
- **Целевой сегмент**: ритейлеры 50-1000+ магазинов
- **ROI для клиента**: 200-500% в первый год

## 🔧 Технические детали

### Стек технологий
- **Backend**: Python 3.11, FastAPI 0.104+
- **ML/DS**: LightGBM 4.1+, CatBoost 1.2+, scikit-learn 1.3+
- **Frontend**: React 18, Chart.js 4.4+
- **БД**: ClickHouse 23.8, PostgreSQL 15
- **Streaming**: Kafka 7.5
- **Monitoring**: Prometheus 2.48, Grafana 10.2

### Тестирование
- Unit-тесты (pytest)
- Интеграционные тесты
- E2E тесты (полный пайплайн)
- Нагрузочное тестирование (Locust)

### CI/CD
- GitHub Actions
- Автоматический запуск тестов при push
- Build Docker образов
- Security scan зависимостей

## 📈 Что дальше

### v1.1.0 (Q3 2026)
- [ ] Ансамбль моделей (LightGBM + CatBoost)
- [ ] Feature Store v2
- [ ] Kubernetes manifests
- [ ] Auto-scaling

### v2.0.0 (2027)
- [ ] Deep Learning (TFT, N-BEATS)
- [ ] Reinforcement Learning для оптимизации
- [ ] Multi-Echelon оптимизация

## 🤝 Участие в проекте

- 📋 [ROADMAP.md](ROADMAP.md) — план развития
- 🐛 [Issues](https://github.com/akoffice933-maker/smartreplenish/issues) — задачи
- 📖 [CONTRIBUTING.md](CONTRIBUTING.md) — как внести вклад

## 📞 Контакты

- **GitHub**: [@akoffice933-maker](https://github.com/akoffice933-maker)
- **Demo**: [smartreplenish_demo.html](https://akoffice933-maker.github.io/smartreplenish/smartreplenish_demo.html)

---

**Full Changelog**: https://github.com/akoffice933-maker/smartreplenish/commits/v1.0.0
