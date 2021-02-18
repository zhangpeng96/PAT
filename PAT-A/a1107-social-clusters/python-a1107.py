"""
    @name     : a1107
    @version  : 21.0217
    @author   : zhangpeng96
    @time     : 50'00"
    @accepted : all
"""

from collections import Counter

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


cluster_root = {}
count = int(input())
father = [i for i in range(count+1)]

for people in range(1, count+1):
    for hobby in map(int, input().split()[1:]):
        # cluster_root的作用就是把合并hobby问题映射到people，合并时找的是people而不是hobby
        if hobby not in cluster_root:
            cluster_root[hobby] = people
        union(people, find(cluster_root[hobby]))

# 查找每一个人组成社交团伙的头目
all_people_root = [ find(people) for people in range(1, count+1) ]
# 按头目划分圈子，并统计该头目下有多少人
cluster = Counter(all_people_root).most_common()

print(len(cluster))
print(*map(lambda x: x[1], cluster))
