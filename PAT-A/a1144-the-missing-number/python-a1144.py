"""
    @name     : a1144
    @version  : 21.0128
    @author   : zhangpeng96
    @time     : 8'18"
    @accepted : all
    @desc     : 测试点4要考虑输入的值无正数的情况
"""

count = int(input())
digit = [int(i) for i in input().split() if i[0] != '-']
digit = sorted( list(set(digit)) )

if digit:
    pos = digit[0]
    for dig in digit:
        if pos != dig:
            break
        pos += 1
    print(pos)
else:
    print(1)
