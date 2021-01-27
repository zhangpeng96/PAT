from itertools import groupby
def op1(op):
    p = sorted(filter(lambda r:r[2]==op, record), key=lambda x:(-x[1], x[0]))
    return '\n'.join( map(lambda x: '{} {}'.format(x[0], x[1]), p) )

def op2(op):
    p = list( map(lambda x: x[1], filter(lambda r:r[3]==op, record)) )
    if p:
        return '{} {}'.format(len(p), sum(p))
    else:
        return ''

def op3(op):
    p = sorted(filter(lambda r:r[4]==op, record), key=lambda x:x[3])
    q = [ ( room, len(list(g)) ) for room, g in groupby(p, lambda x:x[3]) ]
    q = sorted( q, key=lambda x:(-x[1], x[0]) )
    return '\n'.join( map(lambda x: '{} {}'.format(*x), q) )


data_list = ['B123180908127 99', 'B102180908003 86', 'A112180318002 98', 'T107150310127 62', 'A107180908108 100', 'T123180908010 78', 'B112160918035 88', 'A107180908021 98']
query_list = ['1 A','2 107','3 180908','2 999']
record = []
query_id = 0

for data in data_list:
    ids, score = data.split()
    record.append( (ids, int(score), ids[0], ids[1:4], ids[4:10], ids[10:13]) )

for query in query_list:
    query_id += 1
    print('Case {}: {}'.format(query_id, query))
    f, op = query.split()
    if f == '1':
        res = op1(op)
        print(res) if res else print('NA')
    elif f == '2':
        res = op2(op)
        print(res) if res else print('NA')
    elif f == '3':
        res = op3(op)
        print(res) if res else print('NA')
