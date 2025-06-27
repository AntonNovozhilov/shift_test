from shift.models.grade import Grade

from shift.crud.base import BaseCRUD


class GradeCRUD(BaseCRUD):
    pass


grade_crud = GradeCRUD(Grade)
