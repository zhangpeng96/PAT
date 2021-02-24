"""
    @name     : a1126
    @version  : 21.0224
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p6 timeout
"""

def dfs(v1):
    visited[v1] = True
    count['all'] += 1
    for v2 in range(1, vert+1):
        if not visited[v2] and matrix[v1][v2]:
            dfs(v2)


vert, edge = map(int, input().split())

count = {'all': 0, 'odd': 0}
visited = [False] * (vert+1)
degrees = [0] * (vert+1)
matrix = [ [0] * (vert+1) for _ in range(vert+1) ]

for _ in range(edge):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = True
    matrix[v2][v1] = True
    degrees[v1] += 1
    degrees[v2] += 1

dfs(1)

for v in range(1, vert+1):
    if degrees[v] % 2:
        count['odd'] += 1

print(*degrees[1:vert+1])
if count['all'] == vert:
    if count['odd'] == 0:
        print('Eulerian')
    elif count['odd'] == 2:
        print('Semi-Eulerian')
    else:
        print('Non-Eulerian')
else:
    print('Non-Eulerian')
