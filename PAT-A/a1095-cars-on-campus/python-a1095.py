"""
    @name     : a1095
    @version  : 21.0223
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p1,p2,p4 timeout
"""

from sys import stdin
from collections import defaultdict

def time_to_int(string):
    h, m, s = map(int, string.split(':'))
    return h*3600 + m*60 + s

def int_to_time(integer):
    h, _ = divmod(integer, 3600)
    m, s = divmod(_, 60)
    return '{:02}:{:02}:{:02}'.format(h, m, s)


record_count, query_count = map(int, input().split())
record_pair = []
record = defaultdict(list)
park_time = defaultdict(int)
lines = stdin.readlines()

for line in lines[:record_count]:
    plate, times, io = line.split()
    record[plate].append( (time_to_int(times), io) )

for plate, group in record.items():
    i = 0
    group.sort(key=lambda x:x[0])
    while i < len(group)-1:
        if group[i][1] == 'in' and group[i+1][1] == 'out':
            record_pair.append( (plate, group[i][0], group[i+1][0]) )
            park_time[plate] += (group[i+1][0] - group[i][0])
            i += 2
        else:
            i += 1

for line in lines[record_count:]:
    count = 0
    query = time_to_int(line)
    for _, inside, outside in record_pair:
        if inside <= query < outside:
            count += 1
    print(count)

park_time_max = max(park_time.values())
park_id_max = [k for k, v in park_time.items() if v == park_time_max]
print(*park_id_max, int_to_time(park_time_max))
