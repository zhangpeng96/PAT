from math import inf
from copy import copy
from types import SimpleNamespace
# from pprint import pprint as print

capcaity, stations, problems, roads = map(int, input().split())
perfect = capcaity // 2
bike = [0] + list(map(int, input().split()))

spot = stations + 1
# minimum = {'need': inf, 'back': inf}
mini = SimpleNamespace(need=inf, back=inf, path=[])
time = [ [inf] * spot for _ in range(spot) ]

for _ in range(roads):
    s1, s2, t = map(int, input().split())
    time[s1][s2] = time[s2][s1] = t


def Dijkstra(source):
    dist, collected = [inf] * spot,  [False] * spot
    pre = [ [] for _ in range(spot) ]
    dist[source] = 0

    while True:
        v, dist_min = -1, inf
        for i in range(spot):
            if not collected[i] and dist[i] < dist_min:
                v = i
                dist_min = dist[i]
        if v == -1: break
        collected[v] = True

        for w in range(spot):
            if not collected[w] and time[v][w] != inf:
                if dist[w] > dist[v] + time[v][w]:
                    dist[w] = dist[v] + time[v][w]
                    pre[w] = []
                    pre[w].append(v)
                elif dist[w] == dist[v] + time[v][w]:
                    pre[w].append(v)
    return pre


def dfs(v, temp_path, pre):
    temp_path.append(v)
    if v == 0:
        need, back = 0, 0
        for i in temp_path[::-1]:
            # 当车站的存车过多时，归还多余的车
            if bike[i] > perfect:
                back += (bike[i] - perfect)
            # 当车站的存车不足时，补充车
            else:
                # 如果归还的车足够补充，则取走要归还的车
                if back > perfect - bike[i]:
                    back -= (perfect - bike[i])
                # 如果归还的车不够补充，归还的车除了都用来补充外，再从管理处拿车补充
                else:
                    # 注意顺序，先调用back，再清空back
                    print(bike[i], back, need)
                    need += (perfect - bike[i] - back)
                    back = 0

        if need < mini.need:
            mini.need = need
            mini.back = back
            mini.path = temp_path[::-1]
        elif need == mini.need and back < mini.back:
            mini.back = back
            mini.path = temp_path[::-1]
        temp_path.pop()
        return
    # 遍历所有可能性
    for u in pre[v]:
        dfs(u, temp_path, pre)
    temp_path.pop()



pre = Dijkstra(0)
print(pre)
dfs(problems, [], pre)

print(mini.need, '->'.join(map(str, mini.path)), mini.back)

print(mini)
