from copy import copy

number, count, power = map(int, '169 5 2'.split())

result, powers, path = [], [], [None]*count
temp, index = 0, 1
while temp <= number:
    powers.append(temp)
    temp = index**power
    index += 1

def dfs(index, temp_number, temp_count):
    if temp_count == count:
        if temp_number == number:
            result.append( (sum(path), copy(path)) )
            print(result)
        return
    while index >= 1:
        if temp_number + powers[index] <= number:
            path[temp_count] = index
            dfs(index, temp_number + powers[index], temp_count + 1)
        if index == 1:
            return
        index -= 1
    # for i in range(index, 0, -1):
    #     if temp_number + powers[i] <= number:
    #         path[temp_count] = i
    #         dfs(i, temp_number + powers[i], temp_count + 1)
    #     if i == 1:
    #         return

dfs(len(powers)-1, 0, 0)

if result:
    bases = map(lambda x: '{}^{}'.format(x, power), sorted(result)[-1][1])
    print('{} = {}'.format(number, ' + '.join(bases)))
else:
    print('Impossible')
