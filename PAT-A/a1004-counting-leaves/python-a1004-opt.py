"""
    @name     : a1004
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 20'00"
    @accepted : all
    @desc     : 将输入的节点ID统一转换为整数，由于ID是从1递增排列，由
                节点总数可以先生成完整的树，以字典形式存储，优化代码
"""

class Node:
    def __init__(self, child=[]):
        self.child = child

def dfs(root, nodes, depth):
    layer[depth] = layer.get(depth, 0)
    if not nodes[root].child:
        layer[depth] += 1
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

dfs(root, nodes, 0)

print( ' '.join( map(lambda x:str(x[1]), sorted(layer.items()) ) ))
