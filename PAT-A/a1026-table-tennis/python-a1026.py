"""
    @name     : a1026
    @version  : 21.0308
    @author   : zhangpeng96
    @time     : ~4h
    @accepted : p1,p2,p8 error
"""

from math import ceil


def time_to_second(string):
    h, m, s = map(int, string.split(':'))
    return h*3600 + m*60 + s

def second_to_time(integer):
    h, ms = divmod(integer, 3600)
    m, s = divmod(ms, 60)
    return '{:02}:{:02}:{:02}'.format(h, m, s)

class Queue():
    def __init__(self):
        self.q = []
    def __bool__(self):
        return bool(self.q)
    def __repr__(self):
        return '[\n' + ' '.join(map(str, self.q)) + '\n]'
    def empty(self):
        return not bool(self.q)
    def pop(self):
        return self.q.pop(0)
    def push(self, val):
        self.q.append(val)
    def front(self):
        return self.q[0]
    def back(self):
        return self.q[-1]

class Table():
    def __init__(self, vip=False):
        self.arrive = 8*3600
        self.count = 0
        self.vip = vip
    def __lt__(self, other):
        return self.arrive < other.arrive
    def __le__(self, other):
        return self.arrive <= other.arrive
    def __repr__(self):
        return 'VIP:{}, {}\n'.format(self.vip, second_to_time(self.arrive))

class Customer():
    def __init__(self, arrive, using, vip):
        self.arrive = arrive
        self.serve = 0
        self.using = using
        self.wait = 0
        self.vip = bool(vip)
    def __lt__(self, other):
        return self.arrive < other.arrive
    def __le__(self, other):
        return self.arrive <= other.arrive
    def __repr__(self):
        return 'VIP:{}, {}->{}\n'.format(self.vip, second_to_time(self.arrive), second_to_time(self.using))


customer, q_vip, q_normal = [], Queue(), Queue()
result = []

for _ in range(int(input())):
    time, use, vip = input().split()
    use = 120*60 if int(use) > 120 else int(use)*60
    customer.append( Customer(time_to_second(time), use, int(vip)) )

table_count, vip_count = map(int, input().split())
vip_index = list(map(lambda x: int(x)-1, input().split()))

table = [ Table() for _ in range(table_count) ]
for index in vip_index:
    table[index].vip = True

for custom in sorted(customer):
    if custom.vip:
        q_vip.push(custom)
    else:
        q_normal.push(custom)


while q_vip or q_normal:
    # 找即将服务完成的桌子
    next_all_table = min(range(table_count), key=lambda x:table[x])
    next_vip_table = min(iter(vip_index), key=lambda x:table[x])
    # 选桌子
    if (q_vip and q_normal and q_vip.front() < q_normal.front() and table[next_vip_table] <= q_vip.front()) or\
       (q_normal.empty() and table[next_vip_table] <= q_vip.front()):
        next_table_index = next_vip_table
    else:
        next_table_index = next_all_table
    next_table = table[next_table_index]

    if q_vip.empty():
        next_custom = q_normal.front()
        q_normal.pop()
    elif q_normal.empty() or q_vip.front() < next_table:
        next_custom = q_vip.front()
        q_vip.pop()
    else:
        if q_vip.front() < q_normal.front():
            next_custom = q_vip.front()
            q_vip.pop()
        else:
            next_custom = q_normal.front()
            q_normal.pop()
    # 什么时候开始服务，取决于用户时间和球桌空闲时间
    if next_custom < next_table:
        next_custom.serve = next_table.arrive
        next_custom.wait = next_table.arrive - next_custom.arrive
    else:
        next_custom.serve = next_custom.arrive
    if next_custom.serve >= 21 * 3600: continue

    table[next_table_index].arrive = next_custom.serve + next_custom.using
    table[next_table_index].count += 1
    result.append(next_custom)


for custom in result:
    print('{} {} {}'.format(second_to_time(custom.arrive), second_to_time(custom.serve), ceil(custom.wait/60)))

print(*[ t.count for t in table])
