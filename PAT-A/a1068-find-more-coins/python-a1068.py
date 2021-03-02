"""
    @name     : a1068
    @version  : 20.0725
    @accepted : all
    @source   : https://qsctech-sange.github.io/1068-Find-More-Coins.html
"""

count, target = map(int, input().split())
coins = sorted(map(int, input().split()), reverse=True)

dp = [[] for _ in range(target + 1)]

for coin in coins:
    for money in range(target, coin - 1, -1):
        if dp[money - coin] or money - coin == 0:
            dp[money] = dp[money - coin] + [coin]

if not dp[target]:
    print("No Solution")
else:
    print(*sorted(dp[target]))
