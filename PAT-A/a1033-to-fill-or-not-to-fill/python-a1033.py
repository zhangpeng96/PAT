"""
    @name     : a1033
    @version  : 21.0301
    @author   : zhangpeng96
    @time     : > 2 days
    @accepted : all (including nowcoder)
"""

class Station():
    def __init__(self, price, dist):
        self.dist = dist
        self.price = price
    def __lt__(self, other):
        if self.dist != other.dist:
            return self.dist < other.dist
        else:
            return self.price < other.price
    def __repr__(self):
        return '{}km {}$'.format(self.dist, self.price)


capacity, distance, per, count = map(float, input().split())
count = int(count)
station = [ Station(*map(float, input().split())) for _ in range(count) ]
# 加一个终点站，防止下标越界
station = sorted(station) + [ Station(0.0, distance) ]
amount, tank = 0.0, 0.0
max_range = per * capacity

# 如果起始位置有加油站
if station[0].dist == 0.0:
    now = 0
    while now < count:
        # 寻找范围内有无加油站，注意这个反逻辑
        flag = False
        for i in range(now+1, count+1):
            if station[i].dist - station[now].dist <= max_range:
                flag = True
                in_rearch = i
        if not flag:
            far_reach = station[now].dist + max_range
            print('The maximum travel distance = {:.2f}'.format(far_reach))
            break
        # 寻找范围内加油站中是否比当前油价更低
        rear = -1
        for i in range(now+1, in_rearch+1):
            if station[i].price < station[now].price:
                rear = i
                break
        # 如果存在比当前油价更低的加油站
        if rear != -1:
            need = (station[rear].dist - station[now].dist) / per
            # 那么只要保证当前的油足够到下一站即可，如果不足需要加油
            if tank < need:
                refuel = need - tank
                amount += refuel * station[now].price
                tank = 0
            # 如果足够，直接到下一站
            else:
                tank -= need
        # 如果不存在比当前油价更低的加油站
        else:
            # 寻找范围内油价最低的加油站
            priceMin = float('inf')
            for i in range(now+1, in_rearch+1):
                if station[i].price < priceMin:
                    priceMin = station[i].price
                    rear = i
            # 因为没有比当前油价便宜，所以直接加满油
            refuel = capacity - tank
            amount += refuel * station[now].price
            # 计算到下一站需要的油，也就是油箱消耗的油（有范围限制不用考虑下限）
            need = (station[rear].dist - station[now].dist) / per
            tank = capacity - need
        # 到一下站
        now = rear
    # 循环结束后，如果当前站在终点站（即第count+1的下标）那么到站了
    if now == count:
        print('{:.2f}'.format(amount))
# 起始位置没有加油站，寸步难行
else:
    print('The maximum travel distance = 0.00')
