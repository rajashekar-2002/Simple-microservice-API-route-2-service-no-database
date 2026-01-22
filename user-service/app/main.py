from fastapi import FastAPI
from app.routes.users import router as user_router
from app.core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="User Service")

@app.on_event("startup")
async def startup_event():
    logger.info("User service started")

app.include_router(user_router, prefix="/users")
