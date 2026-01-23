from fastapi import APIRouter, Request
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int, request: Request):
    request_id = request.headers.get("X-Request-ID", "N/A")

    logger.info(f"[req_id={request_id}] User requested user_id={user_id}")

    return {
        "id": user_id,
        "name": "Raja",
        "email": "raja@example.com"
    }
