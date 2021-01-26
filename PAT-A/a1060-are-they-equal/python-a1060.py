"""
    @name     : a1060
    @version  : 21.0126
    @author   : zhangpeng96
    @time     : 54'00"
    @accepted : p3,p5 error
"""

# prec, a, b = '3 120 128'.split()
# prec, a, b = '1 1.2300 1.23589'.split()
prec, a, b = '5 1.2300 1.23589'.split()
# prec, a, b = '4 0.01234 0.012345'.split()
# prec, a, b = '5 0.1234 0.12345'.split()
prec, a, b = '1 12300 12358.9'.split()
# prec, a, b = '1 00.0 0.000'.split()

prec, a, b = input().split()
prec, a, b = int(prec), float(a), float(b)

def significance(f):
    f = str(f)
    if f.find('e') != -1:
        return int(f.split('e')[1])
    if f.startswith('0.'):
        for i, dig in enumerate(f.split('.')[1]):
            if dig != '0': return -(i+1)
        return 0
    else:
        return len(f.split('.')[0]) - 1

def round_down(f, prec):
    fs = str(f)
    if fs.find('.') == -1:
        return f
    else:
        intger = len(fs.split('.')[0])
        pos = intger + 1 + prec
        return float(fs[:pos])

def stand(a, prec):
    if a == 0 or a == 0.0:
        pos = 0
    else:
        pos = 1 + significance(a)
        print(significance(a), pos)
    power = 10 ** -pos
    s = round_down(a * power, prec)
    return s, pos

pa = '{:.{prec}f}*10^{}'.format(*stand(a, prec), prec=prec)
pb = '{:.{prec}f}*10^{}'.format(*stand(b, prec), prec=prec)

if pa == pb:
    print('YES {}'.format(pa))
else:
    print('NO {} {}'.format(pa, pb))
