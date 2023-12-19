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