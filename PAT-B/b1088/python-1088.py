'''
    @name      : b1088
    @version   : 20.0518
    @author    : zhangpeng96
    @test_time : 26'32"
    @pass_rate : p0, p2, p3, p4, p5 failed
'''

def equation(x, y):
    solution = []
    for a in range(10, 100):
        b = int(str(a)[::-1])
        if x * b == abs(a - b) * y:
            solution = [a, b, b//y]
    return solution

def decision(me, other):
    if me == other:
        return 'Ping'
    elif me < other:
        return 'Cong'
    elif me > other:
        return 'Gai'


me, x, y = tuple(map(int, '48 3 7'.split()))
# me, x, y = tuple(map(int, input().split()))
solution = equation(x, y)
if solution:
    print('{} {} {} {}'.format(
        me, *[decision(me, p) for p in solution]
    ))
else:
    print('No Solution')
