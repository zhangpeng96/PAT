'''
    @name      : b1069
    @version   : 20.0516
    @author    : zhangpeng96
    @test_time : 22'00"
    @pass_rate : all
'''

# count, gap, start = tuple(map(int, '9 3 2'.split()))
# accounts = ['Imgonnawin!','PickMe','PickMeMeMeee','LookHere','Imgonnawin!','TryAgainAgain','TryAgainAgain','Imgonnawin!','TryAgainAgain']
# accounts = ['PickMe','Imgonnawin!','TryAgainAgain']

count, gap, start = tuple(map(int, input().split()))
accounts = [input() for _ in range(count)]

selected = []
count = 0
for account in accounts[start-1:]:
    if account not in selected:
        if not count % gap:
            selected.append(account)        
        count += 1

if selected:
    print('\n'.join(selected))
else:
    print('Keep going...')
