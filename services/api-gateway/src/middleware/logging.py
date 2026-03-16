"""Middleware для логирования запросов."""
import logging
import time
import json

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """Логирует все входящие запросы и ответы."""
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        
        start_time = time.time()
        
        # Получаем информацию о запросе
        method = scope["method"]
        path = scope["path"]
        query_string = scope.get("query_string", b"").decode()
        
        logger.info(f"Request: {method} {path}?{query_string}")
        
        # Вызываем следующее middleware/приложение
        await self.app(scope, receive, send)
        
        # Логируем время обработки
        process_time = time.time() - start_time
        logger.info(f"Response time: {process_time:.3f}s")
