"""
    @name     : a1114
    @version  : 21.0218
    @author   : zhangpeng96
    @time     : 45'45"
    @accepted : all
    @desc     : 题目难度较大，测试点无坑
"""

class Family():
    def __init__(self):
        self.population = 0
        self.estates = []
        self.areas = []
        self.estate = 0
        self.area = 0
    def calc(self):
        self.estate = sum(self.estates) / self.population
        self.area = sum(self.areas) / self.population

def find(x):
    if x == father[x]:
        return x
    else:
        father[x] = find(father[x])
        return father[x]

def union(a, b):
    fatherA, fatherB = find(a), find(b)
    if fatherA <= fatherB:
        father[fatherB] = fatherA
    else:
        father[fatherA] = fatherB


father = {}
properties = {}
report = {}

for _ in range(int(input())):
    uid, father_id, mother_id, _, *children, estate, area = map(int, input().split())
    properties[uid] = (estate, area)
    father.setdefault(uid, uid)
    for parent_id in [father_id, mother_id]:
        if parent_id != -1:
            father.setdefault(parent_id, parent_id)
            union(uid, parent_id)
    for child_id in children:
        father.setdefault(child_id, child_id)
        union(uid, child_id)

for uid in father.keys():
    root = find(uid)
    # 因为人数是一定每轮要做计算的，所以先根据最高长辈命名判断是否有这个家庭，再创建记录人口
    if root not in report: report[root] = Family()
    report[root].population += 1
    # 所有的人有的没有财产的，因此先判断这个人有没有财产，有再计入最高长辈命名的家庭名下
    if uid in properties:
        estate, area = properties[uid]
        report[root].estates.append(estate)
        report[root].areas.append(area)

for family in report.values():
    family.calc()

print(len(report))
for root, family in sorted(report.items(), key=lambda x:(-x[1].area, x[0])):
    print('{:04} {} {:.3f} {:.3f}'.format(root, family.population, family.estate, family.area))

