'''
    @name      : b1036
    @version   : 20.507.2
    @author    : zhangpeng96
    @test_time : 20'22"
    @pass_rate : all
'''

# input_str = '10 a'
input_str = input()
count, token = int(input_str.split()[0]), input_str.split()[1]
width, height = count, round((count+10e-7)/2)
# 题目中要求采用四舍五入处理，python3中round(9/4)为4，而非5

draw = [token*count] + [token + ' '*(width-2) + token]*(height-2) + [token*count]

print('\n'.join(draw))
