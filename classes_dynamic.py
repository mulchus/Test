
def some_function(self):
    return f'This is from {some_function.__name__} and print {self.hello()}'


class SomeClass1:
    def __init__(self, a):
        self.a = a

    def good_bye1(self):
        return f'Good bye 1, a = {self.a}'


class SomeClass2:
    def __init__(self, b):
        self.b = b

    def good_bye2(self):
        return f'Good bye 2, b = {self.b}'


def dynamic_init(self, a, b):
    SomeClass1.__init__(self, a)  # Инициализация первого родительского класса
    SomeClass2.__init__(self, b)  # Инициализация второго родительского класса


dynamic_class_name = 'SomeDynamicClass'
parent_classes = (SomeClass1, SomeClass2, object)

# Создаём класс динамически
BaseDynamicClass = type(
    dynamic_class_name,                             # имя класса
    parent_classes,               # родительские классы
    {'x': 42, 'y': 100,                             # атрибуты
     'hello': lambda self: f'Hello, x = {self.x}',  # методы (в виде функций)
     '__init__': dynamic_init,                      # добавляем наш инициализатор
     'some_function': some_function,                # методы (в виде функций)
     },
    # some_kwarg='some_kwarg',                        # TODO: дополнительные атрибуты?
)

obj = BaseDynamicClass(100, 200)

print(obj.good_bye1())  # Good bye 1, a = 100
print(obj.good_bye2())  # Good bye 2, a = 100

print(obj.x)
print(obj.y)
print(obj.some_function())  # This is from some_function and print Hello, x = 42
print(obj.hello())          # Hello, x = 42

print(type(obj))
print(BaseDynamicClass.__mro__)

print(obj.__dict__)
print(BaseDynamicClass.__dict__)
