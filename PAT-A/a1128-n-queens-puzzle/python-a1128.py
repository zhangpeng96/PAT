"""
    @name      : a1128
    @version   : 20.0720
    @author    : zhangpeng96
    @test_time : 37'00"
    @pass_rate : all
"""

def is_repeated(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True

def diagonal(n, rows):
    cols = [i+1 for i in range(n)]
    major = list(map(lambda r,c: r+c, rows, cols))
    minor = list(map(lambda r,c: r-c, rows, cols))
    return any([is_repeated(major), is_repeated(minor)])

def decision(n, rows):
    if is_repeated(rows) or diagonal(n, rows):
        return False
    else:
        return True


# count = int('4')
# configurations = ['8 4 6 8 2 7 1 3 5', '9 4 6 7 2 8 1 9 5 3', '6 1 5 2 6 4 3', '5 1 3 5 2 4']
count = int(input())
configurations = [input() for _ in range(count)]
configurations = map(lambda x: tuple(map(int, x.split())), configurations)

for config in configurations:
    if decision(config[0], config[1:]):
        print('YES')
    else:
        print('NO')
