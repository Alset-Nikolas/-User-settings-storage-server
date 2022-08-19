from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
import schemas.user as schemas_user
import schemas.param as schemas_param
import models.param as models_param
from models.user import get_user
from dataclass.param import get_param_obj_from_row


class ParamUrl(Resource):

    def post(self, user_name, type_name, type):
        '''	Установить параметр (1)'''
        if not request.is_json:
            return 'Ожидали json формат {value: 10}', 400

        user_schema = schemas_user.UserSchema()
        param_schema = schemas_param.ParamSchema()

        user_data = {'name': user_name}
        param_data = {'name': type_name, 'type': type}

        try:
            value = request.json['value']
            if isinstance(value, int) and type == 'str':
                raise ValidationError('value is integer')
            param_data['value'] = str(value)
            user_schema.load(user_data)
            param = param_schema.load(param_data)
        except ValidationError as exc:
            return exc.messages, 400

        models_param.update_param(user_name, param)
        return 'ok', 200

    def get(self, user_name, type_name, type):
        schema_param = schemas_param.ParamSchema()
        schema_user = schemas_user.UserSchema()

        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400

        param = models_param.get_param(name=type_name, type=type)
        if param:
            param_obj = get_param_obj_from_row([param.name, param.type, param.value])
            return [schema_param.dump(param_obj)], 200
        return [], 200
