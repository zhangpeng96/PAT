"""
    @name     : a1082
    @version  : 21.0125
    @author   : zhangpeng96
    @time     : > 6 hours
    @accepted : p3 error
"""

from math import ceil

# number = '-123456789'
# number = '100000080'
# number = '100406080'
# number = '100800'

number = input()
number = str(int(number))

digit = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
place = ['', 'Shi', 'Bai', 'Qian']
suffix = ['', 'Wan', 'Yi']
result = []

if number.startswith('-'):
    negative = True
    number = number.lstrip('-')
else:
    negative = False

def repl(s):
    sp = s.rstrip('0')
    s = sp + '*' * (len(s)-len(sp))
    s = s.replace('000', '**0').replace('00', '*0')
    return s

def solve(part):
    if part == '0000':
        return []
    part = repl(part)
    words = []
    for i, dig in enumerate(part[::-1]):
        if dig == '*':
            continue
        dig = int(dig)
        if dig:
            words.append( (digit[dig] + ' ' + place[i]).strip() )
        else:
            words.append( digit[dig] )
    return words

for i in range( ceil(len(number)/4) ):
    part = number[-(1+i*4):-(5+i*4):-1][::-1]
    part = solve(part)
    if part:
        result.append(suffix[i])
    result.extend(part)

if negative:
    result.append('Fu')

print(' '.join(result[::-1]).strip())