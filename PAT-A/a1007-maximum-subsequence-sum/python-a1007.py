count = int(input())
digit = list(map(int, input().split()))

left_pos, right_pos = 0, count-1
temp_sum, temp_pos = 0, 0
sum = -1

for i in range(count):
    temp_sum = temp_sum + digit[i]
    if temp_sum < 0:
        temp_sum = 0
        temp_pos = i + 1
    elif temp_sum > sum:
        sum = temp_sum
        left_pos = temp_pos
        right_pos = i

if sum < 0:
    sum = 0

print(sum, digit[left_pos], digit[right_pos])
