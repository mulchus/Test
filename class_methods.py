class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"вызван метод инстанса {self.name} класса"

    @staticmethod
    def static_method():
        return f"вызван статический метод класса"

    @classmethod
    def class_method(cls):
        return f"вызван метод класса {cls}"


print(MyClass.class_method(), str(MyClass.class_method))
print(MyClass.static_method(), str(MyClass.static_method))
print(MyClass('A').instance_method(), str(MyClass('A').instance_method))
print(MyClass('B').instance_method(), str(MyClass('B').instance_method))

print()


# динамическое добавление метода в класс
def new_instance_method(self):
    return f"вызван новый метод инстанса {self.name} класса"

MyClass.new_instance_method = new_instance_method
print(MyClass('C').new_instance_method(), str(MyClass('C').new_instance_method))


def new_class_method(cls):
    return f"вызван новый метод класса {cls}"

MyClass.new_class_method = classmethod(new_class_method)
print(MyClass.new_class_method(), str(MyClass.new_class_method))


def new_static_method():
    return "вызван новый статический метод класса"

MyClass.new_static_method = staticmethod(new_static_method)
print(MyClass.new_static_method(), str(MyClass.new_static_method))
