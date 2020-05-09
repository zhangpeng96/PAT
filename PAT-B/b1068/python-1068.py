'''
    @name      : b1068
    @version   : 20.0509
    @author    : zhangpeng96
    @test_time : 60'00"
    @pass_rate : p3, p5 failed, p4 timeout
'''
from collections import Counter

def diff_by_surround(arr, x, y, gap):
    x,y = y-1,x-1
    value = arr[x][y]
    if value in unique_pixel:
        # print('>', x,y, value)
        return all(map(lambda n: abs(value-n) > gap,
                        [arr[x-1][y-1], arr[x][y-1], arr[x+1][y-1], arr[x-1][y], arr[x+1][y], arr[x-1][y+1], arr[x][y+1], arr[x+1][y+1]]))
    else:
        return False


# width, height, gap = tuple(map(int, '8 6 200'.split()))
width, height, gap = tuple(map(int, input().split()))

# input_arr = ['0    0    0        0        0        0        0        0','65280    65280    65280    16711479 65280    65280    65280    65280','16711479 65280    65280    65280    16711680 65280    65280    65280','65280    65280    65280    65280    65280    65280    165280   165280','65280    65280    16777015 65280    65280    165280   65480    165280','16777215 16777215 16777215 16777215 16777215 16777215 16777215 16777215']

input_arr = [input() for i in range(height)]

pixel_matrix = [[int(element) for element in line.split()] for line in input_arr]

unique_pixel = set(map(lambda x:x[0], filter(lambda x:x[1] == 1 ,Counter(sum(pixel_matrix, [])).most_common())))

diff_list = []

for i in range(2, width):
    for j in range(2, height):
        if diff_by_surround(pixel_matrix, i, j, gap):
            diff_list.append((i, j, pixel_matrix[j-1][i-1]))


if len(diff_list) == 1:
    print('({}, {}): {}'.format(*diff_list[0]))
elif len(diff_list) == 0:
    print('Not Exist')
else:
    print('Not Unique')