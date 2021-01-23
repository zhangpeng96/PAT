
class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
    def __repr__(self):
        return '{}({}, {})'.format(self.val, self.left, self.right)

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


def create(postL, postR, inL, inR):
    if postL > postR: return None
    k = inL
    root = Node()
    root.val = post_order[postR]
    while k < inR and in_order[k] != post_order[postR]:
        k += 1
    pos = k - inL
    root.left = create(postL, postL+pos-1, inL, k-1)
    root.right = create(postL+pos, postR-1, k+1, inR)
    print(root)
    return root

def create2(root, start, end):
    if start > end: return None
    k = start
    while k < end and in_order[k] != post_order[root]:
        k += 1
    node = Node()
    node.val = post_order[root]
    node.left = create2(root-1-end+k, start, k-1)
    node.right = create2(root-1, k+1, end)
    print(node)
    return node


post_order = [3, 4, 2, 6, 5, 1]
in_order = [3, 2, 4, 1, 6, 5]

tree = create(0, 5, 0, 5)
# print(tree.val)
tree = create2(5, 0, 5)

# level_traversal = []
# level_order(tree, level_traversal)
# print(level_traversal)
