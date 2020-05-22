'''
    @name      : b1091
    @version   : 20.0522
    @author    : zhangpeng96
    @test_time : 14'55"
    @pass_rate : all
'''

count = int(input())
digits = tuple(map(int, input().split()))

# digits = tuple(map(int, '92 5 233'.split()))

def decision(digit):
    for n in range(1, 10):
        if str(digit**2 * n).endswith(str(digit)):
            return n
    return False


for digit in digits:
    n = decision(digit)
    if n:
        print(n, n * digit**2)
    else:
        print('No')