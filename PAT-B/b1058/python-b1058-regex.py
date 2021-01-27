"""
    @name     : b1058
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 43'00"
    @accepted : all
"""

import re

n, m = map(int, input().split())

keys, scores = [], []
wrongs = {}
regex = r'(?<=\(\d\s)(.*?)(?=\))'

for _ in range(m):
    score, _, _, *key = input().split()
    scores.append(int(score))
    keys.append(key)

for i in range(n):
    total = 0
    for j, r in enumerate(re.findall(regex, input())):
        if r.split() == keys[j]:
            total += scores[j]
        else:
            wrongs[j+1] = wrongs.get(j+1, 0) + 1
    print(total)

if wrongs:
    count = max(wrongs.values())
    items = sorted(map(lambda x:x[0], filter(lambda x: x[1]==count, wrongs.items())))
    print(count, ' '.join(map(str, items)))
else:
    print('Too simple')
