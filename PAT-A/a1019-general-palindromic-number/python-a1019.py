"""
    @name     : a1019
    @version  : 21.0227
    @author   : zhangpeng96
    @time     : 20'00"
    @accepted : all
"""

def digit(n, base):
    if n < base:
        return [n]
    else:
        return digit(n//base, base) + [n % base]


pos = 0
flag = True
n, base = map(int, input().split())
number = digit(n, base)

while pos < len(number)//2:
    if number[pos] != number[-pos-1]:
        flag = False
    pos += 1

if flag:
    print('Yes')
else:
    print('No')
print(*number)
