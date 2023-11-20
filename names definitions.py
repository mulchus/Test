
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
