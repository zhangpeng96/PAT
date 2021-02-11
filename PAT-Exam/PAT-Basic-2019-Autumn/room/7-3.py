"""
    @name     : a1047
    @version  : 21.0119
    @author   : zhangpeng96
    @time     : 41'07"
    @accepted : p0 timeout
                p1 timeout
                p2 timeout
                p3 error
                p4 timeout
"""

from itertools import permutations

def judge(a, b):
    if a**3 - (a-1)**3 == (b**2 + (b-1)**2)**2:
        return True
    else:
        return False

start, end = map(int, input().split())
solution = False

for a, b in permutations(range(start, end+1), 2):
    if judge(a, b):
        print(a, b)
        solution = True

if not solution:
    print('No Solution')
