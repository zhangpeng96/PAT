'''
    @name      : b1066
    @version   : 20.0527
    @author    : zhangpeng96
    @test_time : 10'48"
    @pass_rate : p3 timeout
'''


# height, width, start, end, color = map(int, input().split())
# bitmap = [list( map(int, input().split()) ) for _ in range(height)]

height, width, start, end, color = map(int, '3 5 100 150 0'.split())
bitmap = [list( map(int, i.split()) ) for i in ['3 189 254 101 119','150 233 151 99 100','88 123 149 0 255'] ]
bitmap = sum(bitmap, [])

for i, bit in enumerate(bitmap):
    if start <= bit <= end:
        bitmap[i] = color

for i in range(height):
    print(' '.join(map(lambda x: '{:03}'.format(x), bitmap[i*width : (i+1)*width])))


