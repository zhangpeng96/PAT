"""
    @name     : a1002
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : all
"""

# ins1 = '2 1 2.4 0 3.2'
# ins2 = '2 2 1.5 1 0.5'

ins1 = input()
ins2 = input()

a = dict(zip( map(int, ins1.split()[1::2]), map(float, ins1.split()[2::2]) ))
b = dict(zip( map(int, ins2.split()[1::2]), map(float, ins2.split()[2::2]) ))
poly = {}

for key in (a.keys() | b.keys()):
    total = a.get(key, 0.0) + b.get(key, 0.0)
    if total != 0.0:
        poly[key] = total

poly = sorted(poly.items(), reverse=True)
line = ' '.join(map(lambda x: '{:d} {:.1f}'.format(*x), poly))
k = len(poly)

if k:
    print(k, line)
else:
    print(0)
