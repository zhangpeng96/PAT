"""
    @name     : a1130
    @version  : 21.0128（数组形式存储二叉树）
    @author   : zhangpeng96
    @time     : 30'00"
    @accepted : all
"""

def insert(root, node, index):
    left, right = node[index][1:]
    if left != -1:
        root.left = BTNode(node[node[index-1][1]-1][0])
        root.left = insert(root.left, node, node[index-1][1])
    if node[index-1][2] != -1:
        root.right = BTNode(node[node[index-1][2]-1][0])
        root.right = insert(root.right, node, node[index-1][2])
    return root

def in_order(root, nodes, lst, depth):
    if root == -1: return
    val, left, right = nodes[root]
    if depth and (left != -1 or right != -1): lst.append('(')
    in_order(left, nodes, lst, depth+1)
    lst.append(val)
    in_order(right, nodes, lst, depth+1)
    if depth and (left != -1 or right != -1): lst.append(')')

def find_root(nodes):
    pool = set([i+1 for i in range(len(nodes))])
    for node in nodes:
        pool -= set(node[1:])
    return pool.pop()


nodes, traversal = [], []

count = int(input())
for _ in range(count):
    val, left, right = input().split()
    left, right = int(left), right
    nodes.append((val, int(left), int(right)))

root = find_root(nodes)
nodes.insert(0, None)   # 题目中给出的树节点都是从1开始标号的

in_order(root, nodes, traversal, 0)
print(''.join(traversal))

# 测试点2只有一个元素
