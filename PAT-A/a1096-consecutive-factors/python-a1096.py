"""
    @name     : a1096
    @version  : 21.0119
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

from math import sqrt

# number = int('14')
number = int(input())
max_n = int(sqrt(number)) + 1
result = []

for a in range(2, max_n+1):
    product = 1
    for b in range(a, max_n+1):
        product *= b
        if number % product:
            break
        else:
            result.append((b-a+1, a, b))

if len(result):
    length, start, end = sorted(result, key=lambda x: (-x[0], x[1]))[0]
    print(length)
    print('*'.join(map(str, [i for i in range(start, end+1) ])))
else:
    print('1\n{}'.format(number))
