"""
    @name     : a1126
    @version  : 21.0205
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p4 error, p6 timeout
"""

from collections import Counter

count = 0
visited, adjacency = {}, {}

def dfs(v):
    visited[v] = True
    global count
    count += 1
    for vert in adjacency[v]:
        if not visited.get(vert, False):
            dfs(vert)

vert, edge = map(int, input().split())
for _ in range(edge):
    v1, v2 = map(int, input().split())
    adjacency[v1] = adjacency.get(v1, []) + [v2]
    adjacency[v2] = adjacency.get(v2, []) + [v1]

dfs(1)

degree = list(map( lambda x:len(x[1]), sorted(adjacency.items(), key=lambda x: x[0]) ))
degree_odd = [ d % 2 for d in degree ]
amount = Counter(degree_odd)

print(' '.join(map(str, degree)))
if amount.get(0, 0) == vert and count == vert:
    print('Eulerian')
elif amount.get(1, 0) == 2 and amount.get(0, 0) == (vert-2) and count == vert:
    print('Semi-Eulerian')
else:
    print('Non-Eulerian')
