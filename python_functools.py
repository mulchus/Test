from functools import reduce
import operator

numbers = list(range(1, 11))

print(operator.add(1, 2))
print(reduce(operator.add, numbers))
print(reduce(operator.mul, numbers))
print(reduce(operator.sub, numbers))
print(reduce(operator.truediv, numbers))
