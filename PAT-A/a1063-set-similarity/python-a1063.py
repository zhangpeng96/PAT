'''
    @name      : a1063
    @version   : 20.0531
    @author    : zhangpeng96
    @test_time : 27'36"
    @pass_rate : p3, p4 timeout
'''

case_count = int(input())
cases = [input() for _ in range(case_count)]
query_count = int(input())
queries = [tuple(map(int, input().split())) for _ in range(query_count)]

# case_count = int('3')
# cases = ['3 99 87 101','4 87 101 5 87','7 99 101 18 5 135 18 99']
# query_count = int('2')
# queries = [tuple(map(int, i.split())) for i in ['1 2','1 3']]

for a, b in queries:
    a, b = a-1, b-1
    set_a = set(map(int, cases[a].split()[1:]))
    set_b = set(map(int, cases[b].split()[1:]))
    print('{:.1%}'.format( len(set_a & set_b) / len(set_a | set_b) ) )
