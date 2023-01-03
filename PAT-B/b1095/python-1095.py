'''
    @name      : b1095
    @version   : 20.506
    @author    : zhangpeng96
    @test_time : 54'00"
    @pass_rate : p3, p4 timeout
'''

from collections import Counter

def query_type_1(data, arg):
    result = sorted(filter(lambda x:x['level'] == arg, data), key = lambda x:(-x['score'], x['id']))
    if result:
        print('\n'.join(['{id} {score}'.format(**r) for r in result]))
    else:
        print('NA')

def query_type_2(data, arg):
    arg = int(arg)
    result = list(map(lambda x:x['score'], filter(lambda x:x['room'] == arg, data)))
    if result:
        print('{} {}'.format(len(result), sum(result)))
    else:
        print('NA')

def query_type_3(data, arg):
    arg = int(arg)
    result = map(lambda x:x['room'], filter(lambda x:x['date'] == arg, data))
    result = sorted(Counter(result).most_common(), key = lambda x:(-x[1], x[0]))
    if result:
        print('\n'.join(['{} {}'.format(r[0], r[1]) for r in result]))
    else:
        print('NA')

# query_type_1(data, 'A')
# query_type_2(data, 107)
# query_type_3(data, '180908')
# print(data)

data_count, query_count = tuple(map(int, input().split()))

data_list = [input() for _ in range(0, data_count)]
query_list = list(map(lambda x: (int(x.split()[0]), x.split()[1]) , [input() for _ in range(0, query_count)]))

# data_list = ['B123180908127 99', 'B102180908003 86', 'A112180318002 98', 'T107150310127 62', 'A107180908108 100', 'T123180908010 78', 'B112160918035 88', 'A107180908021 98']
# query_list = list(map(lambda x: (int(x.split()[0]), x.split()[1]) , ['1 A','2 107','3 180908','2 999']))

data = list(map(lambda d:{
        'id':  d[0],
        'level': d[0][0],
        'room': int(d[0][1:4]),
        'date': int(d[0][4:10]),
        'order': int(d[0][10:13]),
        'score': int(d[1])
    }, map(lambda x: tuple(x.split()), data_list)))

for query_order, (query_id, query_args) in enumerate(query_list):
    if query_id == 1:
        print('Case %s: 1 %s' % (query_order+1, query_args))
        query_type_1(data, query_args)
    elif query_id == 2:
        print('Case %s: 2 %s' % (query_order+1, query_args))
        query_type_2(data, query_args)
    elif query_id == 3:
        print('Case %s: 3 %s' % (query_order+1, query_args))
        query_type_3(data, query_args)

