'''
    @name      : b1054
    @version   : 20.505
    @author    : zhangpeng96
    @test_time : 28'00"
    @pass_rate : all
'''

# input_count = input()
# input_str = input()
input_str = '5 -3.2 aaa 9999 2.3.4 7.123 2.35'
digit_list = input_str.split()
legal_list = []
illegal_list = []

def is_digit(digit_str):
    return digit_str.replace('.', '', 1).lstrip('-').isdigit()

def in_range(digit_str):
    if digit_str.count('.'):
        if len(digit_str.split('.')[1]) > 2:
            return False
    digit = float(digit_str) if digit_str.count('.') else int(digit_str)
    return True if -1000 <= digit <= 1000 else False

def is_legal(digit_str):
    if is_digit(digit_str):
        return in_range(digit_str)
    else:
        return False

def digit_type(digit_str):
    return float(digit_str) if digit_str.count('.') else int(digit_str)


for digit in digit_list:
    if is_legal(digit):
        legal_list.append(digit)
    else:
        illegal_list.append(digit)

legal_count = len(legal_list)


[print('ERROR: %s is not a legal number' % illegal) for illegal in illegal_list]

if not legal_count:
    print('The average of 0 numbers is Undefined')
elif legal_count == 1:
    average = sum(map(digit_type, legal_list)) / legal_count
    print('The average of {} number is {:.2f}'.format(legal_count, average))
else:
    average = sum(map(digit_type, legal_list)) / legal_count
    print('The average of {} numbers is {:.2f}'.format(legal_count, average))
