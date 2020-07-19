"""
    @name      : a1067
    @version   : 20.0719
    @author    : zhangpeng96
    @test_time : >60'00"
    @pass_rate : p1 timeout
"""

insert = list(map(int, input().split()))
n = insert[0]
insert = insert[1:]

count = 0
number = [0] * n
for i, item in enumerate(insert):
    number[item] = i

for i in range(1, len(number)):
    if i != number[i]:
        while number[0] != 0:
            pos = number[0]
            number[0], number[pos] = number[pos], number[0]
            count += 1
        if i != number[i]:
            number[0], number[i] = number[i], number[0]
            count += 1

print(count)
