"""
    @name     : a1139
    @version  : 21.0223
    @author   : zhangpeng96
    @time     : 60'00"
    @accepted : p5 timeout
"""

from sys import stdin
from collections import defaultdict

vertex, edge = map(int, input().split())
lines = stdin.readlines()
table = defaultdict(list)
matrix = defaultdict(bool)

for line in lines[:edge]:
    v1, v2 = line.split()
    same = True if len(v1) == len(v2) else False
    v1, v2 = abs(int(v1)), abs(int(v2))
    matrix[v1, v2] = True
    matrix[v2, v1] = True
    if same > 0:
        table[v1].append(v2)
        table[v2].append(v1)

for line in lines[edge+1:]:
    friends = []
    a, b = map(lambda x:abs(int(x)), line.split())
    for c in table[a]:
        if c != b:
            for d in table[b]:
                if matrix[c, d] and a != b and a != d and c != d:
                    friends.append( (c, d) )
    print(len(friends))
    for c, d in sorted(friends, key=lambda x: (x[0],x[1])):
        print('{:04} {:04}'.format(c, d))
