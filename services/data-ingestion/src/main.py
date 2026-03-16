"""Главный сервис загрузки данных."""
import logging
import time
import yaml
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def load_config(config_path: str = "config/sources.yaml") -> dict:
    """Загрузить конфигурацию."""
    config_file = Path(config_path)
    if not config_file.exists():
        logger.warning(f"Config file {config_path} not found, using defaults")
        return {}
    
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def main():
    """Основной цикл загрузки данных."""
    logger.info("Data Ingestion Service started")
    
    config = load_config()
    
    while True:
        try:
            # В production здесь будет основной цикл загрузки данных
            # из источников в Kafka и ClickHouse
            logger.info("Processing data sources...")
            time.sleep(60)  # Пауза между итерациями
        except KeyboardInterrupt:
            logger.info("Stopping Data Ingestion Service")
            break
        except Exception as e:
            logger.error(f"Error in data ingestion: {e}")
            time.sleep(10)


if __name__ == "__main__":
    main()
