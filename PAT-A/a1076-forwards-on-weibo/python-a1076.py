"""
    @name     : a1076
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
"""

from sys import stdin

def bfs(query, length):
    count = 0
    visited, layer = [False] * (length+1), [0] * (length+1)
    queue, visited[query], layer[query] = [query], True, 0
    while queue:
        curr = queue[0]
        queue.pop(0)
        for rear in net[curr]:
            if not visited[rear]:
                layer[rear] = layer[curr] + 1
                if layer[rear] <= layer_limit:
                    queue.append(rear)
                    visited[rear] = True
                    count += 1
    return count


length, layer_limit = map(int, input().split())
net = [ [] for _ in range(length+1) ]

lines = stdin.readlines()
for i, line in enumerate(lines[:-1], 1):
    for follower in map(int, line.split()[1:]):
        net[follower].append(i)

for query in map(int, lines[-1].split()[1:]):
    print(bfs(query, length))
