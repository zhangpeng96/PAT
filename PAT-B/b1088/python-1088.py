'''
    @name      : b1088
    @version   : 20.0518
    @author    : zhangpeng96
    @test_time : 83'53"
    @pass_rate : all
'''

def equation(x, y):
    solution = []
    for a in range(10, 100):
        b = int(str(a)[::-1])
        if x * b == abs(a - b) * y:
            solution = [a, b, b/y]
    return solution

def decision(me, other):
    if me == other:
        return 'Ping'
    elif me < other:
        return 'Cong'
    elif me > other:
        return 'Gai'


# me, x, y = tuple(map(int, '48 3 7'.split()))
inputs = input()
me, x, y = tuple(map(int, inputs.split()))

solution = equation(x, y)
if solution:
    print('{} {} {} {}'.format(
        solution[0], *[decision(me, p) for p in solution]
    ))
else:
    print('No Solution')
