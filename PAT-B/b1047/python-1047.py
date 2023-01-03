'''
    @name      : b1047
    @version   : 20.0518
    @author    : zhangpeng96
    @test_time : 11'06"
    @pass_rate : all
'''

from itertools import groupby

# score_list = ['3-10 99','11-5 87','102-1 0','102-3 100','11-9 89','3-2 61']

count = int(input())
score_list = [input() for _ in range(count)]

record = map(lambda r:( r.split()[0].split('-')[0], r.split()[0].split('-')[1], int(r.split()[1]) ), score_list)

score_sum = []

for item, value in groupby(sorted(record, key = lambda x:x[0]), key = lambda x:x[0]):
    score_sum.append([item, sum(map(lambda x: x[2], value))])

print('{} {}'.format(* sorted(score_sum, key = lambda x: -x[1])[0]) )

