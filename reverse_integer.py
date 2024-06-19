import time

while True:
    try:
        number = int(input('get integer:'))
        break
    except ValueError:
        print('not a number')

time1 = time.time()
time.sleep(0.01)
print(''.join(reversed(str(number))))
print(f'{time.time() - time1:.12f}')

time1 = time.time()
time.sleep(0.01)
number2 = list(str(number))
number2.reverse()
print(int(''.join(number2)))
print(f'{time.time() - time1:.12f}')

time1 = time.time()
time.sleep(0.01)
print(int(str(number)[::-1]))
print(f'{time.time() - time1:.12f}')
