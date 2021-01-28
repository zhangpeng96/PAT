"""
    @name     : a1103
    @version  : 21.0128
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p5 timeout
"""

from copy import copy

number, count, power = map(int, input().split())

result, powers, path = [], [], [None]*count
temp, index, factor_sum = 0, 1, 0
while temp <= number:
    powers.append(temp)
    temp = index**power
    index += 1

def dfs(index, temp_number, temp_count):
    global factor_sum, result
    if temp_count == count:
        if temp_number == number:
            factor = sum(path)
            if factor > factor_sum:
                result = copy(path)
                factor_sum = factor
        return
    while index >= 1:
        if temp_number + powers[index] <= number:
            path[temp_count] = index
            dfs(index, temp_number + powers[index], temp_count + 1)
        if index == 1:
            return
        index -= 1
"""也可以用for语句代替while语句
    for i in range(index, 0, -1):
        if temp_number + powers[i] <= number:
            path[temp_count] = i
            dfs(i, temp_number + powers[i], temp_count + 1)
        if i == 1:
            return
"""
dfs(len(powers)-1, 0, 0)

if result:
    bases = map(lambda x: '{}^{}'.format(x, power), result)
    print('{} = {}'.format(number, ' + '.join(bases)))
else:
    print('Impossible')
