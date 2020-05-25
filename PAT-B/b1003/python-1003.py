'''
    @name      : b1003
    @version   : 20.0525.2
    @author    : zhangpeng96
    @test_time : 54'13"
    @pass_rate : all
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
    def unpack(s):
        r = re.split(r'P(.*)AT', s)
        if len(r) == 3:
            a, b, ca = r
            c = ca[:-len(a)] if ca.endswith(a) else ca
            return '{}P{}T{}'.format(a,b,c)
        else:
            return False

    s = unpack(strs)
    while s:
        if case_2(s):
            return True
        else:
            s = unpack(s)
    return False


# count = int(input())
# check_list = [input() for _ in range(count)]

count = int('8')
check_list = ['PAT','PAAT','AAPATAA','AAPAATAAAA','xPATx','PT','Whatever','APAAATAA']
check_list = ['PPPAAATTT','TAP','AAPTAA','AAPAATAAAAAA','AAAPAATAAAAAA','AAAPAAATAAAAAAAAA']
# NO,NO,NO,NO,YES,YES

for check in check_list:
    if case_1(check):
        if case_2(check):
            print('YES')
        elif case_3(check):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
