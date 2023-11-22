from sys import platform

def linux_print():
    print('Printing from Linux...')

def win32_print():
    print('Printing from Windows...')

def darwin_print():
    print('Printing from macOS...')

printer = globals()[platform + '_print']

printer()

exit()
class A:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.var1 *= 2


obj = A(5, 7)
# obj.var1 = 5
print(obj.var1)
print(obj.__init__(5, 6))
print(obj.__dict__)



exit()
from functools import partial
def power(exp, base, free):
    return base ** exp
square = partial(power, 2, 11)
print(square(111))

exit()
def mean():
    sample = []
    def _mean(number, num2):
        sample.append(number)
        print(num2)
        return sum(sample) / len(sample) + num2
    return _mean

current_mean = mean()
print(current_mean(10, 2))


exit()
lazy_var = 5
def func():
    lazy_var = 2
    def nested():
        nonlocal lazy_var
        lazy_var += 1
        print(lazy_var + 1)
    nested()

func()

exit()

print(abs(-15))  # Standard use of a built-in function
abs = 20  # Redefine a built-in name in the global scope
print(abs)
del abs
print(abs(-10))

exit()

print(dir(__builtins__))

print(len(dir(__builtins__)))
print(dir(__doc__))
# This area is the global or module scope
# number = 100
def outer_func():
    # This block is the local scope of outer_func()
    # It's also the enclosing scope of inner_func()
    # number = 50
    def inner_func():
        global number
        # This block is the local scope of inner_func()
        print(number)

    inner_func()

outer_func()



exit()


def start():
    candy = 3

    def get_candy():
        # candy = 5
        
        def increment_candy():
            # global candy
            nonlocal candy
            candy += 1
            return candy
        return increment_candy()

    return get_candy()

print('Всего {} конфет.'.format(start()))


# a = 5
# def abc(b):
#     nonlocal b
#     b += 10
#
#     def xyz(c):
#         c += 15
#         return c
#
#     print(a + b + xyz(1))
#
# print(a+b)
# abc()
