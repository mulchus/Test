# декоратор без вызова и параметров
def foobar(func):
    def wrapper():
        print("Декоратор вызван!")
        return func()
    return wrapper

@foobar  # Просто передаём функцию в декоратор
def hello():
    print("Hello, world!")

hello()


# декоратор с вызовом (и параметрами)
def foobar(arg):
    def decorator(func):
        def wrapper():
            print(f"Декоратор вызван с аргументом: {arg}")
            return func()
        return wrapper
    return decorator

@foobar("Привет")  # Вызываем foobar("Привет"), который вернёт реальный декоратор
def hello():
    print("Hello, world!")

hello()


# декоратор с вызовом (и параметрами)
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
