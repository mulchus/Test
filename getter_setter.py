class MyClass(object):
    def __init__(self, name):
        self._value = 0
        self.name = name
    
    @property
    def value(self):
        print(f"Getting value: {self.name} = { self._value}")
        return self._value
    
    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("value cannot be negative")
        self._value = value
        print(f"Setting value: {self.name} = {self._value}")


some = MyClass('some')
some.value = 5
a = some.value
