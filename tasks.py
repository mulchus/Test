

def duplicate_nums(nums):
    dubl_nums = set([num for num in nums if nums.count(num) > 1])
    return sorted(dubl_nums) if dubl_nums else None


print(duplicate_nums([5, 1, 2, 3, 4, 3, 5, 3, 6, 5]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
