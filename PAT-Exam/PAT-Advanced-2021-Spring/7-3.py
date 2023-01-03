from math import inf
from heapq import heappush
from collections import defaultdict

nodes = defaultdict(int)
count, query = map(int, input().split())
ins = map(int, input().split())

def insert_max_heap(arr):
    heap = []
    for value in arr:
        heappush(heap, -value)
    return [ -value for value in heap ]

for i, val in enumerate(insert_max_heap(ins), 1):
    nodes[val] = i

def judge(arg):
    length = len(arg)
    # root
    if length == 4:
        x = nodes[ int(arg[0]) ]
        if x == 1:
            return True
        else:
            return False
    # sbling
    elif length == 5:
        x, y = nodes[ int(arg[0]) ], nodes[ int(arg[2]) ]
        if (x % 2 == 0 and y == x + 1) or (y % 2 == 0 and x == y + 1):
            return True
        else:
            return False
    # parent
    elif length == 6:
        x, y = nodes[ int(arg[0]) ], nodes[ int(arg[5]) ]
        if x == y // 2:
            return True
        else:
            return False
    # children
    elif length == 7:
        x, y = nodes[ int(arg[0]) ], nodes[ int(arg[6]) ]
        if arg[3] == 'left':
            if x == y * 2:
                return True
            else:
                return False
        elif arg[3] == 'right':
            if x == y * 2 + 1:
                return True
            else:
                return False

for _ in range(query):
    arg = input().split()
    if judge(arg):
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
