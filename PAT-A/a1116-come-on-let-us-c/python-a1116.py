"""
    @name     : a1116
    @version  : 21.0128
    @author   : zhangpeng96
    @time     : 24'12"
    @accepted : all
"""

from math import sqrt

def prime(n):
    if n == 1: return False
    if not n % 2: return n == 2
    if not n % 3: return n == 3
    for p in range(5, int(sqrt(n))+1, 2):
        if not n % p: return False
    return True

def mark(i):
    if i == 0:
        return 'Mystery Award'
    if prime(i+1):
        return 'Minion'
    else:
        return 'Chocolate'

rank, checked = {}, set()
count = int(input())
for i in range(count):
    uid = input()
    rank[uid] = mark(i)

count = int(input())
for _ in range(count):
    query = input()
    result = rank.get(query, False)
    if result:
        if query in checked:
            print('{}: Checked'.format(query))
        else:
            print('{}: {}'.format(query, result))
            checked.add(query)
    else:
        print('{}: Are you kidding?'.format(query))
