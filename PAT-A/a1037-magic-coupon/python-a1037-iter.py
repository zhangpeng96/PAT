"""
    @name     : a1037
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 18'57"
    @accepted : all
"""

count_c = int(input())
coupons = sorted(map(int, input().split()))

count_p = int(input())
products = sorted(map(int, input().split()))

amount = 0
length = min(count_c, count_p)


coupon, product = iter(coupons), iter(products)
for _ in range(length):
    p, q = next(coupon), next(product)
    if p < 0 and q < 0:
        amount += p * q

coupon, product = reversed(coupons), reversed(products)
for _ in range(length):
    p, q = next(coupon), next(product)
    if p > 0 and q > 0:
        amount += p * q

print(amount)
