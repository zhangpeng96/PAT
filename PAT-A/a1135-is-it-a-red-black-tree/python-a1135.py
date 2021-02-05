"""
    @name     : a1135
    @version  : 21.0205
    @author   : zhangpeng96
    @time     : 27'18"
    @accepted : all
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    # def __repr__(self):
    #     return ' ({}>{}<{}) '.format(self.left, self.val, self.right)

class RedBlackTree():
    def insert(self, root, val):
        if root == None:
            root = Node(val)
        elif abs(val) < abs(root.val):
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def black_height(self, root):
        if root == None: return 0
        left_h = self.black_height(root.left)
        right_h = self.black_height(root.right)
        if root.val > 0:
            return max(left_h, right_h) + 1
        else:
            return max(left_h, right_h)

    def root_is_black(self, root):
        if root.val > 0: return True

    def black_is_balanced(self, root):
        if root == None: return True
        left_black = self.black_height(root.left)
        right_black = self.black_height(root.right)
        if left_black != right_black:
            return False
        else:
            return self.black_is_balanced(root.left) and self.black_is_balanced(root.right)

    def no_adjacent_red(self, root):
        if root == None: return True
        if root.val < 0:
            if root.left != None and root.left.val < 0: return False
            if root.right != None and root.right.val < 0: return False
        return self.no_adjacent_red(root.left) and self.no_adjacent_red(root.right)


count = int(input())

for _ in range(count):
    length = int(input())
    sequence = map(int, input().split())
    tree = None
    rbt = RedBlackTree()
    for val in sequence:
        tree = rbt.insert(tree, val)

    # print(tree)
    if rbt.root_is_black(tree) and rbt.black_is_balanced(tree) and rbt.no_adjacent_red(tree):
        print('Yes')
    else:
        print('No')
