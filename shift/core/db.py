from sqlalchemy import BigInteger, Column, Integer
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr

from .config import setting


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    f"postgresql+asyncpg://{setting.postgres_user}:{setting.postgres_password}@{setting.db_host}:{setting.db_port}/{setting.postgres_db}"
)

AsyncSessionLocal = async_sessionmaker(engine)


async def get_async_session():

    async with AsyncSessionLocal() as async_session:
        yield async_session
