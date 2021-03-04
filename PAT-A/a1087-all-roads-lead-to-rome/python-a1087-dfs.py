"""
    @name     : a1087
    @version  : 21.0304 纯DFS版本
    @author   : zhangpeng96
    @time     : 42'36"
    @accepted : all
"""

from collections import defaultdict
from copy import deepcopy
from math import inf

happy = defaultdict(int)
graph = defaultdict(list)
visited = defaultdict(bool)

cities, routes, start = input().split()
cities, routes = int(cities), int(routes)

for _ in range(cities-1):
    city, value = input().split()
    happy[city] = int(value)

for _ in range(routes):
    city1, city2, cost = input().split()
    graph[city1].append( (city2, int(cost)) )
    graph[city2].append( (city1, int(cost)) )

best = {
    'cost': inf,
    'happy': -inf,
    'count': 0,
    'path': []
}

def dfs(root, temp_cost, temp_happy, temp_path):
    if root == 'ROM':
        # 路径优先级：花费最少>幸福值最大>城市平均幸福值最大
        if temp_cost < best['cost']:
            best['count'] = 1
            best['cost'] = temp_cost
            best['happy'] = temp_happy
            best['path'] = deepcopy(temp_path)
        elif temp_cost == best['cost']:
            best['count'] += 1
            if temp_happy > best['happy']:
                best['happy'] = temp_happy
                best['path'] = deepcopy(temp_path)
            elif temp_happy == best['happy']:
                if len(temp_path) < len(best['path']):
                    best['path'] = deepcopy(temp_path)

    for city, cost in graph[root]:
        if not visited[city]:
            visited[city] = True
            temp_path.append(city)
            dfs(city, cost + temp_cost, happy[city] + temp_happy, temp_path)
            visited[city] = False
            temp_path.pop()


dfs(start, 0, 0, [])

happy_avg = best['happy'] // len(best['path'])
print('{count} {cost} {happy} {avg}'.format(**best, avg=happy_avg))
print('->'.join([start] + best['path']))
