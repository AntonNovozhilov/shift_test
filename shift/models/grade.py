from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from shift.core.db import Base


class Grade(Base):
    """Модель грейда."""
    
    title = Column(String(50), nullable=False, unique=True)
    selary = Column(Integer, nullable=False)
    users = relationship("User", back_populates="grade")
