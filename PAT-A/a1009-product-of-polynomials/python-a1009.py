"""
    @name     : a1009
    @version  : 21.0123
    @author   : zhangpeng96
    @time     : 32'28"
    @accepted : all
"""

from itertools import product

# ins1 = '2 1 2.4 0 3.2'
# ins2 = '2 2 1.5 1 0.5'

ins1 = input()
ins2 = input()

a = zip( map(int, ins1.split()[1::2]), map(float, ins1.split()[2::2]) )
b = zip( map(int, ins2.split()[1::2]), map(float, ins2.split()[2::2]) )
poly = {}

prod = map(lambda x: (x[0][0]+x[1][0], x[0][1]*x[1][1]), product(a, b))

for exp, coef in prod:
    poly[exp] = poly.get(exp, 0.0) + coef

poly = list( filter(lambda x:x[1]!=0.0, sorted(poly.items(),reverse=True)) )
line = ' '.join(map(lambda x: '{:d} {:.1f}'.format(*x), poly))
k = len(poly)

if k:
    print(k, line)
else:
    print(0)
