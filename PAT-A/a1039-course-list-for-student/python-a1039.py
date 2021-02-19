"""
    @name     : a1039
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 38'00"
    @accepted : p1 exception
"""

from collections import defaultdict

record = defaultdict(list)

student_n, course_n = map(int, input().split())
for _ in range(course_n):
    course_id = int( input().split()[0] )
    for name in input().split():
        record[name].append(course_id)

for query in input().split():
    print(query, len(record[query]), *sorted(record[query]))
