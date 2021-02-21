"""
    @name     : a1046
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : 15'00"
    @accepted : all
"""

distances = [0] + list(map(int, input().split()[1:]))

for _ in range(int(input())):
    start, end = map(int, input().split())
    if start > end: start, end = end, start
    path1 = sum( distances[start:end] )
    path2 = sum( distances[end:] + distances[:start] )
    print(min(path1, path2))
