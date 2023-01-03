'''
    @name      : a1054
    @version   : 20.0528
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p2 timeout
'''

from collections import Counter

width, height = map(int, input().split())
colors = sum(
    [list(map(int, input().split())) for _ in range(height)], [] )

print(Counter(colors).most_common()[0][0])