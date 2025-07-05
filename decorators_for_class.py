def my_decorator(cls):
    class Wrapped(cls):
        def new_method(self):
            return "This is a new method!"
    return Wrapped


# Вариант декорирования класса по месту
# @my_decorator
class MyClass:
    def original_method(self):
        return "This is the original method!"


# Декорируем класс
decorated_class = my_decorator(MyClass)


# Использование класса
obj = MyClass()
print(obj.original_method())  # "This is the original method!"
try:
    print(obj.new_method())  # AttributeError: 'MyClass' object has no attribute 'new_method'
except AttributeError as e:
    print(e)

obj = decorated_class()
print(obj.new_method())       # "This is a new method!"
