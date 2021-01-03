
score = [100, 95, 95, 85, 77, 85, 97]
score.sort(reverse=True)

def rank_with_same_value(values):
    count = len(values)
    rank = [i+1 for i in range(count)]
    for i in range(count-1):
        if values[i+1] == values[i]:
            rank[i+1] = rank[i]
    return rank

print(
    rank_with_same_value(score)
)
