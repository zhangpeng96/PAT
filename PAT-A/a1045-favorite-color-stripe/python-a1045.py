"""
    @name     : a1045
    @version  : 21.0302
    @author   : zhangpeng96
    @time     : 
    @accepted : p3, p4 timeout
"""

_ = input()
a, ans = [], 0
color_map = [0] * 201

for pos, color in enumerate(map(int, input().split()[1:]), 1):
    color_map[color] = pos

for color in map(int, input().split()[1:]):
    if color_map[color]:
        a.append(color_map[color])

count = len(a)
dp = [0] * count

for i in range(count):
    dp[i] = 1
    for j in range(i):
        if a[i] >= a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(dp[i], ans)

print(ans)
