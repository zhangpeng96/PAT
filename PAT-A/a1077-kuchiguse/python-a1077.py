"""
    @name     : a1077
    @version  : 21.0124
    @author   : zhangpeng96
    @time     : 17'04"
    @accepted : all
"""

count = int(input())
sentences = [ input() for _ in range(count) ]

suffix = False
length = min([len(sentence) for sentence in sentences])

for i in range(length):
    suffix_pool = set( [sentence[-1:-(i+2):-1] for sentence in sentences] )
    if len(suffix_pool) != 1:
        break
    else:
        suffix = suffix_pool.pop()

if suffix == False:
    print('nai')
else:
    print(suffix[::-1])