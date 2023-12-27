# https://contest.yandex.ru/contest/51022/problems/?nc=xY56e43S&success=103957895#998/2023_07_29/qfDIAykiKl

import sys

# 980 2 12 10 30 1
# 980 3 1 10 31 3

# 1001 5 20 14 15 16
# 9009 9 11 12 21 11

start = list(map(int, sys.stdin.readline().strip().split()))
stop = list(map(int, sys.stdin.readline().strip().split()))

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ((stop[0] - start[0]) * 365 + sum(days_in_months[:stop[1] - 1]) -
        sum(days_in_months[:start[1] - 1]) + stop[2] - start[2])

seconds = (stop[3] - start[3]) * 3600 + (stop[4] - start[4]) * 60 + stop[5] - start[5]

if seconds < 0:
    days -= 1
    seconds = 86400 + seconds

print(days, seconds)
