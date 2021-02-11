"""
    @name     : a1047
    @version  : 21.0119
    @author   : zhangpeng96
    @time     : 41'07"
    @accepted : p0 error
                p1 right +1
                p2 timeout
                p3 error
                p4 timeout
"""

# from math import sqrt

def judge(a, b):
    if ( 3*a*a - 3*a + 1) == ( (2*b*b - 2*b + 1) * (2*b*b - 2*b + 1) ):
        return True
    else:
        return False

start, end = map(int, input().split())
solution = False

for a in range(start, end+1):
    for b in range( int(pow( ( 3*a*a - 3*a + 1)//4, 0.25)) ):
        if judge(a, b):
            print(a, b)
            solution = True

if not solution:
    print('No Solution')
