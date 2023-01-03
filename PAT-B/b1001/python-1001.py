'''
    @name      : b1001
    @version   : 20.0525
    @author    : zhangpeng96
    @test_time : 3'00"
    @pass_rate : all
'''

digit = int('3')
count = 0

while digit != 1:
    count += 1
    digit = (3 * digit + 1) // 2 if digit % 2 else digit // 2

print(count)
