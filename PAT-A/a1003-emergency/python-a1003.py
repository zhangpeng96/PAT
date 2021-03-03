"""
    @name     : a1003
    @version  : 21.0303
    @author   : zhangpeng96
    @time     : 56'67"
    @accepted : all
"""

from math import inf

vertex, edge, start, end = map(int, input().split())
rescue = list(map(int, input().split()))
graph = [ [inf] * vertex for _ in range(vertex) ]

for _ in range(edge):
    v1, v2, length = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = length


# Dijkstra
dist, collected = [inf] * vertex, [False] * vertex
team = [0] * vertex
count = [0] * vertex

dist[start] = 0
team[start], count[start] = rescue[start], 1

while True:
    v, dist_min = -1, inf
    for i in range(vertex):
        # 整个Dijkstra算法的跳出条件是所有点被收录
        if not collected[i] and dist[i] < dist_min:
            v = i
            dist_min = dist[i]
    if v == -1: break
    collected[v] = True

    for w in range(vertex):
        if graph[v][w] != inf and not collected[w]:
            if dist[v] + graph[v][w] < dist[w]:
                dist[w] = dist[v] + graph[v][w]
                # 途中的两个点之间找到更短的，所以更短路径数不变（之前的点可能有多条等长都到v点，因此不能归1，要保持v点数目）Y
                count[w] = count[v]
                # 这里team更新是因为没得选择，必须带上
                team[w] = team[v] + rescue[w]

            elif dist[v] + graph[v][w] == dist[w]:
                # 路径等长，路径数累加，比如A到B已经有3条等长路，再有条等长的要累加
                count[w] += count[v]
                # 这里team有条件是因为有两条路径等长，可以选择team最多的
                if team[v] + rescue[w] > team[w]:
                    team[w] = team[v] + rescue[w]

print(count[end], team[end])
