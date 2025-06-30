from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from shift.api.v1.validation import check_selary
from shift.core.db import get_async_session
from shift.core.user import current_user
from shift.crud.info.info import user_info_crud
from shift.models.user import User
from shift.schemas.grade import Grade_Selary
from shift.schemas.user import User_Advanced

info = APIRouter(tags=["info"], dependencies=[Depends(current_user)])


@info.get("/selary/", response_model=Grade_Selary)
async def get_selary(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Получение зарплаты текущего пользователя."""

    if user is None:
        raise HTTPException(
            status_code=401, detail="Только для авторизованного пользователя"
        )
    user_obj = await user_info_crud.get_object(
        session, user.id, related="grade"
    )
    await check_selary(user_obj)
    return user_obj.grade


@info.get("/next_advance/", response_model=User_Advanced)
async def getnext_advanced_date(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Получение информации по дате следующего повышения."""

    user_obj = await user_info_crud.get_object(session, user.id)
    return user_obj
