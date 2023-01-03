'''
    @name      : b1091
    @version   : 20.0522
    @author    : zhangpeng96
    @test_time : 28'15"
    @pass_rate : all
'''

def exchange(galleon, sickle, knut):
    return galleon*17*29 + sickle*29 + knut

def rechange(knut):
    sickle, knut = divmod(knut, 29)
    galleon, sickle = divmod(sickle, 17)
    return galleon, sickle, knut

# price, amount = tuple(map(lambda x: tuple( map(int, x.split('.')) ), '10.16.27 14.1.28'.split()))
# price, amount = tuple(map(lambda x: tuple( map(int, x.split('.')) ), '14.1.28 10.16.27'.split()))

price, amount = tuple(map(lambda x: tuple( map(int, x.split('.')) ), input().split()))

subtract = exchange(*amount) - exchange(*price)

if subtract >= 0:
    print('.'.join(map(str, rechange(subtract))))
else:
    print('-{}'.format(
        '.'.join(map(str, rechange(abs(subtract))))
    ))
