from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class BaseCRUD:

    def __init__(self, model):
        self.model = model

    async def create(self, session: AsyncSession, data: dict):
        """Создание объекта."""

        in_data = self.model(**data.model_dump())
        session.add(in_data)
        await session.commit()
        await session.refresh(in_data)
        return in_data

    async def get_object(
        self, session: AsyncSession, id: int, related: Optional[str] = None
    ):
        """Получение объекта."""

        if related:
            result = await session.execute(
                select(self.model)
                .options(selectinload(getattr(self.model, related)))
                .where(self.model.id == id)
            )
        else:
            result = await session.execute(
                select(self.model).where(self.model.id == id)
            )
        result = result.scalars().first()
        return result

    async def update(self, session: AsyncSession, obj, data: dict):
        """Изменение объекта."""

        updated_data = data
        for key, value in updated_data.items():
            setattr(obj, key, value)
        await session.commit()
        await session.refresh(obj)
        return obj
