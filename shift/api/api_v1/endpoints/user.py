from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from shift.core.user import auth_backend, get_user_manager, current_superuser
from shift.models.user import User
from shift.schemas.user import UserCreate, UserRead, UserUpdate
from shift.crud.info.info import user_info_crud
from shift.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from shift.api.api_v1.validation import check_user

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

user_router = APIRouter()
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)


@user_router.patch('/users/{id}', response_model=UserRead, dependencies=[Depends(current_superuser)])
async def update_user(data: UserUpdate, id: int, session: AsyncSession = Depends(get_async_session), model=User):
    """Обновление пользователя. Только для администратора."""

    await check_user(model, session, id)
    user = await user_info_crud.get_object(session, id)
    user = await user_info_crud.update(session, user, data.model_dump())
    return user

