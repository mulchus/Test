# Почему хваленный map + filter работает медленней первых двух вариантов?

import time

def power(x):
    return x**2

start = time.time()
rez1 = [power(x) for x in range(1_000_000) if x % 2 == 0]
print(f'DELTA0: {time.time() - start}')
print(len(rez1))

rez2 = []
start = time.time()
for x in range(1_000_000):
  if x % 2 == 0:
    rez2.append(power(x))
  continue
print(f'DELTA1: {time.time() - start}')
print(len(rez2))

start = time.time()
arr = list(map(power, filter(lambda x: x%2 == 0, range(1_000_000))))
print(f'DELTA2: {time.time() - start}')
print(len(arr))

# DELTA0: 0.9381000995635986
# 500000
# DELTA1: 1.195199966430664
# 500000
# DELTA2: 1.3024001121521
# 500000