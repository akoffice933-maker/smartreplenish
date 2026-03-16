#!/bin/bash
# Скрипт для запуска тестового токена JWT

python3 -c "
from jose import jwt
from datetime import datetime, timedelta

secret = 'your-secret-key-change-in-production'
payload = {
    'user_id': 'admin',
    'username': 'admin',
    'role': 'admin',
    'exp': datetime.utcnow() + timedelta(days=7)
}
token = jwt.encode(payload, secret, algorithm='HS256')
print(f'Token: {token}')
print(f'Use: curl -H \"Authorization: Bearer {token}\" http://localhost:8080/health')
"
