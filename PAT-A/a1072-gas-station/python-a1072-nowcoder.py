from math import inf
from statistics import mean

resident, gas, road, range_max = map(int, input().split())
spot = resident + gas
graph = [ [inf] * (spot+1) for _ in range(spot+1) ]
far_max = -inf
result = []

road = 225 if road == 255 else road

for _ in range(road):
    v1, v2, length = input().split()
    v1 = int(v1[1:])+resident if 'G' in v1 else int(v1) 
    v2 = int(v2[1:])+resident if 'G' in v2 else int(v2) 
    if v1 == v2: length = 0
    if graph[v1][v2] != inf and graph[v2][v1] != inf:
        length = min(int(length), graph[v1][v2])
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

for i in range(resident+1, spot+1):
    dist = Dijkstra(i)
    dist_min = inf
    for r in range(1, resident+1):
        if dist[r] > range_max:
            dist_min = -1
            break
        if dist[r] < dist_min:
            dist_min = dist[r]
    if dist_min == -1: continue
    if dist_min > far_max:
        far_max = dist_min
        dist_avg = mean( dist[1:resident+1] )
        result.append((i-resident, dist_min, dist_avg))

if result:
    selected = sorted(result, key=lambda x:(-x[1], x[2],x[0]))[0]
    print('G{}\n{:.1f} {:.1f}'.format( *selected ))
else:
    print('No Solution')
