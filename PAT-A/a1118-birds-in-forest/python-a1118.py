"""
    @name     : a1118
    @version  : 21.0218
    @author   : zhangpeng96
    @time     : 36'00"
    @accepted : p3 timeout, p4 error
"""

father = list(range(0, 10010))
# 注意从0开始
exist = [False]*10011
cnt = {}

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
    birds = list(map(int, input().split()[1:]))
    bird_root = birds[0]
    exist[bird_root] = True
    for bird in birds[1:]:
        union(bird_root, bird)
        exist[bird] = True


for bird, is_exist in enumerate(exist[1:], 1):
    if is_exist:
        bird_root = find(bird)
        cnt[bird_root] = cnt.get(bird_root, 0) + 1

tree_n, bird_n = len(cnt), sum(cnt.values())

print(tree_n, bird_n)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print('Yes')
    else:
        print('No')

