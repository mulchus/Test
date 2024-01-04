# https://tproger.ru/translations/demystifying-decorators-in-python
# https://habr.com/ru/companies/otus/articles/727590/


import functools


def benchmark(chars):
    def actual_decorator(func):
        import time
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs).text[:chars]
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
