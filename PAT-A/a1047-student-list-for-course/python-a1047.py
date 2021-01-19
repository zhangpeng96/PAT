"""
    @name     : a1047
    @version  : 21.0119
    @author   : zhangpeng96
    @time     : 26'00"
    @accepted : all
"""

n, k = map(int, input().split())
data = dict(zip( [i+1 for i in range(k)], [ [] for _ in range(k) ] ))

for _ in range(n):
    ins = input().split()
    for i in ins[2:]:
        data[int(i)].append(ins[0])

for item in sorted(data.items(), key=lambda x:x[0]):
    print(item[0], len(item[1]))
    if len(item[1]):
        print('\n'.join(sorted(item[1])))
