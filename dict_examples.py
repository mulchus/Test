class MyDict(dict):
    def __missing__(self, key):
        return f'{key} is missing'


my_dict = MyDict({'a': 1, 'b': 2})
print(my_dict.keys())
print(my_dict['c'])
print(my_dict.get('c'))


dict2 = {'a': 1, 'b': 2}
print(dict2.setdefault('a'))
print(dict2.setdefault('c', 3))
print(dict2)

# Получение словаря из списка кортежей и списка с названиями колонок
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

chain_map = ChainMap(dict1, dict2)
print(chain_map)
print(dict(chain_map))
