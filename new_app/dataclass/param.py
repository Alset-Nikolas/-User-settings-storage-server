import typing
from dataclasses import dataclass


@dataclass
class Param:
    name: str
    type: str
    value: str

    def __str__(self):
        return f'name={self.name}, type={self.type}, value={self.value}'


def get_param_obj_from_row(row: typing.Tuple) -> Param:
    return Param(name=row[0], type=row[1], value=row[2])
