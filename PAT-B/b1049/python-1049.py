'''
    @name      : b1049
    @version   : 20.0516
    @author    : zhangpeng96
    @test_time : 60'00"
    @pass_rate : p2, p3 timeout
'''

from itertools import product

def combination(tuples):
    return map(
        lambda p: sum(tuples[p[0]:p[1]]), 
        product(range(len(tuples) + 1), repeat = 2)
    )

# digit_list = tuple(map(float, '0.1 0.2 0.3 0.4'.split()))

count = int(input())
digit_list = tuple(map(float, input().split()))

print('{:.2f}'.format( sum(combination(digit_list)) ))


'''
    nested loop version

def combination(tuples):
    data = []
    for i in range(len(tuples)+1):
        for j in range(len(tuples)+1):
            if i > j:
                data.append(tuples[j:i])
'''
