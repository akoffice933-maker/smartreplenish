"""Middleware аутентификации на основе JWT."""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
import logging

logger = logging.getLogger(__name__)


class AuthMiddleware:
    """Проверяет JWT токен в заголовках запроса."""
    
    def __init__(self, app, secret_key: str):
        self.app = app
        self.secret_key = secret_key
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        
        request = Request(scope)
        path = request.url.path
        
        # Пропускаем health check и docs
        if path in ["/health", "/docs", "/openapi.json"]:
            return await self.app(scope, receive, send)
        
        # Получаем токен из заголовка
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                scheme, token = auth_header.split()
                if scheme.lower() == "bearer":
                    payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
                    request.state.user = payload
            except (JWTError, ValueError) as e:
                logger.warning(f"Invalid token: {e}")
                response = JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid or expired token"}
                )
                return await response(scope, receive, send)
        
        return await self.app(scope, receive, send)
