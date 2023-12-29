def greeting(name: str = '123') -> str:
    # return "Hello, " + str(name) if name else "Hello, World!"
    return "Hello, " + name


print(greeting.__annotations__)
print(greeting())
print(greeting(5))

my_var: int
my_var = 5  # Passes type check.
other_var: int = 'a'  # Flagged as error by type checker,
# but OK at runtime.


class Example:
    pass
# довольно бессмысленно, но для примера пойдет
example_instance: Example = Example()

# from typing import List, Tuple, Dict, Set

# тип всех элементов списка
primes: list[int]

# тип каждого элемента кортежа
person_info: tuple[str, int, float, float]

# тип ключей, тип значений
stock_prices: dict[str, float]

# тип всех элементов множества
valid_answers: set[str]

months: tuple[str, ...]

from typing import Optional, Union
def add_or_concatenate(a: Union[str, int], b: Union[str, int]):
    return a + b
phone: Optional[str]
phone2: Union[str, None]

print("qwerty" + 1)