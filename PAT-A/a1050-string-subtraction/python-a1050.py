"""
    @name      : a1050
    @version   : 21.0114
    @author    : zhangpeng96
    @test_time : 1'08"
    @pass_rate : all
"""

# s1 = 'They are students.'
# s2 = 'aeiou'

s1 = input()
s2 = input()
print(''.join(filter(lambda x: x not in s2, s1)))
