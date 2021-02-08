"""
    @name     : b1075
    @version  : 21.0208
    @author   : zhangpeng96
    @time     : 60'00"
    @accepted : p5 timeout
"""

# from sys import stdin

head, count, k = input().split()
count, k = int(count), int(k)

# lines = stdin.readlines()
# link_list = dict( zip(map(lambda x:x.split()[0], lines), map(lambda x:x.split()[1:], lines)) )
link_list = {}
for _ in range(count):
    address, data, succr = input().split()
    link_list[address] = [int(data), succr, 9999999]

order = 0
succr = head
while succr != '-1':
    if link_list[succr][0] < 0:
        link_list[succr][2] = order
        order += 1
    succr = link_list[succr][1]

succr = head
while succr != '-1':
    if 0 <= link_list[succr][0] <= k:
        link_list[succr][2] = order
        order += 1
    succr = link_list[succr][1]

succr = head
while succr != '-1':
    if link_list[succr][0] > k:
        link_list[succr][2] = order
        order += 1
    succr = link_list[succr][1]

link_list = sorted(link_list.items(), key=lambda x:x[1][2])

for i in range(order-1):
    print('{} {} {}'.format(link_list[i][0], link_list[i][1][0], link_list[i+1][0]))
print('{} {} -1'.format(link_list[order-1][0], link_list[order-1][1][0]))
