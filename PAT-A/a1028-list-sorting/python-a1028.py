"""
    @name     : a1028
    @version  : 21.0208
    @author   : zhangpeng96
    @time     : 11'40"
    @accepted : all
"""

records = []
count, op = map(int, input().split())
for _ in range(count):
    sn, name, score = input().split()
    records.append( (sn, name, int(score)) )

if op == 1:
    records.sort(key=lambda x:x[0])
elif op == 2:
    records.sort(key=lambda x:(x[1], x[0]))
elif op == 3:
    records.sort(key=lambda x:(x[2], x[0]))

for record in records:
    print('{} {} {}'.format(*record))
