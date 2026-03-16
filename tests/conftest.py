"""Conftest для тестов."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Создать тестовый клиент."""
    from services.api_gateway.src.main import app
    return TestClient(app)
