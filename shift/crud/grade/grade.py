from shift.crud.base import BaseCRUD
from shift.models.grade import Grade


class GradeCRUD(BaseCRUD):
    pass


grade_crud = GradeCRUD(Grade)
