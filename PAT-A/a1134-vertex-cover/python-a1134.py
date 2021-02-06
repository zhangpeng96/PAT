"""
    @name     : a1134
    @version  : 21.0206
    @author   : zhangpeng96
    @time     : 54'12"
    @accepted : p2 timeout
"""

vert_in_edge = {}
edge_cover = {}

vert_count, edge_count = map(int, input().split())

for i in range(edge_count):
    v1, v2 = map(int, input().split())
    vert_in_edge[v1] = vert_in_edge.get(v1, []) + [i]
    vert_in_edge[v2] = vert_in_edge.get(v2, []) + [i]

for _ in range(int(input())):
    nodes = map(int, input().split()[1:])
    edge_cover = dict(zip( [i for i in range(edge_count)], [False]*edge_count ))

    for node in nodes:
        for edge in vert_in_edge.get(node, []):
            edge_cover[edge] = True
    
    if all(edge_cover.values()):
        print('Yes')
    else:
        print('No')
