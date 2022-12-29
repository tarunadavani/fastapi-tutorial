# import uvicorn
from fastapi import FastAPI

from app.api.v1.routers import api_router
from app.core.configuration import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",)

app.include_router(api_router, prefix=settings.API_V1_STR)

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)
