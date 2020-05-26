'''
    @name      : b1010
    @version   : 20.0526
    @author    : zhangpeng96
    @test_time : 38'48"
    @pass_rate : all
'''

# items = tuple(map(int, '3 4 -5 2 6 1 -2 0'.split()))
items = tuple(map(int, input().split()))

bases, exps = items[::2], items[1::2]
deri, zero = [], True

for i in range(len(bases)):
    if exps[i]:
        deri += [ bases[i] * exps[i], exps[i] - 1 ]
        zero = False

if zero:
    print('0 0')
else:
    print(' '.join(map(str, deri)))
