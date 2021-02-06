"""
    @name     : a1064
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 17'00"
    @accepted : all
"""

class BTNode:
    def __init__(self):
        self.val = None

class CBT():
    def in_order_insert(self, root, nodes, it):
        if root >= len(nodes): return
        self.in_order_insert(2*root+1, nodes, it)
        nodes[root].val = next(it)
        self.in_order_insert(2*root+2, nodes, it)

    def level_order(self, nodes):
        return [node.val for node in nodes]


# count = int('10')
# seq = list(map(int, '1 2 3 4 5 6 7 8 9 0'.split()))

count = int(input())
seq = list(map(int, input().split()))
seq.sort()
nodes = [ BTNode() for _ in range(count) ]
cbt = CBT()
cbt.in_order_insert(0, nodes, iter(seq))
print(' '.join(map(str, cbt.level_order(nodes))))
