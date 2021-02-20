"""
    @name     : a1032
    @version  : 21.0220
    @author   : zhangpeng96
    @time     : 33'00"
    @accepted : all
"""

from sys import stdin

data = {}
no_shared = True

head1, head2, count = input().split()
for line in stdin.readlines():
    head, _, rear = line.split()
    data[head] = [rear, False]

while head1 != '-1':
    data[head1][1] = True
    head1 = data[head1][0]

while head2 != '-1':
    if data[head2][1]:
        print(head2)
        no_shared = False
        break
    head2 = data[head2][0]

if no_shared:
    print('-1')
