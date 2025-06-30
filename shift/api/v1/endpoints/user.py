from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shift.api.v1.validation import check_user
from shift.core.db import get_async_session
from shift.core.user import current_superuser
from shift.crud.info.info import user_info_crud
from shift.models.user import User
from shift.schemas.user import UserRead, UserUpdate

user_route = APIRouter(prefix="/users", tags=["user"])


@user_route.patch(
    "/{id}", response_model=UserRead, dependencies=[Depends(current_superuser)]
)
async def update_user(
    data: UserUpdate,
    id: int,
    session: AsyncSession = Depends(get_async_session),
    model=User,
):
    """Обновление пользователя. Только для администратора."""

    await check_user(model, session, id)
    user = await user_info_crud.get_object(session, id)
    user = await user_info_crud.update(session, user, data.model_dump())
    return user
