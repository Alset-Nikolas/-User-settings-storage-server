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


class AddUserSchema(Schema):
    user_name = fields.Str(required=True, min_length=1, error_messages={'required': 'enter name user'})

    @validates('user_name')
    def validate_title(self, user_name: str) -> None:
        '''При добавлении не нужны дубликаты'''
        if get_user(user_name) is not None:
            raise ValidationError(
                f'user "{user_name}"  exists'
            )
