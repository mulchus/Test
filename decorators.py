# https://tproger.ru/translations/demystifying-decorators-in-python
# https://habr.com/ru/companies/otus/articles/727590/
import time


def async_time_it(func):
    async def wrapper(*args, **kwargs):
        print(f"Start benchmarking {func.__name__}.")
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)} seconds to execute.")
        return result
    return wrapper


def time_it(func):
    def wrapper(*args, **kwargs):
        print(f"Start benchmarking {func.__name__}.")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)} seconds to execute.")
        return result
    return wrapper


def main():

    import functools


    def benchmark(chars):
        def actual_decorator(func):
            import time
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                print('[*] Время выполнения: {} секунд.'.format(end - start))
                return return_value
            return wrapper
        return actual_decorator


    def trace(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'TRACE: calling {func.__name__}() '
                  f'with {args}, {kwargs}')

            original_result = func(*args, **kwargs)

            print(f'TRACE: {func.__name__}() '
                  f'returned {original_result!r}')

            return original_result
        return wrapper


    @trace
    @benchmark(500)
    def fetch_webpage(url):
        """Return a friendly greeting."""
        import requests
        webpage = requests.get(url)
        webpage.raise_for_status()
        return webpage

    # fetch_webpage = benchmark(fetch_webpage)
    # fetch_webpage()

    webpage = fetch_webpage('https://google.com')
    # print(webpage)

    print(fetch_webpage.__name__)
    print(fetch_webpage.__doc__)




    @time_it
    def some_func():
        time.sleep(1)

    some_func()


    def logger(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Called {func.__name__} with args={args} and kwargs={kwargs}. Result: {result}")
            return result
        return wrapper

    @logger
    def add(x, y):
        return x + y

    add(1, 2)
    # Output: Called add with args=(1, 2) and kwargs={}. Result: 3


    # Асинъронный декоратор
    from typing import Coroutine
    import asyncio

    def deco(coroutine: Coroutine):
        async def wrapper(*args, **kwargs):
            print('start')
            result = await coroutine(*args, **kwargs)
            print('end')
            return result
        return wrapper


    @deco
    async def func():
        await asyncio.sleep(1)
        return ('some result of func', )


    rez = asyncio.run(func())
    print(rez)
    print(len(rez))
    print(type(rez))


    from functools import lru_cache


    @time_it  # измеряем время выполнения функции
    @lru_cache(maxsize=128)  # кэшируем резульат выполнения функции
    def get_42():
        time.sleep(1)
        return 42

    print(get_42())
    print(get_42())
    print(get_42())
    # get_42 took 1.0003461837768555 seconds to execute.
    # get_42 took 0.0 seconds to execute.
    # get_42 took 0.0 seconds to execute.


if __name__ == '__main__':
    main()
