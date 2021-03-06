"""
    @name     : a1018
    @version  : 21.0306
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

from math import inf
from types import SimpleNamespace


bike = [0]
capcaity, stations, problems, roads = map(int, input().split())
for i in map(int, input().split()):
    bike.append(i - capcaity//2)

spot = stations + 1
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


def dfs(v, temp_path):
    temp_path.append(v)
    if v == 0:
        need, back = 0, 0
        for i in temp_path[::-1]:
            # 当车站的存车过多时，归还多余的车
            if bike[i] > 0:
                back += bike[i]
            # 当车站的存车不足时，补充车
            else:
                # 如果归还的车足够补充，则取走要归还的车
                if back > 0 - bike[i]:
                    back += bike[i]
                # 如果归还的车不够补充，归还的车除了都用来补充外，再从管理处拿车补充
                else:
                    # 注意顺序，先调用back，再清空back
                    need += (0 - bike[i] - back)
                    back = 0
        # 条件判断
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
        dfs(u, temp_path)
    temp_path.pop()


pre = Dijkstra(0)
dfs(problems, [])
print(mini.need, '->'.join(map(str, mini.path)), mini.back)
