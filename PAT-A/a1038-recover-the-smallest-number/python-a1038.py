"""
    @name     : a1038
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 7'30"
    @accepted : all
"""

from functools import cmp_to_key

def cmp(a, b):
    if a + b > b + a:
        return 1
    else:
        return -1

digit = input().split()[1:]
digit.sort(key=cmp_to_key(cmp))
number = int( ''.join(digit) )

print(number)
