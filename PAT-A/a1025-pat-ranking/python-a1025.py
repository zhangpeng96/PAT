'''
    @name      : a1025
    @version   : 21.0103
    @author    : zhangpeng96
    @test_time : 60'
    @pass_rate : all
'''

scores = []
location_count = int(input())
for i in range(location_count):
    test_count = int(input())
    score = []
    for _ in range(test_count):
        text = input().split()
        score.append([ text[0], int(text[1])])
    scores.append(score)

# scores = [[[1234567890001, 95], [1234567890005, 100], [1234567890003, 95], [1234567890002, 77], [1234567890004, 85]], [[1234567890013, 65], [1234567890011, 25], [1234567890014, 100], [1234567890012, 85]]]

scores_2 = []

def rank_with_same_value(values):
    count = len(values)
    rank = [i+1 for i in range(count)]
    for i in range(count-1):
        if values[i+1] == values[i]:
            rank[i+1] = rank[i]
    return rank


for i, score in enumerate(scores):
    # print(score)
    score.sort(key=lambda x:(-x[1], x[0]))
    rank = rank_with_same_value(list(map(lambda x:x[1], score)))
    scores_2.extend( list(map(lambda a,b: a + [ i+1, b], score, rank)) )

scores_2.sort(key=lambda x:(-x[1], x[0]))
rank_2 = rank_with_same_value(list(map(lambda x:x[1], scores_2)))
length = len(rank_2)

print(length)
for i in range(length):
    print(scores_2[i][0], rank_2[i], scores_2[i][2], scores_2[i][3])
