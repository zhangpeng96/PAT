"""
    @name     : a1130
    @version  : 21.0120.2（递归建树，中序遍历输出）
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

class BTNode:
    def __init__(self, tup):
        val, left, right = tup
        self.val = val
        self.left = left
        self.right = right

class BT():
    def insert(self, root, node, index):
        left, right = node[index][1:]
        if left != -1:
            root.left = BTNode(node[left])
            root.left = self.insert(root.left, node, left)
        if right != -1:
            root.right = BTNode(node[right])
            root.right = self.insert(root.right, node, right)
        return root

    def in_order(self, root, lst, depth):
        if root == -1: return
        if depth and (root.left != -1 or root.right != -1): lst.append('(')
        self.in_order(root.left, lst, depth+1)
        lst.append(root.val)
        self.in_order(root.right, lst, depth+1)
        if depth and (root.left != -1 or root.right != -1): lst.append(')')

def find_root(nodes):
    pool = set([i+1 for i in range(len(nodes))])
    for node in nodes:
        pool -= set(node[1:])
    return pool.pop()


nodes = []
result = []

# ins = ['* 8 7','a -1 -1','* 4 1','+ 2 5','b -1 -1','d -1 -1','- -1 6','c -1 -1']
# ins = ['2.35 -1 -1','* 6 1','- -1 4','% 7 8','+ 2 3','a -1 -1','str -1 -1','871 -1 -1']
# for node in ins:
#     val, left, right = node.split()
#     nodes.append((val, int(left), int(right)))

count = int(input())
for _ in range(count):
    val, left, right = input().split()
    nodes.append((val, int(left), int(right)))

head = find_root(nodes)
nodes.insert(0, head)

bt = BT()
tree = BTNode(nodes[head])

bt.insert(tree, nodes, head)
bt.in_order(tree, result, 0)
print(''.join(result))
