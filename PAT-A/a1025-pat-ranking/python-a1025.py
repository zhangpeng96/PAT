
scores = []
location_count = int(input())
for i in range(location_count):
    test_count = int(input())
    scores.append( [tuple(map(int, input().split())) for _ in range(test_count)] )



