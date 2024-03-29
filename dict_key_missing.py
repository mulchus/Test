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
