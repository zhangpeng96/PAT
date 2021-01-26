"""
    @name     : a1090
    @version  : 21.0126
    @author   : zhangpeng96
    @time     : 77'00"
    @accepted : p1,p2,p6 timeout
"""

import sys
sys.setrecursionlimit(20000)

def dfs(root, nodes, depth):
    retailer[depth] = retailer.get(depth, 0) + 1
    if not nodes[root]:
        return
    for node in nodes[root]:
        dfs(node, nodes, depth+1)


# count, price, rate = '9 1.80 1.00'.split()
# ins = map(int, '1 5 4 4 -1 4 5 3 6'.split())
count, price, rate = input().split()
ins = map(int, input().split())
count, price, rate = int(count), float(price), 1+(float(rate)/100)

retailer = {}
nodes = [ [] for _ in range(count) ]

for i, k in enumerate(ins):
    if k == -1:
        root = i
    else:
        nodes[k].append(i)

dfs(root, nodes, 0)

depth, number = sorted(retailer.items())[-1]
total = price * rate**depth
print('{:.2f} {}'.format(total, number))
