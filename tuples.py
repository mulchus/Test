# add element in tuple
# https://bobbyhadz.com/blog/python-tuple-insert-element

my_tuple = ('a', 'b', 'c')
new_tuple = (*my_tuple, 'd')    # unpacking and add element
print(new_tuple)

new_tuple_2 = my_tuple[2].replace('c', 'd')     # return only one element
print(new_tuple_2)
print(my_tuple)     # don't change primary tuple


my_tuple = (1, 2, 3, 4, 5, 6, 7)
print(id(my_tuple))    # id of primary tuple
my_tuple += (0,)
print(id(my_tuple))     # id is different
print(my_tuple)

x = ([1, 2], )
x[0].append(3)    # Items inside tuple are mutable
print(x)
x[0].pop(0)      # Items inside tuple are mutable
print(x)
# x[0] += [4]     # raise TypeError: 'tuple' object does not support item assignment
# x[0] = [4]    # raise TypeError: 'tuple' object does not support item assignment
print(x)

y = ([1, 2])    # y is not a tuple, no "," at end. It's a list
print(type(y))
y.append(3)
print(y)
