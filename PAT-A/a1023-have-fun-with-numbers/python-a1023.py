'''
    @name      : a1023
    @version   : 20.0717
    @author    : zhangpeng96
    @test_time : 5'00"
    @pass_rate : all
'''

input_str = '1234567899'

double = int(input_str) * 2

double_org = set(input_str)
double_set = set(str(double))

if double_org == double_set:
    print('Yes')
    print(double)
else:
    print('No')
    print(double)
