'''
    @name      : b1029
    @version   : 20.505
    @author    : zhangpeng96
    @test_time : 14'00"
    @pass_rate : all
'''

input_aim = '7_This_is_a_test'
input_real = '_hs_s_a_es'
# input_aim = input()
# input_real = input()
output_list = []

def set_with_order(alist):
    return sorted(set(alist), key=alist.index)

ptr = 0
for aim in input_aim:
    if ptr >= len(input_real):
        # print(aim)
        output_list.append(aim.upper())
    else:
        if input_real[ptr] != aim:
            # print(aim)
            output_list.append(aim.upper())
        else:
            ptr += 1

print(''.join(set_with_order(output_list)))
