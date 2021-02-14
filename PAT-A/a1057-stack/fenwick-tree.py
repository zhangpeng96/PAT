

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    def __repr__(self):
        return ' '.join(map(lambda x: '[{}]{}'.format(*x), enumerate(self.tree,1)))

    def lowbit(self, x):
        return x & (-x)

    # 单点更新
    def update(self, pos, val):
        while pos <= self.n:
            self.tree[pos] += val
            pos += self.lowbit(pos)

    def build(self, lst):
        for pos, val in enumerate(lst, 1):
            self.update(pos, val)

    def sum(self, pos):
        amount = 0
        while pos:
            amount += self.tree[pos]
            pos -= self.lowbit(pos)
        return amount


cnt = [1,2,3,4,5,6,7,8,9,10]
fenwick = FenwickTree(100000)
# print(fenwick)
fenwick.build(cnt)
# print(fenwick)

for i in range(1, 11):
    print(i, fenwick.sum(i))