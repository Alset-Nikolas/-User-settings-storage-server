from models import ParametrModel, session, UserModel
import typing
from dataclass.param import Param
from models.user import get_user


def get_param(type, name):
    return session.query(ParametrModel).filter(ParametrModel.type == type).filter(ParametrModel.name == name).first()


def create_param(param_update: Param, user_name: str):
    user = get_user(user_name)
    new_param = ParametrModel(name=param_update.name, type=param_update.type, value=param_update.value, user_id=user.id)
    session.add(new_param)
    session.commit()
    return new_param


def update_value_param(param_obj, new_value):
    param_obj.value = new_value
    session.add(param_obj)
    session.commit()


def update_param(user_name: str, param_update: Param) -> None:
    '''Обновляем параметр или создаем если такого нет'''
    param = get_param(type=param_update.type, name=param_update.name)
    if param is None:
        create_param(param_update, user_name)

        return
    update_value_param(param, param_update.value)
