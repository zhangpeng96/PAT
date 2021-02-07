"""
    @name     : b1049
    @version  : 21.0207
    @author   : zhangpeng96
    @time     : 27'00"
    @accepted : all
    @desc     : 必须用decimal，否则p2精度不够出错
    https://www.dazhuanlan.com/2019/11/30/5de16b44d92f3/
"""

from decimal import Decimal

count = int(input())
digit = map(Decimal, input().split())

result = sum(map(
    lambda i, x: x*(count - i)*(i + 1),
    range(count), digit
))

print('{:.2f}'.format(result))
