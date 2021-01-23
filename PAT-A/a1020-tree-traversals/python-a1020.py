"""
    @name     : a1020
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create(root, start, end):
    if start > end: return None
    i = start
    while i < end and in_order[i] != post_order[root]:
        i += 1
    node = Node(post_order[root])
    node.left = create(root-(end-i)-1, start, i-1)
    node.right = create(root-1, i+1, end)
    return node

def level_order(root, lst):
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


count = int(input())
post_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))

level_traversal = []
bt = create(count-1, 0, count-1)
level_order(bt, level_traversal)
print(' '.join(map(str, level_traversal)))
