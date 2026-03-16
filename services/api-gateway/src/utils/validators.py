"""Утилиты для валидации данных."""
from typing import Optional, List
import re


def validate_shop_id(shop_id: str) -> bool:
    """Валидировать ID магазина."""
    if not shop_id:
        return False
    # Пример: STORE-001
    pattern = r'^[A-Z]+-\d+$'
    return bool(re.match(pattern, shop_id))


def validate_sku_id(sku_id: str) -> bool:
    """Валидировать ID товара."""
    if not sku_id:
        return False
    # Пример: SKU-12345
    pattern = r'^[A-Z]+-\d+$'
    return bool(re.match(pattern, sku_id))


def validate_horizon_days(days: int) -> bool:
    """Валидировать горизонт прогноза."""
    return 1 <= days <= 30


def validate_limit(limit: int, max_limit: int = 10000) -> bool:
    """Валидировать лимит выборки."""
    return 1 <= limit <= max_limit


def sanitize_string(value: str) -> str:
    """Очистить строку от опасных символов."""
    if not value:
        return ""
    # Удаляем потенциально опасные символы
    return re.sub(r'[<>"\';]', '', value)


def parse_comma_separated(value: str) -> List[str]:
    """Разобрать строку с запятыми в список."""
    if not value:
        return []
    return [item.strip() for item in value.split(',') if item.strip()]
