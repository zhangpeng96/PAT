"""
    @name     : b1073
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 36'03"
    @accepted : all
"""

import re

def choice(answer, key):
    if answer:
        if answer < key:
            return 0.5
        elif answer == key:
            return 1.0
    return 0.0

n, m = map(int, input().split())

wrongs = {}
keys, scores = [], []
regex = r'(?<=\(\d\s)(.*?)(?=\))'

for _ in range(m):
    score, _, _, *key = input().split()
    scores.append(int(score))
    keys.append(set(key))

for i in range(n):
    total = 0.0
    for j, answer in enumerate(re.findall(regex, input())):
        answer = set(answer.split())
        total += scores[j] * choice(answer, keys[j])
        for option in (answer ^ keys[j]):
            meta = (j+1, option)
            wrongs[meta] = wrongs.get(meta, 0) + 1
    print('{:.1f}'.format(total))

if wrongs:
    count = max(wrongs.values())
    wrong = [k for k, v in wrongs.items() if v == count]
    wrong.sort(key=lambda x: (x[0],x[1]))
    for i, opt in wrong:
        print('{} {}-{}'.format(count, i, opt))
else:
    print('Too simple')
