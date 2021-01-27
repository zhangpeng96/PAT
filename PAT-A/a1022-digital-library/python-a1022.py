"""
    @name     : a1022
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 22'04"
    @accepted : all
"""

n = int(input())
books = [ [input() for _ in range(6)] for _ in range(n) ]
m = int(input())

for _ in range(m):
    query = input()
    pos, key = query.split(': ')
    pos = int(pos)
    if pos == 3:
        result = [ book[0] for book in books if key in book[pos] ]
    else:
        result = [ book[0] for book in books if book[pos] == key ]
    print(query)
    if result:
        print('\n'.join(sorted(result)))
    else:
        print('Not Found')
