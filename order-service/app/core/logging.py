import logging
from app.core.config import settings

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            f"{settings.SERVICE_NAME} | "
            "%(message)s"
        ),
    )
