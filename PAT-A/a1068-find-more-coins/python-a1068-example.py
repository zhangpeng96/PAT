num_coins, target = list(map(int, input().split()))
coins = sorted(list(map(int, input().split())), reverse=True)
dp = [[] for _ in range(target + 1)]

for coin in coins:
    for money in range(target, coin - 1, -1):
        if dp[money - coin] or money - coin == 0:
            dp[money] = dp[money - coin] + [coin]

if not dp[target]:
    print("No Solution")
else:
    print(" ".join(map(str,sorted(dp[target]))))