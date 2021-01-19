"""
    @name     : a1047
    @version  : 21.0119
    @author   : zhangpeng96
    @time     : 26'00"
    @accepted : p1 error
"""

n, k = map(int, input().split())
data = {}

for _ in range(n):
    ins = input().split()
    for i in ins[2:]:
        i = int(i)
        if i in data:
            data[i].append(ins[0])
        else:
            data[i] = [ins[0]]

for item in sorted(data.items(), key=lambda x:x[0]):
    print(item[0], len(item[1]))
    print('\n'.join(sorted(item[1])))
