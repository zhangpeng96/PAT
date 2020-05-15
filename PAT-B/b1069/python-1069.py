'''
    @name      : b1069
    @version   : 20.0515
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p0, p3 failed
'''

count, gap, start = tuple(map(int, '9 3 2'.split()))

accounts = ['Imgonnawin!','PickMe','PickMeMeMeee','LookHere','Imgonnawin!','TryAgainAgain','TryAgainAgain','Imgonnawin!','TryAgainAgain']
accounts = ['PickMe','Imgonnawin!','TryAgainAgain']


# count, gap, start = tuple(map(int, input().split()))
# accounts = [input() for _ in range(count)]

selected = []

for i, ac in enumerate(accounts[start-1::gap]):
    if ac in selected:
        selected.append(accounts[i+1])
    else:
        selected.append(ac)


if selected:
    print('\n'.join(selected))
else:
    print('Keep going...')
