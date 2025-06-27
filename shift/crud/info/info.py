from shift.models.user import User
from shift.crud.base import BaseCRUD


class InfoCRUD(BaseCRUD):
    pass


user_info_crud = InfoCRUD(User)
