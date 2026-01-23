from fastapi import APIRouter, HTTPException, Request
import httpx
import logging
from urllib.parse import urljoin
from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int, request: Request):
    request_id = request.state.request_id
    logger.info(f"[req_id={request_id}] Forwarding to user-service")

    headers = {"X-Request-ID": request_id}
    url = urljoin(str(settings.USER_SERVICE_URL), f"/users/{user_id}")

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


@router.post("/orders/{user_id}")
async def create_order(user_id: int, request: Request):
    request_id = request.state.request_id
    logger.info(f"[req_id={request_id}] Forwarding to order-service")

    headers = {"X-Request-ID": request_id}
    url = urljoin(str(settings.ORDER_SERVICE_URL), f"/orders/{user_id}")

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.post(url, headers=headers)
        response.raise_for_status()
        return response.json()







# response = await client.get(f"{settings.USER_SERVICE_URL}/users/{user_id}")

# getting double slash after using this
# http://127.0.0.1:8001/ + /users/1 → http://127.0.0.1:8001//users/1


# 🔹 Fix 1: Remove trailing slashes in .env

# Change .env for gateway:

# USER_SERVICE_URL=http://127.0.0.1:8001
# ORDER_SERVICE_URL=http://127.0.0.1:8002


# No trailing slash at the end!

# 🔹 Fix 2 (Optional but safer): Use urljoin in Python
# from urllib.parse import urljoin

# url = urljoin(settings.USER_SERVICE_URL, f"/users/{user_id}")
# response = await client.get(url)