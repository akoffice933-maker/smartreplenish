.PHONY: help up down logs test test-unit test-integration test-e2e test-load clean build

help:
	@echo "SmartReplenish Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make up          Запустить все сервисы"
	@echo "  make down        Остановить все сервисы"
	@echo "  make logs        Просмотр логов"
	@echo "  make test        Запустить все тесты"
	@echo "  make test-unit   Unit-тесты"
	@echo "  make test-integration  Интеграционные тесты"
	@echo "  make test-e2e    E2E тесты"
	@echo "  make test-load   Нагрузочное тестирование"
	@echo "  make clean       Очистка"
	@echo "  make build       Пересборка образов"

up:
	docker-compose up -d
	@echo "Сервисы запущены. Доступ: http://localhost:3000"

down:
	docker-compose down

logs:
	docker-compose logs -f

test: test-unit test-integration test-e2e

test-unit:
	docker-compose exec api-gateway pytest tests/unit -v
	docker-compose exec forecasting pytest tests/unit -v

test-integration:
	pytest tests/integration -v

test-e2e:
	pytest tests/e2e -v

test-load:
	cd tests/performance && locust -f locustfile.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pkl" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

build:
	docker-compose build

.PHONY: init-db migrate backup restore

init-db:
	docker-compose exec clickhouse clickhouse-client --multiquery < infra/clickhouse/init/01_init.sql
	docker-compose exec postgres psql -U admin -d smartreplenish -f /docker-entrypoint-initdb.d/01_init.sql

migrate:
	@echo "Running migrations..."
	@for f in infra/clickhouse/migrations/*.sql; do \
		echo "Applying $$f..."; \
		docker-compose exec -T clickhouse clickhouse-client --multiquery < $$f; \
	done

backup:
	./scripts/backup.sh

restore:
	./scripts/restore.sh
