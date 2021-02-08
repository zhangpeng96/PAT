"""
    @name     : a1074
    @version  : 21.0208
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p5 timeout
"""

def link_output(ll, head):
    if head in ll:
        while head != '-1':
            print('{} {} {}'.format(head, ll[head][0], ll[head][1]))
            head = ll[head][1]

def link_length(ll, head):
    length = 0
    if head in ll:
        while head != '-1':
            length += 1
            head = ll[head][1]
    return length

def link_tail(ll, head):
    tail = '-1'
    if head in ll:
        while head != '-1':
            tail = head
            head = ll[head][1]
    return tail

def partition_reverse(ll, head, length):
    count = 1
    precr, succr = head, ll[head][1]
    while succr != '-1' and count < length:
        next_reverse = ll[succr][1]
        ll[succr][1] = precr
        precr, succr = succr, next_reverse
        count += 1
    ll[head][1] = '-1'
    return precr, succr


link_list = {}
head, count, k = input().split()
count, k = int(count), int(k)

for _ in range(count):
    name, data, succr = input().split()
    link_list[name] = [data, succr]

count = link_length(link_list, head)

for i in range(count//k):
    part_head, head = partition_reverse(link_list, head, k)
    if i:
        link_list[prev_tail][1] = part_head
    else:
        combined_head = part_head
    prev_tail = link_tail(link_list, part_head)
link_list[prev_tail][1] = head

link_output(link_list, combined_head)
