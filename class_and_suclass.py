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
    def exception(self):
        raise Exception(f'Fruit_exception: {self.name}')


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
    
try:
    f1.exception()
except Exception as e:
    print(e)
    