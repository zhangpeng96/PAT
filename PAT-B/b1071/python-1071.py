"""
    @name     : b1071
    @version  : 21.0207
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : all
"""

def battle(token_bag):
    n1, bigger, token, n2 = map(int, input().split())
    if token > token_bag:
        print('Not enough tokens.  Total = {}.'.format(token_bag))
        return token_bag
    if bigger:
        result = True if n2 > n1 else False
    else:
        result = True if n2 < n1 else False
    if result:
        token_bag += token
        print('Win {}!  Total = {}.'.format(token, token_bag))
    else:
        token_bag -= token
        if token_bag >= 0:
            print('Lose {}.  Total = {}.'.format(token, token_bag))
    return token_bag


token_bag, count = tuple(map(int, input().split()))

for _ in range(count):
    token_bag = battle(token_bag)
    if token_bag <= 0:
        print('Game Over.')
        break
