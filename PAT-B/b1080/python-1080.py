"""
    @name      : b1080
    @version   : 21.0105
    @author    : zhangpeng96
    @pass_rate : p3 timeout
"""

p, m, f = map(int, input().split())
grades = [[], [], []]
[grades[0].append(input()) for _ in range(p)]
[grades[1].append(input()) for _ in range(m)]
[grades[2].append(input()) for _ in range(f)]

# p, m, f = map(int, '6 6 7'.split())
# grades = [
#     ['01234 880','a1903 199','ydjh2 200','wehu8 300','dx86w 220','missing 400'],
#     ['ydhfu77 99','wehu8 55','ydjh2 98','dx86w 88','a1903 86','01234 39'],
#     ['ydhfu77 88','a1903 66','01234 58','wehu8 84','ydjh2 82','missing 99','dx86w 81']
# ]
ans = {}
ans_2 = []

def final(lst):
    p, m, f = map(lambda x: 0 if x == -1 else x, lst)
    if m > f:
        g = round(m * 0.4 + f * 0.6)
    else:
        g = f
    if p >= 200 and g >= 60:
        return g
    else:
        return -1

for i, grade in enumerate(grades):
    for gra in grade:
        name, score = gra.split()
        if not ans.get(name):
            ans[name] = [-1, -1, -1]
        ans[name][i] = int(score)

for an in ans.items():
    passed = final(an[1])
    if passed != -1:
        an = list(an)
        an[1].extend([passed])
        ans_2.append(an)

ans_2.sort(key=lambda x:(-x[1][3], x[0]))

for an in ans_2:
    print(an[0], *an[1])