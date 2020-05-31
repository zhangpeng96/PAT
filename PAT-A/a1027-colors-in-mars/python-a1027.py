'''
    @name      : a1027
    @version   : 20.0531
    @author    : zhangpeng96
    @test_time : 19'54"
    @pass_rate : all
'''

decimal_map = dict(zip([0,1,2,3,4,5,6,7,8,9,10,11,12,13], '0123456789ABC'))

def decimal_converter(rgb):
    def digit(n, base = 13):
        if n < base:
            return [n]
        else:
            return digit(n//base, base) + [n % base]
    digits = digit(rgb, 13)
    digits = [0] + digits if len(digits) == 1 else digits
    return ''.join(map(lambda x:decimal_map[x], digits))

# ins = '4 43 71'
ins = input()

digits = map(lambda d:decimal_converter(int(d)), ins.split())
print('#{}{}{}'.format(*digits))
