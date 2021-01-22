"""
    @name     : a1099
    @version  : 21.0122
    @author   : zhangpeng96
    @time     : 35'40"
    @accepted : all
"""

class BTNode:
    def __init__(self):
        self.val = None
        self.left = -1
        self.right = -1

class BST():
    def in_order_insert(self, root, nodes, it):
        if root == -1: return
        self.in_order_insert(nodes[root].left, nodes, it)
        nodes[root].val = next(it)
        self.in_order_insert(nodes[root].right, nodes, it)

    def level_order(self, root, nodes, lst):
        if root == -1: return
        queue = []
        queue.append(nodes[root])
        while queue:
            node = queue.pop(0)
            lst.append(node.val)
            if node.left != -1:
                queue.append(nodes[node.left])
            if node.right != -1:
                queue.append(nodes[node.right])


# ptr = ['1 6','2 3','-1 -1','-1 4','5 -1','-1 -1','7 -1','-1 8','-1 -1']
# seq = list(map(int, '73 45 11 58 82 25 67 38 42'.split()))

count = int(input())
nodes = [ BTNode() for _ in range(count) ]

for i in range(count):
    left, right = map(int, input().split())
    nodes[i].left = left
    nodes[i].right = right

seq = list(map(int, input().split()))
seq.sort()

bt = BST()
bt.in_order_insert(0, nodes, iter(seq))

result = []
bt.level_order(0, nodes, result)
print(' '.join(map(str, result)))
