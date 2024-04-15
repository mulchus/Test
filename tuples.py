# add element in tuple
# https://bobbyhadz.com/blog/python-tuple-insert-element

my_tuple = ('a', 'b', 'c')
new_tuple = (*my_tuple, 'd')
print(new_tuple)

my_tuple = (1, 2, 3, 4, 5, 6, 7)
print(id(my_tuple))
my_tuple += (0,)
print(id(my_tuple))
print(my_tuple)

