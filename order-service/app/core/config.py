import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SERVICE_NAME = os.getenv("SERVICE_NAME", "order-service")
    PORT = int(os.getenv("PORT", 8002))
    USER_SERVICE_URL = os.getenv(
        "USER_SERVICE_URL",
        "http://localhost:8001"
    )

settings = Settings()
