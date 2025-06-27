from typing import Union

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.fastapi_users import FastAPIUsers
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from shift.core.config import setting
from shift.core.db import get_async_session
from shift.models.user import User
from shift.schemas.user import UserCreate


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=setting.secret, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Пароль не может быть короче 8 символов"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Пароль не может содержать email пользователя"
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_user = FastAPIUsers(
    get_user_manager=get_user_manager, auth_backends=[auth_backend]
)

current_user = fastapi_user.current_user(active=True)
current_superuser = fastapi_user.current_user(active=True, superuser=True)
