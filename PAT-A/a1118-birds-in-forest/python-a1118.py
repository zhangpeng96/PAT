"""
    @name     : a1118
    @version  : 21.0218
    @author   : zhangpeng96
    @time     : 36'00"
    @accepted : p4 error
"""

father = {}
count = {}

def find(x):
    if x == father[x]:
        return x
    else:
        father[x] = find(father[x])
        return father[x]

def union(a, b):
    fatherA, fatherB = find(a), find(b)
    if fatherA != fatherB:
        father[fatherA] = fatherB


for _ in range(int(input())):
    birds = map(int, input().split()[1:])
    bird_root = next(birds)
    if bird_root not in father:
        father[bird_root] = bird_root
    for bird in birds:
        if bird not in father:
            father[bird] = bird
        union(bird_root, bird)

for bird in father.keys():
    bird_root = find(bird)
    count[bird_root] = count.get(bird_root,0) + 1

tree_n, bird_n = len(count), sum(count.values())
print(tree_n, bird_n)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print('Yes')
    else:
        print('No')
