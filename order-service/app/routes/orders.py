from fastapi import APIRouter, Request
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/{user_id}")
async def create_order(user_id: int, request: Request):
    request_id = request.headers.get("X-Request-ID", "N/A")

    logger.info(f"[req_id={request_id}] Order request received user_id={user_id}")

    return {
        "message": "Order created",
        "order_id": 123,
        "request_id": request_id
    }
