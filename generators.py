def generator():
    # return 'hello'  # raise StopIteration
    yield from range(3)  # отдаст 0, 1, 2
    return 'hello'  # не выведется


gen = generator()
result = list(gen)

print(gen)
print(result)


def some_generator():
    for i in range(6):
        x = yield i
        print(f'Это обратный a={x}')


gen = some_generator()
a = next(gen)
print(f'Это a={a}')

while a < 4:
    a = gen.send(a + 10)
    print(f'Это a={a}')
