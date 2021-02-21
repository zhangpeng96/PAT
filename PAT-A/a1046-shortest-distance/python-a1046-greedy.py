"""
    @name     : a1046
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 30'00"
    @accepted : all (p2 ~ 72ms)
"""

from itertools import accumulate

distances = map(int, input().split()[1:])
distances = [0] + list(accumulate(distances))

for _ in range(int(input())):
    start, end = map(int, input().split())
    if start > end: start, end = end, start
    path1 = distances[end-1] - distances[start-1]
    path2 = distances[start-1] + distances[-1] - distances[end-1]
    print(min(path1, path2))
