'''
    @name      : b1033
    @version   : 20.506
    @author    : zhangpeng96
    @test_time : 32'12"
    @pass_rate : all
'''

import re

# input_key = input()
# input_str = input()
input_key = '7+IE.'
input_str = '7_This_is_a_test.'

shift = True if input_key.count('+') else False

output_str = input_str
blind_key = list(map(lambda x:x.lower(), input_key.replace('+', '')))


output_str = re.sub('[A-Z]', '', output_str) if shift else output_str

for key in blind_key:
    output_str = output_str.replace(key, '')
    output_str = output_str.replace(key.upper(), '')

print(output_str)