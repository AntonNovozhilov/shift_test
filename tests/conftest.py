import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from shift.core.db import get_async_session
from shift.core.user import current_superuser, current_user, fastapi_user
from shift.main import app

load_dotenv(".env")

from shift.core.base import (
    Base,
    Grade,
    User,
)


class Base_Test(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)


engine = create_async_engine("sqlite+aiosqlite:///test_db.db", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session_test():
    async with async_session() as session:
        yield session


app.dependency_overrides[get_async_session] = get_async_session_test


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base_Test.metadata.create_all)
    session = async_session()
    yield session
    await session.close()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def not_auth_test_client():
    app.dependency_overrides[current_user] = lambda: None
    with TestClient(app) as client:
        yield client


def override_current_user():
    user = User(
        id=1,
        email="asdsuperuser@example.com",
        is_active=True,
        is_verified=True,
        is_superuser=False,
    )
    return user


@pytest.fixture
def test_client():
    def raise_forbidden():
        raise HTTPException(status_code=403, detail="Forbidden")

    app.dependency_overrides[current_user] = override_current_user
    app.dependency_overrides[current_superuser] = lambda: raise_forbidden()
    with TestClient(app) as client:
        yield client


def override_current_superuser():
    user = User(
        id=2,
        email="superuser@example.com",
        is_active=True,
        is_verified=True,
        is_superuser=True,
    )
    return user


@pytest.fixture
def super_user_client():
    app.dependency_overrides[current_superuser] = override_current_superuser
    with TestClient(app) as client:
        yield client


@pytest_asyncio.fixture
async def user_one():
    async for session in get_async_session_test():
        user_o = User(
            email="qweqwedasda@qweqwe.ru",
            hashed_password="chimichangas4life",
            is_active=True,
            is_verified=True,
        )
        session.add(user_o)
        await session.commit()
        await session.refresh(user_o)
        return user_o


@pytest_asyncio.fixture
async def user_two():
    async for session in get_async_session_test():
        user_w = User(
            email="qqweqwedasda@qweqwe.ru",
            hashed_password="chimiqchangas4life",
            is_active=True,
            is_verified=True,
            grade_id=None,
        )
        session.add(user_w)
        await session.commit()
        await session.refresh(user_w)
        return user_w


@pytest_asyncio.fixture
async def user_with_grade():
    """Создаем пользователя с заполненным grade_id."""
    async for session in get_async_session_test():
        grader = Grade(title="Junior", selary=50000)
        session.add(grader)
        await session.commit()
        user = User(
            email="test_user",
            hashed_password="ch11imichangas4life",
            grade_id=grader.id,
        )
        session.add(user)
        await session.commit()
        return user
