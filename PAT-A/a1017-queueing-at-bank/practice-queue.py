from queue import PriorityQueue as PQueue

# 生成 Priority Queue
pq = PQueue()

# 增加元素
pq.put(5)
pq.put(3)
pq.put(2)

# 获得首个元素（不删除）
print(pq.queue[0])

# 循环遍历
while not pq.empty():
    print(pq.get())

