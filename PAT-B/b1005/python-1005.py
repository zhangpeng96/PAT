'''
    @name      : b1005
    @version   : 20.0525
    @author    : zhangpeng96
    @test_time : 24'36"
    @pass_rate : all
'''

def decision(digit):
    digits = []
    while digit != 1:
        digit = (3 * digit + 1) // 2 if digit % 2 else digit // 2
        digits.append(digit)
    return digits

count = int('3')
digits = tuple(map(int, '3 5 6 7 8 11'.split()))

# count = int(input())
# digits = tuple(map(int, input().split()))

covered = []
for i in digits:
    covered.extend(decision(i))

keys = sorted(set(digits) - set(covered), reverse = True)
print(' '.join(map(str, keys)))
