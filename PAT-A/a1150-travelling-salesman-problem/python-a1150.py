"""
    @name     : a1150
    @version  : 21.0224
    @author   : zhangpeng96
    @time     : 56'18"
    @accepted : all
    @source   : https://blog.csdn.net/acm_zh/article/details/86505609
"""

from collections import defaultdict

matrix = defaultdict(int)
travel_plan = []
vertex, edge = map(int, input().split())

for _ in range(edge):
    city1, city2, dist = map(int, input().split())
    matrix[city1, city2] = matrix[city2, city1] = dist

for i in range(1, int(input())+1):
    length, *arr = map(int, input().split())
    visited, destination = [0] * vertex, 0
    for city in arr:
        visited[city-1] += 1
    all_visited, all_connected = all(visited), True
    head_tail = True if arr[0] == arr[-1] else False

    for curr, rear in zip(arr[:-1], arr[1:]):
        dist = matrix[curr, rear]
        if not dist: all_connected = False
        destination += dist

    if all_connected:
        if all_visited and head_tail:
            travel_plan.append( (i, destination) )

        if all_visited and head_tail and length == vertex+1:
            print('Path {}: {} (TS simple cycle)'.format(i, destination))
        elif all_visited and head_tail and length != vertex+1:
            print('Path {}: {} (TS cycle)'.format(i, destination))
        elif not all_visited or not head_tail:
            print('Path {}: {} (Not a TS cycle)'.format(i, destination))
    else:
        print('Path {}: NA (Not a TS cycle)'.format(i))

print('Shortest Dist({}) = {}'.format(*sorted(travel_plan, key=lambda x:x[1])[0]))
