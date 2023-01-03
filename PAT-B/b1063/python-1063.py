'''
    @name      : b1063
    @version   : 20.0508
    @author    : zhangpeng96
    @test_time : 7'11"
    @pass_rate : all
'''

from math import sqrt

count = int(input())
sample_list = [tuple(map(int, input().split())) for _ in range(count)]

length_list = [sqrt(real**2 + imag**2) for real, imag in sample_list]

print('{:.2f}'.format(max(length_list)))