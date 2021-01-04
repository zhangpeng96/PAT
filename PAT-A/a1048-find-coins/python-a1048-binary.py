'''
    @name      : a1048
    @version   : 21.0104
    @author    : zhangpeng96
    @test_time : 12'00"
    @pass_rate : p3,p4 timeout
'''

# _, pay = map(int, input().split())
# coins = list(map(int, input().split()))

_, pay = map(int, '8 15'.split())
coins = list(map(int, '1 2 8 7 2 4 11 15'.split()))

coins.sort()
ans = []

def binary_search(coins, b, i):
    low = i + 1
    high = len(coins) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if coins[mid] == b:
            return b
        elif coins[mid] > b:
            high = mid - 1
        else:
            low = mid + 1
    return -1

for i, coin in enumerate(coins):
    b = pay - coin
    search = binary_search(coins, b, i)
    if search != -1:
        ans = [coin, search]
        break

if ans:
    print(ans[0], ans[1])
else:
    print('No Solution')
