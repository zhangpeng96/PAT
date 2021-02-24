"""
    @name     : a1075
    @version  : 21.0224
    @author   : zhangpeng96
    @time     : 87'11"
    @accepted : p4 timeout
"""

from collections import defaultdict

class NA():
    def __lt__(self, other):
        return True
    def __gt__(self, other):
        return False
    def __add__(self, other):
        return other
    def __radd__(self, other):
        return other
    def __repr__(self):
        return '-'

users, problems, submissions = map(int, input().split())
full_marks = [0] + list(map(int, input().split()))
record = defaultdict(lambda: [NA()]*(problems+1) + [0])
failed = defaultdict(list)

for _ in range(submissions):
    name, pos, score = map(int, input().split())
    if score == -1:
        failed[name].append(pos)
    else:
        record[name][pos] = max(record[name][pos], score)
        if score == full_marks[pos]:
            record[name][problems+1] += 1

for name in record.keys():
    record[name][0] = sum(record[name][1:-1])

for name, pos in failed.items():
    if name in record.keys():
        for p in pos:
            record[name][p] = 0

result = sorted(record.items(), key=lambda x:(-x[1][0], -x[1][problems+1], x[0]))
rank, prev_score = 1, result[0][1][0]
for i, (name, score) in enumerate(result, 1):
    if score[0] == prev_score:
        print(rank, '{:05}'.format(name), *score[:-1])
    else:
        print(i, '{:05}'.format(name), *score[:-1])
        rank, prev_score = i, score[0]
