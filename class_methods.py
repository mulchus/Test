class MyClass:
    def __init__(self, name):
        self.name = name

    def method3(self):
        return f"вызван метод инстанса {self.name} класса"

    @staticmethod
    def method2():
        return f"вызван статический метод класса"

    @classmethod
    def method1(cls):
        return f"вызван метод класса {cls}"


print(MyClass.method1(), str(MyClass.method1))
print(MyClass.method2(), str(MyClass.method2))
print(MyClass('A').method3(), str(MyClass('A').method3))
print(MyClass('B').method3(), str(MyClass('B').method3))
