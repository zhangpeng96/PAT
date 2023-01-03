'''
    @name      : b1067
    @version   : 20.0527.2
    @author    : zhangpeng96
    @test_time : 24'10"
    @pass_rate : all
'''

# correct, attempt = 'Correct%pw 3'.split()
# passwords = ['correct%pw', 'Correct@PW', 'whatisthepassword!', 'Correct%pw']
correct, attempt = input().split()
attempt = int(attempt)

passwords = []
password = input()
while password != '#':
    passwords.append(password)
    password = input()

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
