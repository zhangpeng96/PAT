"""
    @name     : a1032
    @version  : 21.0220
    @author   : zhangpeng96
    @time     : 33'00"
    @accepted : p5 timeout
"""

from sys import stdin

class Node():
    def __init__(self, rear):
        self.next = rear
        self.visited = False

data = {}
no_shared = True

head1, head2, count = input().split()
for _ in range(int(count)):
    head, _, rear = input().split()
    data[head] = Node(rear)

while head1 != '-1':
    data[head1].visited = True
    head1 = data[head1].next

while head2 != '-1':
    if data[head2].visited:
        print(head2)
        no_shared = False
        break
    head2 = data[head2].next

if no_shared:
    print('-1')
