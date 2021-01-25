"""
    @name      : a1063
    @version   : 21.0125
    @author    : zhangpeng96
    @test_time : 29'00"
    @pass_rate : all
"""

case_count = int(input())
cases = [set(input().split()[1:]) for _ in range(case_count)]
query_count = int(input())
queries = [tuple(map(int, input().split())) for _ in range(query_count)]

# case_count = int('3')
# cases = ['3 99 87 101','4 87 101 5 87','7 99 101 18 5 135 18 99']
# query_count = int('2')
# queries = [tuple(map(int, i.split())) for i in ['1 2','1 3']]

for a, b in queries:
    print('{:.1%}'.format( len(cases[a-1] & cases[b-1]) / len(cases[a-1] | cases[b-1]) ) )
