FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.7.1
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY src/ ./src/
COPY config/ ./config/

CMD ["python", "src/main.py"]
