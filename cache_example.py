import time
from functools import cache


@cache
def calc(x):
    print(f'{x} +1 is ...')
    time.sleep(2)
    return x + 1


while True:
    _input = int(input('>> '))
    print(calc(_input))
