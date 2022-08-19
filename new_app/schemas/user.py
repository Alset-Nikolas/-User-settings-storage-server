# import typing
from marshmallow import Schema, fields, ValidationError, post_load, validates_schema, validates
from models.user import get_user


class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={'required': 'enter name user'})

    @validates('name')
    def validate_title(self, name: str) -> None:
        '''Проверим есть ли такой user'''
        if get_user(name) is None:
            raise ValidationError(
                f'user "{name}" not exists'
            )
