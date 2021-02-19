"""
    @name     : a1083
    @version  : 21.0219
    @author   : zhangpeng96
    @time     : 13'17"
    @accepted : all
"""

class Grade():
    def __init__(self, name, uid, score):
        self.name = name
        self.uid = uid
        self.score = int(score)

count = int(input())
grades = [Grade(*input().split()) for _ in range(count)]
low, high = map(int, input().split())

grades = sorted(
    filter(lambda x: low <= x.score <= high, grades),
    key=lambda x:x.score, reverse=True)

if grades:
    for grade in grades:
        print(grade.name, grade.uid)
else:
    print('NONE')
