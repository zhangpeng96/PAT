'''
    @name      : b1068
    @version   : 20.0526.3
    @author    : zhangpeng96
    @test_time : 122'00"
    @pass_rate : p4 timeout
'''

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

def search_bit2(bitmap, x, y, right, bottom, gap):
    checks = []
    if right == 0:
        if x == 0:
            checks += [ bitmap[x+1][y] ]
        elif x == bottom:
            checks += [ bitmap[x-1][y] ]
        else:
            checks += [ bitmap[x-1][y] + bitmap[x+1][y] ]
    elif bottom == 0:
        if y == 0:
            checks += [ bitmap[x][y+1] ]
        elif y == right:
            checks += [ bitmap[x][y-1] ]
        else:
            checks += [ bitmap[x][y-1] + bitmap[x][y+1] ]
    return check_bit(bitmap[x][y], checks, gap)

def single_element(iters, bitmap_line):
    single = []
    for it in iters:
        if bitmap_line.count(it) == 1:
            single.append(it)
    return single


width, height, gap = tuple(map(int, input().split()))
bitmap = [ list( map(int, input().split()) ) for _ in range(height) ]

# width, height, gap = map(int, '2 1 100'.split())
# inputs = ['199 33']
# bitmap = [ list( map(int, i.split()) ) for i in inputs ]
bitmap_line = sum(bitmap, [])

right, bottom = width-1, height-1
unique, option = {}, []

if width == 1 and height == 1:
    option.append(bitmap[0][0])
    unique.update({ bitmap[0][0]: (1, 1)})

elif width == 1 or height == 1:
    for x in range(height):
        for y in range(width):
            if search_bit2(bitmap, x, y, right, bottom, gap):
                bits = bitmap[x][y]
                option.append(bits)
                unique.update({ bits: (y+1,x+1) })
else:
    for x in range(height):
        for y in range(width):
            if search_bit(bitmap, x, y, right, bottom, gap):
                bits = bitmap[x][y]
                option.append(bits)
                unique.update({ bits: (y+1,x+1) })

option = single_element(option, bitmap_line)

if len(option) == 1:
    print('({}, {}): {}'.format(*unique[option[0]], option[0]))
elif len(option) > 1:
    print('Not Unique')
elif len(option) == 0:
    print('Not Exist')
