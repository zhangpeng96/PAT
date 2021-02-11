"""
    @name     : 7-5
    @version  : 21.0209
    @author   : zhangpeng96
    @time     : 54'12"
    @accepted : p0 right +12
                p1 right +3
                p2 right +1
                p3 right +3
                p4 timeout
"""

class Node:
    def __init__(self, data, succr):
        self.data = data
        self.next = succr
        self.order = 9999999

def length(link, head):
    count = 0
    while head != '-1':
        head = link[head].next
        count += 1
    return count

def reverse(link, head):
    precr, succr = head, link[head].next
    while succr != '-1':
        next_succr = link[succr].next
        link[succr].next = precr
        precr, succr = succr, next_succr
    link[head].next = '-1'
    return precr

link = {}

head1, head2, count = input().split()
count = int(count)
for _ in range(count):
    head, *node = input().split()
    link[head] = Node(*node)

length1, length2 = length(link, head1), length(link, head2)

if length1 < length2:
    head1, head2 = head2, head1
    length1, length2 = length2, length1

count = length1 + length2
head2 = reverse(link, head2)

for i in range(1, count+1):
    if ((i % 3 != 0) and head1 != '-1') or (head2 == '-1' and head1 != '-1'):
        link[head1].order = i
        head1 = link[head1].next
    if (i % 3 == 0) and head2 != '-1':
        link[head2].order = i
        head2 = link[head2].next
        
link = sorted(link.items(), key=lambda x:x[1].order)
for i in range(count-1):
    print('{} {} {}'.format(link[i][0], link[i][1].data, link[i+1][0]))
print('{} {} -1'.format(link[count-1][0], link[count-1][1].data))
