"""
    @name     : a1138
    @version  : 21.0203
    @author   : zhangpeng96
    @time     : 15'00"
    @accepted : p4,p5 timeout
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create(root, start, end):
    if start > end: return None
    i = start
    while i < end and in_order[i] != pre_order[root]:
        i += 1
    node = Node(pre_order[root])
    node.left = create(root+1, start, i-1)
    node.right = create(root+1+(i-start), i+1, end)
    return node

def post_order(root, lst):
    if root == None: return
    post_order(root.left, lst)
    post_order(root.right, lst)
    lst.append(root.val)



count = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))

post_traversal = []
bt = create(0, 0, count-1)
post_order(bt, post_traversal)

print(post_traversal[0])
# print(' '.join(map(str, post_traversal)))
