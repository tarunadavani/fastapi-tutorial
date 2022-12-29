"""
    ROUTER FILE
"""
from fastapi import APIRouter

from app.api.v1.endpoints import (
    authentication,
    blog,
    user
)

api_router = APIRouter()

api_router.include_router(authentication.router, tags=["Authentication"])
api_router.include_router(blog.router, prefix="/blog",tags=["Blog"])
api_router.include_router(user.router, prefix="/user",tags=["User"])
