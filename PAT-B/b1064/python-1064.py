'''
    @name      : b1064
    @version   : 20.0522
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
'''

from itertools import combinations
count = int(input())
digits = tuple(input().split())

# digits = tuple('123 899 51 998 27 33 36 12'.split())

friends = set()

def decision(a, b):
    sum_a = sum(map(int, a))
    if sum_a == sum(map(int, b)):
        return sum_a
    else:
        return False

for digit_a, digit_b in combinations(digits, r = 2):
    friend = decision(digit_a, digit_b)
    print(digit_a, digit_b, sum(map(int, digit_a)))
    if friend:
        friends.add(friend)

print(len(friends))
print(' '.join(map(str, sorted(friends))))