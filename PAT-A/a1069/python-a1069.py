'''
    @name      : a1069
    @version   : 20.0531.2
    @author    : zhangpeng96
    @test_time : 13'50"
    @pass_rate : all
'''

# sub = input()
sub = int('99')

while True:
    sub = ''.join(sorted('{:04d}'.format(sub)))
    a, b = int(sub[::-1]), int(sub)
    sub = a - b
    print('{:04d} - {:04d} = {:04d}'.format(a, b, sub))
    if sub == 0 or sub == 6174:
        break
