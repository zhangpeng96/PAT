"""
    @name     : a1145
    @version  : 21.0206
    @author   : zhangpeng96
    @time     : 42'45"
    @accepted : all
"""

from math import sqrt

class Hashing():
    def __init__(self, size):
        self.table = []
        self.size = size
        self.search_time = 0
        self.correct_size()

    def prime(self, n):
        if n == 1: return False
        if not n % 2: return n == 2
        if not n % 3: return n == 3
        if not n % 5: return n == 5
        for p in range(7, int(sqrt(n))+1, 2):
            if not n % p: return False
        return True

    def correct_size(self):
        if not self.prime(self.size):
            while not self.prime(self.size):
                self.size += 1
        self.table = [None] * self.size

    def H(self, val):
        return val % self.size

    def probe(self, i):
        return ( self.H(val) + i**2 ) % self.size

    def insert(self, val):
        for i in range(self.size):
            index = self.probe(i)
            if self.table[index] == None:
                self.table[index] = val
                return index
        print('{} cannot be inserted.'.format(val))

    def query(self, val):
        for i in range(self.size):
            self.search_time += 1
            index = self.probe(i)
            if self.table[index] == val or self.table[index] == None:
                return index
        self.search_time += 1


msize, insert_count, query_count = map(int, input().split())
hashes = Hashing(msize)

for val in map(int, input().split()):
    hashes.insert(val)

for val in map(int, input().split()):
    hashes.query(val)

print('{:.1f}'.format(hashes.search_time/query_count))
