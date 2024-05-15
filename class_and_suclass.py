# задачи из классов и их наследования https://t.me/dvmn_flood/155704

class Fruit:
    fruit_counter = 0
    
    def __init__(self, name: str):
        Fruit.fruit_counter += 1
        self.name = name
    
    def __del__(self):
        Fruit.fruit_counter -= 1
    
    # 2. Имеется класс Fruit. В runtime экземпляры этого класса создаются и удаляются.
    #    Необходимо сделить за утечками памяти, для чего система мониторинга вызывает метод класса instance_count
    #    Необходимо реализовать этот метод
    def instance_count():
        return Fruit.fruit_counter
    
    # 3. Необходимо доработать класс Fruit таким образом, чтобы его можно было итерировать.
    # В качестве коллекции используем имя класса
    def __iter__(self):
        return iter(self.name)
    
    # 4. Необходимо доработать класс Fruit таким образом, чтобы можно было использовать его в менеджере контекста
    #    Выброшенное исключение нужно перехватить и распечатать его значение
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)
        return True


class Banana(Fruit):
    banana_counter = 0
    
    def __init__(self, *args, **kwargs):
        super(Banana, self).__init__(*args, **kwargs)
        Banana.banana_counter += 1
    
    def instance_count():
        return Banana.banana_counter
    
    def __del__(self):
        Banana.banana_counter -= 1


f1 = Fruit('Apple')
f2 = Fruit('Orange')
b1 = Banana('Sweet banana')

print(f'Fruit instance count = {Fruit.instance_count()}')  # Fruit instance count = 2
print(f'Banana instance count = {Banana.instance_count()}')  # Banana instance count = 1
print(b1.name)

del f1
print(f'Fruit instance count = {Fruit.instance_count()}')  # Fruit instance count = 1

del b1
print(f'Banana instance count = {Banana.instance_count()}')

f1 = Fruit('Apple')
for letter in f1:
    print(letter)
    
with Fruit('Apple') as f1:
    print(f'This is {f1.name}')
    raise Exception('this is exception')

print('The end')


class Inspector:
    def __getitem__(self, index):
        print(len(index))
        index = [item + 1 for item in index]
        # for i in range(len(index)):
        #     print(i)
        #     index[i] += 1
        return index


print(Inspector)
print(Inspector())
print(Inspector()[1, 2, 3])
# print(Inspector()(1, 2, 3))
# print(Inspector()["a", "b", 5])


class Age:
    def calc_adult_age(self, age):
        if age < 18:
            print('Not adult')
        else:
            print('Adult')
try:
    with Age() as obj:      # TypeError: 'Age' object does not support the context manager protocol
        obj.calc_adult_age(13)
except TypeError as e:
    print(e)
obj = Age()
obj.calc_adult_age(13)  # "Not adult"


# пример того, как ООП можно использовать для применения принципов DRY
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


student = Student("John", 20, "Computer Science")
teacher = Teacher("Jane", 30, "Computer Science")
student.introduce()
teacher.introduce()
