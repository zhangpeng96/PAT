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

for i, query in enumerate(lines[n:], 1):
    count, start, end = map(int, query.split())
    result = sorted(
        filter(lambda x: start <= x[1] <= end, record),
        key=lambda x: (-x[2], x[1], x[0])
    )
    print('Case #{}:'.format(i))
    if result:
        for res in result[:count]:
            print('{} {} {}'.format(*res))
    else:
        print('None')
