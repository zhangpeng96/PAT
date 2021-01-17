"""
    @name     : a1043
    @version  : 21.0117
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p5 failed
"""

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def insert(self, root, val):
        if root == None:
            root = BTNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def pre_order(self, root, lst):
        if root == None: return
        lst.append(root.val)
        self.pre_order(root.left, lst)
        self.pre_order(root.right, lst)

    def post_order(self, root, lst):
        if root == None: return
        self.post_order(root.left, lst)
        self.post_order(root.right, lst)
        lst.append(root.val)

    def pre_order_mirror(self, root, lst):
        if root == None: return
        lst.append(root.val)
        self.pre_order_mirror(root.right, lst)
        self.pre_order_mirror(root.left, lst)

    def post_order_mirror(self, root, lst):
        if root == None: return
        self.post_order_mirror(root.right, lst)
        self.post_order_mirror(root.left, lst)
        lst.append(root.val)


count = int(input())
seq = list(map(int, input().split()))
# seq = [8, 6, 5, 7, 10, 8, 11]
# seq = [8, 10, 11, 8, 6, 7, 5]
# seq = [8, 6, 8, 5, 10, 9, 11]

bt = BST()
tree = None
pre_seq = []
pre_seq_mirror = []
post_seq = []

for val in seq:
    tree = bt.insert(tree, val)

bt.pre_order(tree, pre_seq)
bt.pre_order_mirror(tree, pre_seq_mirror)

if seq == pre_seq:
    bt.post_order(tree, post_seq)
    print('YES')
    print(' '.join(map(str, post_seq)))
elif seq == pre_seq_mirror:
    bt.post_order_mirror(tree, post_seq)
    print('YES')
    print(' '.join(map(str, post_seq)))
else:
    print('NO')
