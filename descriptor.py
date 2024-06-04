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


if __name__ == "__main__":
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
