"""
    @name     : 7-4
    @version  : 21.0209
    @author   : zhangpeng96
    @time     : 30'35"
    @accepted : p0 timeout
                p1 right +2
                p2 timeout
                p3 timeout
"""

from math import gcd, sqrt

def prime(n):
    if n == 1: return False
    if not n % 2: return False
    if not n % 3: return n == 3
    if not n % 5: return n == 5
    for p in range(7, int(sqrt(n))+1, 2):
        if not n % p: return False
    return True

def judge(a, m):
    am = sum(map(int, str(a)))
    if am == m:
        an = sum(map(int, str(a+1)))
        if prime(gcd(am, an)):
            return an
    return False

count = int(input())
cases = [map(int, input().split()) for _ in range(count)]

for i, (k, m) in enumerate(cases):
    print('Case {}'.format(i+1))
    result = []
    for a in range(pow(10, k-1), pow(10, k)):
        n = judge(a, m)
        if n: result.append( (n, a) )
    if result:
        for res in sorted(result, key=lambda x: (x[0], x[1])):
            print(*res)
    else:
        print('No Solution')



