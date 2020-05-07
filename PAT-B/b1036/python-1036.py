'''
    @name      : b1036
    @version   : 20.507
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p2 failed
'''

# input_str = '10 a'
input_str = input()
count, token = int(input_str.split()[0]), input_str.split()[1]
width, height = count, int(count/2)

draw = [token*count] + [token + ' '*(width-2) + token]*(height-2) + [token*count]

print('\n'.join(draw))
