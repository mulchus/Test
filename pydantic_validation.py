from typing import Annotated
from pydantic import BaseModel, ValidationError, AfterValidator, BeforeValidator


def is_less_than_100(value):
    print(4, type(value))
    if value > 300:
        raise ValueError(f'{value} is less than 300')
    return value

def adding(value):
    print(3, type(value))
    if value % 2 == 0:
        value += 7
    return value

def to_int(value):
    print(1, type(value))
    return int(value)


def multiply(value):
    print(2, type(value))
    return value * 3


MagicNumber = Annotated[int | str, AfterValidator(to_int), BeforeValidator(multiply)]


class MyModel(BaseModel):
    val: Annotated[MagicNumber, AfterValidator(adding), AfterValidator(is_less_than_100)]


if __name__ == '__main__':
    for i in range(6):
        try:
            print(MyModel(val=i.__str__()))
        except (ValueError, TypeError, ValidationError) as err:
            print(err)


