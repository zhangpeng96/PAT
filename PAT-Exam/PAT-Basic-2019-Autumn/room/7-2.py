"""
    @name     : 7-2
    @version  : 21.0209
    @author   : zhangpeng96
    @time     : 6'56"
    @accepted : all
"""

count = int(input())
records = []

for _ in range(count):
    sn, price, amount = input().split()
    amount = int(amount)
    total = int(price)*amount
    records.append( (sn, amount, total) )

records.sort(key=lambda x:x[1], reverse=True)
print(records[0][0], records[0][1])

records.sort(key=lambda x:x[2], reverse=True)
print(records[0][0], records[0][2])