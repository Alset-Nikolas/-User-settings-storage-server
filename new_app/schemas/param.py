from marshmallow import Schema, fields, ValidationError, post_load, validates_schema, post_dump
import typing
from dataclass.param import Param


class ParamSchema(Schema):
    name = fields.Str(required=True, error_messages={'required': 'enter name parametr'})
    type = fields.Str(required=True, error_messages={'required': 'enter type parametr'})
    value = fields.Str(required=True, error_messages={'required': 'enter value parametr'})

    @validates_schema
    def validate_title(self, data: typing.Dict, **kwargs) -> None:
        if data['type'] not in ['int', 'str']:
            raise ValidationError(
                f'type in [int, str]'
            )
        if data['type'] == 'str' and not isinstance(data['value'], str):
            raise ValidationError(
                f'type = {data["type"]} -> value={data["value"]} is not str '
            )

        if data['type'] == 'int' and not data['value'].isdigit():
            raise ValidationError(
                f'type = {data["type"]} -> value={data["value"]} is not int '
            )

    @post_load
    def create_param(self, data: typing.Dict, **kwargs) -> Param:
        return Param(**data)

    @post_dump
    def add_type(self, data: typing.Dict, **kwargs) -> Param:
        if data['type'] == 'int':
            data['value'] = int(data['value'])
        return data
