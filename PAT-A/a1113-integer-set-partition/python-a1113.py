"""
    @name      : a1113
    @version   : 20.0720
    @author    : zhangpeng96
    @test_time : 7'03"
    @pass_rate : all
"""

# count = int('10')
# digits = sorted(map(int, '23 8 10 99 46 2333 46 1 666 555'.split()))

# count = int('13')
# digits = sorted(map(int, '110 79 218 69 3721 100 29 135 2 6 13 5188 85'.split()))

count = int(input())
digits = sorted(map(int, input().split()))

part = count // 2
print( abs((count-part) - part), abs(sum(digits[:part]) - sum(digits[part:])) )
