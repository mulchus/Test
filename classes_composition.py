"""
Композиция классов — это концепция, при которой один класс включает в себя объект(ы) другого класса в качестве
атрибута. Это отличается от наследования, где класс наследует атрибуты и методы другого класса. Композиция обычно
предпочтительна в сравнении с наследованием, так как она обеспечивает более гибкую структуру.
Композиция обычно предпочтительна, когда отношение между двумя классами является «имеет» или «включает», а не
«является». Она делает код более гибким, позволяя изменять поведение объекта, не изменяя его класс напрямую.
Важно отметить, что композиция и наследование могут использоваться вместе в зависимости от конкретных
ребований вашей программы.
"""
# classes_composition.py

print('Пример с композицией')

class Engine:
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()


my_car = Car()

my_car.engine.start()
my_car.engine.stop()

my_car.start_engine()
my_car.stop_engine()


print('\nПример с наследованием')

class Engine:
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')


class Car(Engine):
    def start_engine(self):
        self.start()

    def stop_engine(self):
        self.stop()


my_car = Car()

my_car.start()
my_car.stop()

my_car.start_engine()
my_car.stop_engine()