"""
    @name      : a1065
    @version   : 21.0114
    @author    : zhangpeng96
    @test_time : 5'00"
    @pass_rate : all
"""

count = int(input())
numbers = [map(int, input().split()) for _ in range(count)]

for i, (a,b,c) in enumerate(numbers):
    if a + b > c:
        print('Case #{}: true'.format(i+1))
    else:
        print('Case #{}: false'.format(i+1))
