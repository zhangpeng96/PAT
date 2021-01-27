"""
    @name     : b1062
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 29'00"
    @accepted : all

测试点2
6/18 19/18 3
2/3
"""

from fractions import Fraction
from math import gcd, ceil, floor

# a, b, deno = '7/18 13/20 12'.split()
a, b, deno = input().split()
a, b, deno = Fraction(a), Fraction(b), int(deno)
if a > b: a, b = b, a

start = a.numerator * (deno / a.denominator)
start = int(start)+1 if start==int(start) else ceil(start)
end = b.numerator * (deno / b.denominator)
end = int(end)-1 if end==int(end) else floor(end)

result = []

for nume in range(start, end+1):
    if gcd(nume, deno) == 1:
        result.append( '{}/{}'.format(nume, deno) )

print(' '.join(result))
