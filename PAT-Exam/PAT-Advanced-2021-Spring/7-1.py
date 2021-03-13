from math import sqrt

def prime(n):
    if n == 1: return False
    if not n % 2: return n == 2
    if not n % 3: return n == 3
    if not n % 5: return n == 5
    for i in range(7, int(sqrt(n))+1, 2):
        if not n % i: return False
    return True

number, end = map(int, input().split())
primes = [ i for i in range(2, end) if prime(i) ]
for p in primes:
    print(p)

"""
5 1000
23 263 503 743 983
--
10 200
199
"""

