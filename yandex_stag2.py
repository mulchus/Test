# https://contest.yandex.ru/contest/51022/problems/B/

# 2 5 10
# 1 2
# 1 2 3 4 5
# 1 A 3
# 1 A 4
# 1 A 5
# 1 A 6
# 1 A 7
# -1 A 1
# 1 B 7
# -1 A 6
# -1 B 1
# 1 A 7

import sys
import time


params = list(map(int, sys.stdin.readline().split()))
A = list(sys.stdin.readline().split())
B = list(sys.stdin.readline().split())

start = time.time()
result = []

for i in range(params[2]):
    action = list(sys.stdin.readline().split())
    
    if action[0] == '1':
        if action[1] == 'A':
            A.append(action[2])
        else:
            B.append(action[2])
    else:
        if action[1] == 'A':
            A.remove(action[2])
        else:
            B.remove(action[2])
    
    massive = A if len(A) > len(B) else B
    
    AA = A.copy()
    BB = B.copy()
    
    for char in massive:
        if char in AA and char in BB:
            AA.remove(char)
            BB.remove(char)
    result.append((len(AA) + len(BB)))

print(' '.join(map(str, result)))

print(float(time.time() - start, 7))
