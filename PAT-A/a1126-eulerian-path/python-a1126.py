"""
    @name     : a1126
    @version  : 21.0205
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p4 error, p6 timeout
"""

from collections import Counter, defaultdict

def dfs(v1):
    visited[v1] = True
    count['all'] += 1
    for v2 in range(1, vert+1):
        if not visited[v2] and matrix[v1, v2]:
            dfs(v2)


count = {'all': 0, 'odd': 0}
visited, matrix, degrees = defaultdict(bool), defaultdict(bool), defaultdict(int)

vert, edge = map(int, input().split())
for _ in range(edge):
    v1, v2 = map(int, input().split())
    matrix[v1, v2] = True
    matrix[v2, v1] = True
    degrees[v1] += 1
    degrees[v2] += 1

dfs(1)

for degree in degrees.values():
    if degree % 2:
        count['odd'] += 1

print(*map(lambda x: x[1], sorted(degrees.items())))

if count['all'] == vert:
    if count['odd'] == 0:
        print('Eulerian')
    elif count['odd'] == 2:
        print('Semi-Eulerian')
    else:
        print('Non-Eulerian')
else:
    print('Non-Eulerian')
