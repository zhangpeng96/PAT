"""
    @name      : a1051
    @version   : 21.0115
    @author    : zhangpeng96
    @test_time : > 60'00"
    @pass_rate : all
"""

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return not bool(self.stack)

def judge(cap, std, ins):
    ptr = 0
    for e in std:
        s.push(e)
        if s.size() > cap: 
            return False
        while (not s.empty()) and (s.top() == ins[ptr]):
            p = s.pop()
            ptr += 1
            print('s:',s.stack, 'ptr:', ptr, 'pop:', p)
    if len(std) == ptr:
        return True
    else:
        return False

m, n, count = map(int, input().split())
std = [i+1 for i in range(n)]

for _ in range(count):
    s = Stack()
    ins = list(map(int, input().split()))
    if judge(m, std, ins):
        print('YES')
    else:
        print('NO')
