"""
    @name      : a1067
    @version   : 21.0126
    @author    : zhangpeng96
    @test_time : >60'00"
    @pass_rate : all
"""

n, *insert = input().split()
n, insert = int(n), map(int, insert)

number = [0] * n
for i, dig in enumerate(insert):
    number[dig] = i

count = 0
for i in range(1, n):
    if i != number[i]:
        while number[0] != 0:
            pos = number[0]
            number[0], number[pos] = number[pos], number[0]
            count += 1
        if i != number[i]:
            number[0], number[i] = number[i], number[0]
            count += 1

print(count)
