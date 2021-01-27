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

record = []
query_id = 0

n, m = map(int, input().split())

for _ in range(n):
    ids, score = input().split()
    record.append( (ids, int(score), ids[0], ids[1:4], ids[4:10], ids[10:13]) )

for _ in range(m):
    query = input()
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
