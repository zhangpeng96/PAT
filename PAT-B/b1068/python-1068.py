'''
    @name      : b1068
    @version   : 20.0526
    @author    : zhangpeng96
    @test_time : 102'50"
    @pass_rate : p3, p5 failed, p4 timeout
'''
from collections import Counter

def check_bit(bit, checks, gap):
    return all( map(lambda n: abs(bit - n) > gap, checks) )

def search_bit(bitmap, x, y, right, bottom, gap):
    checks = []
    if x == 0 and y == 0:
        checks += [ bitmap[x][y+1], bitmap[x+1][y+1], bitmap[x+1][y] ]
    elif x == 0 and 0 < y < right:
        checks += [ bitmap[x][y+1], bitmap[x+1][y+1], bitmap[x+1][y], bitmap[x+1][y-1], bitmap[x][y-1] ]
    elif x == 0 and y == right:
        checks += [ bitmap[x+1][y], bitmap[x+1][y-1], bitmap[x][y-1] ]
    elif 0 < x < bottom and y == right:
        checks += [ bitmap[x+1][y], bitmap[x+1][y-1], bitmap[x][y-1], bitmap[x-1][y-1], bitmap[x-1][y] ]
    elif x == bottom and y == right:
        checks += [ bitmap[x][y-1], bitmap[x-1][y-1], bitmap[x-1][y] ]
    elif x == bottom and  0 < y < right:
        checks += [ bitmap[x-1][y], bitmap[x-1][y+1], bitmap[x][y+1], bitmap[x][y-1], bitmap[x-1][y-1] ]
    elif x == bottom and y == 0:
        checks += [ bitmap[x-1][y], bitmap[x-1][y+1], bitmap[x][y+1] ]
    elif 0 < x < bottom and y == 0:
        checks += [ bitmap[x-1][y], bitmap[x-1][y+1], bitmap[x][y+1], bitmap[x+1][y+1], bitmap[x+1][y] ]
    else:
        checks += [ bitmap[x-1][y], bitmap[x-1][y+1], bitmap[x][y+1], bitmap[x+1][y+1], bitmap[x+1][y], bitmap[x+1][y-1], bitmap[x][y-1], bitmap[x-1][y-1]]
    return check_bit(bitmap[x][y], checks, gap)


def single_element(iters):
    single = []
    for value, times in Counter(iters).most_common()[::-1]:
        if times == 1:
            single += [value]
        else:
            break
    return single


width, height, gap = tuple(map(int, input().split()))
bitmap = tuple([ tuple( map(int, input().split()) ) for _ in range(height) ])

# width, height, gap = map(int, '8 6 200'.split())
# inputs = ['0      0    0        0        0        0        0        0','65280    65280    65280    16711479 65280    65280    65280    65280','16711479 65280    65280    65280    16711680 65280    65280    65280','65280    65280    65280    65280    65280    65280    165280   165280','65280    65280    16777015 65280    65280    165280   65480    165280','16777215 16777215 16777215 16777215 16777215 16777215 16777215 16777215']
# bitmap = tuple([ tuple( map(int, i.split()) ) for i in inputs ])

right, bottom = width-1, height-1
unique, option = {}, []

for x in range(height):
    for y in range(width):
        if search_bit(bitmap, x, y, right, bottom, gap):
            bits = bitmap[x][y]
            option.append(bits)
            unique.update({ bits: (y+1,x+1) })

option = single_element(option)

if len(option) == 1:
    print('({}, {}): {}'.format(*unique[option[0]], option[0]))
elif len(option) > 1:
    print('Not Unique')
elif len(option) == 0:
    print('Not Exist')
