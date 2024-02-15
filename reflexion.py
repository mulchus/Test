# Рефлексия — это возможность программы получать доступ к своей собственной структуре и поведению во время выполнения.
# Это означает, что программа может получить информацию о типах объектов, именах методов, атрибутах и других свойствах.
class MyClass:
    def __init__(self):
        self.x = 1
    ...


my_object = MyClass()
print(type(my_object))
print(isinstance(my_object, MyClass))

print(dir(my_object))

print(getattr(my_object, "x"))

setattr(my_object, "x", 2)
print(getattr(my_object, "x"))
