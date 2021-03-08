"""
    @name     : b1068
    @version  : 21.0308.2
    @author   : zhangpeng96
    @time     : 40'00"
    @accepted : all
"""

from sys import stdin
from collections import defaultdict

def check_bit(i, j):
    checked = bitmap[i][j]
    clockwise = [ (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0) ]
    for side_x, side_y in clockwise:
        x, y = i + side_x, j + side_y
        if (x >= 0 and x < width and y >=0 and y < height) and abs(bitmap[x][y]-checked) <= threshold:
            return False
    return True


width, height, threshold = map(int, input().split())
bitmap = [ list( map(int, line.split()) ) for line in stdin.readlines() ]
bitmap = tuple(zip(*bitmap))

counter = defaultdict(int)
for i in range(width):
    for j in range(height):
        if counter[bitmap[i][j]] < 2:
            counter[bitmap[i][j]] += 1

count = 0
result = tuple()

for i in range(width):
    for j in range(height):
        bit = bitmap[i][j]
        if counter[bit] < 2:
            if check_bit(i, j):
                result = (i+1, j+1, bit)
                count += 1

if count == 1:
    print('({}, {}): {}'.format(*result))
elif count > 1:
    print('Not Unique')
else:
    print('Not Exist')
