"""
    @name     : a1102
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 26'19"
    @accepted : all
"""

class BTNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class BinaryTreeInvert():
    def in_order(self, root, nodes, lst):
        if root == -1: return
        self.in_order(nodes[root].right, nodes, lst)
        lst.append(root)
        self.in_order(nodes[root].left, nodes, lst)

    def level_order(self, root, nodes, lst):
        if root == -1: return
        queue = []
        queue.append(nodes[root])
        while queue:
            node = queue.pop(0)
            lst.append(nodes.index(node))
            if node.right != -1:
                queue.append(nodes[node.right])
            if node.left != -1:
                queue.append(nodes[node.left])

def print_int_list(lst):
    print( ' '.join(map(str, lst)) )


# count = int('8')
# ins = ['1 -','- -','0 -','2 7','- -','- -','5 -','4 6']

count = int(input())

nodes = []
pool = set([i for i in range(count)])
in_order_traversal, level_order_traversal = [], []

for _ in range(count):
    left, right = map(int, input().replace('-','-1').split())
    nodes.append(BTNode(left, right))
    pool -= set([left, right])

root = pool.pop()

bt = BinaryTreeInvert()
bt.level_order(root, nodes, level_order_traversal)
bt.in_order(root, nodes, in_order_traversal)

print_int_list(level_order_traversal)
print_int_list(in_order_traversal)
