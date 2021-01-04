'''
    @name      : a1010
    @version   : 21.0104
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
'''


def to_decimal(n, base):
    symbol = '0123456789abcdefghijklmnopqrstuvwxyz'
    digits = map(lambda r: symbol.index(r), n[::-1])
    return sum([ digit * base ** r for r, digit in enumerate(digits) ])

def binary_search(string, num, low=0):
    high = max(num, low)
    while low <= high:
        mid = int((low + high) / 2)
        cnum = to_decimal(string, mid)
        print('>', low, high, mid, cnum, num)
        if cnum == num:
            return mid
        elif cnum > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# n1, n2, tag, radix = '6 110 1 10'.split()
# n1, n2, tag, radix = '1 ab 1 2'.split()
n1, n2, tag, radix = input().split()
tag, radix = int(tag), int(radix)

if tag == 2:
    n1, n2 = n2, n1

num = to_decimal(n1, radix)
low = '0123456789abcdefghijklmnopqrstuvwxyz'.index(max(n2))+1 # 1 1 1 10 -> 2
ans = binary_search(n2, num, low)
if ans == -1:
    print('Impossible')
else:
    print(ans)
