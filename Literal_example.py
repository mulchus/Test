from typing import Literal


def example(x: Literal[1, 2, 3]):
    return x


print(example(2))
print(example(4))

try:
    print(example(4))   # TypeError
except TypeError:
    print('error')


def example2(x: Literal['left', 'center', 'right']):
    return x


print(example2('left'))
print(example2('another'))

try:
    print(example2('another'))   # TypeError ???
except TypeError:
    print('error')
