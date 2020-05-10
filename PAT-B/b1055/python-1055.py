'''
    @name      : b1055
    @version   : 20.0510
    @author    : zhangpeng96
    @test_time : 107'00"
    @pass_rate : p3,p4,p5,p6 failed
'''

number, row = tuple(map(int, '10 3'.split()))
input_str = ['Tom 188','Mike 170','Eva 168','Tim 160','Joe 190','Ann 168','Bob 175','Nick 186','Amy 160','John 159']

# number, row = tuple(map(int, input().split()))
# input_str = [input() for _ in range(number)]

people_dict = dict(zip(map(lambda x:x.split()[0], input_str), map(lambda x:int(x.split()[1]), input_str)))

people_dict = sorted(people_dict.items(), key = lambda x:(-x[1], x[0]), reverse = True)

def row_split(lst, i):
    count = int(len(lst) / i) - 1
    if count:
        return [ lst[ p*i : (p+1)*i] for p in range(count) ] + [ lst[count*i:] ]
    else:
        return [[p] for p in lst[0:i-1]] + [ lst[i:] ]

def row_order(lst):
    r = len(lst)
    if r % 2:
        data = list(map(lambda x: lst[x], 
            [i for i in range(1, r, 2)] + [i-1 for i in range(r, 0, -2)]))
    else:
        data = list(map(lambda x: lst[x], 
            [0] + [i for i in range(2, r, 2)] + [i-1 for i in range(r, 0, -2)]))
    return data

people_row = row_split(people_dict, row)
result = [' '.join(map(lambda x: x[0], row_order(people))) for people in people_row[::-1]]
print('\n'.join(result))

# print(people_row)
# def row_order(lst):
#     mid = int(len(lst) / 2)
#     print(lst, mid)
#     pre = [i-1 for i in range(mid, 0, -1)]
#     nxt = [i+1 for i in range(mid, len(lst))]
#     print(pre, nxt)
