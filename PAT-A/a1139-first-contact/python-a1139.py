"""
    @name     : a1139
    @version  : 21.0223
    @author   : zhangpeng96
    @time     : 60'00"
    @accepted : p1,p2 error p5 timeout
"""

from collections import defaultdict

vertex, edge = map(int, input().split())
table = defaultdict(list)
matrix = defaultdict(bool)

for _ in range(edge):
    v1, v2 = map(int, input().split())
    same = True if v1 * v2 > 0 else False
    v1, v2 = abs(v1), abs(v2)
    matrix[v1, v2] = True
    matrix[v2, v1] = True
    if same > 0:
        table[v1].append(v2)
        table[v2].append(v1)

for _ in range(int(input())):
    friends = []
    a, b = map(lambda x:abs(int(x)), input().split())
    for c in table[a]:
        if c != b:
            for d in table[b]:
                if matrix[c, d] and a != b and a != d and c != d:
                    friends.append( (c, d) )
    print(len(friends))
    for c, d in sorted(friends, key=lambda x: (x[0],x[1])):
        print('{:04} {:04}'.format(c, d))
