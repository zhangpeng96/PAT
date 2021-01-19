"""
    @name     : a1130
    @version  : 21.0119（递归建树，中序遍历输出）
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT():
    def insert(self, root, node, index):
        val, left, right = node[index][0], node[index][1], node[index][2]
        if left != -1:
            root.left = BTNode(node[left][0])
            root.left = self.insert(root.left, node, left)
        if right != -1:
            root.right = BTNode(node[right][0])
            root.right = self.insert(root.right, node, right)
        return root

    def in_order(self, root, lst, depth):
        if root == None: return
        if depth and (root.left or root.right): lst.append('(')
        self.in_order(root.left, lst, depth+1)
        lst.append(root.val)
        self.in_order(root.right, lst, depth+1)
        if depth and (root.left or root.right): lst.append(')')

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
tree = BTNode(nodes[head][0])
bt.insert(tree, nodes, head)
bt.in_order(tree, result, 0)
print(''.join(result))
