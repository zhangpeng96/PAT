"""
    @name     : a1072
    @version  : 21.0304
    @author   : zhangpeng96
    @time     : 56'12"
    @accepted : p4 timeout
"""

from math import inf
from statistics import mean


resident, gas, road, range_max = map(int, input().split())
spot = resident + gas
graph = [ [inf] * (spot+1) for _ in range(spot+1) ]
result, far_max, avg_min = 0, -inf, 0

for _ in range(road):
    v1, v2, length = input().split()
    v1 = int(v1[1:])+resident if v1[0] == 'G' else int(v1)
    v2 = int(v2[1:])+resident if v2[0] == 'G' else int(v2)
    graph[v1][v2] = graph[v2][v1] = int(length)

def Dijkstra(source):
    dist, collected = [inf] * (spot+1), [False] * (spot+1)
    dist[source] = 0
    while True:
        v, dist_min = -1, inf
        for i in range(1, spot+1):
            if not collected[i] and dist[i] < dist_min:
                v = i
                dist_min = dist[i]
        if v == -1: break
        collected[v] = True

        for w in range(1, spot+1):
            if graph[v][w] != inf and not collected[w]:
                if dist[v] + graph[v][w] < dist[w]:
                    dist[w] = dist[v] + graph[v][w]
    return dist

# 假定选择每个待选的加油站位置，求加油站到各个居民点的距离
for i in range(resident+1, spot+1):
    dist = Dijkstra(i)
    dist_min = inf
    for r in range(1, resident+1):
        # 遍历每个居民，注意是居民，只要有居民点超过距离，这个加油位置就不能选
        if dist[r] > range_max:
            dist_min = -1
            break
        if dist[r] < dist_min:
            dist_min = dist[r]
    if dist_min == -1: continue
    dist_avg = mean( dist[1:resident+1] )
    if dist_min > far_max or (dist_min == far_max and dist_avg < avg_min):
        result = i - resident
        far_max = dist_min
        avg_min = dist_avg

if result:
    print('G{}\n{:.1f} {:.1f}'.format( result, far_max, avg_min ))
else:
    print('No Solution')
