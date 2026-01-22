from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    SERVICE_NAME: str = "api-gateway"
    PORT: int = 8000
    USER_SERVICE_URL: AnyHttpUrl = "http://127.0.0.1:8001"
    ORDER_SERVICE_URL: AnyHttpUrl = "http://127.0.0.1:8002"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()





