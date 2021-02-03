"""
    @name     : a1129
    @version  : 21.0203
    @author   : zhangpeng96
    @time     : 24'18"
    @accepted : p3-p5 timeout
"""

from collections import Counter

query, k = map(int, input().split())
record = list(map(int, input().split()))

for i, rec in enumerate(record[1:], 1):
    recommend = Counter(record[0:i]).most_common()
    recommend.sort(key=lambda x: (-x[1], x[0]))
    print('{}: {}'.format(
        rec, ' '.join(map(lambda x:str(x[0]), recommend[0:k]))
    ))

