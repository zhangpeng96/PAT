"""
    @name     : a1053
    @version  : 21.0224
    @author   : zhangpeng96
    @time     : 40'35"
    @accepted : all
"""

class Node():
    def __init__(self, val):
        self.weight = val
        self.children = []

def dfs(root, amount):
    if amount == aim:
        if tree[root].children:
            return
        path.append(tuple(temp))
    if root >= count or amount > aim:
        return
    for uid in tree[root].children:
        temp.append(tree[uid].weight)
        dfs(uid, amount + tree[uid].weight)
        temp.pop()


count, non_leaf, aim = map(int, input().split())
tree = [ Node(int(uid)) for uid in input().split() ]
path = []

for _ in range(non_leaf):
    uid, _, *child = map(int, input().split())
    tree[uid].children = child

root = tree[0]
temp = [root.weight]
dfs(0, root.weight)

for path in sorted(path, reverse=True):
    print(*path)
