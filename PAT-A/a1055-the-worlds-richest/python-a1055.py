"""
    @name     : a1055
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 35'00"
    @accepted : p1,p2 timeout
"""

from sys import stdin

record = []

n, k = map(int, input().split())
lines = stdin.readlines()

for line in lines[:n]:
    name, age, worth = line.split()
    record.append([name, int(age), int(worth)])

record.sort(key=lambda x: (-x[2], x[1], x[0]))

for i, query in enumerate(lines[n:], 1):
    valid = 0
    count, start, end = map(int, query.split())
    print('Case #{}:'.format(i))
    for i in range(n):
        if start <= record[i][1] <= end:
            print(*record[i])
            valid += 1
            if valid == count:
                break
    if not valid:
        print('None')
