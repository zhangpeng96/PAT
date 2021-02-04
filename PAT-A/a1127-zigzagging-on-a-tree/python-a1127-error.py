
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        return '({}=>{}<={}); '.format(self.left, self.val, self.right)

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
        lst.append(node.val)
        if depth % 2:
            if node.right:
                queue.append([node.right, depth+1])
            if node.left:
                queue.append([node.left, depth+1])
        else:
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])


count = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

level_traversal = []
bt = create(count-1, 0, count-1)
level_order(bt, level_traversal)

print(level_traversal)

# print(' '.join(map(str, level_traversal)))
