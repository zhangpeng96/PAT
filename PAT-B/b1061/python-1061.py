'''
    @name      : b1061
    @version   : 20.506
    @author    : zhangpeng96
    @test_time : 15'00"
    @pass_rate : all
'''

# number, count = tuple(map(int, '3 6'.split()))
# score = list(map(int, '2 1 3 3 4 5'.split()))
# solution = list(map(int, '0 0 1 0 1 1'.split()))

number, count = tuple(map(int, input().split()))
score = list(map(int, input().split()))
solution = list(map(int, input().split()))

def calc_score(answer, solution, score):
    return sum(map(lambda a,k,s: (a == k) * s, answer, solution, score))

answer_sheet = [list(map(int, input().split())) for _ in range(0, number)]
# answer_sheet = list(map(lambda x: list(map(int, x.split()))  , ['0 1 1 0 0 1', '1 0 1 0 1 0', '1 1 0 0 1 1']))

output = '\n'.join([str(calc_score(answer, solution, score)) for answer in answer_sheet])
print(output)
