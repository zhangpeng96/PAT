'''
    @name      : a1115
    @version   : 21.0119
    @author    : zhangpeng96
    @test_time : 50'00"
    @pass_rate : p5 failed
'''

import sys
sys.setrecursionlimit(8000)

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():
    def insert(self, root, val):
        if root == None:
            root = BTNode(val)
        elif val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

def dfs(root, depth):
    if root == None:
        return
    node_count[depth] = node_count.get(depth, 0) + 1
    dfs(root.left, depth + 1)
    dfs(root.right, depth + 1)


count = int(input())
ins = map(int, input().split())
# ins = map(int, '25 30 42 16 20 20 35 -5 28'.split())
tree = None
node_count = {}
bt = BST()
for node in ins:
    tree = bt.insert(tree, node)

dfs(tree, 1)

res = sorted(node_count.items(), key=lambda x:-x[0])
n1, n2 = res[0][1], res[1][1]

print('{} + {} = {}'.format(n1, n2, n1+n2))
