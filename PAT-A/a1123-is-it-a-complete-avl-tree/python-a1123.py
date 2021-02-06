"""
    @name     : a1123
    @version  : 21.0206
    @author   : zhangpeng96
    @time     : 37'42"
    @accepted : all
    @desc     : a1066和a1110问题的综合
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    # def __repr__(self):
    #     return ' ({}>{}<{}) '.format(self.left, self.val, self.right)

class AVLTree():
    def rotateLeft(self, a):
        b = a.left
        a.left = b.right
        b.right = a
        return b

    def rotateRight(self, a):
        b = a.right
        a.right = b.left
        b.left = a
        return b

    def rotateLeftRight(self, a):
        a.left = self.rotateRight(a.left)
        return self.rotateLeft(a)

    def rotateRightLeft(self, a):
        a.right = self.rotateLeft(a.right)
        return self.rotateRight(a)

    def height(self, root):
        if root == None: return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        return max(left_h, right_h) + 1

    def balance_factor(self, root):
        left = self.height(root.left)
        right = self.height(root.right)
        return left - right

    def insert(self, root, val):
        if root == None:
            root = Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
            if self.balance_factor(root) > 1:
                if val < root.left.val:
                    root = self.rotateLeft(root)
                else:
                    root = self.rotateLeftRight(root)
        else:
            root.right = self.insert(root.right, val)
            if self.balance_factor(root) < -1:
                if val > root.right.val:
                    root = self.rotateRight(root)
                else:
                    root = self.rotateRightLeft(root)
        return root

def level_order_complete(root, count, level_traversal):
    queue, complete = [], True
    queue.append(root)
    while count:
        node = queue.pop(0)
        if node == None:
            complete = False
            continue
        level_traversal.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
        count -= 1
    return complete


tree = None
avl = AVLTree()
level_traversal = []
# sequence = map(int, '88 70 61 96 120 90 65 68'.split())
count = int(input())
sequence = map(int, input().split())

for val in sequence:
    tree = avl.insert(tree, val)

is_complete = level_order_complete(tree, count, level_traversal)

if is_complete:
    print(' '.join(map(str, level_traversal)))
    print('YES')
else:
    print(' '.join(map(str, level_traversal)))
    print('NO')
