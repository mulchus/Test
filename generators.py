def generator():
    yield from range(3)  # отдаст 0, 1, 2
    return 'hello'  # не выведется


gen = generator()
result = list(gen)

print(gen)
print(result)
