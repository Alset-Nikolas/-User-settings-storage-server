from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
import schemas.user as schemas_user
import schemas.param as schemas_param
import models.param as models_param
from models.user import get_user
from routs.global_func import crutch_type


class GetUserParams(Resource):

    def get(self, user_name: str):
        '''
        	Получить все параметры юзера
        '''
        schema_dump = schemas_param.ParamSchema()
        schema_user = schemas_user.UserSchema()

        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400
        user = get_user(user_name)
        return schema_dump.dump(user.params, many=True), 200

    @staticmethod
    def add_item(user_name: str, param_item: dict, schema_param: schemas_param.ParamSchema) -> dict:
        '''
            Добавить параметр param_item пользователю user_name по схеме schema_param
        '''
        try:
            crutch_type(param_item)
            param_obj = schema_param.load(param_item)
            param_after_dump = schema_param.dump(param_obj)
            param_item['status'] = 'Ok'
            param_item['value'] = param_after_dump['value']
            models_param.update_param(user_name, param_obj)
        except ValidationError as exc:
            param_item['status'] = 'ERROR'
        param_item['operation'] = 'SetParam'
        return param_item

    def post(self, user_name: str):
        '''
        	Установка параметров через JSON-API (имя юзера)
        '''
        schema_user = schemas_user.UserSchema()
        schema_param = schemas_param.ParamSchema()
        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400

        data = request.json
        params = []
        if 'Query' not in data:
            return 'format {Query: ...}', 400

        for item in data['Query']:
            if item['operation'] == 'SetParam':
                item.pop('operation')
                item_mod = self.add_item(user_name, item, schema_param)
                params.append(item_mod)
        return {'Results': params}
