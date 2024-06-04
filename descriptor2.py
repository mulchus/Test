# https://habr.com/ru/companies/otus/articles/801595/
# Реализация паттернов Singleton и Factory

class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __get__(self, instance, owner):
        if self.instance is None:
            self.instance = self.cls()
        return self.instance


class Database:
    def __init__(self):
        print("Создание базы данных")


# применение дескриптора Singleton
class AppConfig:
    db = Singleton(Database)


# тестирование паттерна Singleton
config1 = AppConfig()
config2 = AppConfig()
db1 = config1.db  # создание БД
db2 = config2.db  # не создает новый экземпляр, использует существующий

print(db1 is db2)  # выведет True, подтверждая, что db1 и db2 - один и тот же объект


# применение дескриптора Factory
class VehicleFactory:
    def __init__(self, cls):
        self.cls = cls

    def __get__(self, instance, owner):
        return self.cls()


class Car:
    def drive(self):
        print("Вождение автомобиля")


class Bike:
    def ride(self):
        print("Езда на велосипеде")


# фабрика, создающая автомобили
class AppConfigCar:
    vehicle = VehicleFactory(Car)


# фабрика, создающая велосипеды
class AppConfigBike:
    vehicle = VehicleFactory(Bike)


# создание и использование автомобиля
car_config = AppConfigCar()
car = car_config.vehicle  # создает объект Car
car.drive()

# создание и использование велосипеда
bike_config = AppConfigBike()
bike = bike_config.vehicle  # создает объект Bike
bike.ride()


# property, classmethod и staticmethod
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Получение значения")
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15 градусов Цельсия")
        print("Установка значения")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


c = Celsius(37)
print(c.temperature)
# c.temperature = -300  # вызовет исключение


class A:
    @classmethod
    def method(cls):
        return f"вызван classmethod класса {cls}"


print(A.method())  # вызван classmethod класса <class '__main__.A'>
a = A()
print(a.method())  # вызван classmethod объекта
print(A.__dict__)
print(a.__dict__)


class Math:
    @staticmethod
    def add(x, y):
        return x + y


print(Math.add(5, 7))  # 12
rez = Math()
print(rez.add(15, 17))
