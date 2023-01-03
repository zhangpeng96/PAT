'''
    @name      : b1070
    @version   : 20.0522
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
'''

count = int(input())
ropes = tuple(sorted(map(int, input().split())))

# ropes = tuple(sorted(map(int, '10 15 12 3 4 13 1 15'.split())))

rope_length = ropes[0]

for r in ropes[1:]:
    rope_length = (rope_length + r) // 2

print(rope_length)
