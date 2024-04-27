my_list = [3, 4, 5, 8, 0, 4, 2, 1, 5, 6, 7, 8, 10, 20, 18, 15, 11, 9, 20, 9, 0, 3, 2, 2, 8, 6, 7]

list_result = [x for x in my_list if not x % 2]
print(list_result)

set_result = {x for x in my_list if not x % 2}
print(set_result)

tuple_result = tuple(x for x in my_list if not x % 2)
print(tuple_result)

dict_result = {x: x * 2 for x in my_list if not x % 2}
print(dict_result)
print(*dict_result)

rez_generator = (x for x in my_list if not x % 2)
print(type(rez_generator))

print(next(rez_generator))
print(next(rez_generator))
print(next(rez_generator))

my_list1 = [3, 4, 5, 8, 0, 4, 2, 1, 5, 6, 7, 8, 10]
my_list2 = [10, 15, 11, 9, 20, 9, 0, 3, 2, 2, 8, 6, 7]

print(len(my_list1))
print(len(my_list2))

rez = [x * y for x in my_list1 if x % 2 == 0 for y in my_list2 if y % 2 != 0]
print(rez)

rez_of_set = ['FizzBuzz' if x % 15 == 0 else
              'Fizz' if x % 3 == 0 else
              'Buzz' if x % 5 == 0 else
              x for x in range(1, 101)]
print(rez_of_set)

print([line.strip() for line in open("file.txt")])
