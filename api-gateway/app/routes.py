from fastapi import APIRouter, HTTPException
import httpx
import logging
from urllib.parse import urljoin
from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

# Forward GET /users/{user_id} to user-service
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    logger.info(f"Gateway: forwarding request to user-service user_id={user_id}")
    try:
        url = urljoin(str(settings.USER_SERVICE_URL), f"/users/{user_id}")
        # getting double slash when given as generic string 
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as exc:
        logger.error(f"User service unreachable: {exc}")
        raise HTTPException(status_code=503, detail="User service unavailable")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)


# Forward POST /orders/{user_id} to order-service
@router.post("/orders/{user_id}")
async def create_order(user_id: int):
    logger.info(f"Gateway: forwarding request to order-service user_id={user_id}")
    try:
        url = urljoin(str(settings.ORDER_SERVICE_URL), f"/orders/{user_id}")
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(url)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as exc:
        logger.error(f"Order service unreachable: {exc}")
        raise HTTPException(status_code=503, detail="Order service unavailable")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
