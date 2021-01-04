'''
    @name      : a1048
    @version   : 21.0104
    @author    : zhangpeng96
    @test_time : 20'00"
    @pass_rate : all
'''

# _, pay = map(int, input().split())
# coins = list(map(int, input().split()))

_, pay = map(int, '8 16'.split())
coins = list(map(int, '9 2 9 8 2 4 11 15'.split()))
coins.sort()
cmap = {}
ans = []

for coin in coins:
    if cmap.get(coin):
        cmap[coin] = cmap[coin] + 1
    else:
        cmap[coin] = 1

for a in cmap.keys():
    b = pay - a
    if a == b:
        if cmap.get(b) > 1:
            ans.append((a, b))
            break
        else:
            continue
    if cmap.get(b) and a <= b:
        ans.append((a, b))
        break

if ans:
    print(ans[0][0], ans[0][1])
else:
    print('No Solution')
