from datetime import datetime
from shift.core.utils import time_year

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from shift.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя."""

    reception_at = Column(DateTime, default=datetime.now, nullable=False)
    advancement_date = Column(DateTime, nullable=True, default=time_year)
    grade_id = Column(Integer, ForeignKey("grade.id"), nullable=True)
    grade = relationship("Grade", back_populates="users")
