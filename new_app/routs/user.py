from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
import schemas.user as schemas_user
import schemas.param as schemas_param
import models.param as models_param
from models.user import get_user
from dataclass.param import get_param_obj_from_row


class GetUserParams(Resource):

    def get(self, user_name):
        schema_dump = schemas_param.ParamSchema()
        schema_user = schemas_user.UserSchema()

        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400
        user = get_user(user_name)
        param_objs = [get_param_obj_from_row([param.name, param.type, param.value]) for param in user.params]
        return schema_dump.dump(param_objs, many=True), 200

    def post(self, user_name):
        schema_user = schemas_user.UserSchema()
        try:
            schema_user.load({'name': user_name})
        except ValidationError as exc:
            return exc.messages, 400

        data = request.json
        schema_param = schemas_param.ParamSchema()
        params = []
        if 'Query' not in data:
            return 'format {Query: ...}', 400

        for item in data['Query']:
            if item['operation'] == 'SetParam':
                item.pop('operation')
                param_info = item
                try:
                    value = item['value']
                    if (isinstance(value, int) and type == 'str') or (isinstance(value, str) and type == 'int'):
                        raise ValidationError('value is integer')
                    param_info['value'] = str(item['value'])
                    param_obj = schema_param.load(param_info)
                    param_after_dump = schema_param.dump(param_obj)
                    param_info['status'] = 'Ok'
                    param_info['value'] = param_after_dump['value']
                    models_param.update_param(user_name, param_obj)
                except ValidationError as exc:
                    param_info['status'] = 'ERROR'
                param_info['operation'] = 'SetParam'
                params.append(param_info)

        return {'Results': params}
