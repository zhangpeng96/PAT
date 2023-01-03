'''
    @name      : b1065
    @version   : 20.0508.3
    @author    : zhangpeng96
    @test_time : 103'05"
    @pass_rate : p3, p4 timeout occasionally
'''

# partner_count = 3
# partner_set = set(map(int, '33333 44444'.split()))
# party_set = set(map(int, '55555 44444 10000 88888 22222 11111 23333'.split()))

partner_count = int(input())
partner_set_list = [set(map(int, input().split())) for _ in range(0, partner_count)]

party_count = int(input())
party_set = set(map(int, input().split()))

for partner_set in partner_set_list:
    if partner_set.issubset(party_set):
        party_set -= partner_set

if party_count:
    print(len(party_set))
else:
    print(len(party_set), end='')    

if party_count:
    print(' '.join(sorted(map(lambda x:'{:05d}'.format(x), party_set))), end='')
