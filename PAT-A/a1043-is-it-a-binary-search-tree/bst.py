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

    def in_order(self, root, lst):
        if root == None: return
        self.in_order(root.left, lst)
        lst.append(root.val)
        self.in_order(root.right, lst)

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

    def level_order(self, root, lst):
        # equal to BFS
        # https://github.com/sagar2460/LevelOrder_Traversal/blob/master/LevelOrder_Traversal.py
        # https://github.com/EchoLLLiu/DataStructure/blob/master/ch04tree/BinaryTree.py
        if root == None: return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            lst.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def level_order2(self, root, lst):
        from queue import Queue
        if root == None: return
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            lst.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

    def dfs(self, root, lst):
        if root == None: return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            lst.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

bst = BST()
tree = None

sequence = [8, 10, 11, 8, 6, 7, 5]
for val in sequence:
    tree = bst.insert(tree, val)

traversal_in_order = []
bst.in_order(tree, traversal_in_order)
print(traversal_in_order)

traversal_level_order = []
bst.level_order(tree, traversal_level_order)
print(traversal_level_order)

traversal_dfs = []
bst.dfs(tree, traversal_dfs)
print(traversal_dfs)

traversal_pre_order = []
bst.pre_order(tree, traversal_pre_order)
print(traversal_pre_order)