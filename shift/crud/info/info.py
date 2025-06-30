from shift.crud.base import BaseCRUD
from shift.models.user import User


class InfoCRUD(BaseCRUD):
    pass


user_info_crud = InfoCRUD(User)
