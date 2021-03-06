"""
    @name     : a1030
    @version  : 21.0306
    @author   : zhangpeng96
    @time     : 50'00"
    @accepted : all
"""

from math import inf

cities, highways, start, goal = map(int, input().split())
costing = [ [inf]* cities for _ in range(cities) ]
distance = [ [inf]* cities for _ in range(cities) ]

for _ in range(highways):
    city1, city2, ds, cs = map(int, input().split())
    distance[city1][city2] = distance[city2][city1] = ds
    costing[city1][city2] = costing[city2][city1] = cs

def Dijkstra(source):
    collected = [False] * cities
    dist, cost, pre = [inf] * cities, [inf] * cities, [0] * cities
    dist[source], cost[source], pre[source] = 0, 0, source

    while True:
        v, dist_min = -1, inf
        for i in range(cities):
            if not collected[i] and dist[i] < dist_min:
                v = i
                dist_min = dist[i]
        if v == -1: break
        collected[v] = True

        for w in range(cities):
            if not collected[w] and distance[v][w] != inf:
                if dist[v] + distance[v][w] < dist[w]:
                    dist[w] = dist[v] + distance[v][w]
                    cost[w] = cost[v] + costing[v][w]
                    pre[w] = v
                elif dist[v] + distance[v][w] == dist[w]:
                    if cost[v] + costing[v][w] < cost[w]:
                        cost[w] = cost[v] + costing[v][w]
                        pre[w] = v
    return dist, cost, pre

def find_path(pre, start, goal):
    path = [goal]
    while start != pre[goal]:
        goal = pre[goal]
        path.append(goal)
    path += [start]
    return path[::-1]

dist, cost, pre = Dijkstra(start)
path = find_path(pre, start, goal)

print(*path, dist[goal], cost[goal])
