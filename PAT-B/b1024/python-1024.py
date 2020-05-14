'''
    @name      : b1024
    @version   : 20.0514.3
    @author    : zhangpeng96
    @test_time : 83'12"
    @pass_rate : all
'''
from decimal import Decimal

def decimal_format(deci):
    deci_ns = deci.lstrip('+').lstrip('-')
    if deci_ns.count('-'):
        deci_count = len(deci_ns.split('E')[0].split('.')[1]) + int(deci_ns.split('-')[1])
        return '{:.' + str(deci_count) + 'f}'
    else:
        int_count = int(deci_ns.split('+')[1])
        deci_count = len(deci_ns.split('E')[0].split('.')[1])
        float_count = 0 if deci_count <= int_count else deci_count - int_count
        return '{:.' + str(float_count) + 'f}'

input_str = input()
print( decimal_format(input_str).format(Decimal(input_str)) )


# input_1 = '+1.23400E-03'
# print(decimal_format(input_1).format(Decimal(input_1)))

# input_2 = '-1.2E+10'
# print(decimal_format(input_2).format(Decimal(input_2)))

# input_3 = '-1.0001E+999'
# print(decimal_format(input_3).format(Decimal(input_3)))