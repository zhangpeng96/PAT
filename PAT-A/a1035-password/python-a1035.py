'''
    @name      : a1035
    @version   : 20.0717
    @author    : zhangpeng96
    @test_time : 22'00"
    @pass_rate : p2 failed
'''

count = int(input())
passwords = [input().split() for _ in range(count)]
modified = []

for username, password in passwords:
    distinguish = password.replace('1', '@').replace('0', '%').replace('l', 'L').replace('O', 'o')
    if distinguish != password:
        modified.append('{} {}'.format(username, distinguish))

modify_count = len(modified)

if modify_count:
    print(modify_count)
    [print(m) for m in modified]
else:
    if count == 1:
        print('There is 1 account and no account is modified')
    else:
        print('There is %s accounts and no account is modified' % count)
