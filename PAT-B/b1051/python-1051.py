'''
    @name      : b1051
    @version   : 20.013
    @author    : zhangpeng96
    @test_time : 21'15"
    @pass_rate : p3, p4 failed
'''
from math import pi, sin, cos, radians

def to_algebra(r, p):
    return tuple([r*cos(p), r*sin(p)])

def complex_mul(c1, c2):
    r1, i1 = c1
    r2, i2 = c2
    return tuple([r1*r2 - i1*i2, r1*i2 + i1*r2])

r1, p1, r2, p2 = tuple(map(float, '2.3 0 0 0'.split()))
# r1, p1, r2, p2 = tuple(map(float, '2.3 3.5 5.2 0.4'.split()))
# r1, p1, r2, p2 = tuple(map(float, input().split()))

c1 = to_algebra(r1, p1)
c2 = to_algebra(r2, p2)

print('{:.2f}{:+.2f}i'.format(*complex_mul(c1, c2)))
