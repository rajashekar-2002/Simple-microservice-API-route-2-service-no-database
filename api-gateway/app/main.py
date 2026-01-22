from fastapi import FastAPI
from app.routes import router as gateway_router
from app.core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="API Gateway")

@app.on_event("startup")
async def startup_event():
    logger.info("API Gateway started")

app.include_router(gateway_router)



