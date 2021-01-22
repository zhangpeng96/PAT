"""
    @name     : a1004
    @version  : 21.0122
    @author   : zhangpeng96
    @time     : 30'00"
    @accepted : all
"""

class Node:
    def __init__(self, child=[]):
        self.child = child

def dfs(root, nodes, depth):
    if not nodes.get(root):
        nodes[root] = Node()
    if not nodes[root].child:
        layer[depth] = layer.get(depth, 0) + 1
        return 
    for child in nodes[root].child:
        if not layer.get(depth):
            layer[depth] = 0
        dfs(child, nodes, depth+1)


n, m = map(int, input().split())
nodes = {}
layer = {}
root = '01'

for _ in range(m):
    name, _, *children = input().split()
    nodes[name] = Node(children)

dfs(root, nodes, 0)
print( ' '.join( map(lambda x:str(x[1]), sorted(layer.items(), key=lambda x:x[0])) ))
