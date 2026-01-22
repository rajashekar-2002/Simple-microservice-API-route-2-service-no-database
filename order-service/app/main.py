from fastapi import FastAPI
from app.routes.orders import router as order_router

app = FastAPI(
    title="Order Service",
    version="1.0.0"
)

app.include_router(order_router, prefix="/orders")
# This is an APIRouter object that contains order-related endpoints

# Example
# If orders.py has:

# @router.get("/")
# async def list_orders():
#     return []

# Final endpoint becomes:
# GET /orders/