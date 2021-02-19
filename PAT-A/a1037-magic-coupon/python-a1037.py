"""
    @name     : a1037
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 18'57"
    @accepted : all
    @desc     : https://www.liuchuo.net/archives/2253
"""

count_c = int(input())
coupons = list(map(int, input().split()))

count_p = int(input())
products = list(map(int, input().split()))

coupons.sort()
products.sort()

amount = 0

p, q = 0, 0
while p < count_c and q < count_p and coupons[p] < 0 and products[q] < 0:
    amount += coupons[p] * products[q]
    p += 1
    q += 1

p, q = count_c-1, count_p-1
while p >= 0 and q >= 0 and coupons[p] > 0 and products[q] > 0:
    amount += coupons[p] * products[q]
    p -= 1
    q -= 1

print(amount)
