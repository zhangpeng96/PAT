'''
    @name      : b1073
    @version   : 20.0509
    @author    : zhangpeng96
    @test_time : 76'45"
    @pass_rate : p4 timeout，预处理达300ms，基本无法优化
'''

import re
from collections import Counter

sheet_count, problem_count = tuple(map(int, input().split()))
# sheet_count, problem_count = tuple(map(int, '3 4'.split()))

# input_str1 = [tuple(prob.split()) for prob in ['3 4 2 a c','2 5 1 b','5 3 2 b c','1 5 4 a b d e']]
# input_str2 = ['(2 a c) (3 b d e) (2 a c) (3 a b e)','(2 a c) (1 b) (2 a b) (4 a b d e)','(2 b d) (1 e) (1 c) (4 a b c d)']

input_str1 = [tuple(prob.split()) for prob in [input() for _ in range(problem_count)]]
input_str2 = [input() for _ in range(sheet_count)]

problems = list(map(lambda x: {'score': int(x[0]), 'key': set(x[3:])}, input_str1))

sheets = list(map(lambda x: [set(match.group(1).split()[1:]) for match in re.finditer(r'\((.*?)\)', x)], input_str2))

def multi_choice(answer, key):
    if answer:
        if answer < key:
            return 0.5
        elif answer == key:
            return 1.0
        else:
            return 0
    else:
        return 0

wrong_list = []
score_list = []

for sheet in sheets:
    score = 0
    for i, problem in enumerate(sheet):
        answer, key = problem, problems[i]['key']
        score += multi_choice(answer, key) * problems[i]['score']
        wrong_list.extend(['{}-{}'.format(i+1, option) for option in (answer ^ key) ])
    score_list.append(score)

print('\n'.join(map(lambda x:'{:.1f}'.format(x), score_list)))

wrong_counter = Counter(wrong_list).most_common()

if wrong_counter:
    max_counter = wrong_counter[0][1]
    data = sorted(map(lambda x:x[0], filter(lambda x:x[1] == max_counter, wrong_counter)), key = lambda x:(int(x.split('-')[0]), x.split('-')[1]) )
    [print('{} {}'.format(max_counter, d)) for d in data]
else:
    print('Too simple')
