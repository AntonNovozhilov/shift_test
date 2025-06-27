from sqlalchemy import BigInteger, Column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr

from .config import setting


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(BigInteger, primary_key=True, autoincrement=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(setting.db_url)

AsyncSessionLocal = async_sessionmaker(engine)


async def get_async_session():

    async with AsyncSessionLocal() as async_session:
        yield async_session
