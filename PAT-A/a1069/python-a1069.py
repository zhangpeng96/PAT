'''
    @name      : a1069
    @version   : 20.0531
    @author    : zhangpeng96
    @test_time : 12'22"
    @pass_rate : p2, p3 failed, p4 timeout
'''

# sub = input()
sub = '4'

while True:
    sub = ''.join(sorted(sub))
    a, b = int(sub[::-1]), int(sub)
    sub = a - b
    print('{:04d} - {:04d} = {:04d}'.format(a, b, sub))
    if sub == 0 or sub == 6174:
        break
    sub = str(sub)
