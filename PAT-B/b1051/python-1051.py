'''
    @name      : b1051
    @version   : 20.0513.2
    @author    : zhangpeng96
    @test_time : 26'10"
    @pass_rate : all
'''
from math import pi, sin, cos, radians

def to_algebra(r, p):
    return tuple([r*cos(p), r*sin(p)])

def complex_mul(c1, c2):
    r1, i1 = c1
    r2, i2 = c2
    return tuple([r1*r2 - i1*i2, r1*i2 + i1*r2])

def round_nz(compl, prec = 0):
    return tuple(map(lambda x: round(x, prec) + 0, compl))

# r1, p1, r2, p2 = tuple(map(float, '-0.1 -0.01 5.5 5.5'.split()))
# r1, p1, r2, p2 = tuple(map(float, '2.3 3.5 5.2 0.4'.split()))
r1, p1, r2, p2 = tuple(map(float, input().split()))

c1 = to_algebra(r1, p1)
c2 = to_algebra(r2, p2)

print('{:.2f}{:+.2f}i'.format(* round_nz(complex_mul(c1, c2), 2) ))


'''
    References
    - https://stackoverflow.com/questions/11010683/how-to-have-negative-zero-always-formatted-as-positive-zero-in-a-python-string
    - https://stackoverflow.com/questions/4083401/negative-zero-in-python
'''