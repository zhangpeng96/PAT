'''
    @name      : b1003
    @version   : 20.0525
    @author    : zhangpeng96
    @test_time : 45'58"
    @pass_rate : p1, p5 failed
'''

import re

def case_1(strs):
    if len(strs) == strs.count('P') + strs.count('A') + strs.count('T'):
        return True
    else:
        return False

def case_2(strs):
    x = strs.split('PAT')
    if len(x) == 2:
        if x[0] == x[1] and x[0].count('A') == len(x[0]):
            return True
    return False

def case_3(strs):
    result = re.split(r'P(.*)AT', strs)
    if len(result) == 3:
        a, b, ca = result
        c = ca[:-len(a)] if ca.endswith(a) else ca
        origin = '{}P{}T{}'.format(a,b,c)
        if case_1(origin) and case_2(origin):
            return True
    return False


# count = int(input())
# check_list = [input() for _ in range(count)]

count = int('8')
check_list = ['PAT','PAAT','AAPATAA','AAPAATAAAA','xPATx','PT','Whatever','APAAATAA']

for check in check_list:
    if case_1(check) and (case_2(check) or case_3(check)):
        print('YES')
    else:
        print('NO')
    # print(case_1(check),case_2(check), case_3(check))
    # print(case_1(check) and (case_2(check) or case_3(check)))
