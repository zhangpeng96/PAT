"""
    @name      : a1081
    @version   : 20.0720
    @author    : zhangpeng96
    @test_time : 24'00"
    @pass_rate : all
"""

from fractions import Fraction

count = int(input())
fracs = input().split()
# fracs = '2/5 4/15 1/30 -2/60 8/3'.split()
# fracs = '4/3 2/3'.split()
# fracs = '1/3 -1/6 1/8'.split()

numbers = []

for frac in fracs:
    numer, denom = map(int, frac.split('/'))
    numbers.append(Fraction(numer, denom))

result = sum(numbers)
numer, denom = result.numerator, result.denominator

if numer > denom and denom != 1:
    print( '{} {}/{}'.format(*divmod(numer, denom), denom) )
else:
    print(result)
