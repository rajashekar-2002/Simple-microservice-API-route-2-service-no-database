from fastapi import FastAPI
from app.routes.users import router as user_router

app = FastAPI(
    title="User Service",
    version="1.0.0"
)

app.include_router(user_router, prefix="/users")
