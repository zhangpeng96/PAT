"""
    @name     : a1131
    @version  : 21.0309.2
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
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
    count, pre_line = 0, 0
    for (a, b) in pair_wise(path):
        if line[a, b] != pre_line:
            count += 1
            pre_line = line[a, b]
    return count

def dfs(root, station, temp_path):
    if station > mini.station:
        return
    if root == end:
        if station < mini.station:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        elif station == mini.station and find_transfer(temp_path) < mini.transfer:
            mini.station = station
            mini.transfer = find_transfer(temp_path)
            mini.path = copy(temp_path)
        return
    for child in adj[root]:
        if not visit[child]:
            visit[child] = True
            temp_path.append(child)
            dfs(child, station+1, temp_path)
            visit[child] = False
            temp_path.pop()

def print_path(path):
    # 先把首站看成换乘站，线路初始化为0，也就是只要走就算换线路
    line1, stop_end, transfer = 0, path[-1], path[0]
    for stop1, stop2 in pair_wise(path):
        line2 = line[stop1, stop2]
        # 如果A到B走的线路与之前不同，那么说明A为换乘站（B还没走怎么知道换不换）
        if line2 != line1:
            if line1:   # 从O点开始第1步必然没有换线，所以忽略
                print('Take Line#{} from {:04} to {:04}.'.format(line1, transfer, stop1))
            line1, transfer = line2, stop1
    print('Take Line#{} from {:04} to {:04}.'.format(line1, transfer, stop_end))


adj = defaultdict(list)
line = defaultdict(int)
visit = defaultdict(bool)

for i in range(int(input())):
    station = map(int, input().split()[1:])
    for a, b in pair_wise(station):
        adj[a].append(b)
        adj[b].append(a)
        line[a, b] = line[b, a] = i + 1

for i in range(int(input())):
    mini = SimpleNamespace(station=inf, transfer=inf, path=[])
    start, end = map(int, input().split())
    visit[start] = True
    dfs(start, 0, [start])
    visit[start] = False
    print(mini.station)
    print_path(mini.path)
