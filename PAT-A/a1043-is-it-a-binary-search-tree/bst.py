# import sys
# sys.setrecursionlimit(8000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def insert(self, root, val):
        if root == None:
            root = Node(val)
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

    def mid_order(self, root, lst):
        if root == None: return
        self.mid_order(root.left, lst)
        lst.append(root.val)
        self.mid_order(root.right, lst)

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



bst = BST()
tree = None

sequence = [8, 10, 11, 8, 6, 7, 5]
for val in sequence:
    tree = bst.insert(tree, val)

traversal_mid_order = []
bst.mid_order(tree, traversal_mid_order)
print(traversal_mid_order)