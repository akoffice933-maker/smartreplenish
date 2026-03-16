"""Middleware для ограничения частоты запросов."""
from fastapi import Request
from fastapi.responses import JSONResponse
from collections import defaultdict
import time
import logging

logger = logging.getLogger(__name__)


class RateLimitMiddleware:
    """Ограничивает количество запросов от одного клиента."""
    
    def __init__(self, app, requests: int = 100, period: int = 60):
        self.app = app
        self.requests = requests
        self.period = period
        self.clients: dict = defaultdict(list)
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        
        request = Request(scope)
        client_ip = request.client.host
        current_time = time.time()
        
        # Очищаем старые записи
        self.clients[client_ip] = [
            t for t in self.clients[client_ip]
            if current_time - t < self.period
        ]
        
        # Проверяем лимит
        if len(self.clients[client_ip]) >= self.requests:
            logger.warning(f"Rate limit exceeded for {client_ip}")
            response = JSONResponse(
                status_code=429,
                content={"detail": "Too many requests"}
            )
            return await response(scope, receive, send)
        
        # Добавляем запись
        self.clients[client_ip].append(current_time)
        
        return await self.app(scope, receive, send)
