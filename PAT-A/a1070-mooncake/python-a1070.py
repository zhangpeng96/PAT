"""
    @name      : a1070
    @version   : 20.0719
    @author    : zhangpeng96
    @test_time : 25'00"
    @pass_rate : all
"""

# count, demand = '3 200'.split()
# count, demand = int(count), float(demand)
# amounts = map(float, '180 150 100'.split())
# prices = map(float, '7.5 7.2 4.5'.split())


count, demand = input().split()
count, demand = int(count), float(demand)
amounts = map(float, input().split())
prices = map(float, input().split())


cakes = sorted(map(lambda a,p: {'unit': p/a, 'price': p, 'amount': a}, amounts, prices), key=lambda x:x['unit'], reverse=True)
total = 0.0

for cake in cakes:
    if cake['amount'] >= demand:
        total += cake['unit'] * demand
        break
    else:
        total += cake['price']
        demand -= cake['amount']

print('{:.2f}'.format(total))
