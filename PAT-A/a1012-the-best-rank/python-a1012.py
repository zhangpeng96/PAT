"""
    @name     : a1012
    @version  : 21.0224
    @author   : zhangpeng96
    @time     : 77'23"
    @accepted : all
"""

count, query = map(int, input().split())
name_set = set()
record = [[], [], [], []]
order_map = {3: 'A', 2: 'C', 1: 'M', 0: 'E'}

for _ in range(count):
    name, computer, math, english = map(int, input().split())
    name_set.add(name)
    record[0].append((name, english))
    record[1].append((name, math))
    record[2].append((name, computer))
    record[3].append((name, round((computer + math + english)/3)))

for i in range(4):
    temp = sorted(record[i], key=lambda x:-x[1])
    same, prev, course = 1, temp[0][1], {}
    for rank, (name, score) in enumerate(temp, 1):
        if score == prev:
            course[name] = same
        else:
            course[name] = rank
            same, prev = rank, score
    record[i] = course

for _ in range(query):
    name = int(input())
    if name in name_set:
        rec = [ (rec[name], i) for i, rec in enumerate(record) ]
        rank, course = sorted(rec, key=lambda x:(x[0], -x[1]))[0]
        print(rank, order_map[course])
    else:
        print('N/A')
