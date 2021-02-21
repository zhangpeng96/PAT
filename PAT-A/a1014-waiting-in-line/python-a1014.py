"""
    @name     : a1014
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 46'12"
    @accepted : all
"""

class Queue():
    def __init__(self):
        self.q = []
    def pop(self):
        return self.q.pop(0)
    def push(self, val):
        self.q.append(val)
    def front(self):
        return self.q[0]
    def back(self):
        return self.q[-1]

class Customer():
    def __init__(self, cost):
        self.start = 0
        self.end = 0
        self.cost = cost
    def __bool__(self):
        return self.start < 540
    def begin(self, time):
        self.start = time
        self.end = self.start + self.cost
    def get_time(self):
        hour, minute = divmod(self.end, 60)
        return '{:02d}:{:02d}'.format(hour+8, minute)


window_count, queue_count, custom_count, query_count = map(int, input().split())

customer = [ Customer(int(i)) for i in input().split() ]
windows = [ Queue() for _ in range(window_count) ]

for i in range(custom_count):
    # i从0开始，先考虑占满队列的人
    if i < window_count*queue_count:
        # 取余除数是窗口数实现的效果是依次挨个窗口排，保持每个窗口队列均匀
        window = i % window_count
        # 如果人数少于窗口数，也就是队首，前面没有人，所以直接办业务，时间从0开始
        if i < window_count:
            customer[i].begin(0)
        # 如果人数多于窗口数，说明要排队，等到队列最后一个人办结的时间就可以开始办业务
        else:
            customer[i].begin(windows[window].back().end)
        windows[window].push(customer[i])
    # i从0开始，再考虑站在队列外的人
    else:
        window = 0
        for larger in range(1, window_count):
            # 判断编号更大的窗口队首是否更早出队，如果是则选择那个窗口，否则选择最小的1
            if windows[larger].front().end < windows[window].front().end:
                window = larger
        # 选好窗口，就在这个窗口等着最早办结业务的人出队，确定好在哪个窗口排队后也就知道了
        # 什么时候到自己办业务，也就是队列里最后一个人办完业务，就轮到自己了
        customer[i].begin(windows[window].back().end)
        # 办结业务的人出队后队列有空间，那么push进队列
        windows[window].pop()
        windows[window].push(customer[i])

for query in map(lambda x: int(x)-1, input().split()):
    if customer[query]:
        print(customer[query].get_time())
    else:
        print('Sorry')
