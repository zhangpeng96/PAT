'''
    @name      : b1084
    @version   : 20.0517
    @author    : zhangpeng96
    @test_time : 19'19"
    @pass_rate : all
'''

def counter_char(chars):
    char_map = []
    char, count = '', 0
    for ch in chars + '`':
        if ch == char:
            count += 1
        else:
            char_map.append((char, count))
            char, count = ch, 1
    return char_map[1:]


def sequence_next(seq_str):
    return ''.join(map(lambda x: '{}{}'.format(*x), counter_char(seq_str)))


# input_str = '1 8'
input_str = input()

digit, count = input_str.split()[0], int(input_str.split()[1])

for i in range(count-1):
    digit = sequence_next(digit)

print(digit)