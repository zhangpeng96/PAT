"""
    @name     : a1131
    @version  : 21.0307
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p1-p5 error, p3 timeout
"""

from math import inf
from copy import copy
from itertools import tee
from types import SimpleNamespace
from collections import defaultdict


def pair_wise(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)

def find_transfer(path):
    count = [ len(line[p]) - 1 for p in path ]
    return sum(count)

def dfs(root, station, temp_path):
    # 如果到达终点，判断该条路径最优条件
    if root == end:
        # 先优先选取经过站点最少的路径
        if station < mini.station:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        # 若经过站点数相同，则选择换乘站最少的路径
        elif station == mini.station and find_transfer(temp_path) < mini.transfer:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        return
    # 遍历邻接表
    for child in adj[root]:
        if not visit[child]:
            visit[child] = True
            temp_path.append(child)
            dfs(child, station+1, temp_path)
            visit[child] = False
            temp_path.pop()

def print_path(path):
    s1 = path[0]
    for i, s2 in enumerate(path, 1):
        if len(line[s2]) > 1 or i == len(path):
            name = line[s1] & line[s2]
            print('Take Line#{} from {} to {}.'.format(*name, s1, s2))
            s1 = s2


adj = defaultdict(list)
line = defaultdict(set)
visit = defaultdict(bool)

for i in range(int(input())):
    station = map(int, input().split()[1:])
    for a, b in pair_wise(station):
        adj[a].append(b)
        adj[b].append(a)
        line[a].add(i + 1)
    line[b].add(i + 1)

for i in range(int(input())):
    mini = SimpleNamespace(station=inf, transfer=inf, path=[])
    start, end = map(int, input().split())
    visit[start] = True
    dfs(start, 0, [start])
    visit[start] = False
    print(mini.station)
    print_path(mini.path)
