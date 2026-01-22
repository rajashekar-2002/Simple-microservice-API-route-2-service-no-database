from fastapi import APIRouter, HTTPException
from app.services.user_client import get_user

router = APIRouter()

@router.post("/{user_id}")
async def create_order(user_id: int):
    try:
        user = await get_user(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="User service unavailable")

    return {
        "message": "Order created",
        "user": user,
        "order_id": 123
    }
