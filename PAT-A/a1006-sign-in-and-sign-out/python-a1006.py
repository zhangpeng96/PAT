'''
    @name      : a1006
    @version   : 20.0602
    @author    : zhangpeng96
    @test_time : 11'08"
    @pass_rate : all
'''

from datetime import datetime

# count = int(input())
# records = [input() for _ in range(count)]

records = ['CS301111 15:30:28 17:00:10','SC3021234 08:00:00 11:25:25','CS301133 21:45:00 21:58:40']
unlocks = {}
locks = {}

for record in records:
    name, sign_in, sign_out = record.split()
    unlocks[name] = datetime.strptime(sign_in, '%H:%M:%S')
    locks[name] = datetime.strptime(sign_out, '%H:%M:%S')

print(
    sorted(unlocks.items(), key = lambda x:x[1])[0][0],
    sorted(locks.items(), key = lambda x:x[1])[-1][0]
)
