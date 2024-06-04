# https://habr.com/ru/companies/otus/articles/801595/
import time


class Descriptor:
    def __get__(self, instance, owner):
        print("Getting the attribute")
        return instance._value

    def __set__(self, instance, value):
        print(f"Setting the attribute to {value}")
        instance._value = value

    def __delete__(self, instance):
        print("Deleting the attribute")
        del instance._value

    def __set_name__(self, owner, name):
        print(f"Setting the name to {name}")


class MyClass:
    my_attribute = Descriptor()

    def my_property(self):
        return self._value

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f'STR: {self._value}.'

    def __repr__(self):
        return f'REPR: {self._value}.'


my_object = MyClass(10)
my_object.my_property = 200
print(my_object)
print(my_object.__repr__())
print(my_object.my_property)

print(my_object.my_attribute)

my_object.my_attribute = 20
print(my_object.my_attribute)

del my_object.my_attribute
# print(my_object.my_attribute)     # AttributeError: 'MyClass' object has no attribute '_value'


# дескриптор для валидации данных
class ValidateAge:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Возраст должен быть между 0 и 100 годами")
        setattr(instance, self.private_name, value)


class Person:
    age = ValidateAge()

    def __init__(self, name, age):
        self.name = name
        self.age = age


try:
    p = Person("Kolya", 30)  # валидный возраст
    print(p.age)
    p.age = -5  # невалидный возраст, будет вызвано исключение ValueError
except ValueError as e:
    print(e)


# дескриптор для кэширования
class CachedAttribute:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        if instance not in self.cache:
            self.cache[instance] = self.method(instance)
        return self.cache[instance]


class HeavyComputation:
    @CachedAttribute
    def compute(self):
        # имитация длительного вычисления
        time.sleep(2)
        return "Результат вычисления"


hc = HeavyComputation()
start_time = time.time()
print(hc.compute)  # первый вызов занимает время
print(f"Выполнено за {time.time() - start_time} секунд")

start_time = time.time()
print(hc.compute)  # второй вызов мгновенный, использует кэшированный результат
print(f"Выполнено за {time.time() - start_time} секунд")


# дескриптор для логирования
class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        print(f"Установка {self.private_name} в {value}")
        setattr(instance, self.private_name, value)


class User:
    name = LoggedAttribute()
    age = LoggedAttribute()

    def __init__(self, name, age):
        self.name = name
        self.age = age


u = User("Katya", 30)
u.name = "Katyuha"  # Логируется изменение
u.age = 31  # Логируется изменение
