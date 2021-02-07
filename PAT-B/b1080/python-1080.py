"""
    @name      : b1080
    @version   : 21.0207
    @author    : zhangpeng96
    @pass_rate : all
"""

from sys import stdin

def calculate(args):
    name, score = args
    program, mid_term, final = map(lambda x: 0 if x == -1 else x, score)
    if program < 200:
        return False
    if mid_term > final:
        grade = round(mid_term * 0.4 + final * 0.6)
    else:
        grade = final
    if grade >= 60:
        return [name, *score, grade]
    else:
        return False

p, m, f = map(int, input().split())
lines = stdin.readlines()
report = {}
grades = [ lines[0:p], lines[p:p+m], lines[p+m:] ]

for i, stage in enumerate(grades):
    for grade in stage:
        name, score = grade.split()
        if name not in report:
            report[name] = [-1, -1, -1]
        report[name][i] = int(score)

report = filter(bool, map(calculate, report.items()))
report = sorted(report, key=lambda x: (-x[-1], x[0]))

print('\n'.join(map(lambda x: '{} {} {} {} {}'.format(*x), report)))
