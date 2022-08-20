from marshmallow import ValidationError


def crutch_type(item: dict):
    '''
        Проверка вида (тип=int, value='1') и (тип=str, value=1) -> ошибка типа
        + храним строку в value даже если пришло число (но тип параметра храним как int).
    '''
    if (isinstance(item['value'], int) and item['type'] == 'str') or (
            isinstance(item['value'], str) and item['type'] == 'int'):
        raise ValidationError('value is integer')
    item['value'] = str(item['value'])
