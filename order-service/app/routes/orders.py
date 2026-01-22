from fastapi import APIRouter, HTTPException
from app.services.user_client import get_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


# can also make it get request
@router.post("/{user_id}")
async def create_order(user_id: int):
    logger.info(f"Order request received user_id={user_id}")

    try:
        user = await get_user(user_id)
    except Exception:
        logger.error(f"Failed to fetch user user_id={user_id}")
        raise HTTPException(status_code=400, detail="User service unavailable")

    logger.info(f"Order created for user_id={user_id}")
    return {
        "message": "Order created",
        "user": user,
        "order_id": 123
    }
