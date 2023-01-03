'''
    @name      : b1085
    @version   : 20.0510
    @author    : zhangpeng96
    @test_time : 59'58"
    @pass_rate : p2,p3 pass
'''

from itertools import groupby

count = int('10')
input_list = ['A57908 85 Au','B57908 54 LanX','A37487 60 au','T28374 67 CMU','T32486 24 hypu','A66734 92 cmu','B76378 71 AU','A47780 45 lanx','A72809 100 pku','A03274 45 hypu']

# count = int(input())
# input_list = [input() for _ in range(count)]

grade_weight = {'A': 1, 'B': 1/1.5, 'T': 1.5}
data = sorted(map(lambda x:
    {'id': x[0], 'grade': x[0][0], 'score': int(x[1]), 'school': x[2].lower()}, 
    map(lambda x:x.split(), input_list)
), key = lambda x: x['school'])

def weighted_sum(iters):
    return iters['score'] * grade_weight[iters['grade']]

school_list = []

for school, group in groupby(data, key = lambda x:x['school']):
    group = list(group)
    school_list.append(tuple([school, int(sum(map(weighted_sum, group))), len(group)]))

school_list = sorted(school_list, key = lambda x: (-x[1],x[2],x[0]))

print(len(school_list))
order, prev = 1, school_list[0][1]
for school, score, count in school_list:
    order = order+1 if prev != score else order
    print('{} {} {} {}'.format(order, school, score, count))

# print(school_list)

