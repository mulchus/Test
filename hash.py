_int = 123456789987654321
print(type(_int))
print(_int.__hash__())
print(hash(_int))

_str = 'abcd'
print(type(_str))
print(_str.__hash__())
print(hash(_str))

_frozenset = frozenset([1, 2, 3, 4, 'abc', 'cdf'])
print(type(_frozenset))
print(_frozenset.__hash__())
print(hash(_frozenset))

_tuple = tuple({1, 2, 3, 4, 'abc', 'cdf'})
print(type(_tuple))
print(_tuple.__hash__())
print(hash(_tuple))

_tuple2 = tuple({1, 2, 3, 4, 'abc', 'cdf'})
print(type(_tuple2))
print(_tuple2.__hash__())
print(hash(_tuple2))

print(_tuple2.__hash__().__eq__(_tuple.__hash__()))

if _tuple != _tuple2:
    print(f'Dont worry!!!')

for t in range(len(_tuple)):
    if _tuple[t] == _tuple2[t]:
        continue
    else:
        print(f'Dont worry {_tuple[t]}')
        break


_list = [1, 2, 3, 4, 'abc', 'cdf']
print(type(_list))
print(_list.__hash__())
print(hash(_list))

_dict = dict['a': 1, 'b': 2, 'c': 3]
print(type(_dict))
print(_dict.__hash__())
print(hash(_dict))



# class MyClass:
#     print(f"Создаётся класс MyClass")
#
#
# a = MyClass()
# print(a.__hash__())




# a = 'abcd'
#
# b = 'abcdt'
#
# ab = {'a': '123abc'}
#
# ab['b'] = 123
#
# print(ab['a'].__hash__())
# print(ab['b'].__hash__())
#
# print(hash(ab['a']), hash(ab['b']), sep='- ', end='\n')
#
# print(ab.keys())
