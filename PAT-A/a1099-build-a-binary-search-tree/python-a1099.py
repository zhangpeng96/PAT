
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


bt = BST()
# tree = None

# for val in seq:
#     tree = bt.insert(tree, val)
count = int('9')
nodes = [ BTNode() for _ in range(count) ]
ptr = ['1 6','2 3','-1 -1','-1 4','5 -1','-1 -1','7 -1','-1 8','-1 -1']

for i in range(count):
    left, right = map(int, ptr[i].split())
    nodes[i].left = left
    nodes[i].right = right

seq = list(map(int, '73 45 11 58 82 25 67 38 42'.split()))
seq.sort()
bt.in_order_insert(0, nodes, iter(seq))
level_traversal = []
bt.level_order(0, nodes, level_traversal)
print(level_traversal)
for n in nodes:
    print(n.val)

