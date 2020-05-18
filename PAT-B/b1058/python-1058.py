'''
    @name      : b1058
    @version   : 20.0517.2
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p3 timeout
'''

import re

sheet_count, problem_count = tuple(map(int, '3 4'.split()))
input_str1 = [tuple(prob.split()) for prob in ['3 4 2 a c','2 5 1 b','5 3 2 b c','1 5 4 a b d e']]
input_str2 = ['(2 a c) (2 b d) (2 a c) (3 a b e)','(2 a c) (1 b) (2 a b) (4 a b d e)','(2 b d) (1 e) (2 b c) (4 a b c d)']

# sheet_count, problem_count = tuple(map(int, input().split()))
# input_str1 = [tuple(prob.split()) for prob in [input() for _ in range(problem_count)]]
# input_str2 = [input() for _ in range(sheet_count)]

problems = list(map(lambda x: {'score': int(x[0]), 'key': set(x[3:])}, input_str1))

sheets = list(map(lambda x: [set(match.group(1).split()[1:]) for match in re.finditer(r'\((.*?)\)', x)], input_str2))

wrong_dict = dict(zip( [ i+1 for i in range(problem_count)], [0] * problem_count ))

for sheet in sheets:
    score = 0
    for i, problem in enumerate(sheet):
        result = 1 if problem == problems[i]['key'] else 0
        score += result * problems[i]['score']
        if not result:
            wrong_dict[ i+1 ] += 1
    print(score)

wrong_dict = sorted(wrong_dict.items(), key = lambda x:(-x[1], x[0]) )
wrong_cnt = wrong_dict[0][1]

if wrong_cnt:
    wrongs = []
    for wrong in wrong_dict:
        if wrong[1] == wrong_cnt:
            wrongs.append(str(wrong[0]))
        else:
            break
    print('{} {}'.format(wrong_cnt, ' '.join(wrongs)))
else:
    print('Too simple')
