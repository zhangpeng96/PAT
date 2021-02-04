"""
    @name     : a1086
    @version  : 21.0204
    @author   : zhangpeng96
    @time     : 16'24"
    @accepted : all
"""

class Stack():
    def __init__(self):
        self.stack = []
        self.pre_order = []
        self.in_order = []
    def push(self, val):
        self.stack.append(val)
        self.pre_order.append(val)
    def pop(self):
        val = self.stack.pop()
        self.in_order.append(val)
    def command(self, text):
        cmd, *arg = text.split()
        if cmd == 'Push':
            self.push(int(arg[0]))
        elif cmd == 'Pop':
            self.pop()

def create(root, start, end):
    if start > end: return
    i = start
    while i < end and s.in_order[i] != s.pre_order[root]:
        i += 1
    create(root+1, start, i-1)
    create(root+1+(i-start), i+1, end)
    post_traversal.append(s.pre_order[root])


s = Stack()
post_traversal = []

count = int(input())
for _ in range(count*2):
    s.command(input())

create(0, 0, count-1)

print(' '.join(map(str, post_traversal)))
