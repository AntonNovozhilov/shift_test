from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shift.models.grade import Grade


async def check_unique_title(title: str, session: AsyncSession):
    result = await session.execute(select(Grade).where(Grade.title == title))
    if result.scalars().first():
        raise HTTPException(
            status_code=400, detail=f"Должность с названием '{title}' уже существует."
        )

async def check_user(model, session: AsyncSession, id: int):
    result = await session.execute(select(model).where(model.id == id))
    if not result.scalars().first():
        raise HTTPException(
            status_code=404, detail="Данного id нет в базе данных."
        )
    
async def check_selary(grade: int):
    if grade is None:
        raise HTTPException(
            status_code=400, detail="Ваш грейд не определен, обратитесь к руководителю."
        )