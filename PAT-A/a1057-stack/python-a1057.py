"""
    @name     : a1057
    @version  : 21.0216
    @author   : zhangpeng96
    @time     : >120'00"
    @accepted : p1~p3 timeout
"""

MAXN = 100000

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, pos, val):
        while pos <= self.n:
            self.tree[pos] += val
            pos += self.lowbit(pos)

    def sum(self, pos):
        amount = 0
        while pos:
            amount += self.tree[pos]
            pos -= self.lowbit(pos)
        return amount


class Stack():
    def __init__(self):
        self.s = []

    def not_empty(self):
        return bool(self.s)

    def size(self):
        return len(self.s)

    def push(self, val):
        self.s.append(val)

    def pop(self):
        p = self.s.pop()
        return p


def bisect(x, low=1, high=MAXN):
    while low < high:
        mid = (low + high)//2
        if x <= fenwick.sum(mid):
            high = mid
        else:
            low = mid + 1
    return low

def peek_median():
    median = (stack.size() + 1) // 2
    return bisect(median)


count = int(input())
stack = Stack()
fenwick = FenwickTree(MAXN)


for _ in range(count):
    command, *arg = input().split()

    if command == 'Pop':
        if stack.not_empty():
            val = stack.pop()
            print(val)
            fenwick.update(val, -1)
        else:
            print('Invalid')

    elif command == 'Push':
        val = int(arg[0])
        stack.push(val)
        fenwick.update(val, 1)

    elif command == 'PeekMedian':
        if stack.not_empty():
            print(peek_median())
        else:
            print('Invalid')

    else:
        print('Invalid')
