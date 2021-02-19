"""
    @name     : a1039
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 38'00"
    @accepted : all
"""

from collections import defaultdict

record = defaultdict(list)

student_n, course_n = map(int, input().split())
for _ in range(course_n):
    course_id, count = map(int, input().split())
    # 可能存在有某个课程没有学生选，那么就没有少了一行输入，需要判断跳过
    if count == 0: continue
    for name in input().split():
        record[name].append(course_id)

for query in input().split():
    print(query, len(record[query]), *sorted(record[query]))
