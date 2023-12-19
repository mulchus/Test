#
# a = ["S","O","L","O"]
# b = ["T","H","O","U","G","H", "T"]
# c = ['M', 'O', 'O', 'C', '.']
#
# c = c.remove("O")
# print(a + b + )
#
# exit()
#
# nums = [1, 2, 3]
# map_ = map(lambda x: x * x, nums)
# # print(*map_)
# nums = list(map_)
# print(nums)
# print(*map_)
#
# exit()


lis = ['a', 'b', 'c', 'b']
lis.remove("b")
print(lis)
lis.remove("d")
print(lis)

exit()

def duplicate_nums(nums):
    dubl_nums = set([num for num in nums if nums.count(num) > 1])
    return dubl_nums if dubl_nums else None


print(duplicate_nums([5, 1, 2, 3, 4, 3, 5, 3, 6, 5]))
print(duplicate_nums([100, 81, 72, 43, 72, 81, 99, 5, 99, 100, 12, 5, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
