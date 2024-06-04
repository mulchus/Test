class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['my_attribute'] = 42
        dct['my_new_attribute'] = 'abcdef'
        return super(MyMeta, cls).__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


print(MyClass.my_attribute)
print(MyClass.my_new_attribute)


class ValidationMeta(type):
    def __new__(cls, name, bases, dct):
        if "attribute" not in dct:
            raise ValueError("Класс должен содержать атрибут 'attribute'")
        return super().__new__(cls, name, bases, dct)


class ValidClass(metaclass=ValidationMeta):
    attribute = 42


# ValueError: Класс должен содержать атрибут 'attribute'
# class InvalidClass(metaclass=ValidationMeta):
#     pass


class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class


class Base(metaclass=RegistryMeta):
    pass


class Derived1(Base):
    pass


class Derived2(Base):
    pass


print(RegistryMeta.registry)
