'''
    @name      : b1062
    @version   : 
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all failed
'''

import math


def main():
    start, end, divisor = '7/18 13/20 12'.split()
    start = list(map(int, start.split('/')))
    end = list(map(int, end.split('/')))
    divisor = int(divisor)
    weight = start[1] / divisor
    start[0] /= weight
    weight = end[1] / divisor
    end[0] /= weight
    ran = sorted([start[0], end[0]])
    result = []

    for i in range(math.ceil(ran[0]), math.ceil(ran[1])):
        result.append('{}/{}'.format(i, divisor))

    print(' '.join(result))


if __name__ == '__main__':
    main()
