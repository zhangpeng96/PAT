from collections import defaultdict


nodes = defaultdict(int)
node, query = map(int, input().split())
ins = sorted(map(int, input().split()), reverse=True)
for i, n in enumerate(ins, 1):
    nodes[n] = i

for _ in range(query):
    args = input().split()
    if len(args) == 4:
        a = int(args[0])
        x = nodes[a]
        if x == 1:
            print(1, end='')
        else:
            print(0, end='')
    elif len(args) == 5:
        a, b = int(args[0]), int(args[2])
        x, y = nodes[a], nodes[b]
        if (x % 2 == 0 and y == x + 1) or (y % 2 == 0 and x == y + 1):
            print(1, end='')
        else:
            print(0, end='')
    elif len(args) == 6:
        a, b = int(args[0]), int(args[5])
        x, y = nodes[a], nodes[b]
        if x == y // 2:
            print(1, end='')
        else:
            print(0, end='')
    elif len(args) == 7:
        a, b = int(args[0]), int(args[6])
        x, y = nodes[a], nodes[b]
        if args[3] == 'left':
            if a == b * 2:
                print(1, end='')
            else:
                print(0, end='')
        elif args[3] == 'right':
            if a == b * 2 + 1:
                print(1, end='')
            else:
                print(0, end='')

"""
5 6
23 46 26 35 88
35 is the root
46 and 26 are siblings
88 is the parent of 46
35 is the left child of 26
35 is the right child of 46
-1 is the root
"""
