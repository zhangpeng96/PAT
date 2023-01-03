'''
    @name      : b1050
    @version   : 20.0524
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
'''

from math import sqrt

# count = int('12')
# digits = sorted(map(int, '37 76 20 98 76 42 53 95 60 81 58 93'.split()), reverse = True)

count = int(input())
digits = sorted(map(int, input().split()), reverse = True)

n = int(sqrt(count))
while count % n:
    n -= 1
m = count // n

def paint(matrix):
    for row in matrix:
        print( ' '.join(map(lambda x: '{:d}'.format(x), row)) )

def clockwise(elements, m, n):
    it = iter(elements)
    res = [ [None] * n for _ in range(m)]
    top, left, bottom, right = 0, 0, m - 1, n - 1
    while top <= bottom and left <= right:
        for col in range(left, right+1):
            res[top][col] = next(it)
        for row in range(top+1, bottom+1):
            res[row][right] = next(it)
        if top != bottom:
            for col in range(right-1, left-1, -1):
                res[bottom][col] = next(it)
        if left != right:
            for row in range(bottom-1, top, -1):
                res[row][left] = next(it)
        left, top, right, bottom = left+1, top+1, right-1, bottom-1
    return res

paint(clockwise(digits, m, n))
