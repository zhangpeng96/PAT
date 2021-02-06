"""
    @name     : a1154
    @version  : 21.0206
    @author   : zhangpeng96
    @time     : 13'35"
    @accepted : all
"""

edges = {}

vert_count, edge_count = map(int, input().split())
for i in range(edge_count):
    edges[i] = tuple(map(int, input().split()))

for _ in range(int(input())):
    proper = True
    colors = list(map(int, input().split()))
    for v1, v2 in edges.values():
        if colors[v1] == colors[v2]:
            proper = False
            break
    if proper:
        k = len(set(colors))
        print('{}-coloring'.format(k))
    else:
        print('No')
