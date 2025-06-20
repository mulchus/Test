from collections import deque
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        result = func(*args, **kwargs)
        end = time.time()
        print(end)
        print(f"{func.__name__} took {end - start} seconds to execute.")
        return result
    return wrapper


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

some_deque = deque(some_list)

@time_it
def deque_append():
    for _ in range(100000):
        some_deque.append(11)

@time_it
def list_append():
    for _ in range(100000):
        some_list.append(11)


deque_append()
list_append()

# TODO: почему то странный вывод времени, то по 0, то поочередно 0. Где кэшируется?