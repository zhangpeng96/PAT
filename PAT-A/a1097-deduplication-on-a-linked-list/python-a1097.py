"""
    @name     : a1097
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 31'00"
    @accepted : p3, p4 timeout
"""

def print_sorted_linked(ll):
    # p2 要考虑没有重复值的情况，也就是结果链表为空
    if ll:
        for i in range(len(ll)-1):
            print('{} {} {}'.format(*ll[i], ll[i+1][0]))
        print('{} {} -1'.format(*ll[-1]))


header, count = input().split()
key_pool = set()
linked = {}
unique_linked, duplicate_linked = [], []

for _ in range(int(count)):
    address, key, succr = input().split()
    linked[address] = [int(key), succr, False]

head = header
while head != '-1':
    value, succr, _ = linked[head]
    value_a = abs(value)
    if value_a in key_pool:
        duplicate_linked.append([head, value])
    else:
        unique_linked.append([head, value])
    key_pool.add(value_a)
    head = succr

print_sorted_linked(unique_linked)
print_sorted_linked(duplicate_linked)
