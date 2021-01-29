"""
    @name     : a1119
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 22'00"
    @accepted : all
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def create(preLeft, preRight, postLeft, postRight):
    if preLeft == preRight:
        return Node(pre_order[preLeft])
    if pre_order[preLeft] == post_order[postRight]:
        i = preLeft + 1
        while i <= preRight and pre_order[i] != post_order[postRight-1]:
            i += 1
        leftTree = i - preLeft - 1
        if i - preLeft > 1:
            node = Node()
            node.left = create(preLeft + 1, i - 1, postLeft, postLeft + leftTree - 1)
        else:
            global unique
            unique = False
            node = Node()
    node.val = post_order[postRight]
    node.right = create(i, preRight, postLeft + leftTree, postRight - 1)
    return node

def in_order(root, lst):
    if root == None: return
    in_order(root.left, lst)
    lst.append(root.val)
    in_order(root.right, lst)


count = int(input())
pre_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

unique = True
in_order_traversal = []
bt = create(0, count-1, 0, count-1)
in_order(bt, in_order_traversal)
if unique:
    print('Yes')
else:
    print('No')
print(' '.join(map(str, in_order_traversal)))
