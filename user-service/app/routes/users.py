from fastapi import APIRouter, HTTPException
from app.models.user import User
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

USERS = {
    1: User(id=1, name="Raja", email="raja@example.com"),
    2: User(id=2, name="Kiran", email="kiran@example.com"),
}

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    logger.info(f"Fetching user user_id={user_id}")

    user = USERS.get(user_id)
    if not user:
        logger.error(f"User not found user_id={user_id}")
        raise HTTPException(status_code=404, detail="User not found")

    logger.info(f"User found user_id={user_id}")
    return user
