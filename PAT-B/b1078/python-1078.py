'''
    @name      : b1078
    @version   : 20.0516
    @author    : zhangpeng96
    @test_time : 36'48"
    @pass_rate : all
'''

def compress(strs):
    chars = []
    char, count = '', 1
    for ch in strs + '`':
        if ch == char:
            count += 1
        else:
            count = '' if count == 1 else count
            chars += [(char, count)]
            char, count = ch, 1
    return ''.join(map(lambda x: '{}{}'.format(x[1], x[0]), chars[1:]))


def decompress(strs):
    chars = []
    char, count = '', '0'
    for ch in strs:
        if ch.isdigit():
            count += ch
        else:
            char, count = ch, int(count)
            count = count if count else 1
            chars += [(char, count)]
            char, count = '', '0'
    return ''.join(map(lambda x: x[0] * x[1], chars))



op = input()
input_str = input()

# op = 'C'
# input_str = 'TTTTThhiiiis isssss a   tesssst CAaaa as'
# input_str = '5T2h4is i5s a3 te4st CA3a as10Z'

if op == 'C':
    print(compress(input_str))
elif op == 'D':
    print(decompress(input_str))

