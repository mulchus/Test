x = [2, 1, 4, 3, 5]
z = [1, 2, 3, 4, 5]

squared = map(lambda y: y**2, x)
sorted_squares = sorted(squared)
squares = list(squared)
print(sorted_squares)
print(squares)

# print(sorted(squared))
# print(sorted(squared))

z.reverse()

multiplications = map(lambda xx, zz: xx * zz, x, z)

print(list(multiplications))
print()
# print(sorted(squared)) == sorted(squared))

# Объединение двух списков с помощью функции zip()
first_names = ['John', 'Emma', 'Jessica']
last_names = ['Doe', 'Smith', 'Thompson']
full_names = list(map(lambda x, y: x + ' ' + y, first_names, last_names))
print(full_names) # Output: ['John Doe', 'Emma Smith', 'Jessica Thompson']



def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5, 6]

map_obj = map(square, numbers)  # c map
print(type(map_obj))
print(list(map_obj))
print(map_obj)
print()

lst_comp = [square(x) for x in numbers]  # c list comprehension, обязательно в []
print(type(lst_comp))
print(lst_comp)
print()

gen_exp = (square(x) for x in numbers)  # c generator expressions, обязательно в ()
print(type(gen_exp))
print(list(gen_exp))
# or
print(list(square(x) for x in numbers))  # без дополнительных скобок ()
print(gen_exp)
print()
