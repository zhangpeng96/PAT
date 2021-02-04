"""
    @name     : a1127
    @version  : 21.0204
    @author   : zhangpeng96
    @time     : 55'00"
    @accepted : all
"""

class Node:
    def __init__(self, val=None):
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
    queue.append([root, 0])
    while queue:
        node, depth = queue.pop(0)
        lst[depth] = lst.get(depth, []) + [node.val]
        if node.left:
            queue.append([node.left, depth+1])
        if node.right:
            queue.append([node.right, depth+1])


count = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

order, result = {}, []
bt = create(count-1, 0, count-1)
level_order(bt, order)

for depth, level in order.items():
    if depth % 2:
        result.extend(level)
    else:
        result.extend(level[::-1])

print(' '.join(map(str, result)))
