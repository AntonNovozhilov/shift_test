from datetime import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    reception_at: datetime
    advancement_date: datetime
    grade_id: Optional[int] = None


class User_Advanced(schemas.BaseModel):
    advancement_date: datetime

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    grade_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "password": "example_password",
                "grade_id": 1,
            }
        }


class UserUpdate(schemas.BaseModel):
    grade_id: int
