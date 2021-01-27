"""
    @name     : a1036
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 18'30"
    @accepted : all
"""

count = int(input())
male, female = [], []
sf, sm = None, None

for _ in range(count):
    x = input().split()
    record = ( int(x[3]), x[0], x[2] )
    if x[1] == 'M':
        male.append(record)
    elif x[1] == 'F':
        female.append(record)

if female:
    sf, *r = sorted(female, reverse=True)[0]
    print(' '.join(r))
else:
    print('Absent')

if male:
    sm, *r = sorted(male)[0]
    print(' '.join(r))
else:
    print('Absent')

if sf == None or sm == None:
    print('NA')
else:
    print(sf-sm)
