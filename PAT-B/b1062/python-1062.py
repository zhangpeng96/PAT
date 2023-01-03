'''
    @name      : b1062
    @version   : 20.0514.3
    @author    : zhangpeng96
    @test_time : 63'28"
    @pass_rate : all
'''

from math import ceil, floor

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
start, end = tuple(map(lambda x: int(x.split('/')[0]) / int(x.split('/')[1]), input_str.split()[:2]))

if start > end:
    start, end = end, start

start = ceil((start * divisor) + 1e-7)
end = floor((end * divisor) - 1e-7)

frac_list = [(i, divisor) for i in range(start, end+1)]

'''
    Alternative 

end = ceil((end * divisor) - 1e-7)

frac_list = [(i, divisor) for i in range(start, end)]
'''

print(
    ' '.join(map(lambda x: '{}/{}'.format(*x), filter(is_irreducible, frac_list)))
)
