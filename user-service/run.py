import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="http://localhost:8001",
        port=settings.PORT,
        reload=True
    )
