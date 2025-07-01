from shift.core.db import get_async_session
from shift.core.base import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def create_superuser(session: AsyncSession = Depends(get_async_session)):
        superuser = User(
            email='super@user.ru',
            password='superadmin',
            is_active=True,
            is_superuser=True,
            is_verified=True,
        )
        session.add(superuser)
        await session.commit()
        return superuser
