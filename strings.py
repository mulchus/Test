import time

words = ['word'] * 10000 # 000

start_time = time.time()
sentence = ''
# sentence = [word for word in words]

for word in words:
    sentence += word + ' '
print(sentence)
print(time.time() - start_time)

start_time = time.time()
sentence = ' '.join(words)
print(sentence)
print(time.time() - start_time)


def find_words(words):
    ok_words = []
    for word in words:
        for row in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']:
            if all(char in row for char in list(word.lower())):
                ok_words.append(word)
    return ok_words


print(find_words(["Hello","Alaska","Dad","Peace"]))
print(find_words(["omk"]))

# Решение из вики
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         #
#         set1 = {'q','w','e','r','t','y','u','i','o','p'}
#         set2 = {'a','s','d','f','g','h','j','k','l'}
#         set3 = {'z','x','c','v','b','n','m'}
#
#         res = []
#         for i in words:
#             wordset = set(i.lower())
#             if (wordset&set1 == wordset) or (wordset&set2 == wordset) or (wordset&set3 == wordset):
#                 res.append(i)
#         return res

import re
text = "Hello, world!"
result = re.split(r"\W+", text)
print(result)

result = re.subn(r"\s", "-", text)
print(result)


class Example:
    def __init__(self):
        self.value = 42

    def __repr__(self):
        return 'Example(' + str(self.value) + ')'

    def __str__(self):
        return 'The value is ' + str(self.value)


e = Example()

print(str(e))   # "The value is 42"
print(repr(e))  # "Example(42)"
