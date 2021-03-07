"""
    @name     : a1111
    @version  : 21.0307
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p2-p4 timeout
"""

from math import inf


spot, street = map(int, input().split())
length = [ [inf]*spot for _ in range(spot) ]
time = [ [inf]*spot for _ in range(spot) ]
count = [ [1]*spot for _ in range(spot) ]

for _ in range(street):
    v1, v2, directed, t1, t2 = map(int, input().split())
    length[v1][v2] = t1
    time[v1][v2] = t2
    if not directed:
        length[v2][v1] = t1
        time[v2][v1] = t2

start, end = map(int, input().split())

def Dijkstra(source, graph, condition):
    dist, weight = [inf] * spot, [inf] * spot
    collected = [False] * spot
    pre = [ i for i in range(spot)]
    dist[source] = 0
    while True:
        v, dist_min = -1, inf
        for i in range(1, spot):
            if not collected[i] and dist[i] < dist_min:
                v = i
                dist_min = dist[i]
        if v == -1: break
        collected[v] = True

        for w in range(1, spot):
            if graph[v][w] != inf and not collected[w]:
                if dist[v] + graph[v][w] < dist[w]:
                    dist[w] = dist[v] + graph[v][w]
                    weight[w] = weight[v] + condition[v][w]
                    pre[w] = v
                elif dist[v] + graph[v][w] == dist[w] and weight[v] + condition[v][w] < weight[w]:
                    weight[w] = weight[v] + condition[v][w]
                    pre[w] = v
    return dist, pre

def get_path(path, start, end):
    res = [end]
    while path[end] != start:
        res.append(path[end])
        end = path[end]
    res.append(start)
    return res[::-1]

def parse_path(path):
    return ' -> '.join(map(str, path))

best_dist, path_dist = Dijkstra(start, length, time)
best_dist, path_dist = best_dist[end], get_path(path_dist, start, end)

best_time, path_time = Dijkstra(start, time, count)
best_time, path_time = best_time[end], get_path(path_time, start, end)

if path_dist == path_time:
    print('Distance = {}; Time = {}: {}'.format(best_dist, best_time, parse_path(path_dist)))
else:
    print('Distance = {}: {}'.format(best_dist, parse_path(path_dist)))
    print('Time = {}: {}'.format(best_time, parse_path(path_time)))
