"""
    @name      : a1067
    @version   : 20.0719.2
    @author    : zhangpeng96
    @test_time : >60'00"
    @pass_rate : p1 timeout
"""

insert = input().split()
n = int(insert[0])

count = 0
number = [0] * n
for i, item in enumerate(insert[1:]):
    number[int(item)] = i

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
