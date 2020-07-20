"""
    @name      : a1060
    @version   : 20.0720.1
    @author    : zhangpeng96
    @test_time : 32'00"
    @pass_rate : p3, p5 failed
"""

# precision, digit_1, digit_2 = input().split()
precision, digit_1, digit_2 = '3 120 128'.split()
precision, digit_1, digit_2 = '5 0.01234 0.012345'.split()
precision, digit_1, digit_2 = int(precision), float(digit_1), float(digit_2)

def exp(digit):
    dig = int(digit)
    a, b = str(digit).split('.')
    if dig:
        return len(a)-1
    elif digit == 0.0:
        return -1
    else:
        count = -1
        for i in b:
            if i != '0':
                break
            count -= 1
        return count


def chopping(digit):
    ep = exp(digit) + 1
    base = digit / (10**ep)
    r = 10**precision
    formats = '{:.' + str(precision) + 'f}*10^{}'
    return formats.format(int(base*r)/r, ep)

str1, str2 = chopping(digit_1), chopping(digit_2)

if str1 == str2:
    print('YES {}'.format(str1))
else:
    print('NO {} {}'.format(str1, str2))
