"""
    @name     : a1056
    @version  : 21.0214
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

from math import ceil

class Queue:
    def __init__(self, arr=[]):
        self.queue = arr
    def size(self):
        return len(self.queue)
    def front(self):
        return self.queue[0]
    def push(self, val):
        self.queue = self.queue + [val]
    def pop(self):
        self.queue = self.queue[1:]

class Mouse:
    def __init__(self, weight=0):
        self.weight = weight
        self.rank = 0


amount, count = map(int, input().split())
weight = list(map(int, input().split()))
inital = list(map(int, input().split()))

mice = [ Mouse(w) for w in weight ]
match = Queue(inital)

while match.size() > 1:
    candidate = match.size()
    group = ceil(candidate / count)
    greater = match.front()

    for i in range(candidate):
        pointer = match.front()
        if mice[pointer].weight > mice[greater].weight:
            greater = pointer
        mice[pointer].rank = group + 1
        match.pop()

        if not ((i+1) % count) or i == candidate-1:
            match.push(greater)
            greater = match.front()

mice[match.front()].rank = 1

print(*map(lambda x:x.rank, mice))
