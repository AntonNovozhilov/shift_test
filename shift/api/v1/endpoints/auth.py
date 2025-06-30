from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession

from shift.api.v1.validation import check_user
from shift.core.db import get_async_session
from shift.core.user import auth_backend, current_superuser, get_user_manager
from shift.crud.info.info import user_info_crud
from shift.models.user import User
from shift.schemas.user import UserCreate, UserRead, UserUpdate

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

auth_route = APIRouter()
auth_route.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
auth_route.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
