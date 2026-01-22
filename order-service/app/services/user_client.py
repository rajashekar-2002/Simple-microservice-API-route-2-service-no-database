import httpx
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

async def get_user(user_id: int):
    logger.info(f"Calling user-service user_id={user_id}")

    async with httpx.AsyncClient(timeout=2.0) as client:
        response = await client.get(
            f"{settings.USER_SERVICE_URL}/users/{user_id}"
        )

        response.raise_for_status()
        logger.info(f"Received response from user-service user_id={user_id}")
        return response.json()


# 4️⃣ response.raise_for_status()

# Checks the HTTP status code
# If status is:
# 200–299 → OK, continue
# 400–599 → raises an exception (httpx.HTTPStatusError)
# Example:
# 404 → User not found
# 500 → User service crashed
# 👉 This prevents silently returning bad responses