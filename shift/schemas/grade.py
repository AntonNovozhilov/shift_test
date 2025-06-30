from pydantic import BaseModel, Field, field_validator


class Grade(BaseModel):
    title: str = Field("Название должности", max_length=50, min_length=1)
    selary: int = Field()

    @field_validator("selary")
    def validate_selary(cls, value: int) -> int:
        if value <= 0:
            raise ValueError(
                "Зарплата не может быть отрицательной или равной нулю."
            )
        return value


class GradeCreate(Grade):

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Менеджер",
                "selary": 50000,
            }
        }


class Grade_Selary(BaseModel):
    selary: int

    class Config:
        from_attributes = True
