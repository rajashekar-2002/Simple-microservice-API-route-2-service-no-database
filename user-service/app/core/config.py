import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SERVICE_NAME = os.getenv("SERVICE_NAME", "user-service")
    PORT = int(os.getenv("PORT", 8001))

settings = Settings()
