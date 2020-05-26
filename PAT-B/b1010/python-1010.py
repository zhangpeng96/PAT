'''
    @name      : b1010
    @version   : 20.0526
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p2, p4 failed
'''

items = tuple(map(int, '3 4 -5 2 0 1 -2 0'.split()))
# items = tuple(map(int, input().split()))

bases, exps = items[::2], items[1::2]
deri = []

for i in range(len(bases)):
    base, exp = bases[i] * exps[i], exps[i] - 1
    if base:
        deri += [ base, exp ]
    elif base == 0 and exp == 0:
        deri += [0, 0]

# print(deri)
print(' '.join(map(str, deri)))
