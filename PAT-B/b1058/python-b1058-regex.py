import re

n, m = map(int, input().split())

keys, scores = [], []
students, totals, wrongs = [], [0]*n, {}
regex = r'(?<=\(\d\s)(.*?)(?=\))'

for _ in range(m):
    score, _, _, *key = input().split()
    scores.append(int(score))
    keys.append(set(key))

for _ in range(n):
    answer = [ set(r.split()) for r in re.findall(regex, input()) ]
    students.append(answer)

for i, student in enumerate(students):
    for j, answer in enumerate(student):
        if answer == keys[j]:
            totals[i] += scores[j]
        else:
            wrongs[j+1] = wrongs.get(j+1, 0) + 1

print('\n'.join(map(str, totals)))

if wrongs:
    result = sorted(wrongs.items(), key=lambda x:-x[1])
    count = result[0][1]
    items = sorted(map(lambda x:x[0], filter(lambda x: x[1]==count, result)))
    print(count, ' '.join(map(str, items)))
else:
    print('Too simple')