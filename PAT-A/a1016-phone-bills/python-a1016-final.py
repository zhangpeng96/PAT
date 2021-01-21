"""
    @name     : a1016
    @version  : 21.0121
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p1,p2,p3 error
"""

def fee(start, end):
    period = '{} {}'.format(start.split(':',1)[1], end.split(':',1)[1])
    start = list(map(int, start.split(':')))
    end = list(map(int, end.split(':')))
    part = 60-start[-1] + end[-1]
    start_h = start[1] * 24 + start[2] + 1
    end_h = end[1] * 24 + end[2]
    minute = (end_h - start_h)*60 + part
    part_fee = (60-start[-1]) * price[start[-2]] + end[-1] * price[end[-2]]
    amount = sum([price[hour % 24] * 60 for hour in range(start_h, end_h)])
    amount = (amount + part_fee) / 100
    print('{} {} ${:.2f}'.format(period, minute, amount))
    return amount


record = {}

price = list(map(int, input().split() ))
count = int(input())
for _ in range(count):
    name, date, state = input().split()
    if name not in record:
        record[name] = []
    record[name].append([date, state])

record = sorted(record.items(), key=lambda x: x[0])

for name, rec in record:
    i, amount = 0, 0.0
    rec.sort(key=lambda x:x[0])
    month = rec[0][0].split(':')[0]
    print(name, month)
    while i < len(rec)-1:
        if rec[i][1] == 'on-line' and rec[i+1][1] == 'off-line':
            dail_amount = fee(rec[i][0], rec[i+1][0])
            amount += dail_amount
            i += 2
            continue
        i += 1
    print('Total amount: ${:.2f}'.format(amount))
