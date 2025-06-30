from fastapi import APIRouter

from .endpoints.auth import auth_route
from .endpoints.grade import grade
from .endpoints.info import info
from .endpoints.user import user_route

main_router = APIRouter()


main_router.include_router(auth_route)
main_router.include_router(user_route)
main_router.include_router(grade)
main_router.include_router(info)
