"""
    @name     : a1118
    @version  : 21.0218
    @author   : zhangpeng96
    @time     : 36'00"
    @accepted : p4 timeout
"""

import sys
from collections import defaultdict


def find(x):
    y = x
    while x != father[x]:
        x = father[x]
    while y != father[y]:
        y, father[y] = father[y], x
    return x

def union(a, b):
    fatherA, fatherB = find(a), find(b)
    if fatherA != fatherB:
        father[fatherA] = fatherB


father = {}
count = defaultdict(int)

for _ in range(int(input())):
    birds = map(int, input().split()[1:])
    bird_root = next(birds)
    father.setdefault(bird_root, bird_root)
    for bird in birds:
        father.setdefault(bird, bird)
        union(bird_root, bird)

for bird in father.keys():
    bird_root = find(bird)
    count[bird_root] += 1

tree_n, bird_n = len(count), sum(count.values())
print(tree_n, bird_n)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print('Yes')
    else:
        print('No')
