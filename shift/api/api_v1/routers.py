from fastapi import APIRouter

from .endpoints.grade import grade
from .endpoints.info import info
from .endpoints.user import user_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(grade)
main_router.include_router(info)
