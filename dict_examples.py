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


def compare_templates_indexes(curent_templates_index: dict, new_templates_index: dict) -> tuple:
    curent_templates_index_keys = set(curent_templates_index.keys())
    new_templates_index_keys = set(new_templates_index.keys())
    shared_keys = curent_templates_index_keys.intersection(new_templates_index_keys)
    added = curent_templates_index_keys - new_templates_index_keys
    removed = new_templates_index_keys - curent_templates_index_keys
    modified = ({o: (curent_templates_index[o], new_templates_index[o])
                for o in shared_keys if curent_templates_index[o] != new_templates_index[o]})
    same = set(o for o in shared_keys if curent_templates_index[o] == new_templates_index[o])
    return added, removed, modified, same


x = {"a": 1, "d": 2, 'z': 3, 'p': 20}
y = {"a": 12, "c": 4, 'b': 5, 'p': 20}
added, removed, modified, same = compare_templates_indexes(y, x)
print(added, removed, modified, same)


# разница между двумя списками словарей, например кверисетами
list_of_dicts_1 = [
    {"a": 1, "b": 2, 'c': 5, 'd': 20},
    {"a": 2, "b": 4, 'c': 5, 'd': 20},
    {"a": 3, "b": 6, 'c': 5, 'd': 20},
    {"a": 4, "b": 8, 'c': 5, 'd': 20},
    {"a": 5, "b": 10, 'c': 7, 'd': 20},
    {"a": 6, "b": 12, 'c': 7, 'd': 20},
]

list_of_dicts_2 = [
    {"a": 1, "b": 2, 'c': 5, 'd': 20},
    {"a": 2, "b": 4, 'c': 5, 'd': 20},
    {"a": 3, "b": 6, 'c': 5, 'd': 20},
]

diff = []
for dict1 in list_of_dicts_1:
    if dict1 not in list_of_dicts_2:
        diff.append(dict1)

print(diff)

