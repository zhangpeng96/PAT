"""
    @name     : a1097
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 31'00"
    @accepted : p3, p4 timeout
"""

from sys import stdin

def print_sorted_linked(ll):
    # p2 要考虑没有重复值的情况，也就是结果链表为空
    if ll:
        for i in range(len(ll)-1):
            print('{} {} {}'.format(*ll[i], ll[i+1][0]))
        print('{} {} -1'.format(*ll[-1]))


head, count = input().split()
key_pool = set()
linked = {}
unique_linked, duplicate_linked = [], []

for line in stdin.readlines():
    address, *value = line.split()
    linked[address] = value

while head != '-1':
    key, succr = linked[head]
    absolute = abs(int(key))
    if absolute in key_pool:
        duplicate_linked.append([head, key])
    else:
        unique_linked.append([head, key])
    key_pool.add(absolute)
    head = succr

print_sorted_linked(unique_linked)
print_sorted_linked(duplicate_linked)
