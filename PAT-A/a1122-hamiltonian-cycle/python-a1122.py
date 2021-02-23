"""
    @name     : a1122
    @version  : 21.0223
    @author   : zhangpeng96
    @time     : 22'00"
    @accepted : all
"""

def judge(n, arr, vertex):
    if arr[0] != arr[-1] or n != (vertex+1) or len(set(arr)) != vertex:
        return False
    for v1, v2 in zip(arr[:-1], arr[1:]):
        if not graph[v1][v2]: return False
    return True


vertex_n, edge_n = map(int, input().split())

graph = [ [False]*(vertex_n+1) for _ in range(vertex_n+1) ]  

for _ in range(edge_n):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

for _ in range(int(input())):
    n, *arr = map(int, input().split())
    if judge(n, arr, vertex_n):
        print('YES')
    else:
        print('NO')
