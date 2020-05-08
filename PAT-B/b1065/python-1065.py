'''
    @name      : b1065
    @version   : 20.0508
    @author    : zhangpeng96
    @test_time : 42'00"
    @pass_rate : p1 format, p3, p4 failed
'''

partner_count = int(input())
# partner_count = 3
# partner_set = set(map(int, '33333 44444'.split()))

partner_set_list = [set(map(int, input().split())) for _ in range(0, partner_count)]

# party_set = set(map(int, '55555 44444 10000 88888 22222 11111 23333'.split()))
party_count = int(input())

party_set = set(map(int, input().split()))

for partner_set in partner_set_list:
    if partner_set.issubset(party_set):
        party_set -= partner_set

print(len(party_set))
print(' '.join(sorted(map(lambda x:str(x), party_set))))
