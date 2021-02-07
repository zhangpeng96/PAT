"""
    @name     : b1049
    @version  : 21.0207
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : p2,p3 timeout
"""

from decimal import Decimal
from itertools import accumulate

count = int(input())
digit = list(map(Decimal, input().split()))

result = sum( map(lambda x: sum(accumulate(digit[x:])), range(count)) )

print('{:.2f}'.format(result))
