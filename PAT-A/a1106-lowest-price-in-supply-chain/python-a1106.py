"""
    @name     : a1106
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 25'00"
    @accepted : p2,p3,p5,p6,p7 timeout
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(20000)

def dfs(root, nodes, depth):
    if not nodes[root]:
        retailer[depth] += 1
        return
    for node in nodes[root]:
        dfs(node, nodes, depth+1)


count, price, rate = input().split()
count, price, rate = int(count), float(price), 1+(float(rate)/100)

nodes = []
retailer = defaultdict(int)

for i in range(count):
    nodes.append( list(map(int, input().split()[1:])) )

dfs(0, nodes, 0)

depth, number = sorted(retailer.items())[0]
total = price * rate**depth
print('{:.4f} {}'.format(total, number))
