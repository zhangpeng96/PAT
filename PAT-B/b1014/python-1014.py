'''
    @name      : b1014
    @version   : 20.0520
    @author    : zhangpeng96
    @test_time : 45'00"
    @pass_rate : all
'''

def decode_week(str1, str2, pos = False):
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i] and str1[i] in 'ABCDEFG':
            if pos:
                return i
            return ord(str1[i]) - 64

def decode_hour(str1, str2):
    pos = decode_week(str1, str2, True) + 1
    str1, str2 = str1[pos:], str2[pos:]
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i] and str1[i] in '0123456789ABCDEFGHIJKLMN':
                return str1[i]

def decode_min(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i] and str1[i].isalpha():
            return i

input_str = [
    '3485djDkxh4hhGE ', 
    '2984akDfkkkkggEdsb ', 
    's&hgsfdk ', 
    'd&Hyscvnm'
]
# input_str = [input() for _ in range(4)]

format_weeks = ['', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
format_hours = dict(zip('0123456789ABCDEFGHIJKLMN', range(24)))

print('{} {:02d}:{:02d}'.format(
    format_weeks[ decode_week(input_str[0], input_str[1]) ],
    format_hours[ decode_hour(input_str[0], input_str[1]) ],
    decode_min(input_str[2], input_str[3]),
))
