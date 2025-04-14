import string

s = "Hello, world!"

# эффективно удалить все стандартные знаки препинания из строки в Python
print(s.translate(str.maketrans("", "", string.punctuation)))

