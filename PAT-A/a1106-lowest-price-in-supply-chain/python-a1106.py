"""
    @name     : a1106
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 25'00"
    @accepted : p3,p6,p7 segment fault
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def dfs(root, nodes, depth):
    if not nodes[root]:
        if depth > retailer['min']:
            return
        else:
            retailer[depth] += 1
            retailer['min'] = depth
            return
    for node in nodes[root]:
        dfs(node, nodes, depth+1)


count, price, rate = input().split()
count, price, rate = int(count), float(price), 1+(float(rate)/100)

nodes = []
retailer = defaultdict(int)
retailer['min'] = 999999

for line in sys.stdin.readlines():
    nodes.append( list(map(int, line.split()[1:])) )

dfs(0, nodes, 0)
del retailer['min']

depth, number = sorted(retailer.items())[0]
total = price * rate**depth
print('{:.4f} {}'.format(total, number))
