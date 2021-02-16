"""
    @name     : b1020/a1070
    @version  : 21.0216
    @author   : zhangpeng96
    @time     : 15'30"
    @accepted : all
"""

class mookcake:
    def __init__(self, amount, price):
        self.price = price
        self.amount = amount
        self.unit = price / amount 


count, demand = input().split()
count, demand = int(count), float(demand)
amounts = map(float, input().split())
prices = map(float, input().split())

cakes = map(lambda a,p: mookcake(a, p), amounts, prices)
cakes = sorted(cakes, key=lambda x:x.unit, reverse=True)

total = 0.0

for cake in cakes:
    if cake.amount >= demand:
        total += cake.unit * demand
        break
    else:
        total += cake.price
        demand -= cake.amount

print('{:.2f}'.format(total))
