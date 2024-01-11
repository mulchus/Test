def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


random_list = [6, 5, 2, 4, 1, 3]


bubble_sort(random_list)
print(random_list)
