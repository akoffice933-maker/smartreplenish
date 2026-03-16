"""Утилиты для метрик."""
import time
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)


def timing_decorator(func: Callable) -> Callable:
    """Декоратор для замера времени выполнения функции."""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = await func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.debug(f"{func.__name__} executed in {elapsed_time:.3f}s")
        return result
    return wrapper


def calculate_percentile(values: list, percentile: float) -> float:
    """Вычислить перцентиль."""
    if not values:
        return 0.0
    
    sorted_values = sorted(values)
    index = int(len(sorted_values) * percentile / 100)
    return sorted_values[min(index, len(sorted_values) - 1)]


class MetricsCollector:
    """Коллектор метрик для API Gateway."""
    
    def __init__(self):
        self.request_times: dict = {}
        self.request_counts: dict = {}
    
    def record_request(self, endpoint: str, duration: float):
        """Записать метрики запроса."""
        if endpoint not in self.request_times:
            self.request_times[endpoint] = []
            self.request_counts[endpoint] = 0
        
        self.request_times[endpoint].append(duration)
        self.request_counts[endpoint] += 1
        
        # Храним только последние 1000 значений
        if len(self.request_times[endpoint]) > 1000:
            self.request_times[endpoint] = self.request_times[endpoint][-1000:]
    
    def get_p95_latency(self, endpoint: str) -> float:
        """Получить p95 latency для эндпоинта."""
        if endpoint not in self.request_times:
            return 0.0
        return calculate_percentile(self.request_times[endpoint], 95)
    
    def get_rps(self, endpoint: str, window_seconds: int = 60) -> float:
        """Получить RPS для эндпоинта."""
        if endpoint not in self.request_counts:
            return 0.0
        return self.request_counts[endpoint] / window_seconds


metrics = MetricsCollector()
