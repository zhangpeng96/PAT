"""
    @name      : a1060
    @version   : 20.0719.2
    @author    : zhangpeng96
    @test_time : 32'00"
    @pass_rate : p3, p5, p6 failed
"""

# precision, digit_1, digit_2 = input().split()
precision, digit_1, digit_2 = '3 120 128'.split()
precision, digit_1, digit_2 = '1 0.0 0.1'.split()
precision, digit_1, digit_2 = int(precision), float(digit_1), float(digit_2)

def exp(digit):
    dig = int(digit)
    if dig:
        return len(str(dig))
    else:
        return int('{:e}'.format(digit).split('e')[1]) + 1

def chopping(digit):
    ep = exp(digit)
    base = digit / (10**ep)
    r = 10**precision
    formats = '{:.' + str(precision) + 'f}*10^{}'
    return formats.format(int(base*r)/r, ep)

str1, str2 = chopping(digit_1), chopping(digit_2)

if str1 == str2:
    print('YES {}'.format(str1))
else:
    print('NO {} {}'.format(str1, str2))
