from fastapi import FastAPI
from app.routes.orders import router as order_router
from app.core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Order Service")

@app.on_event("startup")
async def startup_event():
    logger.info("Order service started")

app.include_router(order_router, prefix="/orders")



# This is an APIRouter object that contains order-related endpoints

# Example
# If orders.py has:

# @router.get("/")
# async def list_orders():
#     return []

# Final endpoint becomes:
# GET /orders/