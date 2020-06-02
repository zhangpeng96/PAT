'''
    @name      : a1010
    @version   : 20.0602
    @author    : zhangpeng96
    @test_time : 99'19;
    @pass_rate : 12/20 pass
'''

def deci_to_radix(n, base, symbol = '0123456789abcdefghijklmnopqrstuvwxyz'):
    def digit(n, base):
        if n < base:
            return [n]
        else:
            return digit(n//base, base) + [n % base]
    return ''.join(map(lambda i: symbol[i], digit(n, base)))

def radix_to_deci(n, base, symbol = '0123456789abcdefghijklmnopqrstuvwxyz'):
    digits = map(lambda r: symbol.index(r), n[::-1])
    return sum( digit * base ** r for r, digit in enumerate(digits) )

def radix_equal(n, common):
    for r in range(1, 37):
        if common == radix_to_deci(n, r):
            return r
    return 'Impossible'

n1, n2, tag, radix = '6 110 1 10'.split()
n1, n2, tag, radix = '1 ab 1 2'.split()
tag, radix = int(tag), int(radix)

if tag == 2:
    n1, n2 = n2, n1

common = radix_to_deci(n1, radix)
print( radix_equal(n2, common) )
