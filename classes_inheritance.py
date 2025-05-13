print('Примеры c классами. Наследование. Поиск методов в дедушких классах.')
print('Пример 1. У родительских классов нет метода. Методы определены в дедушкиных классахю Наследование идет вертикально, <object> последним.')

class Class0:
    def m(self):
        print("In Class0")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class0):
    pass

class Class3(Class1):
    pass

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()
print(Class4.__mro__)


print('Пример 2. У второго родительского класса есть метод. Методы определены и в дедушкиных классах. Наследование идет вертикально, <object> последним.')

class Class0:
    def m(self):
        print("In Class0")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class0):
    pass

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()
print(Class4.__mro__)


print('Пример 3. У второго родительского класса есть метод. Дедушкин класс общий для обоих родителей. Метод определен и в дедушкином классе. Наследование идет горизонтально, <Class1> и <object> последними.')

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    pass

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()
print(Class4.__mro__)


print('Пример 4. Инициализация родительского метода Class2 в классе Class3. И вызов метода m по MRO и напрямую из указанного класса.')

class Class0:
    def m(self):
        print("In Class0")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def __init__(self, var1, var2):
        print(f"Init Class2.  {var1}, {var2}")

class Class3(Class2, Class1, Class0):
    # pass
    def __init__(self):
        print("Init Class3")
        super().__init__('-var1-',  '-var2-')

    def m(self):
        print("In Class3")
        super().m()  # Вызов следующего метода в MRO
        Class0.m(self)  # Явный вызов метода из Class0

print(Class3.mro())
a = Class3()
a.m()
