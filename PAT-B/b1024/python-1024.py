'''
    @name      : b1024
    @version   : 20.0514
    @author    : zhangpeng96
    @test_time : 32'58"
    @pass_rate : p5, p6 failed
'''

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

# input_str = input()
# print( decimal_format(input_str).format(eval(input_str)) )


input_1 = '+1.23400E-03'
print(decimal_format(input_1).format(eval(input_1)))

input_2 = '-1.2E+10'
print(decimal_format(input_2).format(eval(input_2)))
