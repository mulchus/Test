# Методы экземпляра (`self`):
# ✓ Работают с конкретным объектом
# ✓ Изменяют атрибуты экземпляра
# ✓ Доступ к атрибутам класса через self.__class__
class MyClass:
    def method(self):
        return "Метод экземпляра", self

# 🔹 Методы класса (`cls`, `@classmethod`):
# ✓ Работают с классом в целом
# ✓ Могут изменять атрибуты класса
# ✓ Не изменяют атрибуты экземпляра
    @classmethod
    def class_method(cls):
        return "Метод класса", cls

# 🔹 Статические методы (`@staticmethod`):
# ✓ Не принимают self или cls
# ✓ Не изменяют состояние ни экземпляра, ни класса
# ✓ Используются для вспомогательных функций
    @staticmethod
    def static_method():
        return "Статический метод"

exemp = MyClass()
#print(MyClass.method())        # TypeError: MyClass.method() missing 1 required positional argument: 'self'
print(exemp.method())           # ("Метод экземпляра", <__main__.MyClass object at 0x000002B0BECB7C50>)
print(MyClass.class_method())   # ("Метод класса", <class '__main__.MyClass'>)
print(exemp.class_method())     # ("Метод класса", <class '__main__.MyClass'>)
print(MyClass.static_method())  # "Статический метод"
print(exemp.static_method())    # "Статический метод"
print()

# 🔹 Применение в реальном коде:

class Pizza:
    def __init__(self, ingredients: list = None):
        self.ingredients = [] if ingredients is None else ingredients

    def get_cap_ingredients(self):
        """Send capitalized ingredients names
        """
        return [ingredient.capitalize() for ingredient in self.ingredients]

    @classmethod
    def margherita(cls):
        return cls(["моцарелла", "помидоры"])

    @staticmethod
    def circle_area(r):
        import math
        return r ** 2 * math.pi

pizza1 = Pizza.margherita()     # Классовый метод
print(pizza1)                   # <__main__.Pizza object at 0x000001BF996AE8D0>
print(pizza1.margherita())      # <__main__.Pizza object at 0x000001BF996AE8D0>
print(Pizza.circle_area(4))     # 50.26548245743669
print(pizza1.circle_area(3))    # 28.274333882308138
print(pizza1.ingredients)       # ['моцарелла', 'помидоры']
#print(Pizza.get_cap_ingredients()) # TypeError: Pizza.get_cap_ingredients() missing 1 required positional argument: 'self'
print(pizza1.get_cap_ingredients()) # ['Моцарелла', 'Помидоры']

pizza2 = Pizza(["бамбук"])
print(pizza2.get_cap_ingredients()) # ['Бамбук']

pizza3 = Pizza()
print(pizza3.get_cap_ingredients()) # []


# 🔹 Вывод:
# ✓ Методы экземпляра изменяют данные конкретного объекта
# ✓ Методы класса работают с классом и создают альтернативные конструкторы
# ✓ Статические методы полезны для утилитарных функций
