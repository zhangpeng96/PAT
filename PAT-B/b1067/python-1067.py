'''
    @name      : b1067
    @version   : 20.0527
    @author    : zhangpeng96
    @test_time : 24'10"
    @pass_rate : p2,p3,p4 failed
'''

# correct, attempt = 'Correct%pw 3'.split()
# passwords = ['correct%pw', 'Correct@PW', 'whatisthepassword!', 'Correct%pw']
correct, attempt = input().split()
attempt = int(attempt)

passwords = []
password = input()
while password != '#':
    password = input()
    passwords.append(password)
passwords = passwords[:-1]

for password in passwords:
    if password == correct:
        print('Welcome in')
        break
    else:
        print('Wrong password: %s' % password)
        attempt -= 1
    if not attempt:
        print('Account locked')
        break
