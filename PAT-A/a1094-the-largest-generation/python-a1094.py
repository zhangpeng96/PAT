"""
    @name     : a1094
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 6'18"
    @accepted : all
"""

class Node:
    def __init__(self, child=[]):
        self.child = child

def dfs(root, nodes, depth):
    layer[depth] = layer.get(depth, 0) + 1
    if not nodes[root].child:
        return 
    for child in nodes[root].child:
        dfs(child, nodes, depth+1)


n, m = map(int, input().split())
root = int('01')
layer = {}
nodes = dict(zip( [i+1 for i in range(n)], [ Node() for _ in range(n) ]))

for _ in range(m):
    name, _, *children = map(int, input().split())
    nodes[name] = Node(children)

dfs(root, nodes, 1)

level, number = sorted(layer.items(), key=lambda x:x[1])[-1]
print(number, level)

