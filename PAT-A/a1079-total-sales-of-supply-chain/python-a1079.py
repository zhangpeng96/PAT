"""
    @name     : a1079
    @version  : 21.0220
    @author   : zhangpeng96
    @time     : 23'15"
    @accepted : p2,p3,p6 timeout
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def dfs(root, nodes, depth):
    if not nodes[root]:
        retailer[root] = [depth, sales[root]]
        return
    for node in nodes[root]:
        dfs(node, nodes, depth+1)


count, price, rate = input().split()
count, price, rate = int(count), float(price), 1+(float(rate)/100)

nodes, sales = [], {}
retailer = defaultdict(int)

for i, line in enumerate(sys.stdin.readlines()):
    no_leaf, *child = map(int, line.split())
    if no_leaf:
        nodes.append(child)
    else:
        nodes.append([])
        sales[i] = child[0]

dfs(0, nodes, 0)

amount = sum([ (price*rate**depth) * sale for depth, sale in retailer.values() ])
print('{:.1f}'.format(amount))
