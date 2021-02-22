"""
    @name     : a1021
    @version  : 21.0222
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p3 timeout
"""

from sys import stdin
from collections import defaultdict

def dfs1(root, visited):
    for node in tree[root]:
        if not visited[node]:
            visited[node] = True
            dfs1(node, visited)

def find_component(nodes):
    count = 0
    visited = defaultdict(bool)
    for node in nodes:
        if not visited[node]:
            count += 1
            visited[node] = True
            dfs1(node, visited)
    return count

def dfs2(root, depth, visited):
    if depth > depths['max']:
        depths['max'] = depth
    for node in tree[root]:
        if not visited[node]:
            visited[node] = True
            dfs2(node, depth+1, visited)

def find_depth(nodes):
    depth = defaultdict(list)
    for node in nodes:
        depths['max'] = 0
        visited = defaultdict(bool)
        visited[node] = True     
        dfs2(node, 0, visited)
        depth[ depths['max'] ].append(node)
    return depth


count = int(input())
tree = defaultdict(list)
nodes = list(range(1, count+1))
depths = {'max': 0}

for line in readlines():
    node1, node2 = map(int, line.split())
    tree[node1].append(node2)
    tree[node2].append(node1)

component = find_component(nodes)
if component == 1:
    path = find_depth(nodes)
    for p in path[ max(path.keys()) ]:
        print(p)
else:
    print('Error: {} components'.format(component))
