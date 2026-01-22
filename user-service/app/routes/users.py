from fastapi import APIRouter, HTTPException
from app.models.user import User

router = APIRouter()

# Fake in-memory data
USERS = {
    1: User(id=1, name="Raja", email="raja@example.com"),
    2: User(id=2, name="Kiran", email="kiran@example.com"),
}

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
