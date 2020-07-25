"""
    @name      : a1078
    @version   : 20.0721
    @author    : zhangpeng96
    @test_time : 30'00"
    @pass_rate : p3 timeout
"""

from math import sqrt

def is_prime(n):
    if n == 1: return False
    if not n % 2: return n == 2
    if not n % 3: return n == 3
    if not n % 5: return n == 5
    for p in range(7, int(sqrt(n))+1, 2):
        if not n % p: return False
    return True

def correct_size(size):
    if is_prime(size):
        return size
    else:
        while not is_prime(size):
            size += 1
        return size

def insert(size, key):
    for i in range(size):
        index = (key + size**2) % size
        if not hashes[index]:
            hashes[index] = True
            result.append(str(index))
            return
    result.append('-')

size, count = map(int, '4 4'.split())
keys = map(int, '10 6 4 15'.split())

size = correct_size(size)
hashes = [False] * size
result = []

[insert(size, key) for key in keys]
print(' '.join(result))