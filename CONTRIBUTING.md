# Вклад в проект SmartReplenish

Приветствуем вас! Мы рады любому вкладу в развитие SmartReplenish.

## Как внести вклад

### 1. Репозиторий

1. Forkните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/amazing-feature`)
3. Внесите изменения
4. Закоммитьте (`git commit -m 'Add amazing feature'`)
5. Отправьте (`git push origin feature/amazing-feature`)
6. Откройте Pull Request

### 2. Требования к коду

#### Python код

```python
# Используйте type hints
def calculate_forecast(shop_id: str, sku_id: str, horizon: int) -> list[float]:
    """Рассчитать прогноз спроса.
    
    Args:
        shop_id: ID магазина
        sku_id: ID товара
        horizon: Горизонт прогноза в днях
    
    Returns:
        Список прогнозов на каждый день
    """
    pass
```

#### Стиль кода

- **Black** для форматирования
- **isort** для сортировки импортов
- **ruff** для линтинга
- **mypy** для типизации

```bash
# Перед коммитом запустите
black services/
isort services/
ruff check services/
mypy services/
```

### 3. Тесты

Все PR должны включать тесты:

```bash
# Unit тесты
pytest services/api-gateway/tests/

# Интеграционные тесты
pytest tests/integration/

# E2E тесты
pytest tests/e2e/
```

### 4. Документация

- Обновляйте README.md при изменении API
- Добавляйте docstrings к новым функциям
- Обновляйте CHANGELOG.md

## Ветвление

| Ветка | Описание |
|-------|----------|
| `main` | Production-ready код |
| `develop` | Активная разработка |
| `feature/*` | Новые фичи |
| `bugfix/*` | Исправление багов |
| `hotfix/*` | Срочные fixes для production |

## Коммиты

Используем [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: добавить новый алгоритм прогнозирования
fix: исправить расчёт страхового запаса
docs: обновить README
style: форматирование кода
refactor: рефакторинг модуля оптимизации
test: добавить тесты для API
chore: обновить зависимости
```

## Code Review

- Минимум 1 аппрув от maintainer
- Все CI checks должны проходить
- No unresolved comments

## Контакты

- **Telegram**: @smartreplenish_dev
- **Email**: dev@smartreplenish.com

---

Спасибо за ваш вклад! 🚀
