"""
    @name     : a1076
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p0, p1 error, p4 timeout
"""

from collections import defaultdict

def bfs(query):
    count = 0
    visited, layer = defaultdict(bool), defaultdict(int)
    queue, visited[query], layer[query] = [query], True, 0
    while queue:
        curr = queue[0]
        queue.pop(0)
        for rear in net[curr]:
            layer[rear] = layer[curr] + 1
            if (not visited[rear]) and (layer[rear] <= level_limit):
                queue.append(rear)
                visited[rear] = True
                count += 1
    return count


net = defaultdict(list)
count, level_limit = map(int, input().split())
for i in range(1, count+1):
    for follower in map(int, input().split()[1:]):
        net[follower].append(i)

# print(net)

for query in map(int, input().split()[1:]):
    print(bfs(query))
