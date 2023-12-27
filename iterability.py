_str = 'abcd'
for item in _str:
    print(item, end='-')
print('\n')

_frozenset = frozenset([1, 2, 3, 4, 'abc', 'cdf'])
for item in _frozenset:
    print(item, end='-')
print('\n')
    
_tuple = tuple({1, 2, 3, 4, 'abc', 'cdf'})
for item in _tuple:
    print(item, end='-')
print('\n')

_list = [1, 2, 3, 4, 'abc', 'cdf']
for item in _list:
    print(item, end='-')
print('\n')

_dict = dict['a': 1, 'b': 2, 'c': 3]
for item in _dict:
    print(item, end='-')
print('\n')

_set = set['a': 1, 'b': 2, 'c': 3]
for item in _set:
    print(item, end='-')
print('\n')

_int = 123456789987654321
for item in _int:
    print(item, end='-')
print('\n')

_float = 123.456789987654321
for item in _float:
    print(item, end='-')
print('\n')

