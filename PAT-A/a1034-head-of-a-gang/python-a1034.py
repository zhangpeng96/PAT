"""
    @name     : a1034
    @version  : 21.0307
    @author   : zhangpeng96
    @time     : 50'00"
    @accepted : all
"""

from itertools import cycle


def find(x):
    if x == father[x]:
        return x
    father[x] = find(father[x])
    return father[x]

def union(a, b):
    fatherA, fatherB = find(a), find(b)
    if fatherA != fatherB:
        father[fatherA] = fatherB
        # A合并到B中，对应团伙所有人也并入B，原A清空
        gangs[fatherB] += [ g for g in gangs[fatherA] ]
        gangs[fatherA] = []


count, threshold = map(int, input().split())
# 并查集关系数组
father = list(range(count))
# 记录各团伙的总计时间
gang_time = [0] * count
# 团伙各个人信息，初始每个团伙以自己为成员
gangs = [ [i] for i in range(count) ]

result = []
# 名字下标转换
name_to_int = {}
int_to_name = {}

# 循环迭代器，用于生成名字的下标
it = cycle(range(count))

for i in range(count):
    *names, time = input().split()
    for name in names:
        if name not in name_to_int.keys():
            pos = next(it)
            # 名字下标关系映射
            name_to_int[name] = pos
            int_to_name[pos] = name
        # 每个人总计
        gang_time[ name_to_int[name] ] += int(time)
    union(name_to_int[names[0]], name_to_int[names[1]])

# 合并各个团伙后遍历，按条件筛选结果
for gang in gangs:
    if len(gang) <= 2: continue
    # 计算该团伙的总时间
    time_total = sum([ gang_time[p] for p in gang ])
    if time_total <= 2 * threshold: continue
    # 求时间最长的人的下标
    head, _ = max([ (p, gang_time[p]) for p in gang ], key=lambda x:x[1])
    result.append( (int_to_name[head], len(gang)) )

result.sort(key=lambda x:x[0])
print(len(result))
for r in result:
    print(*r)
