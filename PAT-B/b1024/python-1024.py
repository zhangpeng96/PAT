'''
    @name      : b1024
    @version   : 20.0514.2
    @author    : zhangpeng96
    @test_time : 32'58"
    @pass_rate : p5, p6 failed
'''

def decimal_format(deci):
    deci_ns = deci.lstrip('+').lstrip('-')
    if deci_ns.count('-'):
        deci_count = len(deci_ns.split('E')[0].split('.')[1]) + int(deci_ns.split('-')[1])
        return ('{:.' + str(deci_count) + 'f}').format(eval(deci))
    else:
        int_count = int(deci_ns.split('+')[1])
        deci_count = len(deci_ns.split('E')[0].split('.')[1])
        if int_count <= 99:
            float_count = 0 if deci_count <= int_count else deci_count - int_count
            return ('{:.' + str(float_count) + 'f}').format(eval(deci))
        else:
            deci = deci.split('E')[0] + 'E+99'
            int_count -= 99
            float_count = 0 if deci_count <= int_count else deci_count - int_count
            return ('{:.' + str(float_count) + 'f}').format(eval(deci))


# input_str = input()
# print( decimal_format(input_str).format(eval(input_str)) )


# input_1 = '+1.23400E-00'
# print(decimal_format(input_1))

input_2 = '-0.01E+90'
print(decimal_format(input_2))
# -9999999999999999594167244563503627314919960896484514396697390098067039229509544255160320
