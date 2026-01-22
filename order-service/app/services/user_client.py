import httpx

USER_SERVICE_URL = "http://localhost:8001"

async def get_user(user_id: int):
    async with httpx.AsyncClient(timeout=2.0) as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        response.raise_for_status()
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