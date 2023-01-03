'''
    @name      : b1004
    @version   : 20.0516
    @author    : zhangpeng96
    @test_time : 5'17"
    @pass_rate : all

    以下代码没有使用解释器调试，直接在PAT文本框中编写通过

'''

count = int(input())

scores = [input() for _ in range(count)]

scores = sorted(map(lambda x:[x.split()[0], x.split()[1], int(x.split()[2])], scores), key = lambda x:x[2])

print('{} {}'.format(scores[-1][0], scores[-1][1]))
print('{} {}'.format(scores[0][0], scores[0][1]))
