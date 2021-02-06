
# edge_end = {}
vert_in_edge = {}
edge_cover = {}

vert, edge = map(int, input().split())

for i in range(edge):
    v1, v2 = map(int, input().split())
    vert_in_edge[v1] = vert_in_edge.get(v1, []) + [i]
    vert_in_edge[v2] = vert_in_edge.get(v2, []) + [i]

for _ in range(int(input())):
    print('--', edge)
    nodes = map(int, input().split()[1:])
    edge_cover = dict(zip( [i for i in range(edge)], [False]*edge ))
    print('===', edge, edge_cover)
    for node in nodes:
        for edge in vert_in_edge.get(node, []):
            print(node, edge, edge_cover)
            edge_cover[edge] = True
    # print(vert_in_edge, edge_cover)