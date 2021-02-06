"""
    @name     : a1132
    @version  : 21.0206
    @author   : zhangpeng96
    @time     : 6'00"
    @accepted : all
    @desc     : p2,p3 要考虑x*y为零的情况
"""

count = int(input())
for _ in range(count):
    digit = input()
    k = len(digit)
    x, y = int(digit[0:k//2]), int(digit[k//2:])
    if x * y == 0:
        print('No')
    else:
        if int(digit) % (x * y):
            print('No')
        else:
            print('Yes')
