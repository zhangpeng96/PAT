"""
    @name     : a1060
    @version  : 21.0126
    @author   : zhangpeng96
    @time     : 54'00"
    @accepted : all
"""

from decimal import Decimal, getcontext, ROUND_DOWN

# prec, a, b = '3 120 128'.split()
# prec, a, b = '1 2 1'.split()
# prec, a, b = '5 00.01 0.0001'.split()
# prec, a, b = '4 0.01234 0.012345'.split()
# prec, a, b = '5 0.1234 0.12345'.split()
# prec, a, b = '1 12300 12358.95'.split()
prec, a, b = '1 00.0 0.000'.split()

prec, a, b = input().split()
prec, a, b = int(prec), Decimal(a), Decimal(b)

def stand(a, prec):
    getcontext().prec = prec
    getcontext().rounding = ROUND_DOWN
    if a == Decimal(0):
        pos = 0
    else:
        pos = 1 + a.adjusted()
    power = Decimal(10) ** Decimal(-pos)
    s = a * power
    return s, pos

pa = '{:.{prec}f}*10^{}'.format(*stand(a, prec), prec=prec)
pb = '{:.{prec}f}*10^{}'.format(*stand(b, prec), prec=prec)

if pa == pb:
    print('YES {}'.format(pa))
else:
    print('NO {} {}'.format(pa, pb))
