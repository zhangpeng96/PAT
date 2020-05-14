'''
    @name      : b1062
    @version   : 20.0514
    @author    : zhangpeng96
    @test_time : 21'17"
    @pass_rate : p1 failed
'''

from math import ceil

def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a

def is_irreducible(frac):
    if gcd(*frac) == 1 and frac[1] != 1:
        return True
    else:
        return False


input_str = '7/18 13/20 12'
# input_str = input()

divisor = int(input_str.split()[2])
# start, end = tuple(map(lambda x: x.split('/')[0] / x.split('/')[1]), input_str.split()[:2])
# start = ceil(int(x.split('/')[0]) / int(x.split('/')[1]) * divisor)
# start = ceil(int(x.split('/')[0]) / int(x.split('/')[1]) * divisor)

start, end = tuple(
    sorted(
        map(
        lambda x: ceil(int(x.split('/')[0]) / int(x.split('/')[1]) * divisor), 
        input_str.split()[:2]
    )
))

frac_list = [(i, divisor) for i in range(start, end)]

print(
    ' '.join(map(lambda x: '{}/{}'.format(*x), filter(is_irreducible, frac_list)))
)
