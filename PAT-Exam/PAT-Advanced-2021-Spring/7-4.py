from copy import copy

spot, route = map(int, input().split())
adj = [ [] for _ in range(spot+1) ]
visited = [False] * (spot+1)
dist = {}
for _ in range(route):
    start, end, length = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
    dist[start, end] = dist[end, start] = length

for i in range(spot+1):
    adj[i].sort()

def dfs(root, temp_path):
    visited[root] = True
    if all(visited):
        path = copy(temp_path)
        return
    for node in adj[root]:
        if not visited[node]:
            temp_path.append(node)
            dfs(node, temp_path)
            temp_path.pop()

path = []
dfs(0, [])
print(*path)

"""
7 10
0 2 1
0 4 5
0 7 3
0 6 4
0 5 5
1 2 2
1 7 2
2 3 4
3 4 2
6 7 9
--
0 2 1 7 6 3 4 5
33
--
7 8
0 2 1
0 4 5
0 7 3
1 2 2
1 7 2
2 3 4
3 4 2
6 5 1
--
0 2 1 7 3 4
5 6
"""