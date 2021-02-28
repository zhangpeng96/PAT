"""
    @name     : a1013
    @version  : 21.0228
    @author   : zhangpeng96
    @time     : 45'00"
    @accepted : p2, p4 timeout
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(8000)

def dfs(v1, visited):
    visited[v1] = True
    for v2 in range(1,cities+1):
        if not visited[v2] and graph[v1, v2]:
            dfs(v2, visited)

def find_component(nodes, pre_visited):
    count = 0
    visited = defaultdict(bool)
    visited[pre_visited] = True
    for node in nodes:
        if not visited[node]:
            dfs(node, visited)
            count += 1
    return count


cities, highways, checked = map(int, input().split())
graph = defaultdict(bool)

for _ in range(highways):
    city1, city2 = map(int, input().split())
    graph[city1, city2] = True
    graph[city2, city1] = True


for city in map(int, input().split()):
    component_count = find_component(range(1,cities+1), city)
    print(component_count-1)
