'''
    @name      : a1017
    @version   : 20.0717.2
    @author    : zhangpeng96
    @test_time : >60'00"
    @pass_rate : all
'''

from queue import PriorityQueue as PQueue

# n, k = map(int, '7 3'.split())
# customers = ['07:55:00 16', '17:00:01 2', '07:59:59 15', '08:01:00 60', '08:00:00 30', '08:00:02 2', '08:03:00 10']

n, k = map(int, input().split())
customers = [input() for _ in range(n)]


def time_second(strs):
    hour, minute, second = map(int, strs.split(':'))
    return hour*3600 + minute*60 + second

window = PQueue()
[window.put(8*3600) for _ in range(k)]

customers = map(lambda x: ( time_second(x.split()[0]), int(x.split()[1])*60 ), customers)
customers = sorted(filter(lambda x:x[0] <= 61200, customers), key=lambda x: x[0])

wait_time = 0

for start, duration in customers:
    wait = window.queue[0]
    if wait <= start:
        window.put(start + duration)
        window.get()
        # print('n', wait, start, start+duration)
    else:
        wait_time += wait-start
        window.put(wait + duration)
        window.get()
        # print('a', wait, wait-start, wait+duration)

print('{:.1f}'.format(wait_time/(len(customers)*60)))
