
def dfs(root, nodes, depth):
    if not nodes[root]:
        return 
    for node in nodes[root]:
        dfs(node, nodes, depth+1)

nodes = [ [] for _ in range(count) ]
max_depth = 0
for i, k in enumerate(ins):
    nodes[k].append(i)
    if k == -1: root = i

print(root)
for i,node in enumerate(nodes):
    print(i, node)

"""
4
0 []
1 [0]
2 []
3 [7]
4 [2, 3, 5]
5 [1, 6]
6 [8]
7 []
8 [4]

[[], [0], [], [7], [2, 3, 5], [1, 6], [8], [], [4]]
"""
