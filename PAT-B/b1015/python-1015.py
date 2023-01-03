'''
    @name      : b1015
    @version   : 20.0511
    @author    : zhangpeng96
    @test_time : 38'27"
    @pass_rate : p3,p4 timeout  p2 timeout intermittently
'''

# count, admission, excellent = tuple(map(int, '14 60 80'.split()))

# input_list = ['10000001 64 90','10000002 90 60','10000011 85 80','10000003 85 80','10000004 80 85','10000005 82 77','10000006 83 76','10000007 90 78','10000008 75 79','10000009 59 90','10000010 88 45','10000012 80 100','10000013 90 99','10000014 66 60'] 

count, admission, excellent = tuple(map(int, input().split()))

input_list = [input() for _ in range(count)]

data = map(lambda x:tuple(map(int, x.split())), input_list)

admiss = list(filter(lambda x: x[1] >= admission and x[2] >= admission, data))

ee = sorted(filter(lambda x: x[1] >= excellent and x[2] >= excellent, admiss), key = lambda x: (- (x[1]+x[2]), -x[1], x[0]))

ae = sorted(filter(lambda x: x[1] >= excellent and x[2] < excellent, admiss), key = lambda x: (- (x[1]+x[2]), -x[1], x[0]))

ea = sorted(filter(lambda x: x[1] < excellent and x[2] < excellent and x[1] >= x[2], admiss), key = lambda x: (- (x[1]+x[2]), -x[1], x[0]))

aa = sorted(filter(lambda x: x[1] < excellent and x[1] < x[2], admiss), key = lambda x: (- (x[1]+x[2]), -x[1], x[0]))

res = '\n'.join(map(lambda x:'{} {} {}'.format(x[0], x[1], x[2]), ee+ae+ea+aa))

print(len(admiss))
print(res, end = '')
