"""
    @name     : a1142
    @version  : 21.0216
    @author   : zhangpeng96
    @time     : 40'00"
    @accepted : all
"""

from itertools import combinations

adj_list = {}

def is_clique(vertex):
    for v1, v2 in combinations(vertex,2):
        if not adj_table[v1][v2]:
            return 'Not a Clique'
    shared = set.intersection(*map(
        lambda x: set( adj_list.get(x,[]) ), vertex
    ))
    for v in shared:
        if v not in vertex: return 'Not Maximal'
    return 'Yes'


vertex_n, edge_n = map(int, input().split())
adj_table = [ [ 0 for _ in range(vertex_n+1) ] for _ in range(vertex_n+1) ]

for _ in range(edge_n):
    v1, v2 = map(int, input().split())
    adj_list[v1] = adj_list.get(v1, []) + [v2]
    adj_list[v2] = adj_list.get(v2, []) + [v1]
    adj_table[v1][v2] = adj_table[v2][v1] = 1

for _ in range(int(input())):
    clique = list( map(int, input().split()[1:]) )
    print(is_clique(clique))
