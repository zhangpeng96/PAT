'''
    @name      : b1093
    @version   : 20.0511
    @author    : zhangpeng96
    @test_time : 24'32"
    @pass_rate : all
'''

from collections import Counter

# str1 = 'This is a sample test'
# str2 = 'to show you_How it works'

str1 = input()
str2 = input()

def replace_except_first(strs, char_tuple):
    strs = strs[::-1]
    for char, count in char_tuple:
        strs = strs.replace(char, '', count-1)
    return strs[::-1]

def repeat_counter(strs):
    return list(filter(lambda x: x[1] > 1, Counter(strs).items()))

str0 = str1 + str2

print(
    replace_except_first(str0, repeat_counter(str0))
)
