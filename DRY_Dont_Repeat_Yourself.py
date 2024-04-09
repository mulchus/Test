"""
DRY - это принцип разработки, который означает "Don't Repeat Yourself" (не повторяйся). В контексте программирования,
DRY означает, что любой фрагмент кода должен иметь только один источник истины, и он должен быть легко доступен и
изменяем. Это уменьшает количество дублирующегося кода и упрощает процесс сопровождения и изменения кода.
Класс Person содержит общие атрибуты и поведение для всех людей в системе. Классы Student и Teacher наследуют от Person
и добавляют свои определенные атрибуты и поведение. Таким образом, мы избегаем дублирования кода таких атрибутов, как
имя и возраст, или таких методов, как внедрение.

Используя ООП и наследование, мы можем эффективно применять принципы DRY и сделать код более удобным в сопровождении и
расширяемым. Точно так же вы можете использовать функции и композицию более высокого порядка в FP для достижения тех
же целей.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        super().introduce()
        print(f"I am majoring in {self.major}.")


class Teacher(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def introduce(self):
        super().introduce()
        print(f"I teach in the {self.department} department.")


student1 = Student('Вася', 25, 'мажор')
print(student1.introduce())
