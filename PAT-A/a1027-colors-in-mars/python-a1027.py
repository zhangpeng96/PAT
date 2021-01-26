"""
    @name      : a1027
    @version   : 21.0126
    @author    : zhangpeng96
    @test_time : 19'54"
    @pass_rate : all
"""

def radix(n, base):
    char = '0123456789ABC'
    if n < base:
        return char[n]
    else:
        return radix(n//base, base) + char[n % base]

r, g, b = map(lambda x: radix(int(x), 13), input().split())
print('#{:>02}{:>02}{:>02}'.format(r, g, b))
