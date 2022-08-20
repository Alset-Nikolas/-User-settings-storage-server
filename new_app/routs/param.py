from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
import schemas.user as schemas_user
import schemas.param as schemas_param
import models.param as models_param
from routs.global_func import crutch_type

class ParamUrl(Resource):

    def post(self, user_name, param_name, type):
        '''
            Установить параметр (1)
        '''
        if not request.is_json:
            return 'Ожидали json формат. Пример:{value: 10}', 400

        user_schema = schemas_user.UserSchema()
        param_schema = schemas_param.ParamSchema()

        user_data = {'name': user_name}
        param_data = {'name': param_name, 'type': type}

        try:
            param_data['value'] = request.json['value']
            crutch_type(param_data)
            user_schema.load(user_data)
            param = param_schema.load(param_data)
        except ValidationError as exc:
            return exc.messages, 400

        models_param.update_param(user_name, param)
        return 'ok', 200

    def get(self, user_name, param_name, type):
        '''
            Получить параметр (имя юзера, имя параметра, тип) – если параметр не был задан, ошибка.
        '''
        schema_param = schemas_param.ParamSchema()
        schema_user = schemas_user.UserSchema()

        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400

        param = models_param.get_param(name=param_name, type=type)
        if param:
            return [schema_param.dump(param)], 200
        return [], 200
