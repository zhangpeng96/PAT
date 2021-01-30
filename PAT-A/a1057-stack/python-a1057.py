"""
    @name     : a1057
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 54'00"
    @accepted : p1~p3 timeout, p4 error
"""

class Stack():
    def __init__(self):
        self.s = []
    def push(self, val):
        self.s.append(val)
    def pop(self):
        p = self.s.pop()
        print(p)
    def peek(self):
        n = len(self.s)
        if n % 2:
            p = sorted(self.s)[ (n+1)//2-1 ]
        else:
            p = sorted(self.s)[ n//2-1 ]
        print(p)

count = int(input())
stack = Stack()
for _ in range(count):
    command, *arg = input().split()
    if command == 'Pop':
        try:
            stack.pop()
        except:
            print('Invalid')
    elif command == 'PeekMedian':
        try:
            stack.peek()
        except:
            print('Invalid')
    elif command == 'Push':
        stack.push(arg[0])
    else:
        print('Invalid')
