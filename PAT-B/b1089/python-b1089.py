"""
    @name     : b1089
    @version  : 21.0216
    @author   : zhangpeng96
    @time     : 41'42"
    @accepted : all
"""

from itertools import combinations

count = int(input())
say = [ int(input()) for _ in range(count) ]
solution = False


for wolf1, wolf2 in combinations(range(count), 2):
    role, lie = [1]*count, []
    for i in range(count):
        role[wolf1], role[wolf2] = -1, -1
        # say[i]表示i发言认为某人是不是狼人
        # abs(say[i]-1)是i发言所说的某人，查看在假设下这个人是不是狼人
        if say[i] * role[ abs(say[i])-1 ] < 0:
            lie.append(i)
    # 有两个人说谎，且说谎的人一个是狼人，一个是好人，那么角色表示为-1、+1
    if len(lie) == 2 and (role[ lie[0] ] + role[ lie[1] ] == 0):
        solution = True
        print('{} {}'.format(wolf1+1, wolf2+1))
        break

if not solution:
    print('No Solution')
