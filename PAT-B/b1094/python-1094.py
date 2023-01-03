'''
    @name      : b1094
    @version   : 20.0512.2
    @author    : zhangpeng96
    @test_time : 30'00"
    @pass_rate : all
'''

import math

def prime(n):
    if not n % 2: return n == 2
    if not n % 3: return n == 3
    if not n % 5: return n == 5
    for p in range(7, int(math.sqrt(n))+1, 2):
        if not n % p: return False
    return True

# length, count = tuple(map(int, '20 5'.split()))
# big_int = '23654987725541023819'

length, count = tuple(map(int, input().split()))
big_int = input()

template = '{:0' + str(count) + '}'
combation = len(big_int) - count + 1
save = None

for data in map(lambda i: int(big_int[i:i+count]), [i for i in range(combation)]):
    if prime(data):
        save = data
        break

if save:
    print(template.format(save))
else:
    print('404')
