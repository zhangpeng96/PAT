"""
    @name     : a1052
    @version  : 21.0208
    @author   : zhangpeng96
    @time     : 45'00"
    @accepted : p3 timeout
    @desc     : p4要考虑筛选后的链表为空的情况
"""

from sys import stdin

count, head = input().split()

link_list = {}
for line in stdin.readlines():
    address, data, succr = line.split()
    link_list[address] = [int(data), succr, False]

order = 0
while head != '-1':
    order += 1
    link_list[head][2] = True
    head = link_list[head][1]

link_list = sorted(filter(lambda x:x[1][2], link_list.items()), key=lambda x:x[1][0])

if link_list:
    print(order, link_list[0][0])
    for i in range(order-1):
        print('{} {} {}'.format(link_list[i][0], link_list[i][1][0], link_list[i+1][0]))
    print('{} {} -1'.format(link_list[order-1][0], link_list[order-1][1][0]))
else:
    print('0 -1')
