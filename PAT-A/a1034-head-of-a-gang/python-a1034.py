"""
    @name     : a1034
    @version  : 21.0307
    @author   : zhangpeng96
    @time     : 50'00"
    @accepted : p3 error
"""

def find(x):
    if x == father[x]:
        return x
    father[x] = find(father[x])
    return father[x]

def union(a, b):
    fatherA, fatherB = find(a), find(b)
    if fatherA != fatherB:
        father[fatherA] = fatherB        
        gangs[fatherB] += [ g for g in gangs[fatherA] ]
        gangs[fatherA] = []


count, threshold = map(int, input().split())
it = iter(range(count))
father = list(range(count))
gang_time = [0] * count
gangs = [ [i] for i in range(count) ]

result = []
name_to_int = {}
int_to_name = {}

for i in range(count):
    *names, time = input().split()
    for name in names:
        if name not in name_to_int.keys():
            pos = next(it)
            name_to_int[name] = pos
            int_to_name[pos] = name
        gang_time[ name_to_int[name] ] += int(time)
    union(name_to_int[names[0]], name_to_int[names[1]])

for gang in gangs:
    if len(gang) <= 2: continue
    time_total = sum([ gang_time[p] for p in gang ])
    if time_total <= 2 * threshold: continue
    head, _ = max([ (p, gang_time[p]) for p in gang ], key=lambda x:x[1])
    result.append( (int_to_name[head], len(gang)) )

result.sort(key=lambda x:x[0])
print(len(result))
for r in result:
    print(*r)
