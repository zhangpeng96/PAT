'''
    @name      : a1041 (hash)
    @version   : 21.0104
    @author    : zhangpeng96
    @test_time : 12'
    @pass_rate : all
'''


ins = '7 5 31 5 88 67 88 17'
# ins = '5 888 666 666 888 888'
digit = ins.split()[1:]

bets = {}
winner = -1

for bet in digit:
    if bets.get(bet):
        bets[bet] = bets[bet] + 1
    else:
        bets[bet] = 1

for bet, times in bets.items():
    if times == 1:
        winner = bet
        break

if winner != -1:
    print(winner)
else:
    print('None')
