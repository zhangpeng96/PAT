
# token_bag, count = tuple(map(int, '100 4'.split()))
# rounds = ['8 0 100 2','3 1 50 1','5 1 200 6','7 0 200 8']

token_bag, count = tuple(map(int, '100 4'.split()))
rounds = ['8 0 100 2','3 1 200 1','5 1 200 6','7 0 200 8']

def battle(round_str, token_bag):
    n1, bigger, token, n2 = tuple(map(int, round_str.split()))
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


# token_bag, count = tuple(map(int, input().split()))
# rounds = [input() for _ in range(count)]

for r in rounds:
    token_bag = battle(r, token_bag)
    if token_bag <= 0:
        print('Game Over.')
        break
