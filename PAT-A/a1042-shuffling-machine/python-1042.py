"""
    @name      : a1042
    @version   : 20.0720
    @author    : zhangpeng96
    @test_time : 14'00"
    @pass_rate : all
"""

def shuffle(cards, orders):
    shuffled = [None] * len(cards)
    for i, order in enumerate(orders):
        order = order - 1
        shuffled[order] = cards[i]
    return shuffled


deck = [
    'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13',
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
    'J1', 'J2'
]

repeat = int(input())
order = list(map(int, input().split()))

for i in range(repeat):
    deck = shuffle(deck, order)

print(' '.join(deck))



"""

repeat = int('2')
order = list(map(int, '36 52 37 38 3 39 40 53 54 41 11 12 13 42 43 44 2 4 23 24 25 26 27 6 7 8 48 49 50 51 9 10 14 15 16 5 17 18 19 1 20 21 22 28 29 30 31 32 33 34 35 45 46 47'.split()))

cards = ['S3', 'H5', 'C1', 'D13', 'J2']
orders = [4, 2, 5, 3, 1]

"""