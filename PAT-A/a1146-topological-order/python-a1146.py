"""
    @name     : a1146
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 34'50"
    @accepted : all
"""

from copy import copy

adj_list = {}
indegree = {}
wrong = []

vert, edge = map(int, input().split())

for _ in range(edge):
    v1, v2 = map(int, input().split())
    if v1 not in adj_list:
        adj_list[v1] = []
    adj_list[v1].append(v2)
    # 不要用if else形式，会漏掉else情况下初始化后插入元素
    indegree[v2] = indegree.get(v2, 0) + 1

query = int(input())

for option in range(query):
    degree = copy(indegree)
    seq = map(int, input().split())
    for v in seq:
        if degree.get(v, 0):
            wrong.append(option)
            break
        for a in adj_list.get(v, []):
        # 使用get而不要直接引用键名，因为建字典时没有初始化全部键值，键名不存在会报错
            degree[a] -= 1

print(' '.join(map(str, wrong)))
