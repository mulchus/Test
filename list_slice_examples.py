# Циклический сдвиг списка
def rotate(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate([1, 2, 3, 4, 5], 2))  # → [4, 5, 1, 2, 3]

#  Извлечение элементов по шаблону
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days[::3])  # → ['Mon', 'Thu', 'Sun']
print(days[5:])   # → ['Sat', 'Sun']

# Чётные и нечётные индексы
nums = list(range(10))
print(nums[::2])  # чётные индексы → [0, 2, 4, 6, 8]
print(nums[1::2]) # нечётные индексы → [1, 3, 5, 7, 9]

# Массовое обновление по срезу
nums = [0]*10
nums[::2] = range(5)  # → [0, 0, 1, 0, 2, 0, 3, 0, 4, 0]
print(nums)

# Парсинг строки фиксированными блоками
def parse_by_blocks(data, block_size):
    if block_size > len(data):
        raise ValueError('block_size mast be less than data length')
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

print(parse_by_blocks('abcdefghij', 2))  # → ['ab', 'cd', 'ef', 'gh', 'ij']


# Срезы в многомерных структурах
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print([row[1] for row in matrix])     # → [2, 5, 8]
print([matrix[i][i] for i in range(3)])  # → [1, 5, 9]

# Использование `slice()` вручную
s = slice(2, 8, 2)
lst = list(range(10))
print(lst[s])  # → [2, 4, 6]

# NumPy: срезы в многомерных массивах
import numpy as np
arr = np.arange(100).reshape(10, 10)
print(type(arr))
print(arr[-3:, -3:])  # Подматрица 3×3 в правом нижнем углу

# Pandas: срезы по строкам и условиям
import pandas as pd
df = pd.DataFrame({'A': [1,2,3,4], 'B': [10,20,30,40]})
print(df)
print(df.iloc[:2])  # первые 2 строки
print(df.loc[df['A'] > 2])   # строки, где A > 2

# Срезы в байтовых объектах
b = b'Hello, world!'
print(b[:5])  # → b'Hello'
ba = bytearray([10, 20, 30, 40])
print(list(ba[1:3]))  # → [20, 30]
