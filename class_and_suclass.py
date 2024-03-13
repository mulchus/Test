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
print(Inspector()(1, 2, 3))
print(Inspector()["a", "b", 5])
    